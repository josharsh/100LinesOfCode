require 'open-uri'
require 'multi_xml'
require 'nokogiri'
require 'net/http'

puts 'Please input valid rss url: '
url = gets.chomp
		 
# convert @url variable to a URI
uri = URI(url)

# initialize response with the uri
begin
    response = Net::HTTP.get(uri)

rescue SystemCallError => e
    p 'Invalid rss or no internet connection'
else
    # parse the XML using Nokogiri
    doc = MultiXml.parse(response) 

    doc1 = doc['rss']['channel']
    title = doc['rss']['channel']['description']

    puts 'Title: ' + title
    puts ''

    # iterate through the first <item> tag
    doc1.each do |name, content|
        if name == 'item'
            puts "Description: #{content[0]['title']}"
            puts ''
            puts "Link: #{content[0]['link']}"
        end
    end
end
