# ゲノム分析AI 概観

DNA/RNA配列データを機械学習・深層学習で解析する技術領域。従来の統計手法では捉えきれない長距離依存性やエピジェネティック要因を学習できる点が強み。本ドキュメントは主要4領域を俯瞰する。

---

## 1. 変異検出（Variant Calling）

ゲノム変異検出AIは、NGSリードから SNV/indel を高精度に同定する深層学習ツール群である。Googleの **DeepVariant** はリードをpileup画像化しCNNで遺伝子型を分類する手法で、Illumina短鎖からPacBio HiFi、ONTまで対応し業界標準の高精度を誇る。**Clair3** はRNNとピラミッド型CNNを組み合わせ、ONTロングリードでの高速かつ低計算資源での変異検出に特化し、近年はClair3-RNAやDuplex対応版も登場している。**NeuSomatic** はCNNベースで腫瘍-正常ペアまたは単一腫瘍試料からの体細胞変異検出を行い、複数コーラーのコンセンサスを超える精度を示す。用途は臨床診断、がんゲノム解析、希少疾患の生殖細胞系列変異特定、農業・微生物ゲノム研究まで広く、PrecisionFDAやGIABベンチマークで従来のGATK HaplotypeCallerを上回る結果が報告されている。

---

## 2. 立体構造予測（Protein Structure Prediction）

**AlphaFold2** はGoogle DeepMindが開発した革新的モデルで、タンパク質のアミノ酸配列から立体構造をオングストローム精度で予測し、2024年ノーベル化学賞の対象となった。後継の **AlphaFold3** は拡散モデル型アーキテクチャを採用し、タンパク質単体に加えDNA/RNA・低分子リガンド・金属イオン・修飾残基を含む複合体構造を一体予測でき、結合ポーズ予測では2Å以内の的中率76%と従来ドッキング（DiffDock 38%）を大きく凌駕する。Meta社の **ESMFold** は大規模タンパク質言語モデルに基づきMSAを省略するため数秒で構造推論でき、メタゲノム規模スクリーニングに好適。Baker研の **RoseTTAFold** は3トラック型ネットワークで全原子版もリリースされ、RFdiffusionによるde novoタンパク質設計の基盤となる。創薬では、Isomorphic Labsが数千〜万規模の化合物の結合予測を数日で実行し、抗体探索、標的同定、酵素改変、疾患機序解明まで応用が拡大している。

---

## 3. ゲノム基盤モデル（Genomic Foundation Models）

ゲノム基盤モデルは、大量のDNA/RNA配列を自己教師あり学習で事前学習し、下流タスクに転移利用できる大規模モデル群である。**DNABERT** はBERTベースでk-merトークン化を用い、プロモーター予測やスプライス部位同定に応用される。**Nucleotide Transformer**（InstaDeep）は最大2.5Bパラメータで多種ゲノムを学習し、変異効果予測や調節領域分類で高精度を示す。**HyenaDNA** はHyena演算子による長文脈処理に特化し、最大100万塩基の一括入力で染色体スケールの依存関係を捉える。**Evo**（Arc Institute）はStripedHyenaアーキテクチャで原核生物ゲノム全体を単一ヌクレオチド解像度で学習し、タンパク質・RNA・制御配列の同時生成やCRISPR-Cas系の新規設計に応用される。いずれもゼロショット推論や配列生成、合成生物学での機能予測に活用が進む。

---

## 4. 一細胞解析（Single-Cell Analysis）

一細胞解析向けAI基盤モデルは、数千万〜数億細胞規模のscRNA-seqデータで事前学習したTransformer系モデルが主流となっている。**scGPT**（Cui et al., Nature Methods 2024）は約3,300万細胞で学習し、遺伝子発現値をトークン化するフラッシュアテンション構造を採用、細胞タイプ分類・バッチ補正・遺伝子調節ネットワーク（GRN）推定・摂動予測などをファインチューニングで統合的に扱える。**Geneformer**（Theodoris et al., Nature 2023）は約3,000万細胞のコーパスで遺伝子をランク順にトークン化し、ゼロショットでの転写因子同定や疾患関連遺伝子の文脈依存的機能予測に強みを持つ。**scFoundation**（Hao et al., Nature Methods 2024）は1億細胞・1億パラメータ規模で、リードデプス非依存の発現回復や薬剤応答予測に優れる。応用面では、未知細胞タイプの注釈付け、マルチオミクス統合、がん微小環境のGRN推定、in silico摂動による創薬標的探索が進展している。

---

## まとめ

