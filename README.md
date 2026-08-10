## AI Module Service
---
A lightweight FastAPI service for managing document processing using MinIO (S3) and Ollama. It extracts hotel/business contact details and generates text summaries from files with Pydantic structured outputs.

### Tech Stack
---
- FastAPI
- Ollama (llama3.2:3b)
- MinIO (aiobotocore)
- mammoth (DOCX parsing)
- Python 3.12+ / Poetry

### Quick Start
---
Install Dependencies:
> poetry install 

Environment Setup (.env):
```DEBUG=True
APP_HOST=0.0.0.0
APP_PORT=8000

MINIO_HOST=s3
MINIO_PORT=9000
MINIO_USER=minio
MINIO_PASSWORD=password

LLM_HOST=http://172.17.0.1:11434
LLM_MODEL=llama3.2:3b
```

Run App:
> make build

## What can you get
#### The first result
<img width="1024" height="778" alt="first" src="https://github.com/user-attachments/assets/42f05380-0a34-410c-bc8f-71a8faada05f" />

#### The second result
<img width="1024" height="572" alt="duo" src="https://github.com/user-attachments/assets/b934cd71-714d-4357-ae58-dee49b5f0d31" />


