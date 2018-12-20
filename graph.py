from stack_array import * #Needed for Depth First Search
from queue_array import * #Needed for Breadth First Search

class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to = []
        self.checked = False
        self.color = None

class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified
           in the input file should appear on the adjacency list of each vertex of the two vertices associated
           with the edge.'''
        self.vertex_list = {}
        file = open(filename, "r")
        self.seen = {}
        for line in file:
            words = line.split() # Create a list of the two vertices in the pair

            if not words[0] in self.seen and words[1] in self.seen: # If left vertex not in list but right vertex is
                self.add_vertex(words[0]) # Add left vertex to list
                self.seen[words[0]] = None
                self.add_edge(words[0], words[1]) # Add each vertex to the other's adjacency list

            elif words[0] in self.seen and words[1] in self.seen: # If both vertices in list
                self.add_edge(words[0], words[1]) # Add each vertex to the other's adjacency list

            elif words[0] in self.seen and not words[1] in self.seen: # If left vertex in list but not right vertex
                self.add_vertex(words[1]) # Add right vertex to list
                self.seen[words[1]] = None
                self.add_edge(words[0], words[1]) # Add each vertex to the other's adjacency list

            else: # If neither vertex in list
                self.add_vertex(words[0]) # Add left vertex to list
                self.add_vertex(words[1]) # Add right vertex to list
                self.seen[words[0]] = None
                self.seen[words[1]] = None
                self.add_edge(words[0], words[1]) # Add each vertex to the other's adjacency list
        file.close()

    def add_vertex(self, key):
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        found = key in self.vertex_list.keys()
        if not found: # If no vertex in list with given key as id, add to vertex list
            new_vertex = Vertex(key)
            self.vertex_list[key] = new_vertex

    def get_vertex(self, key):
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        try:
            return self.vertex_list[key]
        except:
            return None

    def add_edge(self, v1, v2):
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        self.vertex_list[v1].adjacent_to.append(v2) # Add second vertex to first vertex's adjacency list
        self.vertex_list[v2].adjacent_to.append(v1) # Add first vertex to second vertex's adjacency list

    def get_vertices(self):
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        keys = list(self.vertex_list.keys())
        keys.sort()
        return keys

    def conn_components(self):
        '''Returns a list of lists.  For example, if there are three connected components
           then you will return a list of three lists.  Each sub list will contain the
           vertices (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item of each sublist.
           This method MUST use Depth First Search logic!'''
        connected = []
        key_list = self.get_vertices()
        stack = Stack(len(self.vertex_list))
        for key in key_list:
            if not self.vertex_list[key].checked:
                sub_list = []
                stack.push(self.vertex_list[key])
                while not stack.is_empty():
                    s = stack.peek()
                    sub_list.append(stack.pop().id)
                    if not s.checked:
                        s.checked = True
                    adj_list = []
                    for vertex in s.adjacent_to:
                        adj_list.append(vertex)
                    for i in range(len(adj_list)):
                        if not self.vertex_list[adj_list[i]].checked:
                            stack.push(self.vertex_list[adj_list[i]])
                            self.vertex_list[adj_list[i]].checked = True
            sub_list.sort()
            if len(connected) == 0 or connected[-1] != sub_list:
                connected.append(sub_list)
        # connected.sort(key=lambda x: x[0])
        return connected

    def is_bipartite(self):
        '''Returns True if the graph is bicolorable and False otherwise.
           This method MUST use Breadth First Search logic!'''
        vertex_queue = Queue(len(self.vertex_list))
        for k in self.vertex_list:
            current_vertex = self.vertex_list[k]
            vertex_queue.enqueue(current_vertex)
            if current_vertex.color is None:
                current_vertex.color = 0
            while not vertex_queue.is_empty():
                current_vertex = vertex_queue.dequeue()
                for v in current_vertex.adjacent_to:
                    if self.vertex_list[v].color == current_vertex.color:
                        return False
                    elif self.vertex_list[v].color is None:
                        if current_vertex.color == 0:
                            self.vertex_list[v].color = 1
                        else:
                            self.vertex_list[v].color = 0
                        vertex_queue.enqueue(self.vertex_list[v])
        return True

# g = Graph("vertices.txt")
# g.is_bipartite()
