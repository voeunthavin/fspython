# fspython

Learning python on various topic

## Clean and isolated development environment

`python -m venv .venv`

### Activate

`source .venv/bin/activate`
`python -m pip install -e .`

### Deactivate

`deactivate`

## Using Requirement Files

`python -m pip freeze > requirements.txt`

### Install Requirement Files

`python -m pip install -r requirements.txt`

### Install Dev Requirement Files

`python -m pip install -r requirements-dev.txt`

### Fine-Tuning Requirements

`python -m pip install -U -r requirements.txt`
