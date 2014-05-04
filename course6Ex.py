#这里采取集合存储网页和相关内容，实际编程环境中通过urllib进行获取
cache = {
   'http://udacity.com/cs101x/urank/index.html': """<html>
<body>
<h1>Dave's Cooking Algorithms</h1>
<p>
Here are my favorite recipies:
<ul>
<li> <a href="http://udacity.com/cs101x/urank/hummus.html">Hummus Recipe</a>
<li> <a href="http://udacity.com/cs101x/urank/arsenic.html">World's Best Hummus</a>
<li> <a href="http://udacity.com/cs101x/urank/kathleen.html">Kathleen's Hummus Recipe</a>
</ul>

For more expert opinions, check out the 
<a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a> 
and <a href="http://udacity.com/cs101x/urank/zinc.html">Zinc Chef</a>.
</body>
</html>






""", 
   'http://udacity.com/cs101x/urank/zinc.html': """<html>
<body>
<h1>The Zinc Chef</h1>
<p>
I learned everything I know from 
<a href="http://udacity.com/cs101x/urank/nickel.html">the Nickel Chef</a>.
</p>
<p>
For great hummus, try 
<a href="http://udacity.com/cs101x/urank/arsenic.html">this recipe</a>.

</body>
</html>






""", 
   'http://udacity.com/cs101x/urank/nickel.html': """<html>
<body>
<h1>The Nickel Chef</h1>
<p>
This is the
<a href="http://udacity.com/cs101x/urank/kathleen.html">
best Hummus recipe!
</a>

</body>
</html>






""", 
   'http://udacity.com/cs101x/urank/kathleen.html': """<html>
<body>
<h1>
Kathleen's Hummus Recipe
</h1>
<p>

<ol>
<li> Open a can of garbonzo beans.
<li> Crush them in a blender.
<li> Add 3 tablesppons of tahini sauce.
<li> Squeeze in one lemon.
<li> Add salt, pepper, and buttercream frosting to taste.
</ol>

</body>
</html>

""", 
   'http://udacity.com/cs101x/urank/arsenic.html': """<html>
<body>
<h1>
The Arsenic Chef's World Famous Hummus Recipe
</h1>
<p>

<ol>
<li> Kidnap the <a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a>.
<li> Force her to make hummus for you.
</ol>

</body>
</html>

""", 
   'http://udacity.com/cs101x/urank/hummus.html': """<html>
<body>
<h1>
Hummus Recipe
</h1>
<p>

<ol>
<li> Go to the store and buy a container of hummus.
<li> Open it.
</ol>

</body>
</html>

""", 
}

#搜索操作：根据关键字找出权重最大的网页url
def lucky_search(index, ranks, keyword):
    url = lookup(index, keyword)
    if url==None:
        return None
    else:
        #print(url)
        #print(ranks)
        max = 0
        right = ""
        for entry in url:
            if  max < ranks[entry]:
                max = ranks[entry]
                right = entry
        return right


#计算每个网址对应的权重，类似于google的pagerank
def compute_ranks(graph):
    d = 0.8 # damping factor
    numloops = 10
    
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages
    
    for i in range(0, numloops):
        newranks = {}
        for page in graph:            
            newrank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    #print(page)
                    newrank = newrank + d * (ranks[node] / len(graph[node]))
            newranks[page] = newrank
        ranks = newranks
    return ranks


#爬虫根据seed页面爬取整个网络，获得每个url对应的链接列表，即返回值graph及关键词所对应的url列表
def crawl_web(seed): # returns index, graph of inlinks
    tocrawl = [seed]
    crawled = []
    graph = {}  # <url>, [list of pages it links to]
    index = {} 
    while tocrawl: 
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            graph[page] = outlinks            
            union(tocrawl, outlinks)
            crawled.append(page)
    return index, graph


#获取url网址中的网页内容
def get_page(url):
    if url in cache:
        return cache[url]
    else:
        return None

#获取当前网页中的下一个链接
def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

#获取当前网页中所有链接
def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


#合并操作
def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)
            
#把每个url和对应的网页内容加入到集合index中
def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

#把网页中出现的每个关键词和出现的url列表进行映射
def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]
        
#根据关键词进行查找
def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None



index , graph = crawl_web('http://udacity.com/cs101x/urank/index.html') 
if 'http://udacity.com/cs101x/urank/index.html' in graph:
    print(graph['http://udacity.com/cs101x/urank/index.html'])
#print(index)
print(graph)
ranks = compute_ranks(graph)
print(ranks)
print(lucky_search(index, ranks, 'Hummus'))
print(lucky_search(index, ranks, 'the'))
print (lucky_search(index, ranks, 'babaganoush'))

