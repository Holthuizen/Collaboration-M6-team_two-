# tutorial-06-Holthuizen
tutorial-06-Holthuizen created by GitHub Classroom


#DFS
  good for finding all notes and edges(connections)
  datastructure: stack (first in first out), this make recursion possible
  
  
  overview of the algorithm as implemented in search.py: 
  
  
  load all nodes into a stack
  loop over entire stack, until target is found. 
  if current node is already seen, skip to the next node. 
  if current node has not yet been seen: 
    marks as visited: 
    loop over its neighbours: 
      if neighbour not visited: 
        add to stack
        set parrent to "current node"
        append to stack
        

