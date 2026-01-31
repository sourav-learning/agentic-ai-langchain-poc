# Notes

## How to install uv package manager

### Search with "uv package manager" go to astral website
* Link with installation commands : https://docs.astral.sh/uv/getting-started/installation/#installation-methods

### Run command on powershell terminal of VS Code
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

### Set path - Run from cmd

Initialize workspace
uv init 
This creates the boiler plate files

### Create virtual environment
uv venv

### Activate Virtual Environment
.venv\Scripts\activate

### Deactivate Virtual Environment
deactivate

### To list the required libraries for installing by one command
Create requirements.txt file outside .venv
Add the required libraries in the file

### Command to install the libraries using uv
uv add -r requirements.txt
* To add any library other than those under requirements, directly type uv add <libraryname>

### To store API keys and other secrets
Create .env file (outside .venv - . denotes hidden file)
Add the keys

