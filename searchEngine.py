from googlesearch import search


def searchFor():
    searchFile = open("search.txt", 'r')
    linkFile = open("links.txt", 'w')
    text = searchFile.read()
    searchList = search(text, tld='co.in', num=10, stop=10, pause=2)
    for link in searchList:
        linkFile.write(link + '\n')

searchFor()