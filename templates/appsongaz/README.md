> Push project to Github:
    git init
    git commit -m "first commit"
    git branch -M master
    git remote add origin https://github.com/SaberHardy/YourProjectName.git
    git push -u origin master

In case you modifed something in the project and you want to update your github repo:

    git commit -m "your message"
    git  push -u origin main

But in case someone did changes from other account:
    - Do a pull request first:
        - git pull
    - Push the changes to your repo:
        - git add .  (to add all modified files) or git add
        -  git push -u origin master
    
That's all
