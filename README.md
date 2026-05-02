# Flight Ops Maintenance Portal

EcoLift Aerospace (Hamburg, Germany) uses this internal web application to track open and completed aircraft maintenance work orders across its regional fleet. Technicians can query tasks by work-order description or aircraft registration, and supervisors use the search interface to monitor task completion status in real time.

> ⚠️ **This repository contains intentional security vulnerabilities for demonstration and training purposes. Do not deploy to production or expose to untrusted networks.**

---

## Setup

```bash
pip install pipenv
pipenv install
pipenv run python -m server
```

Then open [http://localhost:5000](http://localhost:5000) in your browser.

### Environment variables

| Variable | Default | Description |
|---|---|---|
| `SQLITE_URI` | `:memory:` | Path to a persistent SQLite database file |
| `DEBUG` | `False` | Set to `1` to enable Flask debug mode |
