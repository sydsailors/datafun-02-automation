# datafun-02-automation

This project uses basic Python functions to create folders and to do useful things. 

Steps already completed:
1. [Set up the Machine](https://github.com/denisecase/pro-analytics-01/blob/main/01-machine-setup/MACHINE-SETUP.md)
2. [Initialized a new Project](https://github.com/denisecase/pro-analytics-01/blob/main/02-project-initialization/PROJECT-INITIALIZATION.md)

## Before/During Working on the Project
1. Pull the Latest Changes from GitHub 
   
```shell
git pull origin main
```

2. Activate the Project Virtual Environment

```powershell
source .venv/bin/activate
```

3. Install Dependencies As Needed 

```powershell
source .venv/bin/activate
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install -r requirements.txt
```

4. Run Script 

```powershell
source .venv/bin/activate
python3 demo-script.py
```

## Add Module 1 utils file to Project Folder
Add new empty file in VS Code and paste module 1 repo (utils_sydneysailors.py) into new empty file.

## Add new Python File
Create new Python file (sydneysailors_project_setup.py) in VS Code.

## Functions Implemented 
- `for item in range` - to create folders for a given range
- `for name in list` - to create folders from a list of names
- list comprehension
- `while` loop - to create folders periodically over time
- `for item in list` - to create folders from a list of names with options to standardize names

## Git Commands
```shell
git add .
git commit -m "Add sydneysailors_project_setup.py files"
git push -u origin main
```

