

class Node:
    def __init__(self,data,level,fval,move_to_reach,parent):
        self.parent=parent
        self.data = data
        self.level = level
        self.fval = fval
        self.move_to_reach=move_to_reach
    
    def generate_child(self):
        [[x1,y1],[x2,y2]]=self.find(self.data,'-')
        val_list_1 = [[x1,y1-1],[x1,y1+1],[x1-1,y1],[x1+1,y1]]
        val_list_2 = [[x2,y2-1],[x2,y2+1],[x2-1,y2],[x2+1,y2]]
        children = []
        for i in val_list_1:
            child = self.shuffle(self.data,x1,y1,i[0],i[1])
            if child is not None:
                children.append(child)

        for i in val_list_2:
            child = self.shuffle(self.data,x2,y2,i[0],i[1])
            if child is not None:
                children.append(child)
        # print([i.data for i in children])
        return children
        

    
    def shuffle(self,puz,x1,y1,x2,y2):
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data) and puz[x2][y2]!='-':
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            child =Node(temp_puz,self.level+1,0,None,self)
            if (x1<x2):
                child.move_to_reach=(puz[x2][y2],"up")
            elif (x1>x2):
                child.move_to_reach=(puz[x2][y2],"down")
                
            elif (y1<y2):
                child.move_to_reach=(puz[x2][y2],"left")
                
            elif (y1>y2):
                child.move_to_reach=(puz[x2][y2],"right")
                
            return child
        else:
            return None
    

    def find(self,puz,x):
        index_arr=[]
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data)):
                if puz[i][j] == x:
                    index_arr.append([i,j])
        return index_arr
    
    def copy(self,root):
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp   

class Puzzle:
    def __init__(self,size):
        self.n = size
        self.open = []
        self.closed = []
    def accept(self):
        puz = []
        for i in range(0,self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz

    def f(self,start,goal):
        return self.h(start.data,goal)+start.level

    def f2(self,start,goal):
        return self.h_manhattan(start.data,goal)+start.level 


    def find_position(self,arr, x):
        for i in range(self.n):
            for j in range(self.n):
                if arr[i][j] == x:
                    return i, j

    # Hamming Distance (No of Misplaced Tiles)
    def h(self,start,goal):
        temp = 0
        for i in range(0,self.n):
            for j in range(0,self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '-':
                    temp += 1
        return temp

    # Manhattan Distance
    def h_manhattan(self,start, goal):
        count = 0
        for i in range(self.n):
            for j in range(self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '-':
                    x, y = self.find_position(goal, start[i][j])
                    count += abs(i-x) + abs(j-y)
        return count
        

    def manhattan_process(self,start_list,goal_list):
        start = start_list
        goal= goal_list
        start = Node(start,0,0,None,None)
        start.fval = self.f2(start,goal)

        
        self.open.append(start)
        print("\n\n")
        # p=1
        nodes_traversed=0
        while True:
            cur = self.open[0] 
            nodes_traversed=nodes_traversed+1
            # print(cur.move_to_reach, cur.data)
            """ If the difference between current and goal node is 0 we have reached the goal node"""
            if(self.h_manhattan(cur.data,goal) == 0):
                self.closed.append(cur)
                break
            for i in cur.generate_child():
                i.fval = self.f2(i,goal)
                self.open.append(i)
            self.closed.append(cur)
            del self.open[0]
# """ sort the open list based on f value """
            self.open.sort(key = lambda x:x.fval,reverse=False)
        
        final_list=[self.closed[-1]]
        while True:
            if final_list[0]==None:
                break
            final_list.insert(0,final_list[0].parent)
        
        the_file=open('Sample_Output_Manhattan.txt', 'w+')
        the_file.truncate()

        for i in final_list:
            if i !=None:
                    if i.move_to_reach != None:
                        the_file.write(str(i.move_to_reach)+'\n')
        the_file.close()
        print("nodes traversed by Manhattan:",nodes_traversed)
        print("Manhattan process done")
    
    def hamming_process(self,start_list,goal_list):
        # """ Accept Start and Goal Puzzle state"""
        start = start_list
        goal= goal_list
        start = Node(start,0,0,None,None)
        start.fval = self.f(start,goal)

        
        # """ Put the start node in the open list"""
        self.open.append(start)
        nodes_traversed=0
        print("\n\n")
        # p=1
        while True:
            # p=p+1
            # if p==10:
            #     break
            cur = self.open[0]
            nodes_traversed=nodes_traversed+1        
            # print(cur.move_to_reach, cur.data)
            """ If the difference between current and goal node is 0 we have reached the goal node"""
            if(self.h(cur.data,goal) == 0):
                self.closed.append(cur)
                break
            for i in cur.generate_child():
                i.fval = self.f(i,goal)
                self.open.append(i)
            self.closed.append(cur)
            del self.open[0]
# """ sort the open list based on f value """
            self.open.sort(key = lambda x:x.fval,reverse=False)
        
        final_list=[self.closed[-1]]
        while True:
            if final_list[0]==None:
                break
            final_list.insert(0,final_list[0].parent)
        
        the_file=open('Sample_Output_Hamming.txt', 'w+')
        the_file.truncate()

        for i in final_list:
            if i !=None:
                    if i.move_to_reach != None:
                        the_file.write(str(i.move_to_reach)+'\n')
        the_file.close()
        print("nodes traversed by hamming:",nodes_traversed)
        print("Hamming Process Done")
        

        



start_config=input("Enter filename of textfile with start configuration:").strip()
goal_config=input("Enter filename of textfile with goal configuration:").strip()
fin = open(start_config,'r')
start_list=[]
for line in fin.readlines():
    start_list.append( [ x for x in line.rstrip("\n").split() ] )
fin = open(goal_config,'r')
goal_list=[]
for line in fin.readlines():
    goal_list.append( [ x for x in line.rstrip("\n").split() ] )

puz1=Puzzle(len(start_list))
puz2=Puzzle(len(start_list))

puz2.hamming_process(start_list,goal_list)
puz1.manhattan_process(start_list,goal_list)