| 領域 | 代表モデル | 主用途 |
|------|-----------|-------|
| 変異検出 | DeepVariant, Clair3, NeuSomatic | 臨床診断・がんゲノム |
| 立体構造予測 | AlphaFold3, ESMFold, RoseTTAFold | 創薬・タンパク質設計 |
| ゲノム基盤モデル | Evo, Nucleotide Transformer, HyenaDNA | 配列生成・機能予測 |
| 一細胞解析 | scGPT, Geneformer, scFoundation | 細胞分類・GRN推定 |

2024〜2026年にかけて、基盤モデル化・マルチモーダル化・長文脈化が共通トレンドとなっており、創薬・合成生物学・精密医療への実装が加速している。

---

## 5. 倫理・規制

ゲノム分析AIの倫理・規制は国際的に急速に整備が進んでいる。**GDPR** では遺伝情報は第9条の「特別カテゴリデータ」に該当し、原則処理禁止で明示的同意や公衆衛生上の必要性など厳格な例外要件を満たす必要がある。米国では **GINA法**（2008）が雇用・健康保険での遺伝情報差別を禁止するが、生命保険・長期介護保険は対象外という欠落が残る。日本では **個人情報保護法** で全ゲノム配列が「要配慮個人情報」に位置付けられ、**次世代医療基盤法**（2023年改正で仮名加工医療情報を導入）により認定事業者経由での研究利活用が可能となった。医療機器規制ではFDAがAI/ML-based SaMDの **PCCP**（Predetermined Change Control Plan）を本格運用し、承認済みAI医療機器は1000件超。PMDAもIDATEN制度でアップデート前提の承認を進める。**AI創薬** ではICHガイドライン整備が進行中で、学習データの品質・説明可能性・バイアス管理が承認審査の鍵となっている。

---

## 6. 日本のゲノムAI動向

日本のゲノム分析AI領域では、官民連携による基盤整備と専門企業の技術開発が加速している。AMEDの **「全ゲノム解析等実行計画」** はがん・難病10万人規模のデータ蓄積を進め、2026年時点で事業実施組織を中核に臨床応用と創薬活用のフェーズへ移行しつつある。**東京大学医科学研究所** はヒトゲノム解析センターを軸にAI駆動型バリアント解釈基盤を構築し、**理化学研究所** はスーパーコンピュータ「富岳」や生命機能科学研究センターを活用して大規模マルチオミクス解析・生成AIによる配列設計を推進している。**Preferred Networks** は深層学習と創薬・タンパク質構造予測を融合した基盤モデル開発を進め、**MOLCURE** はAIと湿式実験を統合した抗体・中分子設計で存在感を高めている。**エルピクセル** は医用画像とゲノム解釈の横断解析、**Xenon Molecular** は量子化学×AIによる分子設計、**Rhelixa** はエピゲノム解析受託とバイオインフォ基盤でそれぞれ独自ポジションを築いている。

---

## 7. 実装サンプルコード

主要モデルのPython最小実装例。

### 7.1 ESMFold（タンパク質構造予測）

MSA不要で単一配列から高速に3D構造を予測。HuggingFace transformers経由でPDB形式出力。

```bash
pip install torch transformers accelerate
```

```python
import torch
from transformers import AutoTokenizer, EsmForProteinFolding
from transformers.models.esm.openfold_utils.protein import to_pdb, Protein
from transformers.models.esm.openfold_utils.feats import atom14_to_atom37

tokenizer = AutoTokenizer.from_pretrained("facebook/esmfold_v1")
model = EsmForProteinFolding.from_pretrained("facebook/esmfold_v1", low_cpu_mem_usage=True).eval()

sequence = "MKTAYIAKQRQISFVKSHFSRQLEERLGLIEVQAPILSRVGDGTQDNLSGAEK"
inputs = tokenizer([sequence], return_tensors="pt", add_special_tokens=False)

with torch.no_grad():
    outputs = model(**inputs)

final_atom_positions = atom14_to_atom37(outputs["positions"][-1], outputs)
pdb = to_pdb(Protein(aatype=inputs["input_ids"][0].numpy(),
                     atom_positions=final_atom_positions[0].numpy(),
                     atom_mask=outputs["atom37_atom_exists"][0].numpy(),
                     residue_index=torch.arange(len(sequence)).numpy() + 1,
                     b_factors=outputs["plddt"][0].numpy()))
open("predicted.pdb", "w").write(pdb)
```

### 7.2 Nucleotide Transformer（DNA配列埋め込み）

6-merトークン化したDNA配列から平均プーリングで配列埋め込みを取得。下流の分類・回帰タスクに転用可能。

