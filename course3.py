p =[0,1,1]
p[0] = p[0]+p[1]
p[1] = p[0]+p[2]
p[2] = p[0]+p[1]
print(p)


udacious_univs = [['Udacity',90000,0]]

usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]

def total_enrollment(li):
    result = [0,0]
    tution,students = 0,0
    i,j=0,0
    while i<len(li):
        students = students+li[i][1]
        tution = tution+li[i][1]*li[i][2]
        i = i+1
    result[0] = students
    result[1] = tution
    return  result[0], result[1]

print(total_enrollment(udacious_univs))
print(total_enrollment(usa_univs))




def get_page(url):
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return  '<html> <body> This is a test page for learning to crawl! <p> It is a good idea to  <a href="http://www.udacity.com/cs101x/crawling.html">learn to crawl</a> before you try to  <a href="http://www.udacity.com/cs101x/walking.html">walk</a> or  <a href="http://www.udacity.com/cs101x/flying.html">fly</a>. </p> </body> </html> '
        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return  '<html> <body> I have not learned to crawl yet, but I am quite good at  <a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>. </body> </html>'
        elif url == "http://www.udacity.com/cs101x/walking.html":
            return '<html> <body> I cant get enough  <a href="http://www.udacity.com/cs101x/index.html">crawling</a>! </body> </html>'
        elif url == "http://www.udacity.com/cs101x/flying.html":
            return '<html> <body> The magic words are Squeamish Ossifrage! </body> </html>'
    except:
        return ""
    return ""

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)


def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


#def crawl_web(seed,max_pages):
def crawl_web(seed,max_depth):
    tocrawl = [seed]
    crawled = []
    #index=[]
    havecrawled = [seed]
    depth,count = 0,0
    while tocrawl:
        #print(havecrawled)
        page = tocrawl.pop()
        #if page not in crawled and count<max_pages :
        if page not in crawled:
            #if get_all_links(get_page(page)) not in havecrawled :
            #print(get_all_links(get_page(page)))
            if depth<max_depth:
                depth = depth +1
                union(tocrawl, get_all_links(get_page(page)))
                #union(havecrawled, get_all_links(get_page(page)))
            crawled.append(page)


            #content = get_page(page)
            #add_page_to_index(index,page,content):
            #union(tocrawl, get_all_links(content))
            #crawled.append(page)
        #return index






    return crawled


def check_havecrawled(links):

    return False


print(crawl_web("http://www.udacity.com/cs101x/index.html",0))
print(crawl_web("http://www.udacity.com/cs101x/index.html",1))
print(crawl_web("http://www.udacity.com/cs101x/index.html",2))
#print(crawl_web("http://www.udacity.com/cs101x/index.html",10))
