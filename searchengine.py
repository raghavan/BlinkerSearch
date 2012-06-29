import pickle

#read python dict back from the file
index = {}
graph = {}
try:
	output_index = open('index.pkl', 'rb')
	output_graph = open('graph.pkl', 'rb')
	index = pickle.load(output_index)
	graph = pickle.load(output_graph)
	output_index.close()
	output_graph.close()
except:
	print ""
	
def lookup(index,keyword):
    if keyword in index:
        return index[keyword]
    return None


while True:
	print "Enter a text to search "
	keyword = raw_input(">")
	if keyword == 'Exit' or keyword == 'exit':
		exit()
	else:
		print lookup(index,keyword)
		


