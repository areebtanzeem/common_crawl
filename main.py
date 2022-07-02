import cdx_toolkit
import sys



cdx = cdx_toolkit.CDXFetcher(source='cc')

url = str(input("Enter Domain Name: "))
path = str(input("Enter File Path: "))
links = cdx.iter(url, limit=99999999999999999999999999)
all_links = []

for obj in links:
    all_links.append(obj['url'])

sanitized = list(set(all_links))


with open(path,"w") as f:
    for obj in sanitized:
        print(obj)
        f.write(obj+"\n")

