import argparse
from collections import deque 
import copy
import heapq


class Node():
    def __init__(self, state, parent, path=None, mnh_dist=None):
        self.state= state
        self.parent= parent
        self.north=None
        self.east=None
        self.west=None
        self.south=None
        self.path= path
        self.mnh_dist=mnh_dist
        
    def get_parent(self):
        return self.parent
    
    def get_north(self):
        return self.north

    def get_south(self):
        return self.south

    def get_east(self):
        return self.east

    def get_west(self):
        return self.west

    def get_path(self):
        return self.path
    
    def set_north(self, n):
        self.north= n
        
    def set_east(self, e):
        self.east= e
    
    def set_south(self, s):
        self.south=s

    def set_west(self, w):
        self.west=w

    def get_state(self):
        return self.state

    def set_state(self,state):
        self.state=state

    def set_path(self,n):
        self.path.append(n)
            
    def compare_state(self, statex):

        if self.get_state().get_num_cheeses() == statex.get_num_cheeses() and self.get_state().get_curr_location() == statex.get_curr_location() and self.get_state().get_cheeses() == statex.get_cheeses():
            return True
        else:
            return False
    
    def get_path(self):
        return self.path

    def __lt__(self, other):
        return self.mnh_dist < other.mnh_dist

class CurrentState():

    def __init__(self, num_cheeses,curr_location,cheeses, array):  # i removed array from here bc i dont think we need it for current state
        self.num_cheeses=num_cheeses
        self.array=array
        self.curr_location=curr_location
        self.cheeses=cheeses
        #self.path = path

    def get_array(self):
        return self.array

    def get_num_cheeses(self):
        return self.num_cheeses
    def get_curr_location(self):
        return self.curr_location

    def get_cheeses(self):
        return self.cheeses

    def set_num_cheeses(self, n):
        self.north= n

    def set_curr_location(self, n):
        self.curr_location= n

    def set_cheeses(self, n):
        self.cheeses= n

    def is_goal(self):
        if self.num_cheeses == 0:
            return True
        else:
            return False
    


def read_file(filename):
    file=open(filename,"r")
    array=[]

    for line in file:
        arr_line=list(line)
        arr_line.pop(len(arr_line)-1)
        array.append(arr_line)
    return array

def count_cheeses(array):
    count=0
    cheeses=[]
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j]==".":
                count +=1
                cheeses.append((i,j))
    return count,cheeses

def check_goal_state(state):
    num_cheese = state.get_num_cheeses()
    cheese_left = state.get_cheeses()
    if num_cheese == 0 and cheese_left == []:
        return True
    else:
        return False

def transition(current_state, direction):
    
    last_num_cheese=current_state.get_num_cheeses()
    last_cheeses=current_state.get_cheeses()
    lst=list(current_state.get_curr_location())
    new_array= copy.deepcopy(current_state.get_array())
    if direction=="N":
        lst[0] = lst[0]-1

    if direction=="S":
        lst[0] = lst[0]+1

    if direction=="E":
        lst[1] = lst[1]+1

    if direction=="W":
        lst[1] = lst[1]-1

    new_loc = tuple(lst)

    if new_array[lst[0]][lst[1]] == "%":

        return current_state 
           
    
    new_num_cheese= copy.deepcopy(last_num_cheese)
    new_cheeses= copy.deepcopy(last_cheeses)

    if new_array[lst[0]][lst[1]] == ".":

        new_array[lst[0]][lst[1]] = " "
        new_num_cheese -= 1
        # for i in range(len(new_cheeses)):
        #     if new_cheeses[i] == new_loc:
        #         new_cheeses.pop(i)
        new_cheeses.remove(new_loc)

    new_state = CurrentState(new_num_cheese, new_loc, new_cheeses, new_array)
    
    return new_state


def make_first_node(array):


    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j]=="P":
                    
                loc=(i,j)
    x,y=count_cheeses(array)
    root_state=CurrentState(x,loc,y,array)
    lista=[loc]
    root_node= Node(root_state,None,lista)
    
    return root_node

def already_expanded(liss, node):
    answer = False
    for i in liss:
        if node.compare_state(i.get_state()) == True:
            answer = True
            break
    return answer

def calc_dist(state):
    dist_from_cheeses=[]
    if len(state.get_cheeses())==0:
        return [0]
    else:
        for i in state.get_cheeses():
            mnh_dist=abs(state.get_curr_location()[0]-i[0])+abs(state.get_curr_location()[1]-i[1])
            dist_from_cheeses.append(mnh_dist)
        return dist_from_cheeses

