# Genome Analysis AI — Overview

A structured reference documenting the landscape of AI for genome analysis: core techniques, key foundation models, Japanese and international initiatives, ethics & regulation, implementation samples, and future outlook.

> Note: Main content is written in Japanese. This README provides an English entry point.

## Repository Layout

| File | Contents |
|------|----------|
| [`genome_ai.md`](./genome_ai.md) | Main document — 8 chapters: variant calling, protein structure prediction, genomic foundation models, single-cell analysis, ethics & regulation, Japanese ecosystem, implementation samples, future outlook |
| [`glossary.md`](./glossary.md) | Glossary of 65 terms across biology, sequencing, ML, and genomic-AI specifics |
| [`references.md`](./references.md) | Curated links: landmark papers, databases, model repositories, Japanese resources, learning materials |
| [`demo.py`](./demo.py) | Runnable standalone demo (numpy only) — k-mer tokenization, pseudo-embedding, cosine similarity, and SNV detection |

## Chapter Map (`genome_ai.md`)

| # | Topic | Representative keywords |
|---|-------|------------------------|
| 1 | Variant Calling | DeepVariant, Clair3, GIAB |
| 2 | Protein Structure Prediction | AlphaFold3, ESMFold, RFdiffusion |
| 3 | Genomic Foundation Models | Evo, HyenaDNA, Nucleotide Transformer |
| 4 | Single-Cell Analysis | scGPT, Geneformer, scFoundation |
| 5 | Ethics & Regulation | GDPR, GINA, PCCP, 次世代医療基盤法 |
| 6 | Japan Ecosystem | AMED WGS Plan, Fugaku, PFN, MOLCURE |
| 7 | Implementation Samples | HuggingFace transformers, scanpy |
| 8 | Future Outlook | Multi-omics, long-context, causal inference, PRS |

## Running the Demo

```bash
pip install numpy
python3 demo.py
```

The demo generates 10 random DNA sequences (120 bp each) and walks through:

1. **k-mer tokenization** (k=3, 6) — analogous to word tokenization in NLP
2. **Pseudo-embedding** — k-mer frequency vectors, L2-normalized (64-dim for k=3)
3. **Cosine similarity matrix** — all pairwise comparisons
4. **Most-similar pair** — identified from the similarity matrix
5. **SNV detection** — reference vs. query base-by-base, reports (position, REF, ALT)

Requires only the Python standard library plus `numpy`.

## Suggested Reading Order

1. Skim `genome_ai.md` end-to-end for the big picture
2. Consult `glossary.md` for unfamiliar terms
3. Run `demo.py` to internalize the k-mer → embedding → variant detection flow
4. Dive into papers and tools via `references.md`

## Scope & Status

- Written for learners and practitioners already familiar with general software/ML concepts.
- Snapshot: **2026-04-18**. Foundation models and regulatory details move fast — verify specifics against primary sources before production use.
- Main document is in Japanese; glossary and references include English terms and URLs.

## License

Documentation and demo code are provided for educational purposes. Attribution welcomed.
