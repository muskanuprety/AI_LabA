import argparse
from collections import deque 



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






    def add_node(self, state):
        
        
        self.add_helper(data, self.root)
            
        

class CurrentState():

    def __init__(self, num_cheeses,curr_location,cheeses, path):  # i removed array from here bc i dont think we need it for current state
        self.num_cheeses=num_cheeses
        #self.array=array
        self.curr_location=curr_location
        self.cheeses=cheeses
        self.path = path

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
        if self.num_cheeses ==0:
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

# def check_goal_state(state):
#     num_cheese = state.get_num_cheese
#     if num_cheese ==0:
#         return True
#     else:
#         return False

def transition(current_state, direction):
    last_num_cheese=current_state.get_num_cheese()
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
        return None
        ##return current_state
        

        new_loc = tuple(lst)


        if array[lst[0]][lst[1]] == ".":
            new_num_cheese = copy.deepcopy(last_num_cheese)
            new_num_cheese -=1
            new_cheeses = copy.deepcopy(last_cheeses)
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
    root_state=CurrentState(x,array,loc,y)
    root_node= Node(root_state)
    return root_node



def DFS(root_node):
    expanded=[]
    front = []
    
    goal_found=False
    front.append(root_node)
    while goal_found==False:

        north= transition(front[len(front)-1].get_state(),"N")
        south= transition(front[len(front)-1].get_state(),"S")
        east= transition(front[len(front)-1].get_state(),"E")
        west= transition(front[len(front)-1].get_state(),"W")

        goal_found = north.is_goal() or south.is_goal() or east.is_goal or west.is_goal()

        node_north = Node(north, root_node)
        node_south = Node(south, root_node)
        node_east = Node( east, root_node)
        node_west = Node(west, root_node)

        if node_west not in expanded and node_west != None:
            front.append(node_west)

        if node_east not in expanded and node_east != None:
            front.append(node_east)

        if node_south not in expanded and node_south != None:
            front.append(node_south)

        if node_north not in expanded and node_north != None:
            front.append(node_north)


        expanded.append(front.pop())

    return True 

        


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    

    args=parser.parse_args()
    D_array = read_file(args.file)

    DFS(make_first_node(D_array))







    
