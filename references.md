# ゲノムAI分野 参考文献・リソース集

## 主要論文

- [AlphaFold3 (Nature, 2024)](https://www.nature.com/articles/s41586-024-07487-w) — タンパク質・核酸・低分子を含む複合体構造を高精度で予測する拡散ベースモデル。
- [Evo: DNA foundation model (Science, 2024)](https://www.science.org/doi/10.1126/science.ado9336) — 分子からゲノムスケールまで予測・生成可能なDNA基盤モデル。
- [scGPT (Nature Methods, 2024)](https://www.nature.com/articles/s41592-024-02201-0) — 単一細胞マルチオミクス向けの生成的事前学習トランスフォーマー。
- [Geneformer (Nature, 2023)](https://www.nature.com/articles/s41586-023-06139-9) — 約3000万の単一細胞転写物で事前学習したネットワーク生物学基盤モデル。
- [DeepVariant (Nature Biotechnology, 2018)](https://www.nature.com/articles/nbt.4235) — ディープニューラルネットによる高精度バリアントコール。
- [Nucleotide Transformer (Nature Methods, 2024)](https://www.nature.com/articles/s41592-024-02523-z) — ヒト・多種ゲノムで事前学習したDNA言語モデルのベンチマーク。
- [ESM-2 / ESMFold (Science, 2023)](https://www.science.org/doi/10.1126/science.ade2574) — 進化スケールのタンパク質言語モデルによる構造予測。
- [Enformer (Nature Methods, 2021)](https://www.nature.com/articles/s41592-021-01252-x) — 長距離相互作用を学習した遺伝子発現予測モデル。
- [DNABERT-2 (ICLR, 2024)](https://arxiv.org/abs/2306.15006) — 多種ゲノム対応の効率的DNA言語モデル。
- [scFoundation (Nature Methods, 2024)](https://www.nature.com/articles/s41592-024-02305-7) — 大規模単一細胞RNA-seq基盤モデル。

## ゲノム・バイオデータベース

- [NCBI](https://www.ncbi.nlm.nih.gov/) — 米国国立生物工学情報センターの総合生物情報ポータル。
- [Ensembl](https://www.ensembl.org/) — 脊椎動物を中心としたゲノムアノテーションデータベース。
- [UCSC Genome Browser](https://genome.ucsc.edu/) — ゲノム配列とアノテーションのインタラクティブ可視化。
- [1000 Genomes Project](https://www.internationalgenome.org/) — 多様な集団のヒトゲノムバリエーションカタログ。
- [UK Biobank](https://www.ukbiobank.ac.uk/) — 50万人規模の健康・遺伝・画像データリソース。
- [GTEx Portal](https://gtexportal.org/home/) — 組織別遺伝子発現とeQTLの公開データベース。
- [Human Cell Atlas](https://www.humancellatlas.org/) — 全ヒト細胞の包括的参照アトラスプロジェクト。
- [Genome in a Bottle (GIAB)](https://www.nist.gov/programs-projects/genome-bottle) — NISTによるバリアントコール評価用リファレンス標準。
- [gnomAD](https://gnomad.broadinstitute.org/) — 数十万人規模の集団アリル頻度データベース。
- [UniProt](https://www.uniprot.org/) — タンパク質配列・機能情報の統合データベース。

## AI基盤モデル/ツールリポジトリ

- [Hugging Face — InstaDeep Nucleotide Transformer](https://huggingface.co/InstaDeepAI) — Nucleotide TransformerなどDNA基盤モデルの公式配布。
- [GitHub — Evo (Arc Institute)](https://github.com/evo-design/evo) — Evoモデルの公式実装とチェックポイント。
- [GitHub — scGPT](https://github.com/bowang-lab/scGPT) — scGPTの学習・推論コードとチュートリアル。
- [HuggingFace — Geneformer](https://huggingface.co/ctheodoris/Geneformer) — Geneformer公式モデルと使用例。
- [GitHub — DeepVariant](https://github.com/google/deepvariant) — Google製のバリアントコーラー実装。
- [GitHub — AlphaFold](https://github.com/google-deepmind/alphafold) — AlphaFold 2系の公式オープンソース実装。
- [GitHub — ESM (Meta AI)](https://github.com/facebookresearch/esm) — タンパク質言語モデルESM系の公式リポジトリ。
- [GitHub — Enformer (DeepMind)](https://github.com/google-deepmind/deepmind-research/tree/master/enformer) — Enformerモデルの公式コード。
- [Hugging Face — Hub](https://huggingface.co/models) — バイオ・ゲノム系を含むオープンモデルの集約ハブ。
- [GitHub — Bioconductor](https://github.com/Bioconductor) — Rベースのゲノム解析パッケージ群。

## 日本のリソース

- [AMED (日本医療研究開発機構)](https://www.amed.go.jp/) — 医療・ゲノム関連研究の国内ファンディング機関。
- [ToMMo (東北メディカル・メガバンク機構)](https://www.megabank.tohoku.ac.jp/) — 日本人集団の大規模ゲノム・コホート解析拠点。
- [NBDC (バイオサイエンスデータベースセンター)](https://biosciencedbc.jp/) — 日本のライフサイエンスデータ統合ポータル。
- [DDBJ (日本DNAデータバンク)](https://www.ddbj.nig.ac.jp/) — 国際塩基配列DB連携の日本側拠点。
- [jMorp (ToMMo多層オミクス参照パネル)](https://jmorp.megabank.tohoku.ac.jp/) — 日本人集団のアリル頻度・オミクス参照データ。
- [GEM Japan](https://gemj.amed.go.jp/) — AMED主導の国内ゲノム医療実現に向けた統合プロジェクト。
- [PubCaseFinder](https://pubcasefinder.dbcls.jp/) — 希少疾患診断支援のための表現型検索ツール。
- [TogoVar](https://togovar.biosciencedbc.jp/) — 日本人集団を含むバリアント統合データベース。
- [DBCLS (ライフサイエンス統合データベースセンター)](https://dbcls.rois.ac.jp/) — 国内ライフサイエンスDB統合・教材開発拠点。

## 学習教材

- [Coursera — Genomic Data Science Specialization (Johns Hopkins)](https://www.coursera.org/specializations/genomic-data-science) — ゲノムデータ解析の基礎から応用まで網羅するオンライン講座。
- [edX — Data Analysis for Life Sciences (HarvardX)](https://www.edx.org/series/data-analysis-for-the-life-sciences) — 生命科学のための統計・データ解析シリーズ。
- [Rosalind](https://rosalind.info/problems/locations/) — バイオインフォマティクスをプログラミング問題で学ぶプラットフォーム。
- [Bioinformatics Algorithms (Compeau & Pevzner)](https://bioinformaticsalgorithms.com/) — 主要アルゴリズムを扱う教科書とオンライン教材。
- [Harvard Chan Bioinformatics Core — Training](https://hbctraining.github.io/main/) — NGS解析・単一細胞解析などの実習教材。
- [Galaxy Training Network](https://training.galaxyproject.org/) — Galaxyプラットフォームを用いたバイオインフォ実習集。
- [DeepLearning.AI — AI for Medicine](https://www.coursera.org/specializations/ai-for-medicine) — 医療AIの実践的コース（画像・ゲノム含む）。
- [TOGO TV (DBCLS)](https://togotv.dbcls.jp/) — 日本語のライフサイエンスツール使い方動画集。
- [Bioconductor — Courses and Materials](https://bioconductor.org/help/course-materials/) — Rによるゲノム解析の公式教材アーカイブ。
