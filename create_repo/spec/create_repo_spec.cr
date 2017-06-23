require "./spec_helper"

describe CreateRepo do

  it "has a version number" do
    CreateRepo::VERSION.should be_a String
  end

  describe "#new" do
    it "can return a repo object" do
      CreateRepo::Repo.new.should be_a CreateRepo::Repo
    end

    it "can have a username and repo_name" do
      repo = CreateRepo::Repo.new("llamicron", "test_repo")
      repo.username.should be_a String
      repo.repo_name.should be_a String
    end
  end

end
