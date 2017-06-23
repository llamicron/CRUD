#!/usr/bin/env ruby
require "git"

log = Dir.home + "/.push_dotfiles.log"
dotfiles_dir = Dir.home + "/dotfiles/"

File.open(log, "a") do |file|
  file.puts "\n---\n"
  file.puts "Attempted push at " + Time.now.to_s

  begin
    dotfiles = Git.init(dotfiles_dir)
    dotfiles.add(:all=>true)
    dotfiles.commit_all("Automated push at " + Time.now.to_s)
    dotfiles.push
    file.puts "Push successful"
  rescue Git::GitExecuteError
    file.puts "Nothing to push"
  end

  file.puts "End of push"
end

