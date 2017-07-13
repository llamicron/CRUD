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

storage = File.expand_path("~/.servers.yml")
unless File.empty?(storage)
  servers = YAML.parse(File.read(storage)).as_h
else
  servers = {} of String => String
end

case command
when "add"
  print "Enter a memorable name for this server: "
  name = gets
  print "Enter the username you want to login with: "
  username = gets
  print "Server IP: "
  ip = gets

  servers[name.to_s] = "#{username.to_s}@#{ip.to_s}"

  # Store details
  File.open(storage, "w") do |f|
    YAML.dump(servers, f)
  end
when "list"
  server_table = TerminalTable.new
  server_table.headings = ["Name", "Address"]
  servers.each do |name, ip|
    server_table << [name.to_s, ip.to_s]
  end
  puts server_table.render
when "help"
  puts <<-help
    servers
    servers list   :   List all stored servers
    servers add    :   Store a new server
    ---
    TIP: run
      servers list | grep [name]
    to search for a specific server
  help
end
