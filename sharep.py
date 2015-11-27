import urllib2
import argparse

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

	
parser = argparse.ArgumentParser(description='Sharepoint Scanner')
parser.add_argument('--url', type=str, help='URL of the Sharepoint instance (e.g. http://enisa.europa.eu')
parser.add_argument('--file', type=str, help='URL resource list', required=True)
args = parser.parse_args()
parser.print_help()
	
fobj = open(args.file)
target_url = args.url

full_urls = []
for line in fobj:
	line = line.strip('\n')
	full_urls.append(target_url+line)

for url in full_urls:
    try:
        connection = urllib2.urlopen(url)
        print connection.getcode(),url 
        connection.close()
    except urllib2.HTTPError, e:
        print e.getcode(), url

