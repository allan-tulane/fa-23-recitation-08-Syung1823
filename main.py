from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    vis = dict()
    fron = []
    edges = dict()
    edges['s'] = 0
    heappush(fron, (0, source))
    while len(fron) != 0:
        dis, node = heappop(fron)
      
        if node in vis:
            continue
        
        vis[node] = (dis,edges[node])
        

        for n, w in graph[node]:
            if n in edges:
                edges[n] = min(edges[node] + 1, edges[n])
            else:
              edges[n] = edges[node] + 1
            heappush(fron, (dis + w, n))
    
    
    return vis




    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    vis = set()
    fron = set()
    path = dict()
    fron.add(source)


    while len(fron) != 0:
        for i in fron:
            node = i
            break
        if node in vis:
            fron.pop(0)
            continue
        else:
            vis = vis|fron
        temp = []
        for node in fron:
            for n in graph[node]:
                if n in vis:
                    continue
                else:
                    path[n] = node
                    temp.append(n)
        fron.clear()
        fron = set(temp)

    return path



   
        





def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }
graph = get_sample_graph()
parents = bfs_path(graph, 's')  
print(parents)

    
def get_path(parents, destination):
    temp = destination
    prev = ''
    final = ''
    while True:
        if temp =='s':
            break
        else:
            temp = parents[temp]
            final += temp


    return final[::-1]
    

