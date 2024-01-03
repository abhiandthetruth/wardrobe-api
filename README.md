## Almirah API

To start the dev server do the following
```bash
pip3 install -r requirements.txt
uvicorn --app-dir src/ --port 8000 --host 0.0.0.0 --reload  main:app
```