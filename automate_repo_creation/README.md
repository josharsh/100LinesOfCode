# Automate Repo Creation


### Steps to run project
- Make sure you have python installed along with pip
- Then `cd automate_repo_creation`
- Create vitrual environment `python3 -m venv venv` or `virtualenv -p python3 venv` to install required packages or you can install the required pacakges globally wthout creating virtual environment
- To install required packages: `pip install -r requirements.txt`
- Create credentials.yaml `touch credentials.yaml` and fill neccessary data with the help of credentials.yaml.example file
- Provide user access to execute script `chmod u+x script.sh`
- Finaly run the project: `./script.sh <name_of_repo>`

### Note: If you don't have VS code you can comment the last line of `script.sh`

### Things needed to run:
- Github Personal Access Token

### Create github personal access:
- Go to Github Setting -> Developer Setting -> Personal Access Token -> Generate new token or simply go to this [link](https://github.com/settings/tokens/new)
- Make sure to select `repo` in scope while generating token
