# CRUD - CRappy Utility Directory
Each directory in this repository is a seperate utility that I wrote (or stole, lmao), that saves me a few seconds here and there. Feel free to use any of them, but use at your own risk. Some (most) are not finished.

4 of them were made as their own repo before I organized them into CRUD, those being:

* [connect](http://github.com/llamicron/connect)
* [create_repo](http://github.com/llamicron/create_repo)
* [md_link_generator](http://github.com/llamicron/md_link_generator)
* [push_dotfiles](http://github.com/llamicron/push_dotfiles)

I'm am leaving the original repo there, but it will no longer be updated.

All of these use `make`, so go into the repo you want and run `make install`. Pretty simple. Most are Crystal lang/Ruby, so you may want to have those installed.

## Servers
You should be able to store ip addresses for your servers, raspberry pis, etc with a human-readable name. then run
```
$ servers connect [name]
```
to open up an ssh session.

## create_repo
This will create a repository on Github through the command line, as opposed to using the web interface. Good for rapid prototying where you don't want to mess up your flow. Takes seconds, and gives you a clickable link, if your terminal supports it. Run this and it will take you through the steps (after installing it (`make install`)):
```
$ create_repo
```

I understand that some people are uncomfortable entering your github password, but it's required for creating a repo. Check out the source code, I'm not doing anything malicious.

## md_link_generator
This will find all `.md` files in your project and generate a link to them. Mostly useless, but i use it occasionally. There are some test files in the project directory, so after installing it (`make install`), try running it (`$ md_link_gen`) from within that directory. Also, it's one line long, so that's pretty cool.

## push_dotfiles
This is a script that will commit and push changes in my `~/dotfiles` directory to github. I have a cron job running it daily. You can really use this with any git repo, but I use it for dotfiles.
