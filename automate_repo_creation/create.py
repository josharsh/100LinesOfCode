import os
import sys
import requests
import yaml
import json

credentials = yaml.load(open("credentials.yaml"), Loader=yaml.FullLoader)

def create():
    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": "token {}".format(credentials["personal_acess_token"])
    }
    parent_dir = credentials["path"]
    username = credentials["github_username"]
    repo_name = str(sys.argv[1])
    path = os.path.join(parent_dir,repo_name)
    try:
        os.makedirs(path)
    except Exception:
        print("You have already created {} folder in path {}".format(repo_name, parent_dir))
        exit(1)
    data = json.dumps({"name": repo_name, "description": "This is repo was created with script"})

    response = requests.post(url, data=data, headers=headers)
    print("Succesfully created repository {}".format(repo_name))


if __name__ == "__main__":
    create()
