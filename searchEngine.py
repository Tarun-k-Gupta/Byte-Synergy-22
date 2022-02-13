from googlesearch import search


def searchFor():
    searchFile = open("search.txt", 'r')
    linkFile = open("links.txt", 'w')
    text = searchFile.read()
    searchList = search(text, tld='co.in', num=10, stop=10, pause=2)
    wiki = "en.wikipedia.org"
    for link in searchList:
        linkFile.write(link + '\n')
        if(link.split('/')[2] == wiki) :
            linkFile.write("TRUE\n")
        else:
            linkFile.write("FALSE\n")

searchFor()
