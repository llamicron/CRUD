# Prettier version
# Dir.glob("**/*").select { |file| file.ends_with?(".md") }.each { |file| puts "[#{file.chomp(".md")}]" + "(#{file})" + "\n\n" }
# Shorter version. I know it's against style guides but I need to save those characters
Dir.glob("**/*").select{|f|f.ends_with?(".md")}.each{|f|puts "[#{f.chomp(".md")}]"+"(#{f})"+"\n\n"}
