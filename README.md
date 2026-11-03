# EvidenceGate — Citation-Aware Retrieval & Abstention Benchmark

Reproducible, synthetic-document evaluation harness for **BM25** and **TF-IDF**, with auditable extractive answers and source citations. This is **not a generative LLM**.

## Quick start
```bash
python -m pip install -e ".[dev]"
python -m pytest -q
python -m evidencegate --products 60 --k 5 --output outputs/metrics.json
```

## Architecture
- `dataset.py`: deterministic fictional policy corpus, current and obsolete versions, QA ground truth
- `retrieval.py`: BM25 and TF-IDF retrieval; obsolete documents excluded
- `answering.py`: transparent answer extraction with exact product identity and source citation checks
- `evaluate.py`: Recall@k, MRR@k, answer exact match, citation accuracy, abstention, unsupported-answer rate
- `__main__.py`: command-line experiment and JSON output

## Dataset
All documents are **original synthetic fictional product policies**, generated locally. No external data or personal information. MIT license applies to source code and generator.

## Evaluation
60 products produce 120 documents (60 current, 60 archived) and 120 questions (60 answerable, 60 unanswerable). Only current documents are retrievable. Ground truth is generated alongside the corpus. The answerer is deterministic, not an LLM. See `reports/metrics.json` for locally measured results and `docs/TR_EGITIM.md` for the Turkish tutorial.

## Limitations
English-only template questions and simple synthetic documents make this benchmark unusually easy. Perfect scores **do not** establish real-world retrieval accuracy, LLM factuality, or hallucination resistance. CI smoke tests are separate from full benchmark results.
