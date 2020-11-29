import random
from datetime import datetime
import bisect #binairy insert

try:
    from maze import Maze
except:
    from exercise.maze import Maze



class Search:

    def __init__(self, graph):
        self.graph = graph
        random.seed(datetime.now())

    
    #DFS
    def depth_first_solution(self):

        self.graph.reset_state()

        stack = [self.graph.start]
        visited = []

        while len(stack) > 0:
            current_node = stack.pop()
            if current_node != self.graph.target:
                if current_node not in visited:
                    visited.append(current_node)
                    neighbours = current_node.get_neighbours()
                    random.shuffle(neighbours) #un-deterministic 
                    for next_node in neighbours:
                        if next_node not in visited:
                            next_node.set_parent(current_node)
                            stack.append(next_node) #place on top
            else:
                break
        print("The number of visited nodes is: {}".format(len(visited)))
        self.highlight_path()


    #BFS
    def breadth_first_solution(self):
        #regenerate maze
        self.graph.reset_state()
        #un ordered queue, first in first out
        queue = [self.graph.start]
        visited = [] 

        while len(queue) > 0:
            current_node = queue.pop(0)#dequeue operation
            if(current_node != self.graph.target):
                if(current_node not in visited):
                    visited.append(current_node)
                    for next_node in current_node.get_neighbours():
                        if next_node not in visited:
                            next_node.set_parent(current_node)
                            #append discovered notes to the queue
                            queue.append(next_node)
            else:
                break
        print("The number of visited nodes is: {}".format(len(visited)))
        self.highlight_path()



    # ADD YOU IMPLEMENTATIONS FOR GREEDY AND ASTAR HERE!
    # pick the lowest manhattan distance from its available neighbours 
    # use a priority queue to guide the dissision process. 



    def greedy_search(self):
        #regenerate maze
        self.graph.reset_state()
        priority_queue = [self.graph.start]
        visited = []
        while len(priority_queue)>0: 
            current = priority_queue.pop()
            if (current != self.graph.target):
                if(current not in visited):
                    visited.append(current)
                    for neighbour in current.get_neighbours(): 
                        if neighbour not in visited: 
                            neighbour.set_parent(current)
                            neighbour.set_score(neighbour.manhattan_distance(self.graph.target))
                            bisect.insort(priority_queue, neighbour)
            else:
                break
        print("The number of visited nodes is: {}".format(len(visited)))
        self.highlight_path()                       

    def a_star_search(self):
        self.graph.reset_state()
        priority_queue = [self.graph.start] #open list
        visited = [] #close list 
        # while the priority queue is not empty
        while len(priority_queue) > 0:
            #the current node is the first node of the priority queue=
            current = priority_queue.pop()
            # if the current node is not the target
            if (current != self.graph.target):
                #add the current node to the visited nodes
                if(current not in visited):
                    visited.append(current)
                    # for all neighbouring nodes of the current node
                    for neighbour in current.get_neighbours(): 
                        # if they have not been visited yet
                        if neighbour not in visited: 
                            # compute the new distance
                            # compute the new score ( fscore plus gscore )
                            new_score = current.distance + neighbour.manhattan_distance(self.graph.target)
                            # if the neighbouring node is not in the priority queue
                            if neighbour not in priority_queue:
                                
                                # set the current node to be their parent (discussion point)
                                #neighbour.set_parent(current)
                                ##i dislike like hiding the distance update in set_parrent, so this is an alternative:
                                neighbour.parent = current
                                neighbour.distance = current.distance + 1
                                
                                # the score of the neighbouring node is the new score ? 
                                current.set_score(new_score)
                                # insert the neighbouring node into the priority queue
                                bisect.insort_left(priority_queue, neighbour)
                                print("current",current)
                            
                            # else if the the new distance is smaller than the current distance of the neighbouring node
                            else: #in open list / priority queue
                                if current.distance +1 < neighbour.distance: # +1? you still need to move from current to neighbour
                                    #set the current node to be their parent (note distance gets updated)
                                    neighbour.set_parent(current)
                                    # remove the neighbouring node from the priority queue
                                    priority_queue.remove(neighbour)
                                    # insert the neighbouring node into the priority queue
                                    bisect.insort_left(priority_queue,neighbour)
            else:
                break
        print("A* -> The number of visited nodes is: {}".format(len(visited)))
        self.highlight_path()    


    def highlight_path(self):
        # Compute the path, back to front.
        current_node = self.graph.target.parent
        print("Path length is: {}".format(self.graph.target.distance))
        while current_node is not None and current_node != self.graph.start:
            # print(current_node)
            current_node.set_color((248, 220, 50))
            current_node = current_node.parent

                   

