require "./src/create_repo.cr"

unless ARGV.size == 2
  print "Github username: "
  username = gets.to_s.chomp
  print "Repository name: "
  repo_name = gets.to_s.chomp
else
  if ARGV.include? "--login"
    CreateRepo::login
  end
  username = ARGV[0]
  repo_name = ARGV[1]
end

repo = CreateRepo::Repo.new(username, repo_name)

repo.create

puts ""
puts "Repository created at http://github.com/#{username}/#{repo_name}"
