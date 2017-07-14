require "yaml"
require "terminal_table"

if ARGV.empty?
  command = "help"
  args = [] of String
else
  command = ARGV[0]
  args = ARGV
  args.shift
end

servers = {} of String => Tuple(String, String)

storage = File.expand_path("~/.servers.yml")

if File.exists?(storage)
  unless File.empty?(storage)
    YAML.parse(File.read(storage)).each do |name, address|
      servers[name.to_s] = {address[0].to_s, address[1].to_s}
    end
  end
end

case command
when "add"
  print "Enter a memorable name for this server: "
  name = gets
  print "Enter the username you want to login with: "
  username = gets
  print "Server IP: "
  ip = gets

  servers[name.to_s] = {username.to_s, ip.to_s}

  # Store details
  File.open(storage, "w") do |f|
    YAML.dump(servers, f)
  end
when "list"
  server_table = TerminalTable.new
  server_table.headings = ["Name", "Address"]
  servers.each do |name, ip|
    server_table << [name.to_s, ip[0].to_s + "@" + ip[1].to_s]
  end
  puts server_table.render
when "help"
  puts <<-help
    <-- servers -->

    Important: You need to have ssh keys setup on the server you want to connect to

    Commands:
    servers list           :   List all stored servers
    servers add            :   Store a new server
    servers connect [name] :   Connect to a server
    servers clear          :   Erases all stored servers (Caution)

    ---

    TIP: run
      servers list | grep [name]
    to search for a specific server

    <---->
  help
when "connect"
  server_name = args[0] unless args.empty?
  if !server_name
    print "Please enter a server name: "
    server_name = gets.to_s
  end
  server = servers[server_name]
  system("ssh #{server[0]}@#{server[1]}")
when "clear"
  print "Are you sure you want to erase all stored servers? This can't be undone [y/n]: "
  choice = gets
  if choice
    if choice.to_s == "y"
      File.delete(storage)
      puts "Cleared"
    else
      puts "Nothing cleared"
    end
  end
end
