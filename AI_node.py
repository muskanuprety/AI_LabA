import argparse
from collections import deque 
import copy


class Node():
    def __init__(self, state= None, parent=None):
        self.state=state
        self.parent= parent
        self.north=None
        self.east=None
        self.west=None
        self.south=None
        self.path=[]
        
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
    def set_path(self,path):
        self.path.append(path)
            
    def compare_state(self, statex):

        if self.get_state().get_num_cheeses() == statex.get_num_cheeses() and self.get_state().get_curr_location() == statex.get_curr_location() and self.get_state().get_cheeses() == statex.get_cheeses():
            return True
        else:
            return False
    def get_path(self):
        return self.path

class CurrentState():

    def __init__(self, num_cheeses,curr_location,cheeses):  # i removed array from here bc i dont think we need it for current state
        self.num_cheeses=num_cheeses
        #self.array=array
        self.curr_location=curr_location
        self.cheeses=cheeses
        #self.path = path

    def get_num_cheeses(self):
        return self.num_cheeses

    def get_path(self):
        return self.path

    def set_path(self, n):
        self.path = n

    #def get_array(self):
        #return self.array

    def get_curr_location(self):
        return self.curr_location

    def get_cheeses(self):
        return self.cheeses

    def set_num_cheeses(self, n):
        self.north= n

    #def set_array(self, n):
        #self.array= n

    def set_curr_location(self, n):
        self.curr_location= n

    def set_cheeses(self, n):
        self.cheeses= n

    def is_goal(self):
        if self.num_cheeses == 0:
            return True
        else:
            return False

    # def compare_state(self, statex):

    #     if self.get_num_cheeses() == statex.get_num_cheeses() and self.get_curr_location() == statex.get_curr_location() and self.get_cheeses() == statex.get_cheeses():
    #         return True
    #     else:
    #         return False

    


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

def transition(current_state, direction, array):
    
    last_num_cheese=current_state.get_num_cheeses()
    last_cheeses=current_state.get_cheeses()
    lst=list(current_state.get_curr_location())
    
    if direction=="N":
        lst[0] = lst[0]-1

    if direction=="S":
        lst[0] = lst[0]+1

    if direction=="E":
        lst[1] = lst[1]+1

    if direction=="W":
        lst[1] = lst[1]-1

    new_loc = tuple(lst)

    if array[lst[0]][lst[1]] == "%":

        return current_state 
           

    
    
    new_num_cheese= copy.deepcopy(last_num_cheese)
    new_cheeses= copy.deepcopy(last_cheeses)

    if array[lst[0]][lst[1]] == ".":
        array[lst[0]][lst[1]] = " "
        new_num_cheese -= 1
        for i in range(len(new_cheeses)):
            if new_cheeses[i] == new_loc:
                new_cheeses.pop(i)

    new_state = CurrentState(new_num_cheese, new_loc, new_cheeses)
    
    return new_state


def make_first_node(array):


    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j]=="P":
                    
                loc=(i,j)
    x,y=count_cheeses(array)
    root_state=CurrentState(x,loc,y)
    root_node= Node(root_state)
    return root_node

def xyz(liss, node):
    answer = False
    for i in liss:
        if node.compare_state(i.get_state()) == True and i.get_parent()==node.get_parent():
                answer = True
    return answer



