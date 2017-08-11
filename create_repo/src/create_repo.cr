require "./create_repo/*"
require "stdio"

include CreateRepo::Helpers

module CreateRepo
  class Repo

    property :url, :username, :repo_name

    def initialize(username="", repo_name="")
      @url = "https://api.github.com/user/repos"
      @username = username
      @repo_name = repo_name
    end

    def create
      raise "You need to provide a url" unless !@url.empty?
      print "Github password:"
      capture_stdout {
        `curl -u #{@username} \"https://api.github.com/user/repos\" -d \'{\"name\":\"#{@repo_name}\"}\'`
      }
    end

  end
end
