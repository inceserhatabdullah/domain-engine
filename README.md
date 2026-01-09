# domain-engine
Domain-engine is a domain-aware AI systems framework for building semantic ingestion, chunking, embedding, and reasoning pipelines over long and complex documents.

## Folder Structure
```
domain-engine/
├── README.md
├── pyproject.toml
├── requirements.txt
├── data/
│   └── samples/
├── domain_engine/
│   ├── ingest/
│   │   ├── loaders.py        # pdf, docx, txt
│   │   ├── cleaners.py       # noise, headers, artifacts
│   │   └── normalizer.py
│   │
│   ├── chunking/
│   │   ├── base.py           # ChunkStrategy interface
│   │   ├── naive.py          # paragraph / sliding window
│   │   └── legal.py          # iddia / olay / norm (ilk domain)
│   │
│   ├── semantics/
│   │   ├── extractor.py     # claim, event, entity çıkarımı
│   │   └── schemas.py       # domain semantic models
│   │
│   ├── embedding/
│   │   ├── base.py
│   │   ├── ollama.py
│   │   └── openai.py
│   │
│   ├── store/
│   │   ├── base.py
│   │   ├── faiss_store.py
│   │   └── qdrant_store.py
│   │
│   ├── retrieval/
│   │   └── hybrid.py
│   │
│   ├── reasoning/
│   │   └── legal_analysis.py
│   │
│   └── pipelines/
│       └── legal_ingest.py
│
└── experiments/
    └── notebooks/
```