def DFS(root_node, array):
    expanded=[]
    front = []
    
    goal_found=False
    front.append(root_node)

    while goal_found==False:
        #print("aaoia")
        node2expand=front.pop()
        loc=node2expand.get_state().get_curr_location()
        print(loc)
        print(array[loc[0]][loc[1]])

        if xyz(expanded, node2expand)==False:
            
        

            expanded.append(node2expand)

            north= transition(node2expand.get_state(),"N", array)
            south= transition(node2expand.get_state(),"S", array)
            east= transition(node2expand.get_state(),"E", array)
            west= transition(node2expand.get_state(),"W", array)

            

            x3 = check_goal_state(east)
            x4 = check_goal_state(west)
            x1 = check_goal_state(north)
            x2 = check_goal_state(south)

            goal_found = x1 or x2 or x3 or x4
        #goal_found = north.is_goal() or south.is_goal() or east.is_goal or west.is_goal()
            node_path=node2expand.get_path()
            
            node_north = Node(north,node2expand)
            node_north.set_path(node_path.append("N"))
            
            node_south = Node(south, node2expand)
            node_north.set_path(node_path.append("S"))


            node_east = Node( east, node2expand)
            node_north.set_path(node_path.append("E"))

            node_west = Node(west, node2expand)
            node_north.set_path(node_path.append("W"))

            front.append(node_north)
            front.append(node_south)
            front.append(node_east)
            front.append(node_west)
        


        print(len(expanded))
        print(len(front))
    
    print(goal_found)
    


def calc_dist(state):
    dist_from_cheeses=[]
    for i in state.get_cheeses():
        mnh_dist=abs(state.get_curr_location()[0]-i[0])+abs(state.get_curr_location()[1]-i[1])
        dist_from_cheeses.append(mnh_dist)
    return dist_from_cheeses


def BFS(root_node, array):
    expanded=[]
    front = []
    
    goal_found=False
    front.append(root_node)

    while goal_found==False:
        #print("aaoia")
        node2expand=front.pop(0)

        if xyz(expanded, node2expand)==False:
            
        

            expanded.append(node2expand)

            north= transition(node2expand.get_state(),"N", array)
            south= transition(node2expand.get_state(),"S", array)
            east= transition(node2expand.get_state(),"E", array)
            west= transition(node2expand.get_state(),"W", array)

            

            x3 = check_goal_state(east)
            x4 = check_goal_state(west)
            x1 = check_goal_state(north)
            x2 = check_goal_state(south)

            goal_found = x1 or x2 or x3 or x4
        #goal_found = north.is_goal() or south.is_goal() or east.is_goal or west.is_goal()

            node_north = Node(north,node2expand)
            node_south = Node(south, node2expand)
            node_east = Node( east, node2expand)
            node_west = Node(west, node2expand)

            front.append(node_north)
            front.append(node_south)
            front.append(node_east)
            front.append(node_west)
        


        print(len(expanded))
        print(len(front))
    
    print(goal_found)
    

def GBFS(root_node, array):


    expanded=[]
    front = []
    all_mhnd={}
    goal_found=False

    front.append(root_node)

    while goal_found==False:
        
        print (len(front))

        if len(expanded)==0:
            node2expand=front[0]
        
        else:
            
            for i in front:
                
                
                all_mhnd[min(calc_dist(i.get_state()))]=i
            node2expand=all_mhnd[min(all_mhnd.keys())]

        if (xyz(expanded, node2expand)==False):

            expanded.append(node2expand)


            north= transition(node2expand.get_state(),"N", array)
            south= transition(node2expand.get_state(),"S", array)
            east= transition(node2expand.get_state(),"E", array)
            west= transition(node2expand.get_state(),"W", array)

            node_north = Node(north, root_node)
            node_south = Node(south, root_node)
            node_east = Node( east, root_node)
            node_west = Node(west, root_node)

            front.append(north)
            front.append(south)
            front.append(east)
            front.append(west)




        

            front.remove(node2expand)


            goal_found = check_goal_state(north) or check_goal_state(north) or check_goal_state(north) or check_goal_state(north)


         


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    

    args=parser.parse_args()
    D_array = read_file(args.file)

    # x =transition(make_first_node(D_array).get_state(), "E", D_array)
    # print(x.get_curr_location())

    DFS(make_first_node(D_array),D_array)
    # GBFS(make_first_node(D_array), D_array)
    # x = make_first_node(D_array)
    # s = x.get_state()

    # print(s.get_num_cheeses())
    # print(s.get_curr_location())
    # print(s.get_cheeses())





    
