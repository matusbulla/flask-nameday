# Flask Nameday API

Returns today's Slovak nameday as JSON.

```json
{"date": "2026-04-24", "name": "Juraj"}
```

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
cd src
flask run
```

API available at `http://127.0.0.1:5000/`

```bash
$ curl http://127.0.0.1:5000/
```

## Tests

```bash
cd src
pytest tests/ -v
```
