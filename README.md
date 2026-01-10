# domain-engine
Domain-engine is a domain-aware AI systems framework for building semantic ingestion, chunking, embedding, and reasoning pipelines over long and complex documents.

## Setup Environments
- First set up your `.venv`

```
python3 -m venv .env
source .venv/bin/activate (macos/linux, in Windows change `bin` with `Scripts`)
```

### Install dependencies
```
pip3 install -r requirements.txt
```

### Run api
```
uvicorn app.main:app --reload --log-config logging.yaml
```