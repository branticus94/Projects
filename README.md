# Projects

- [About Me](#woman-about-me)
- [Previous Projects](#previous-projects)
- [How I will be using Github for this assignment](#how-i-will-be-using-github-for-this-assignment)
- [Working with files in git and github](#working-with-files-in-git-and-github)
- [Creating a .gitignore, explaining what it is for! (What poetry! 📚)](#creating-a-gitignore-explaining-what-it-is-for)
- [Creating a requirements.txt (can be empty), explaining what it is for](#creating-a-requirementstxt-can-be-empty-explaining-what-it-is-for)

# :woman: **About Me!**

> [!WARNING]
> Have tried to use as many markdown (and github flavoured markdown) features as possible so that I can refer to this page at a later date, please note this may elicit a sense that your timeline has reverted to the 1990s when myspace was a thing and people tried to make their page look as fancy as possible by using every known feature!

## Name
Alexandra aka ~~Branticus94 (please don't laugh at my username I made it circa 2019 when I was first dabbling with code, unmarried (hence Brant), using a nickname I was adorned with during my school years when I was rather fond of greek/roman history and mythology, think: this is sparta)~~ 'Alex' Howland

## Fun Facts

Proud mom to a beautiful 4 month old boy named Charlie[^1] 
> [!CAUTION]
> ***SPOILER: baby SPAM alert***, reveal collapsed section at your own mercy

  <details>
    
  <summary>👶🍼 Peekaboo!</summary>
  
  ![Picture of my adorable baby](Assignment 1/Photos/CharlieCanoeing.jpg)
    
  </details>

[^1]: Who very recently went on his first canoe journey

Favourite colour: $${\color{rgba(255, 223, 0, 0.8)}Yellow}$$ (Cool! Github released Tex support and now allow you to add colours to the markdown... oops I mean *colors* as I'm a coder now :smiley: ooooo, and smileys hello :eyes:)

Favourite coding related quote:
  > \"It’s not a bug; it’s an undocumented feature. Anonymous\"

Favourite 5 cuisines in order of preference:
1. Indian 
2. Thai
3. Italian
4. Mexican
5. Ethiopian

> [!NOTE]
> This list is not exhausitive, will eat any and all food 😆.

# Previous Projects
I have had the coding 💻 bug for a few years now and recently took part in the Python and apps kickstarter course!

I worked with a team of two other coders to create a nifty little [spreadsheet analysis application](https://github.com/branticus94/CFG_Python_Project/blob/main/SpreadsheetAnalysis.py) in python, here is a little video tour of our project: 

https://github.com/user-attachments/assets/ac460154-79c7-4c34-817e-c2ca8e159863

# How I will be using Github for this assignment
I will be using Github for this assignment as a remote repository to store code. 

In order to fulfil the requirements I needed to create a repo on github named Projects. I created the repo with the built in GUI in Github:

![image](https://github.com/user-attachments/assets/aaf5df65-14cc-41cb-be50-6952a23f729e)

I then used the computer terminal to create my file for upload to the remote repo. I first navigated  to the folder I wish to create my folder in using  the "cd" command (change directory), my preferred folder being documents. I checked I was in the correct directory with "ls" (list) command: 

```
AlexHowland@Toms-MacBook-Pro-2 ~ % ls
Applications	Documents	Library		Music		Public
Desktop		Downloads	Movies		Pictures	PycharmProjects
AlexHowland@Toms-MacBook-Pro-2 ~ % cd Documents
AlexHowland@Toms-MacBook-Pro-2 Documents % ls
Degree		Python		CV and Job Applications
```

Once  I was in the correct location I made a directory using the "mkdir" command, naming the directory Projects, again checking the output of my code as I went:

```
AlexHowland@Toms-MacBook-Pro-2 Documents % mkdir Projects
AlexHowland@Toms-MacBook-Pro-2 Documents % ls
Degree		Projects
Python		CV and Job Applications
```

Once the folder was created I used the "cd" command to change directory to within the folder, followed by the "git init" command to initialise git within the directory:
```
AlexHowland@Toms-MacBook-Pro-2 Documents % cd Projects
AlexHowland@Toms-MacBook-Pro-2 Projects % git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint: 
hint: 	git config --global init.defaultBranch <name>
hint: 
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint: 
hint: 	git branch -m <name>
Initialized empty Git repository in /Users/AlexHowland/Documents/Projects/.git/
```

I created a readme file using the "touch" command, confirming the output with the "ls" command:
```
AlexHowland@Toms-MacBook-Pro-2 Projects % touch README.md
AlexHowland@Toms-MacBook-Pro-2 Projects % ls
README.md
```

I then checked the git status, as you can see I am on the master/main branch, there have been no commits and I have one untracked file, the README.md file.  
```
AlexHowland@Toms-MacBook-Pro-2 Projects % git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	README.md

nothing added to commit but untracked files present (use "git add" to track)
```

I used the ''git add'' command to move my file from the local working directory into the local staging area to prepare for  the commit, using the "git status" command you can see I now have one file to be committed:
```
AlexHowland@Toms-MacBook-Pro-2 Projects % git add README.md
AlexHowland@Toms-MacBook-Pro-2 Projects % git status  
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   README.md
```

I then used "git commit" to move the file from the local staging area to the local repo with the message _'initial commit'_, I can see that there is one file changed with no insertions/deletions:
```
AlexHowland@Toms-MacBook-Pro-2 Projects % git commit -m 'initial commit'
[master (root-commit) 4b1de82] initial commit
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md
```

Finally to move the file from the local repo to the remote repo I performed the following. I used the git remote add origin command to specify the location of the remote repo where I wish to push/pull my files to/from. The git branch -M main command is used to rename the current branch from master to main to avoid naming conflicts. Finally I used the git push command to send my files to the remote repo on Github: 
```
AlexHowland@Toms-MacBook-Pro-2 Projects % git remote add origin git@github.com:branticus94/Projects.git
git branch -M main
git push -u origin main
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 222 bytes | 222.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To github.com:branticus94/Projects.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

To test out the "git pull" command I edited the markdown file in the github using the GUI:

<img width="800" alt="image" src="https://github.com/user-attachments/assets/0ad8105c-ed3f-4868-a9ef-4cc84557812d">

Once I had completed some of my write up, making a few commits along the way and testing the output/fixing any bugs (note to self: backticks for quoting code rather than single quotes!) to allow me to track my work! I then reverted to the terminal to test the connection and whether I could obtain the changes on my terminal, as you can see from the below I used the git pull command which produced a fast forward merge as there were no conflicts withere were several insertions and deletions to the README file I initially created: 

```
AlexHowland@Toms-MacBook-Pro-2 Projects % git pull
remote: Enumerating objects: 11, done.
remote: Counting objects: 100% (11/11), done.
remote: Compressing objects: 100% (9/9), done.
remote: Total 9 (delta 5), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (9/9), 5.62 KiB | 523.00 KiB/s, done.
From github.com:branticus94/Projects
   f8a7b68..02ef326  main       -> origin/main
Updating f8a7b68..02ef326
Fast-forward
 README.md | 114 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++--------------
 1 file changed, 100 insertions(+), 14 deletions(-)
AlexHowland@Toms-MacBook-Pro-2 Projects % 
```

I then used vim to review the file and continue documenting and working on my local machine (as you can see from my screenshot!:
![screenshot of using vim to edit README.md file](Photos/pullrequestvim.png)

I then repeated the process (getting a little quicker this time!) to send my local changes back to Github! So happy that I've managed to make it communicate both ways 😄

```
AlexHowland@Toms-MacBook-Pro-2 Projects % vi README.md
AlexHowland@Toms-MacBook-Pro-2 Projects % git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	pullrequestvim.png

no changes added to commit (use "git add" and/or "git commit -a")
AlexHowland@Toms-MacBook-Pro-2 Projects % git add .
AlexHowland@Toms-MacBook-Pro-2 Projects % git commit -m 'edited README.md describing pull request and edit markdown in vim'
[main 293cb1f] edited README.md describing pull request and edit markdown in vim
 2 files changed, 4 insertions(+), 1 deletion(-)
 create mode 100644 pullrequestvim.png
AlexHowland@Toms-MacBook-Pro-2 Projects % git push
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 1.05 MiB | 13.72 MiB/s, done.
Total 4 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:branticus94/Projects.git
   30589f5..293cb1f  main -> main
AlexHowland@Toms-MacBook-Pro-2 Projects % 
```

# Working with files in git and github

- [Checking the status](#checking-the-status)
- [Creating a branch](#creating-a-branch)
- [Adding files to a branch](#adding-files-to-a-branch)
- [Adding commits with meaningful messages](#adding-commits-with-meaningful-messages)
- [Opening a pull request]()
- [Merging and deploying to main branch]()

For this assignment I created a project which takes a users favourite ice cream flavour. I first created a directory to create my project in: 
```
AlexHowland@Toms-MacBook-Pro-2 Projects % ls
Photos			README.md		Secrets			requirements.txt	secret.txt
AlexHowland@Toms-MacBook-Pro-2 Projects % mkdir Favourite
```

I then changed to that directory and created a python file using vim which takes a user input and outputs a friendly message with the users input:
```
AlexHowland@Toms-MacBook-Pro-2 Projects % cd Favourite
AlexHowland@Toms-MacBook-Pro-2 Favourite % touch favourite.py
AlexHowland@Toms-MacBook-Pro-2 Favourite % vi favourite.py
AlexHowland@Toms-MacBook-Pro-2 Favourite % cat favourite.py
# Take user input for favourite ice cream flavour printing the output
favourite = input("What is your favourite ice cream flavour?")

print("No way! I love " + favourite + " too!")
```

## Checking the status
Now I wanted to add a new feature to this project, if the user input is chocolate I want to rickroll the user, displaying a picture of chocolate flavoured _'rick rolls'_. I first wanted to ensure that my python program was updated on main, so I used the git status command, I forgot to push these changes to github so I added, committed and pushed to my project:

```
AlexHowland@Toms-MacBook-Pro-2 Projects % git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	Favourite/

nothing added to commit but untracked files present (use "git add" to track)
AlexHowland@Toms-MacBook-Pro-2 Projects % git add .
AlexHowland@Toms-MacBook-Pro-2 Projects % git commit -m 'added favourite python project'
[main 4852a33] added favourite python project
 1 file changed, 4 insertions(+)
 create mode 100644 Favourite/favourite.py
AlexHowland@Toms-MacBook-Pro-2 Projects % git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 457 bytes | 457.00 KiB/s, done.
Total 4 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:branticus94/Projects.git
   d2f5815..4852a33  main -> main
```

## Creating a branch
I want to create my functionality on a separate branch so I used the "git branch" command to create a separate branch called 'if_chocolate':

```
AlexHowland@Toms-MacBook-Pro-2 Projects % git branch if_chocolate
AlexHowland@Toms-MacBook-Pro-2 Projects % git branch
  if_chocolate
* main
```

I then switched to work in that branch using "git checkout", I could have achieved the same by using "git checkout -b if chocolate" command which creates and switches to the branch in one fell swoop:
```
AlexHowland@Toms-MacBook-Pro-2 Projects % git checkout if_chocolate
Switched to branch 'if_chocolate'
```

As you can see all of my files/directories are within this branch still:
```
AlexHowland@Toms-MacBook-Pro-2 Projects % ls
Favourite		Photos			README.md		Secrets			requirements.txt	secret.txt
```

I then changed directory to Favourite, the location of my favourite ice cream flavour python program:
```
AlexHowland@Toms-MacBook-Pro-2 Projects % cd Favourite
AlexHowland@Toms-MacBook-Pro-2 Favourite % ls
favourite.py
```

I amended the program to use the pillow module to open an image of rick rolls:
```
AlexHowland@Toms-MacBook-Pro-2 Favourite % vi favourite.py 
AlexHowland@Toms-MacBook-Pro-2 Favourite % cat favourite.py
# Imports PIL module
from PIL import Image

# Take user input for favourite ice cream flavour printing the output
favourite = input("What is your favourite ice cream flavour?")

print("No way! I love " + favourite + " too!")

# If favourite flavour is chocolate display rick rolls:

if favourite.lower() == 'chocolate':
    image = Image.open('rick_rolls.jpeg')
    image.show()
```

## Adding files to a branch
I then added a jpeg file to this directory of 'rick rolls' which I moved from my downloads folderas you can see the folder now contains the program and the picture:
```
AlexHowland@Toms-MacBook-Pro-2 Favourite % mv /Users/AlexHowland/Downloads/rick_rolls.jpeg /Users/AlexHowland/Documents/Projects/Favourite
AlexHowland@Toms-MacBook-Pro-2 Favourite % ls
favourite.py	rick_rolls.jpeg
```

I used the git status command to check the status, as you can see I had a change to the favourite.py file and a new untracked file (the picture I just added):
```
AlexHowland@Toms-MacBook-Pro-2 Favourite % git status
On branch if_chocolate
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   favourite.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	rick_rolls.jpeg
no changes added to commit (use "git add" and/or "git commit -a")
```

## Adding commits with meaningful messages
I then added a commit on this branch using the "git add ." command to add all of the above changes and then the "git commit -m 'message'" command:
```
AlexHowland@Toms-MacBook-Pro-2 Favourite % git add .
AlexHowland@Toms-MacBook-Pro-2 Favourite % git status
On branch if_chocolate
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   favourite.py
	new file:   rick_rolls.jpeg

AlexHowland@Toms-MacBook-Pro-2 Favourite % git commit -m 'added if chocolate function to favourite program'
[if_chocolate 3ffc0b9] added if chocolate function to favourite program
 2 files changed, 9 insertions(+)
 create mode 100644 Favourite/rick_rolls.jpeg
```

I then used the git push command to push the branch and new commit to Github:
```
AlexHowland@Toms-MacBook-Pro-2 Favourite % git push
fatal: The current branch if_chocolate has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin if_chocolate

To have this happen automatically for branches without a tracking
upstream, see 'push.autoSetupRemote' in 'git help config'.

AlexHowland@Toms-MacBook-Pro-2 Favourite % git push --set-upstream origin if_chocolate
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 8 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 45.96 KiB | 11.49 MiB/s, done.
Total 5 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
remote: 
remote: Create a pull request for 'if_chocolate' on GitHub by visiting:
remote:      https://github.com/branticus94/Projects/pull/new/if_chocolate
remote: 
To github.com:branticus94/Projects.git
 * [new branch]      if_chocolate -> if_chocolate
branch 'if_chocolate' set up to track 'origin/if_chocolate'.
```

## Opening a pull request
I then went to Github to open my pull request:
![image](https://github.com/user-attachments/assets/95202c87-5585-4311-94c8-e32d4671a45a)
![image](https://github.com/user-attachments/assets/c2f28b28-a54e-4252-82a2-84fd13a6d567)

I reviewed the changes I made:
![image](https://github.com/user-attachments/assets/dab6b4b7-4672-490b-a341-7908df96db8f)

I then clicked 'create pull request':
![image](https://github.com/user-attachments/assets/2d102489-b9bc-4046-8642-993811be8e99)

As you can see this added my pull request:
![image](https://github.com/user-attachments/assets/64047202-22a7-4d8c-9763-45b689c67f1e)

## Merging and deploying to main branch
I then merged the pull request deploying to the main branch:
![image](https://github.com/user-attachments/assets/a62bdbbe-bfe6-4650-bab9-c8a0b6a9fd91)

As you can see I am on the main branch and can now see my new file 'rick_rolls.jpeg' as well as my updated favourite.py file:
![image](https://github.com/user-attachments/assets/f5d2987b-2a55-4dc7-81ed-6d240c018fff)

# Creating a .gitignore, explaining what it is for
Gitignore files are important files which allow the user to hide certain files or parts of the project which you would not want to share, protecting the git repository. It acts as a list of instructions of files or file directories or types of files that git needs to ignore. A .gitignore file is typically created in the repository's root directory.

Examples of such files would be files containing sensitive information (e.g. personal passwords, API keys, security certificates), files which are large as these bloat the system (e.g. compiled source), packages which have been used to make the program, files which hold local logs/databases operating system generated files (e.g. DS_store - mac file which holds information about the folder a file is in when viewing it using finder) or environment variables. 

You should use a .gitignore file to allow your repo to be clean (i.e. free from unnecessary files), secure and efficient. 

There are a couple of ways to create this file, one would be using the terminal. I would do this by navigatting to the root directory of the repo and using the "touch command", I was already in the root directory at this stage:

```
AlexHowland@Toms-MacBook-Pro-2 Projects % touch .gitignore
```

I would then use nano/vim (or indeed any text editor/IDE) to open and edit the file.

To save some time I could instead use templates (widely available for various programming languages and frameworks) as a starting point these can be found on [Github](https://github.com/github/gitignore).

The .gitignore file is then configured to either ignore specific files or directories by:
- Listing their name
- Ignoring specific directories by adding a slash to the directory name
- Ignoring files by extension using an asteriks before the file extension

I tested this out on my own machine I first created a secrets.txt file and Secrets directory with a supersecret.txt file within:

```
AlexHowland@Toms-MacBook-Pro-2 Projects % touch secrets.txt
AlexHowland@Toms-MacBook-Pro-2 Projects % ls
CharlieCanoeing.jpg	Create repo GitHub.png	README.md		Secrets			pullrequestvim.png	secrets.txt
AlexHowland@Toms-MacBook-Pro-2 Projects % vi secrets.txt   
AlexHowland@Toms-MacBook-Pro-2 Projects % git add .
AlexHowland@Toms-MacBook-Pro-2 Projects % git commit -m 'added secret file with empty gitignore'
[main 9ba08ff] added secret folder and file with empty gitignore
 1 file changed, 1 insertion(+)
 create mode 100644 secrets.txt
AlexHowland@Toms-MacBook-Pro-2 Projects % git push
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 365 bytes | 365.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:branticus94/Projects.git
   d3944bd..9ba08ff  main -> main
AlexHowland@Toms-MacBook-Pro-2 Projects % cd Secrets
AlexHowland@Toms-MacBook-Pro-2 Secrets % touch supersecret.txt
AlexHowland@Toms-MacBook-Pro-2 Secrets % ls
supersecret.txt
AlexHowland@Toms-MacBook-Pro-2 Secrets % cd ..
AlexHowland@Toms-MacBook-Pro-2 Projects % git add .
AlexHowland@Toms-MacBook-Pro-2 Projects % git commit -m 'added secret folder'
[main 31a80df] added secret folder
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 Secrets/supersecret.txt
AlexHowland@Toms-MacBook-Pro-2 Projects % git push
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 326 bytes | 326.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:branticus94/Projects.git
   9ba08ff..31a80df  main -> main
```

As you can see when I pushed my code, these files with an empty .gitignore file my secrets were shared with Github (oh no!):
![image](https://github.com/user-attachments/assets/29c349c7-f566-4982-97b6-7188042e515c)

I wouldn't want this to happen so I went about removing the files as per the below:
```
AlexHowland@Toms-MacBook-Pro-2 Projects % rm secrets.txt
AlexHowland@Toms-MacBook-Pro-2 Projects % cd Secrets
AlexHowland@Toms-MacBook-Pro-2 Secrets % ls
supersecret.txt
AlexHowland@Toms-MacBook-Pro-2 Secrets % rm supersecret.txt
AlexHowland@Toms-MacBook-Pro-2 Secrets % cd ..
AlexHowland@Toms-MacBook-Pro-2 Projects % rmdir Secrets
AlexHowland@Toms-MacBook-Pro-2 Projects % ls
CharlieCanoeing.jpg	Create repo GitHub.png	README.md		pullrequestvim.png
AlexHowland@Toms-MacBook-Pro-2 Projects % git add .
AlexHowland@Toms-MacBook-Pro-2 Projects % git commit -m 'removed secret files ready to test .gitignore'
[main 55df3d2] removed secret files ready to test .gitignore
 2 files changed, 1 deletion(-)
 delete mode 100644 Secrets/supersecret.txt
 delete mode 100644 secrets.txt
AlexHowland@Toms-MacBook-Pro-2 Projects % git push
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (2/2), 255 bytes | 255.00 KiB/s, done.
Total 2 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:branticus94/Projects.git
   31a80df..55df3d2  main -> main
```

As you can see my secrets were removed: 
![image](https://github.com/user-attachments/assets/d05a6cfd-d845-4348-a2eb-b245fe8b1a46)

I re-made the Secrets directory (with a supersecret.txt file inside) and secret.txt file using the "ls" command to prove their existence on my local machine:
```
AlexHowland@Toms-MacBook-Pro-2 Projects % mkdir Secrets
AlexHowland@Toms-MacBook-Pro-2 Projects % cd Secrets
AlexHowland@Toms-MacBook-Pro-2 Secrets % touch supersecret.txt
AlexHowland@Toms-MacBook-Pro-2 Secrets % cd ..
AlexHowland@Toms-MacBook-Pro-2 Projects % touch secret.txt
AlexHowland@Toms-MacBook-Pro-2 Projects % ls
CharlieCanoeing.jpg	Create repo GitHub.png	README.md		Secrets			pullrequestvim.png	secret.txt
```

I then update my .gitignore file using vim, pushing the results to my github repo:
```
AlexHowland@Toms-MacBook-Pro-2 Projects % vi .gitignore
AlexHowland@Toms-MacBook-Pro-2 Projects % cat .gitignore
# Ignore secret file 
secret.txt

# Ignore secrets folder 
Secrets/
AlexHowland@Toms-MacBook-Pro-2 Projects % git add .
AlexHowland@Toms-MacBook-Pro-2 Projects % git commit -m 'updated .gitignore'
[main b4e60a8] updated .gitignore
 1 file changed, 5 insertions(+)
AlexHowland@Toms-MacBook-Pro-2 Projects % git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 331 bytes | 331.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:branticus94/Projects.git
   55df3d2..b4e60a8  main -> main
```

My .gitignore file has now been updated on github:
![image](https://github.com/user-attachments/assets/d9b72f41-7693-4bbf-bd47-b46421dcf516)
![image](https://github.com/user-attachments/assets/d379c739-33d3-47d2-a85b-d1f726d8752d)

...and my secret files are safe and sound on my local machine, woohoo! 🥳:
```
AlexHowland@Toms-MacBook-Pro-2 Projects % ls -a
.			.git			CharlieCanoeing.jpg	README.md		pullrequestvim.png
..			.gitignore		Create repo GitHub.png	Secrets			secret.txt
AlexHowland@Toms-MacBook-Pro-2 Projects % 
```

# Creating a requirements.txt (can be empty), explaining what it is for
A requirements.txt is a text file which lists all of a python projects dependencies[^2] in one place. 

This is important for several reasons:
- Makes project easily reproducible on another machine - same environment allows you to produce the same results (hopefully!)
- Ensures compatibility - helps avoid conflicts between packages by ensuring the correct versions which currently work together are again used together on other machines
- When deploying the file a requirements.txt file is provided allowing the dependencies to be installed correctly
- Can manage dependencies (add/update/remove packages) easily as needed without manually keeping note of them.

One could use the command line to create an write a requirements.txt file and write the packages in the following format:
```
package_name == version_number
```
However this can get quite tedious. Thankfully, from my research I understand this can be done for you using an IDE (woohoo! 🥳).

I therefore tested this out by opening my python project using Pycharm IDE:
<img width="1440" alt="Screenshot 2024-09-02 at 13 37 40" src="https://github.com/user-attachments/assets/decb96f8-5d98-40a4-8246-284c18ede373">

I used the following pip[^3] command to generate the file:
```
pip freeze › requirements.txt
```

As if by magic the file was created and added straight to my project:
<img width="1440" alt="Screenshot 2024-09-02 at 13 37 46" src="https://github.com/user-attachments/assets/6d97e575-1fcb-4e03-83d3-4dcccd40f9be">

[^2]: Libraries or packages created by others which are used to make the project at hand e.g. matplot lib is a maths library which is commonly used
[^3]: Pip is a package manager for python packages or modules.
