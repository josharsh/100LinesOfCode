"""Script to automate repository creation on github and local machine"""

import json
import os
import sys
import requests
import yaml

credentials = yaml.load(open("credentials.yaml", encoding="utf-8"), Loader=yaml.FullLoader)

def create():
    """Creates a repository on github and local machine"""
    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {credentials['personal_acess_token']}"
    }
    parent_dir = credentials["path"]
    username = credentials["github_username"]
    repo_name = str(sys.argv[1])
    path = os.path.join(parent_dir,repo_name)
    try:
        os.makedirs(path)
    except Exception:
        print(f"You have already created {repo_name} folder in path {parent_dir}")
        exit(1)
    data = json.dumps({"name": repo_name, "description": "This is repo was created with script"})

    response = requests.post(url, data=data, headers=headers)
    print(f"Succesfully created repository {repo_name}")


if __name__ == "__main__":
    create()
