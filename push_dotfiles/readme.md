# Push Dotfiles
This is a script that will automatically commit and push my `~/dotfiles` directory to github, so I don't have to worry about it. I have this configured with crontab, to run every day.

Logfile and dotfiles location is specified in `push_dotfiles.rb`. Change those to the correct information for your system, then run `make install`. That will copy `push_dotfiles.rb` to `~/bin/push_dotfiles` (note the lack of `.rb`), and add execution to it (requires `sudo`). You may need to create `~/bin` if you don't already have it.
