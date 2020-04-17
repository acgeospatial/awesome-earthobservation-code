import requests 
from bs4 import BeautifulSoup, SoupStrainer
from datetime import datetime
today = str(datetime.today().strftime('%Y-%m-%d'))

content = requests.get('https://github.com/acgeospatial/awesome-earthobservation-code/blob/master/README.md').content
lslink =[]
flag = False
for link in BeautifulSoup(content, parse_only=SoupStrainer('a')):
    if hasattr(link, "href"):
        if (link['href']) == '#start-here':
            flag = True
        if (link['href']) == '#end':
            flag = False
        else:
            pass
        if flag == True:
            if 'https' in (link['href']):
                lslink.append(link['href'])
            else:
                pass

## adapted from https://pastebin.com/wf2SgCZp
_OUTPUT_FILENAME = today+"-awesome-eo-code-bookmarks.html"

with open(_OUTPUT_FILENAME, 'w') as f:

    # Write the header
    f.write("""<!DOCTYPE NETSCAPE-Bookmark-file-1>
    <!-- This is an automatically generated file.
        It will be read and overwritten.
        DO NOT EDIT! -->
    <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
    <TITLE>Awesome-EO-code-Bookmarks</TITLE>
    <H1>EO-Bookmarks</H1>
    <DL><p>\n""")

    for row in lslink:
            f.write('\t<DT><A HREF="')
            f.write(row)
            f.write('">')
            f.write(row)
            f.write('</A>\n')

    f.write('</DL><p>\n')
