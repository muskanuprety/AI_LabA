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

    def compare_state(self, statex):

        if self.get_num_cheeses() == statex.get_num_cheeses() and self.get_curr_location() == statex.get_curr_location() and self.get_cheeses() == statex.get_cheeses():
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
    if num_cheese ==0 and cheese_left == []:
        return True
    else:
        return False

def transition(current_state, direction, array):
    last_num_cheese=current_state.get_num_cheeses()
    last_cheeses=current_state.get_cheeses()
    last_loc=current_state.get_curr_location()
    lst = list(last_loc)

    if direction=="N":
        lst[0] = lst[0]-1


    if direction=="S":
        lst[0] = lst[0]+1


    if direction=="E":
        lst[0] = lst[1]+1


    if direction=="W":
        lst[0] = lst[1]-1


    if array[lst[0]][lst[1]] == "%":

        return current_state
        ##return current_state
        

    new_loc = tuple(lst)

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

def xyz(liss, state):
    answer = False
    for i in liss:
        if state.compare_state(i) == True:
                answer = True
    return answer



def DFS(root_node, array):
    expanded=[]
    front = []
    
    goal_found=False
    front.append(root_node.get_state())

    while goal_found==False:
        #print("aaoia")

        if xyz(expanded, front[len(front)-1]):
            front.pop()
        else:

            expanded.append(front[len(front)-1])

            north= transition(front[len(front)-1],"N", array)
            south= transition(front[len(front)-1],"S", array)
            east= transition(front[len(front)-1],"E", array)
            west= transition(front[len(front)-1],"W", array)

            front.pop()

            x3 = check_goal_state(east)
            x4 = check_goal_state(west)
            x1 = check_goal_state(north)
            x2 = check_goal_state(south)

            goal_found = x1 or x2 or x3 or x4
        #goal_found = north.is_goal() or south.is_goal() or east.is_goal or west.is_goal()

            # node_north = Node(north,front[len(front)-1])
            # node_south = Node(south, front[len(front)-1])
            # node_east = Node( east, front[len(front)-1])
            # node_west = Node(west, front[len(front)-1])

            front.append(north)
            front.append(south)
            front.append(east)
            front.append(west)
        


        print(len(expanded))
        print(len(front))
    
    print(goal_found)
    

def calc_dist(state):
    dist_from_cheeses=[]
    for i in state.get_cheeses():
        mnh_dist=abs(state.get_curr_location[0]-i[0])+abs(state.get_curr_location[1]-i[1])
        dist_from_cheeses.append(mnh_dist)
    return mnh_dist


def GBFS(root_node, array):


    expanded=[]
    front = []
    all_mhnd={}
    goal_found=False
    front.append(root_node)

    while goal_found==False:
        print (len(expanded))

        if len(expanded)==0:
            node2expand=front[0]
        
        else:
            
            for i in front:
                
                state=i.get_state()
                all_mhnd[min(calc_dist(state))]=i
            node2expand=all_mhnd[min(all_mhnd.values())]

        north= transition(node2expand.get_state(),"N", array)
        south= transition(node2expand.get_state(),"S", array)
        east= transition(node2expand.get_state(),"E", array)
        west= transition(node2expand.get_state(),"W", array)

        node_north = Node(north, root_node)
        node_south = Node(south, root_node)
        node_east = Node( east, root_node)
        node_west = Node(west, root_node)

        if node_west not in expanded:
            front.append(node_west)

        if node_east not in expanded:
            front.append(node_east)

        if node_south not in expanded:
            front.append(node_south)

        if node_north not in expanded:
            front.append(node_north)

        goal_found = north.is_goal() or south.is_goal() or east.is_goal or west.is_goal()


         


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    

    args=parser.parse_args()
    D_array = read_file(args.file)

    #DFS(make_first_node(D_array))
    GBFS(make_first_node(D_array), D_array)
    # x = make_first_node(D_array)
    # s = x.get_state()

    # print(s.get_num_cheeses())
    # print(s.get_curr_location())
    # print(s.get_cheeses())





    
