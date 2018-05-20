import requests
import sys
from bs4 import BeautifulSoup

def importBookmarks(bookmark):
	savedUrl = 'http://devapi.saved.io/bookmarks/'
	payload =  bookmark
	
	r = requests.post(savedUrl, params=payload)
	if r.status_code == 200:
		return
	else:
		print("\nERROR: ", r.status_code)
		return
	

def main(argv):


	devkey = "YOUR_DEVKEY"
	key = "YOUR_KEY"


	bookmarks = []
	collection = "Inbox"
	with open(argv[0], 'rb') as html:
		for line in html:
			soup = BeautifulSoup(line, "html5lib")

			if soup.h3 != None:
				if soup.h3.contents[0] == "Inbox":
					continue
				collection = soup.h3.contents[0]
				continue

			if soup.a != None:
				bookmarkTitle = soup.a.contents[0]
				bookmarkUrl = soup.a.get('href')
				if collection == "Inbox":
					bookmark = {
						'devkey': devkey,
						'key': key,
						'url': bookmarkUrl,
						'title': bookmarkTitle,
					}
				elif collection == "Trash":
					continue
				else:
					bookmark = {
						'devkey': devkey,
						'key': key,
						'url': bookmarkUrl,
						'title': bookmarkTitle,
						'list': collection
					}
				bookmarks.append(bookmark)

	print("IMPORTING\n")
	for bookmark in bookmarks:
		importBookmarks(bookmark)
	print("DONE\n")

	return


main(sys.argv[1:])