```bash
pip install torch transformers
```

```python
import torch
from transformers import AutoTokenizer, AutoModelForMaskedLM

model_name = "InstaDeepAI/nucleotide-transformer-500m-human-ref"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForMaskedLM.from_pretrained(model_name)

dna_sequences = ["ATGCGTACGTAGCTAGCTAGCATCGATCGATCGATCGTAGCTAGCTAGC",
                 "GCTAGCTAGCATCGATCGTAGCTAGCGTACGTAGCATGCATGCGATCGA"]
tokens = tokenizer.batch_encode_plus(dna_sequences, return_tensors="pt", padding=True)["input_ids"]
attention_mask = tokens != tokenizer.pad_token_id

with torch.no_grad():
    outputs = model(tokens, attention_mask=attention_mask, output_hidden_states=True)

embeddings = outputs["hidden_states"][-1]
mask = attention_mask.unsqueeze(-1).float()
mean_embeddings = (embeddings * mask).sum(1) / mask.sum(1)
print(f"埋め込み次元: {mean_embeddings.shape}")  # (2, 1280)
```

### 7.3 Geneformer（scRNA-seq細胞タイプ推論）

約3000万細胞で事前学習された基盤モデル。遺伝子発現ランクをトークン化し、細胞タイプ分類をファインチューニング済みモデルで実行。

```bash
pip install torch transformers datasets scanpy
pip install git+https://huggingface.co/ctheodoris/Geneformer.git
```

```python
from geneformer import TranscriptomeTokenizer, Classifier
import scanpy as sc

adata = sc.read_h5ad("your_scRNAseq.h5ad")
adata.obs["n_counts"] = adata.X.sum(axis=1)
adata.write_loom("input.loom")

tk = TranscriptomeTokenizer({"cell_type": "cell_type"}, nproc=4)
tk.tokenize_data("./", "./tokenized", "prefix", file_format="loom")

cc = Classifier(classifier="cell",
                cell_state_dict={"state_key": "cell_type", "states": "all"},
                freeze_layers=2, num_crossval_splits=1)
cc.evaluate_saved_model(model_directory="ctheodoris/Geneformer",
                        id_class_dict_file="id_class_dict.pkl",
                        test_data_file="./tokenized/prefix.dataset",
                        output_directory="./results", output_prefix="eval")
```

> **補足**: ESMFoldは400aa超でGPUメモリ逼迫しやすい（`model.esm.half()` で半精度化推奨）。Nucleotide Transformerは6-merトークン化のため最大約6000bp。scGPT利用時は `pip install scgpt` で `scgpt.tasks.CellTypeAnnotation` を参照。

---

## 8. 今後の展望（2026年以降）

2026年以降のゲノム分析AIは、**マルチオミクス統合** が本格化し、ゲノム・エピゲノム・プロテオーム・空間トランスクリプトームに病理画像やMRIを融合する基盤モデルが主流となる見込みである。EvoやNucleotide Transformer後継となる **数百万トークン級の長文脈ゲノム基盤モデル** が登場し、エンハンサー・プロモーター相互作用や非コード領域変異の機能予測精度が飛躍的に向上する。**因果推論**（Mendelian randomization×深層学習、CRISPRスクリーン連携）により、相関を超えた遺伝子機能解明とドラッグターゲット同定が進展し、生成AIはAlphaFold3系の構造予測と結合して合成生物学・de novoタンパク質設計・ゲノム配列生成を加速する。臨床面では **PRSの多祖先対応・非線形化**、digital twinによる個別治療シミュレーション、ACMG基準を超えるAI支援VUS再分類が実装され、希少疾患診断や予防医療の精密化が一段と進むと予測される。

---

## 参考: 主要トピック早見表

| 章 | テーマ | キーワード |
|----|-------|-----------|
| 1 | 変異検出 | DeepVariant, Clair3, GIAB |
| 2 | 立体構造予測 | AlphaFold3, ESMFold, RFdiffusion |
| 3 | ゲノム基盤モデル | Evo, HyenaDNA, Nucleotide Transformer |
| 4 | 一細胞解析 | scGPT, Geneformer, scFoundation |
| 5 | 倫理・規制 | GDPR, GINA, 次世代医療基盤法, PCCP |
| 6 | 日本の動向 | AMED全ゲノム計画, 富岳, PFN, MOLCURE |
| 7 | 実装サンプル | HuggingFace, transformers, scanpy |
| 8 | 今後の展望 | マルチオミクス, 長文脈, 因果推論, PRS |
