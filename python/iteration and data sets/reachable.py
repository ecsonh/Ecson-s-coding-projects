# Submitter: ecsonh(Hsu, Ecson)
# Partner  : ricarddr(Reyes, Ricardo)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming
import goody
import prompt
from collections import defaultdict


def read_graph(file : open) -> {str:{str}}:
    
    graph_dict={}
    with file as open_file:
        for line in open_file:
            v =line.rstrip('\n').split(';')[0]
            k =line.rstrip('\n').split(';')[1]
            if v not in graph_dict.keys():
                graph_dict[v] = {k}
            else:
                    graph_dict[v].add(k)
                
    return graph_dict


def graph_as_str(graph : {str:{str}}) -> str:
    string = ''
    for i,j in {v:[i for i in sorted(graph[v])] for v in sorted(graph.keys(), key = lambda x: x[0])}.items():
        string += "  " + str(i) +' -> ' + str(j)+'\n'
    return string
            
        
def reachable(graph : {str:{str}}, start : str, trace : bool = False) -> {str}:
    
    reached = set()
    search = [start]
    pri = 0
    
    if graph.get(start) != None:
        
        while search != []:
            for v, n in {v:[i for i in sorted(graph[v])] for v in sorted(graph.keys(), key = lambda x: x[0])}.items():
                if search != []:
                    
                    pri = 0
            
                    if v == search[0]:
                        if pri == 0 and trace == True:
                            print("reached set    =", reached)
                            print("exploring list =", search)
                            print("transferring node", search[0] ,"from the exploring list to the reached set")
                            pri = 1
                            
                        if search[0] in reached:
                            search.remove(search[0])
                        else:
                            search = [*search, *n[:: -1]]
                            reached.add(search[0])
                            search.remove(search[0])
                        
                    elif search[0] not in graph:
                        
                        if pri == 0 and trace == True:
                            print("reached set    =", reached)
                            print("exploring list =", search)
                            print("transferring node", search[0] ,"from the exploring list to the reached set")
                            pri = 1
                        
                        reached.add(search[0])
                        search.remove(search[0])
                        
                    if pri == 1 and trace == True:
                        print("after adding all nodes reachable directly from", v ," but not already in reached, exploring =", search)
                        print('')
                        pri = 2
                        
        return reached
    
    else:
        
        return None


if __name__ == '__main__':
    # Write script here
    file = open(input("Input the file name detailing the graph: "))
    
    graph = read_graph(file)
    
    print("\nGraph: str (source node) -> [str] (sorted destination nodes)")
    print(graph_as_str(graph))
    
    while True:
        node = input("Input one starting node (or input done): ")
        if node == 'done':
            break
        else:
            edge = reachable(graph, node)
            if edge == None:
                print("  Entry Error: '" + node + "';  Illegal: not a source node\n  Please enter a legal String")
            else:
                tracing = input("Input tracing algorithm option[True]: ")
                if tracing == "True":
                    edge = reachable(graph, node, True)
                print("From the starting node", node + ", its reachable nodes are:", edge)
        print('')
    
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
