import requests 
from bs4 import BeautifulSoup, SoupStrainer

content = requests.get('https://github.com/acgeospatial/awesome-earthobservation-code/blob/master/README.md').content
lslink =[]
for link in BeautifulSoup(content, parse_only=SoupStrainer('a')):
  if hasattr(link, "href"):
    lslink.append(link['href'])
## I've added flags on the readme.md page to know where the links reside.
lslink_filter=[]
flag = False
for _, value in enumerate(lslink):
    if value == '#start-here':
        flag = True
    if value == '#end':
        flag = False
    else:
        pass
    if flag == True:
        lslink_filter.append(value)
## lskink_filter should contain all the urls and junk between start-here and end        
ls_final = list(filter(lambda k: 'https' in k, lslink_filter)) ## remove all the non urls

## adapted from https://pastebin.com/wf2SgCZp

_OUTPUT_FILENAME = "awesome-eo-code-bookmarks.html"
 
fout = open(_OUTPUT_FILENAME, 'w')

# Write the header
fout.write("""<!DOCTYPE NETSCAPE-Bookmark-file-1>
<!-- This is an automatically generated file.
    It will be read and overwritten.
    DO NOT EDIT! -->
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Awesome-EO-code-Bookmarks</TITLE>
<H1>EO-Bookmarks</H1>
<DL><p>\n""")
 

for row in ls_final:
        fout.write('\t<DT><A HREF="')
        fout.write(row)
        fout.write('">')
        fout.write(row)
        fout.write('</A>\n')
 
fout.write('</DL><p>\n')
 
fout.close()
