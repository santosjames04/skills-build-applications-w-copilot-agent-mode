OctoFit Tracker — Backend setup

This folder contains the backend scaffold for the OctoFit Tracker project.

1) Create a Python virtual environment (from workspace root):

```bash
python3 -m venv octofit-tracker/backend/venv
source octofit-tracker/backend/venv/bin/activate
```

2) Install project requirements:

```bash
pip install -r octofit-tracker/backend/requirements.txt
```

3) Typical next steps (suggested):
- Start a Django project inside `octofit-tracker/backend/`.
- Configure Django settings for the chosen DB (the instructions reference djongo/pymongo).
- Add REST API endpoints with Django REST Framework.

Notes:
- Follow the project instructions in `.github/instructions` for exact package and environment guidance.
- Do not change directories when running agent-mode commands; instead, reference the full paths as shown above.