def DFS(root_node, array):
    expanded=[]
    front = []
    goal_found=False
    front.append(root_node)
    while goal_found==False:
        node2expand=front.pop()
        loc=node2expand.get_state().get_curr_location()
        if already_expanded(expanded, node2expand)==False:
            expanded.append(node2expand)
            array_in_question = copy.deepcopy(node2expand.get_state().get_array())
            north= transition(node2expand.get_state(),"N")
            south= transition(node2expand.get_state(),"S")
            east= transition(node2expand.get_state(),"E")
            west= transition(node2expand.get_state(),"W")
            x3 = check_goal_state(east)
            x4 = check_goal_state(west)
            x1 = check_goal_state(north)
            x2 = check_goal_state(south)
            goal_found = x1 or x2 or x3 or x4
            node_path= node2expand.get_path()
            new_path_north = copy.deepcopy(node_path)
            new_path_north.append(north.get_curr_location())
            node_north = Node(north,node2expand, new_path_north)
            new_path_south = copy.deepcopy(node_path)
            new_path_south.append(south.get_curr_location())
            node_south = Node(south, node2expand, new_path_south)
            new_path_east = copy.deepcopy(node_path)
            new_path_east.append(east.get_curr_location())
            node_east = Node(east, node2expand, new_path_east)
            new_path_west = copy.deepcopy(node_path)
            new_path_west.append(west.get_curr_location())
            node_west = Node(west, node2expand, new_path_west)
            front.append(node_north)
            front.append(node_south)
            front.append(node_east)
            front.append(node_west)
            if x3:
                gg = node_east
            if x4:
                gg = node_west
            if x1:
                gg = node_north
            if x2:
                gg = node_south
    solved_maze = copy.deepcopy(array)
    right_path = gg.get_path()
    for i in right_path:
        solved_maze[i[0]][i[1]] = "#"
    x = ""
    for i in solved_maze:
        for j in i:
            x = x + j
        x = x+'\n'
    print(x)
    print(len(right_path))


def BFS(root_node, array):
    expanded=[]
    front = []
    goal_found=False
    front.append(root_node)
    while goal_found==False:
        node2expand=front.pop(0)
        loc=node2expand.get_state().get_curr_location()
        if already_expanded(expanded, node2expand)==False:
            expanded.append(node2expand)
            array_in_question = copy.deepcopy(node2expand.get_state().get_array())
            north= transition(node2expand.get_state(),"N")
            south= transition(node2expand.get_state(),"S")
            east= transition(node2expand.get_state(),"E")
            west= transition(node2expand.get_state(),"W")
            x3 = check_goal_state(east)
            x4 = check_goal_state(west)
            x1 = check_goal_state(north)
            x2 = check_goal_state(south)
            goal_found = x1 or x2 or x3 or x4
            node_path= node2expand.get_path()
            new_path_north = copy.deepcopy(node_path)
            new_path_north.append(north.get_curr_location())
            node_north = Node(north,node2expand, new_path_north)
            new_path_south = copy.deepcopy(node_path)
            new_path_south.append(south.get_curr_location())
            node_south = Node(south, node2expand, new_path_south)
            new_path_east = copy.deepcopy(node_path)
            new_path_east.append(east.get_curr_location())
            node_east = Node(east, node2expand, new_path_east)
            new_path_west = copy.deepcopy(node_path)
            new_path_west.append(west.get_curr_location())
            node_west = Node(west, node2expand, new_path_west)
            front.append(node_north)
            front.append(node_south)
            front.append(node_east)
            front.append(node_west)
            if x3:
                gg = node_east
            if x4:
                gg = node_west
            if x1:
                gg = node_north
            if x2:
                gg = node_south
    solved_maze = copy.deepcopy(array)
    right_path = gg.get_path()
    for i in right_path:
        solved_maze[i[0]][i[1]] = "#"
    x = ""
    for i in solved_maze:
        for j in i:
            x = x + j
        x = x+'\n'
    print(x)
    print(len(right_path))


