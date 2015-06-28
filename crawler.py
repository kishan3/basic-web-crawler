from bs4 import BeautifulSoup
import urllib2
import re

'''asking user for root page to begin with '''
seed_page = raw_input("enter a url to begin : ")

'''asking for how much we want to crawl'''
numberOfPages = int (raw_input("enter number of pages to be crawled :"))


tocrawl =[]
crawled = []
def get_all_links(url):
    '''This function takes a url and returns all the links 
    present on that page '''
    
    fetched_page = urllib2.urlopen(url)

    #reading the fetched page

    page_text = fetched_page.read()
    
    soup = BeautifulSoup(page_text)
    repositoryOfLinks = soup.find_all('a', attrs={'href' : re.compile('^http://')}) 
    
    return repositoryOfLinks


def crawl_web(seed_page):
    
    
    '''This function take a root url and start parsing from that 
    page until number of pages to be crawled are reached.
        It returns crawled pages and pages that are yet to be crawled 
    '''
    
    tocrawl = [seed_page]
    crawled = []
    #checking how many pages we have crawled
    while len(crawled) < numberOfPages:
        #This is a DFS on each new page last link     
        #will be traversed first
        page = tocrawl.pop()
        # print page
        if page != seed_page:
            page = page['href']
        if page not in crawled:
            links = get_all_links(page)
            #print "len of tocrawl" , len(tocrawl)
            tocrawl.extend(links)
            crawled.append(page)
        #len(tocrawl)   
    return crawled , tocrawl

#print tocrawl

crawled , tocrawl = crawl_web(seed_page)
print "This are the links we have crawled so far : " , crawled
print "This are the links we are yet to crawl : " , tocrawl
print "Length of tocrawl : " , len(tocrawl)