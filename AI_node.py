import argparse



class Node():
    def __init__(self, state= None):
        self.state=state
        self.parent= None
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

    def __init__(self, num_cheeses, array,curr_location,cheeses):
        self.num_cheeses=num_cheeses
        self.array=array
        self.curr_location=curr_location
        self.cheeses=cheeses

    def get_num_cheeses(self):
        return num_cheeses

    def get_array(self):
        return self.array

    def get_curr_location(self):
        return self.curr_location

    def get_cheeses(self):
        return self.cheeses

    def set_num_cheeses(self, n):
        self.north= n

    def set_array(self, n):
        self.array= n

    def set_curr_location(self, n):
        self.curr_location= n

    def set_cheeses(self, n):
        self.cheeses= n

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

def transition(current_state, direction):
    last_num_cheese=current_state.get_num_cheese()
    last_cheeses=current_state.get_cheeses()
    last_loc=current_state.get_curr_location()

    if direction=="N":
        lst = list(last_loc)
        lst[0] = lst[0]-1

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



        new_loc = tuple(lst)

    if direction=="S":
        lst = list(last_loc)
        lst[0] = lst[0]+1
        new_loc = tuple(lst)

    if direction=="E":
        lst = list(last_loc)
        lst[0] = lst[1]+1
        new_loc = tuple(lst)

    if direction=="W":
        lst = list(last_loc)
        lst[0] = lst[1]-1
        new_loc = tuple(lst)




def make_first_node(array):


    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j]=="P":
                    
                loc=(i,j)
    x,y=count_cheeses(array)
    root_state=CurrentState(x,array,loc,y)
    root_node= Node(root_state)
    return root_node






if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    nodes=[]

    args=parser.parse_args()
    D_array = read_file(args.file)

    nodes.append(make_first_node(D_array))







    