def GBFS(root_node, array):
    expanded=[]
    front = []
    goal_found=False
    front.append(root_node)
    while goal_found==False:
        node2expand = heapq.heappop(front)
        # loc=node2expand.get_state().get_curr_location()
        # print(loc)
        # print(array[loc[0]][loc[1]])
        node_path = node2expand.get_path()
        if (already_expanded(expanded, node2expand)==False):
            expanded.append(node2expand)
            north= transition(node2expand.get_state(),"N")
            south= transition(node2expand.get_state(),"S")
            east= transition(node2expand.get_state(),"E")
            west= transition(node2expand.get_state(),"W")
            new_path_north = copy.deepcopy(node_path)
            new_path_north.append(north.get_curr_location())
            node_north = Node(north, root_node,new_path_north, min(calc_dist(north)))
            new_path_south = copy.deepcopy(node_path)
            new_path_south.append(south.get_curr_location())
            node_south = Node(south, root_node, new_path_south,min( calc_dist(south)))
            new_path_east = copy.deepcopy(node_path)
            new_path_east.append(east.get_curr_location())
            node_east = Node( east, root_node, new_path_east, min(calc_dist(east)))
            new_path_west = copy.deepcopy(node_path)
            new_path_west.append(west.get_curr_location())
            node_west = Node(west, root_node, new_path_west,min( calc_dist(west)))
            heapq.heappush(front, node_north)
            heapq.heappush(front, node_south)
            heapq.heappush(front,node_east)
            heapq.heappush(front,node_west)
            x3 = check_goal_state(east)
            x4 = check_goal_state(west)
            x1 = check_goal_state(north)
            x2 = check_goal_state(south)
            goal_found = x1 or x2 or x3 or x4
            if x3:
                gg = node_east
            if x4:
                gg = node_west
            if x1:
                gg = node_north
            if x2:
                gg = node_south
    solved_maze = copy.deepcopy(array)
    right_path = gg.get_path()
    for i in right_path:
        solved_maze[i[0]][i[1]] = "#"
    x = ""
    for i in solved_maze:
        for j in i:
            x = x + j
        x = x+'\n'
    print(x)
    print(len(right_path))


def Astar(root_node, array):
    expanded=[]
    front = []
    goal_found=False
    front.append(root_node)
    while goal_found==False:
        node2expand = heapq.heappop(front)
        if (already_expanded(expanded, node2expand)==False):
            expanded.append(node2expand)
            north= transition(node2expand.get_state(),"N")
            south= transition(node2expand.get_state(),"S")
            east= transition(node2expand.get_state(),"E")
            west= transition(node2expand.get_state(),"W")
            node_path = node2expand.get_path()
            new_path_north = copy.deepcopy(node_path)
            new_path_north.append(north.get_curr_location())
            node_north = Node(north, root_node,new_path_north, min(calc_dist(north))+len(node_path))
            new_path_south = copy.deepcopy(node_path)
            new_path_south.append(south.get_curr_location())
            node_south = Node(south, root_node, new_path_south,min( calc_dist(south))+len(node_path))
            new_path_east = copy.deepcopy(node_path)
            new_path_east.append(east.get_curr_location())
            node_east = Node( east, root_node, new_path_east, min(calc_dist(east))+len(node_path))
            new_path_west = copy.deepcopy(node_path)
            new_path_west.append(west.get_curr_location())
            node_west = Node(west, root_node, new_path_west,min( calc_dist(west))+len(node_path))
            heapq.heappush(front, node_north)
            heapq.heappush(front, node_south)
            heapq.heappush(front,node_east)
            heapq.heappush(front,node_west)
            x3 = check_goal_state(east)
            x4 = check_goal_state(west)
            x1 = check_goal_state(north)
            x2 = check_goal_state(south)
            goal_found = x1 or x2 or x3 or x4
            if x3:
                gg = node_east
            if x4:
                gg = node_west
            if x1:
                gg = node_north
            if x2:
                gg = node_south
    solved_maze = copy.deepcopy(array)
    right_path = gg.get_path()
    for i in right_path:
        solved_maze[i[0]][i[1]] = "#"
    x = ""
    for i in solved_maze:
        for j in i:
            x = x + j
        x = x+'\n'
    print(x)
    print(len(right_path))
         


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    

    args=parser.parse_args()
    D_array = read_file(args.file)

    # x =transition(make_first_node(D_array).get_state(), "E", D_array)
    # print(x.get_curr_location())

    # DFS(make_first_node(D_array),D_array)
    # GBFS(make_first_node(D_array), D_array)
    Astar(make_first_node(D_array), D_array)
    # x = make_first_node(D_array)
    # s = x.get_state()

    # print(s.get_num_cheeses())
    # print(s.get_curr_location())
    # print(s.get_cheeses())





    
