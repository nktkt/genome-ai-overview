#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ゲノムAI概念学習用デモスクリプト
================================
ゲノム配列を題材に機械学習の基本概念を教育目的で疑似実装する。

扱う概念:
    - DNA配列のランダム生成
    - k-merによるトークン化（NLPの単語分割に相当）
    - k-mer頻度ベクトルを用いた疑似埋め込み (Embedding)
    - コサイン類似度による配列間類似度の計算
    - リファレンス配列とクエリ配列の比較による SNV 検出

依存: Python標準ライブラリ + numpy のみ
"""

import random
from collections import Counter
from itertools import product
import numpy as np


def generate_random_dna(length: int, seed: int = None) -> str:
    """指定された長さのランダムなDNA配列 (A/T/G/C) を生成する。"""
    if seed is not None:
        random.seed(seed)
    bases = ['A', 'T', 'G', 'C']
    return ''.join(random.choice(bases) for _ in range(length))


def tokenize_kmers(sequence: str, k: int = 3) -> list:
    """DNA配列を長さkのk-merに分割する（スライディングウィンドウ）。"""
    if k <= 0 or k > len(sequence):
        return []
    return [sequence[i:i + k] for i in range(len(sequence) - k + 1)]


def kmer_embedding(sequence: str, k: int = 3) -> np.ndarray:
    """k-mer頻度に基づく疑似埋め込みベクトルを生成する（L2正規化）。"""
    all_kmers = [''.join(p) for p in product('ATGC', repeat=k)]
    kmer_index = {kmer: i for i, kmer in enumerate(all_kmers)}

    counts = Counter(tokenize_kmers(sequence, k))
    vec = np.zeros(len(all_kmers), dtype=np.float64)
    for kmer, cnt in counts.items():
        if kmer in kmer_index:
            vec[kmer_index[kmer]] = cnt

    norm = np.linalg.norm(vec)
    if norm > 0:
        vec = vec / norm
    return vec


def cosine_similarity(vec_a: np.ndarray, vec_b: np.ndarray) -> float:
    """2つのベクトルのコサイン類似度を返す。"""
    norm_a = np.linalg.norm(vec_a)
    norm_b = np.linalg.norm(vec_b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return float(np.dot(vec_a, vec_b) / (norm_a * norm_b))


def detect_snv(reference: str, query: str) -> list:
    """同一長の配列を位置ごとに比較し、SNV位置を [(pos, ref, alt), ...] で返す。"""
    if len(reference) != len(query):
        raise ValueError("リファレンスとクエリの配列長が一致しません。"
                         "InDel等はアラインメント後に実施してください。")
    variants = []
    for pos, (ref_base, qry_base) in enumerate(zip(reference, query)):
        if ref_base != qry_base:
            variants.append((pos, ref_base, qry_base))
    return variants


def introduce_mutations(sequence: str, num_mutations: int, seed: int = None) -> str:
    """既存配列にランダムな塩基置換を num_mutations 個導入する。"""
    rng = random.Random(seed)
    seq_list = list(sequence)
    positions = rng.sample(range(len(seq_list)), min(num_mutations, len(seq_list)))
    bases = ['A', 'T', 'G', 'C']
    for pos in positions:
        current = seq_list[pos]
        candidates = [b for b in bases if b != current]
        seq_list[pos] = rng.choice(candidates)
    return ''.join(seq_list)


def main():
    random.seed(42)
    np.random.seed(42)

    NUM_SEQS = 10
    SEQ_LEN = 120
    K = 3

    print("=" * 70)
    print(" ゲノムAI概念学習デモ  (標準ライブラリ + numpy のみ)")
    print("=" * 70)
    print(f"\n[ステップ1] ランダムDNA配列を {NUM_SEQS} 本生成 (長さ={SEQ_LEN})\n")

    sequences = [generate_random_dna(SEQ_LEN) for _ in range(NUM_SEQS)]
    for i, seq in enumerate(sequences):
        print(f"  seq{i:02d}: {seq[:60]}...")

    print(f"\n[ステップ2] k-merトークン化のサンプル\n")
    sample_3 = tokenize_kmers(sequences[0], k=3)
    sample_6 = tokenize_kmers(sequences[0], k=6)
    print(f"  seq00 の先頭10個 (k=3): {sample_3[:10]}")
    print(f"  seq00 の先頭10個 (k=6): {sample_6[:10]}")
    print(f"  (総k-mer数: k=3 → {len(sample_3)}, k=6 → {len(sample_6)})")

    print(f"\n[ステップ3] 疑似埋め込み (k-mer頻度ベクトル, 次元={4**K})\n")
    embeddings = [kmer_embedding(seq, k=K) for seq in sequences]
    print(f"  各配列を {4**K} 次元のベクトルに変換。")
    print(f"  seq00 のベクトル先頭8成分: {np.round(embeddings[0][:8], 4).tolist()}")
    print(f"  L2ノルム (正規化済): {np.linalg.norm(embeddings[0]):.4f}")

    print(f"\n[ステップ4] 全ペアのコサイン類似度行列\n")
    sim_matrix = np.zeros((NUM_SEQS, NUM_SEQS), dtype=np.float64)
    for i in range(NUM_SEQS):
        for j in range(NUM_SEQS):
            sim_matrix[i, j] = cosine_similarity(embeddings[i], embeddings[j])

    header = "       " + " ".join([f"s{j:02d}  " for j in range(NUM_SEQS)])
    print(header)
    for i in range(NUM_SEQS):
        row_vals = " ".join([f"{sim_matrix[i, j]:.3f}" for j in range(NUM_SEQS)])
        print(f"  s{i:02d}: {row_vals}")

    print(f"\n[ステップ5] 最も似た配列ペア (対角除外)\n")
    best_sim = -1.0
    best_pair = (-1, -1)
    for i in range(NUM_SEQS):
        for j in range(i + 1, NUM_SEQS):
            if sim_matrix[i, j] > best_sim:
                best_sim = sim_matrix[i, j]
                best_pair = (i, j)
    i, j = best_pair
    print(f"  最類似ペア: seq{i:02d} と seq{j:02d}  (類似度={best_sim:.4f})")
    print(f"    seq{i:02d}: {sequences[i][:60]}...")
    print(f"    seq{j:02d}: {sequences[j][:60]}...")

    print(f"\n[ステップ6] SNV (単一塩基多型) 検出デモ\n")
    reference = sequences[0]
    query = introduce_mutations(reference, num_mutations=5, seed=123)
    print(f"  リファレンス(先頭80bp): {reference[:80]}")
    print(f"  クエリ      (先頭80bp): {query[:80]}")

    snvs = detect_snv(reference, query)
    print(f"\n  検出されたSNV数: {len(snvs)}")
    print(f"  詳細 (位置, REF, ALT):")
    for pos, ref_base, alt_base in snvs:
        print(f"    位置 {pos:4d}: {ref_base} → {alt_base}")

    ref_emb = kmer_embedding(reference, k=K)
    qry_emb = kmer_embedding(query, k=K)
    print(f"\n  リファレンス vs クエリ(5変異)の類似度: "
          f"{cosine_similarity(ref_emb, qry_emb):.4f}")
    print(f"  → わずかな変異では埋め込みはほぼ同じ方向を指す。")

    print("\n" + "=" * 70)
    print(" デモ終了")
    print("=" * 70 + "\n")


if __name__ == '__main__':
    main()
