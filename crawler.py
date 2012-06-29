def crawl_web(seed_url,max_depth):	         
        to_be_crawled = [[seed_url,0]]
	crawled = []
	index = {}
	graph = {}
	count =0;
	i = 0
	depth= 0
	while to_be_crawled:
                if i <= (len(to_be_crawled)-1):
                        now_crawling = to_be_crawled[i][0]
                        current_depth = to_be_crawled[i][1]
                        if now_crawling not in crawled:
                            page = get_page(now_crawling)                    
                            add_to_index(index,page,now_crawling)
                            obtained_links = get_all_links(page)
                            add_to_graph(graph,now_crawling,obtained_links)
                            for obtained_link_val in obtained_links:
                                if obtained_link_val not in crawled and obtained_link_val not in to_be_crawled and current_depth < max_depth:
                                        to_be_crawled.append([obtained_link_val,current_depth+1])                           
                            crawled.append(now_crawling)                                                                
                        i += 1
                else:
                        break
        return index,graph

def add_to_dictionary(dictionary,key,value):
    if key in dictionary:
        if value not in dictionary[key]:
            dictionary[key].append(value)
    else:
        dictionary[key] = [value]

def add_to_graph(index,keyword,obtained_urls):
        for url in obtained_urls:
            add_to_dictionary(index,keyword,url)                        


def add_to_index(index,page,url):
        for keyword in page.split():
            add_to_dictionary(index,keyword,url)                        

def get_all_links(page):    
    links =[]
    while True:        
	url,endPos = get_next_target(page)
	if url:		
                page = page[endPos+1:]                        
		links.append(url)
	else:
		break
    return links

def get_page(url):
        try:
               import urllib
               return urllib.urlopen(url).read()
        except:
               return ""
	
def get_next_target(page):
	start_link = page.find("<a href")
	if start_link == -1:
		return None,-1
	start_url = page.find('"',start_link+1);
	end_url = page.find('"',start_url+1);
	url = page[start_url+1:end_url]	
	return url,end_url


def lookup(index,keyword):
    if keyword in index:
        return index[keyword]
    return None

seed_url = 'http://www.cs.uic.edu'	
index,graph = crawl_web(seed_url,3)

#print lookup(index,'sujatha')

import re
url_name = re.search(r"\.([a-z]*)\.",seed_url).group(1)
index_file_name = str('index'+url_name+'.pkl')
graph_file_name = str('graph'+url_name+'.pkl')

import pickle
output_index = open(index_file_name, 'wb')
output_graph = open(graph_file_name, 'wb')
pickle.dump(index, output_index)
pickle.dump(graph, output_graph)
output_index.close()
output_graph.close()




