# PStruc Example Project

This project demonstrates the PStruc library usage for enhancing a project with ChatGPT's assistance. PStruc creates a `pstruc_example.yaml` file, which, along with specific questions, is provided to ChatGPT. The insights or enhancements suggested by ChatGPT are then used to modify the code.

The project is split into three versions, each representing a stage of development:

- `version_1`: Initial version with potential code issues and missing elements.
- `version_2`: Revised code based on ChatGPT's suggestions, improved to adhere to PEP8 guidelines.
- `version_3`: Further enhancements and feature additions proposed by ChatGPT.

Each version folder contains the project files and a `readme.md` file, detailing the ChatGPT interactions and suggested modifications. The `readme.md` in `version_1` is empty as it's the starting point.

*Note*: Setting up and running the project is optional and mainly for experimentation with ChatGPT enhancements.

## Setup Instructions

### 1. Clone the repository.

```
git clone https://github.com/nachokhan/pstruc_example.git
```

### 2. Create and activate the virtual environment:

```
python -m venv .env
source .env/bin/activate
```

### 3. Install dependecies.

```
pip install -r requirements.txt
```

### 4. Run the code 
```
python main.py
```

## USing PStruc
Run the following command to generate the project structure:

```
pstruc -ip ".env",".git","*pycache*","*.yml","version_*","readme.md" -fc "*.py" -o pstruc_example -f yaml
```

### Argument Explanation
- **-ip**: Ignores specified patterns like `.env`, `.git`, `*pycache*`, `*.yml`, `version_*`, and `readme.md`.
- **-fc**: Includes the content of Python files (`*.py`).
- **-o**: Sets the output file's name as `pstruc_example.yaml`.
- **-f**: Chooses YAML as the output format.

The command generates a `pstruc_example.yaml` file, representing the project's structure, including Python files' content while excluding the defined patterns.



