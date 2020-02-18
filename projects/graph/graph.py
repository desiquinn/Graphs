"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # TODO
        # vertex represented as a key:set pair
        # key - node
        # set - the value
        self.vertices[vertex_id] = set()  

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # TODO
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Can not create edge based on given vertices")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # TODO
        # same as get all edges, or get all adjacencies
        # returns an agajency list
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # TODO
        # Create a queue
        # one letter variables are hard to debug, linter don't like them
        queue = Queue()
        # Create a visited set (use set because O(1) search)
        visited = set()
        # Add starting node to the queue
        queue.enqueue(starting_vertex)
        # While: queue is not empty
        while queue.size() > 0:
            # Pop first node out of queue
            vertex = queue.dequeue()
            # if not visted
            if vertex not in visited:
                # mark as visited
                visited.add(vertex)
                # Here is where we should print vertex bc it was just visted
                print(vertex)
                # get adjacent edges and add to list
                for neighbor in self.get_neighbors(vertex):
                    queue.enqueue(neighbor)
        # goto top of loop - happens automatically

        """
        We have to figure out where to print each vertex
        step1: is the problem something we can solve with graphs
        step2: translate problem into graph language
        step3: where do we insert some sort of function or do something
        in it somewhere.
        The question is, what is is asking us to do, and where do we want
        to do it? Usually right after it's visited.
        """

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # TODO
        # Create a stack
        stack = Stack()
        # Create a visited set (use set because O(1) search)
        visited = set()
        # Add starting node to the stack
        stack.push(starting_vertex)
        # While: stack is not empty
        while stack.size() > 0:
            # Pop first node out of stack
            # the difference between bft and dft is when you
            # take the item out.  bft order doesn't matter
            # with dft order it has to come out first
            vertex = stack.pop()
            # if not visted
            if vertex not in visited:
                # mark as visited
                visited.add(vertex)
                # Here is where we should print vertex bc it was just visted
                print(vertex)
                # get adjacent edges and add to list
                for neighbor in self.get_neighbors(vertex):
                    stack.push(neighbor)
        # goto top of loop - happens automatically


    def dft_recursive(self, starting_vertex, visited= None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited == None:
            visited = set()
        # Check if the node is visited
        if starting_vertex in visited:
            return None
        #if not ...
        else:
            # mark it as visited
            visited.add(starting_vertex)
            # print
            print(starting_vertex)
            # call Dft_recursive on neightbors
            for neighbor in self.get_neighbors(starting_vertex):
                if neighbor not in visited:
                    self.dft_recursive(neighbor, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # TODO
        # Create a queue
        queue = Queue()
        # Create a visited set (use set because O(1) search)
        visited = set()
        # Add starting PATH to the queue
        #need to use a list because for a path order matters
        queue.enqueue([starting_vertex])
        # While: queue is not empty
        while queue.size() > 0:
            # Pop first PATH out of queue
            v_path = queue.dequeue()
            # grab the last vertex from the path
            vertex = v_path[-1]
            # Here is where you want to check if it's destination_vertex
            if vertex == destination_vertex:
                # then return the path
                return v_path
            # check if not visted
            elif vertex not in visited:
                # mark as visited
                visited.add(vertex)
                # Here is where we should print vertex bc it was just visted
                print(vertex)
                # get adjacent edges and add to back of path
                for neighbor in self.get_neighbors(vertex):
                    # make a copy of the path
                    new_path = v_path.copy()
                    # add neighbor to the back of that path
                    new_path.append(neighbor)
                    # add the path to the queue
                    queue.enqueue(new_path)
        # goto top of loop - happens automatically

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # TODO
        # Create a stack
        stack = Stack()
        # Create a visited set (use set because O(1) search)
        visited = set()
        # Add starting PATH to the stack
        stack.push([starting_vertex])
        # While: stack is not empty
        while stack.size() > 0:
            # Pop PATH out of stack
            v_path = stack.pop()
            # grab the last vertex from the path
            vertex = v_path[-1]
            # Here is where you want to check if it's destination_vertex
            if vertex is destination_vertex:
                # then return the path
                return v_path
            # check if not visted
            elif vertex not in visited:
                # mark as visited
                visited.add(vertex)
                # Here is where we should print vertex bc it was just visted
                print(vertex)
                # get adjacent edges and add to back of path
                for neighbor in self.get_neighbors(vertex):
                    # make a copy of the path
                    new_path = v_path.copy()
                    # add neighbor to the back of that path
                    new_path.append(neighbor)
                    # add the path to the queue
                    stack.push(new_path)
        # goto top of loop - happens automatically

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, v_path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # TODO
        # initialize visted and v_path first and should only run on 1st pass
        if visited is None:
            visited = set()
        if v_path is None:
            #add starting vertex path to path
            v_path = [ starting_vertex ]

        #if not visited
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            # grab last vertex from path
            # vertex = v_path[-1]
            # Check if the node is the destination
            if starting_vertex == destination_vertex:
                # return the path?
                return v_path
            # mark it as visited
            # print
            print(starting_vertex)
            # call Dft_recursive on neightbors
            for neighbor in self.get_neighbors(starting_vertex):
                if neighbor not in visited:
                    # # make copy of path
                    copy_path = v_path.copy()
                    # add neighbor to the back of the path
                    copy_path.append(neighbor)
                    # send neighbor back into function
                    new_path = self.dfs_recursive(neighbor, destination_vertex, visited, copy_path)
                    if new_path is not None:
                        return new_path
if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print("Starting bft")
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("Starting dft")
    graph.dft(1)
    print("Starting dft_recursive")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("Starting bfs with 6 as destination")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("Starting dfs with 6 as destination")
    print(graph.dfs(1, 6))
    print("Starting dfs_resursive with 6 as destination")
    print(graph.dfs_recursive(1, 6))
