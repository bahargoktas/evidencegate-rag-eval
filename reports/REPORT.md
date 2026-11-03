# EvidenceGate — Local Benchmark Report

**Date:** 2026-11-03

The completed local implementation was executed with 60 products, 120 generated documents, 120 questions, seed 20261103, and k=5. All nine local tests passed. Both BM25 and TF-IDF produced the following results:

| Metric | BM25 | TF-IDF |
|---|---:|---:|
| Recall@5 | 1.000 | 1.000 |
| MRR@5 | 1.000 | 1.000 |
| Answer exact match | 1.000 | 1.000 |
| Citation accuracy | 1.000 | 1.000 |
| Unanswerable abstention | 1.000 | 1.000 |
| Unsupported answer rate | 0.000 | 0.000 |

The uploaded GitHub code is a transcription of the locally executed implementation. The GitHub revision itself has **not** been independently executed or CI-verified at the time of publication. These numbers are valid only for the deliberately easy synthetic dataset, not for production RAG or real-world LLM hallucination performance.
