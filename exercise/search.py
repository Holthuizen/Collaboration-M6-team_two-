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

                        
    # while openSet is not empty
    #     current := the node in openSet having the lowest fScore[] value
    #     if current = goal
    #         return reconstruct_path(cameFrom, current)
    #     openSet.Remove(current)

    #     for each neighbor of current
    #         // d(current,neighbor) is the weight of the edge from current to neighbor
    #         // tentative_gScore is the distance from start to the neighbor through current
    #         tentative_gScore := gScore[current] + d(current, neighbor)
    #         if tentative_gScore < gScore[neighbor]
    #             // This path to neighbor is better than any previous one. Record it!
    #             cameFrom[neighbor] := current
    #             gScore[neighbor] := tentative_gScore
    #             fScore[neighbor] := gScore[neighbor] + h(neighbor)
    #             if neighbor not in openSet
    #                 openSet.add(neighbor)

    # // Open set is empty but goal was never reached
    # return failure

    #gscore is == grid_element.distance
    #fscore is == grid_element.score

    def a_star_search(self):
        #reset maze/graph
        self.graph.reset_state()
        start = self.graph.start
        start.set_distance(0)
        priority_queue = [start]
        visited = [] #checked / finished 

        while len(priority_queue)>0: 
            n = priority_queue.pop()  #take the best node of the list
            if (n != self.graph.target): #while goal not found do:
                if(n not in visited):
                    visited.append(n) #mark note as finally checked
                    for s in n.get_neighbours(): 
                        if s not in visited: #if s is finally checked: Do nothing
                            #if s is already in priority_queue
                            if s in priority_queue:
                                print("in pq: ",s)
                                # with LOWER cost (start --> neighbour dist): Do nothing: 
                                
                                #HIGHER cost (start --> neighbour dist), Do:
                                if n.distance + 1 < s.distance: ##does this any sence ?? 
                                    #update cost and make n its parent
                                    s.set_parent(n)
                                    s.set_score(s.distance  + s.manhattan_distance( self.graph.target ) )
                                    #i guess this needs to happen here: 
                                    priority_queue.remove(s)
                                    bisect.insort_left(priority_queue,s)
        
                            if s not in priority_queue: # if s is NOT YET in list: 
                                #Add s with newly calculated cost and n as parrent 
                                s.set_parent(n)
                                s.set_score( s.distance + s.manhattan_distance( self.graph.target ) ) #traveled distance + distance to target
                                bisect.insort_left(priority_queue,s)
                                print("NOT in pq: ",s)
                                              
                else: 
                    print("allready checked")
                      
            else:
                break
        print("The number of visited nodes is: {}".format(len(visited)))
        self.highlight_path()                       



    def highlight_path(self):
        # Compute the path, back to front.
        current_node = self.graph.target.parent
        print("Path length is: {}".format(self.graph.target.distance))
        while current_node is not None and current_node != self.graph.start:
            # print(current_node)
            current_node.set_color((248, 220, 50))
            current_node = current_node.parent
