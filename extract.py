import sys

def extract(namefile):
	UrlDatabase = dict()
	url_list = open(namefile, 'r')
	
	#builds a dictionary with urls as keys and urls as values
	for line in url_list:
		junk_line, line = line.split("=", 1)
		url, line = line.split(" ", 1)
		url = url.strip('"')
		junk_line, line = line.split("tags=") 
		tags, junk_line = line.split(">", 1)
		tags = tags.strip('"')
		tag_list = tags.split(",")
		UrlDatabase[url] = tag_list
		
	for key in UrlDatabase:	#DEBUG
		print key, UrlDatabase[key]
		
	url_list.close()
	
extract('urls.html') #DEBUG
