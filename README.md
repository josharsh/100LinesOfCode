# 100LinesOfCode
This repository contains all the applications, extensions, add-ons, designs, themes and anything else which is productive developed in less than #100LinesOfCode.

# Purpose
Purpose of this repository is to promote development of productive applications and utilities which seem so common yet might not be into use. Trigger your brain, take the challenge of developing something in less than #100LinesofCode. 

# Contributing
For Contrubuting norms and guidelines, go to CONTRIBUTING.MD


## Adding Your Code:
Here are the steps:
1: Develop something in the programming language of your choice for any platform in less than #100LinesOfCode
2: Fork this repository
3: Clone this repository 
```
$ git clone "https://www.github.com/{Username}/Minor-1-Swarm-Intelligence.git"
```
where username is your GitHub account username.

4. Create a branch where you can do your local work.
Never work on **master** branch as we do not allow master commits except by admins.
```
$ git branch {branchname}
$ git checkout branchname
```

5. Do your work and stage your changes.
```
$ git add <filename>
```

6. Commit you changes with a commit message containing your name, file(s) worked upon, changes added.
```
$ git commit -m "Name| files| Changes"
```

7. Push changes to your forked repository
```
$ git push -u origin branchname
```

##### Synchronize forked repository with Upstream repository

1. Create upstream as our repository
```
$ git remote add upstream "https://www.github.com/NishkarshRaj/Minor-1-Swarm-Intelligence"
```

2. Fetch upstream changes in local machine
```
$ git fetch upstream
```

3. Switch to master branch
```
$ git checkout master
```

4. Merge changes in local machine
```
$ git merge upstream/master
```

5. Push changes to your forked GitHub repository
```
$ git push -f origin master
```

## Structure of Your Code:
The *root* directory of your developed application must contain
* A README.md describing your project, idea and Implementation
* Source code for your app
* Link to working app (In case the app in an extension ,add On etc.)
* If Possible, Deploy the code onto a hosting platform.

Note: Please Add Author's name in Readme.md of application. 


