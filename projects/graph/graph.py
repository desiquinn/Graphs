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
        pass  # TODO

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
                for next_vert in self.vertices[vertex]:
                    queue.enqueue(next_vert)
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
                for next_vert in self.vertices[vertex]:
                    stack.push(next_vert)
        # goto top of loop - happens automatically


    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

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
                # Here is where you want to check if it's destination_vertex
                if vertex is destination_vertex:
                    # then return the path
                    return visited
                # get adjacent edges and add to list
                else:
                    for next_vert in self.vertices[vertex]:
                        queue.enqueue(next_vert)
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
        # Add starting node to the stack
        stack.push(starting_vertex)
        # While: stack is not empty
        while stack.size() > 0:
            # Pop first node out of stack
            vertex = stack.pop()
            # if not visted
            if vertex not in visited:
                # mark as visited
                visited.add(vertex)
                # Here is where we should print vertex bc it was just visted
                print(vertex)
                # Here is where you want to check if it's destination_vertex
                if vertex is destination_vertex:
                    # then return the path
                    return visited
                # get adjacent edges and add to list
                else:
                    for next_vert in self.vertices[vertex]:
                        stack.push(next_vert)
        # goto top of loop - happens automatically

    def dfs_recursive(self, starting_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

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
    print(graph.dfs_recursive(1, 6))
