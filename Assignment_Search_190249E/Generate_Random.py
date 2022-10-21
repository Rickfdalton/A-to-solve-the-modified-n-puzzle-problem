from random import randrange
from re import S


def generate_random_start(x):
    start=[]
    for i in range(x):
        start.append(['0']*x)
    count=1
    for i in range(x):
        for j in range(x):
            start[i][j]=str(count)
            count=count+1
    x1= randrange(x)
    y1= randrange(x)
    x2= randrange(x)
    y2= randrange(x)
    start[x1][y1]='-'
    start[x2][y2]='-'
    return start


def shuffle(puz,x1,y1,x2,y2):
        if x2 >= 0 and x2 < len(puz) and y2 >= 0 and y2 < len(puz) and puz[x2][y2]!='-':
            temp_puz = []
            temp_puz = [x[:] for x in puz]
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None

def move_random(arr,count):
    #change value to change no of moves
    if count==10:
        return arr 
    index_arr=[]
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if arr[i][j] == '-':
                index_arr.append([i,j])
    [[x1,y1],[x2,y2]]=index_arr

    val_list_1 = [[x1,y1-1],[x1,y1+1],[x1-1,y1],[x1+1,y1]]
    val_list_2 = [[x2,y2-1],[x2,y2+1],[x2-1,y2],[x2+1,y2]]
    children = []
    for i in val_list_1:
        child = shuffle(arr,x1,y1,i[0],i[1])
        if child is not None:
            children.append(child)
    for i in val_list_2:
        child = shuffle(arr,x2,y2,i[0],i[1])
        if child is not None:
            children.append(child)
    return move_random(children[randrange(len(children))],count+1)
        
    
#change value to set length of square
start=generate_random_start(20)


start_file=open('start.txt', 'w+')
start_file.truncate(0)
for i in start:
    start_file.write(' '.join(i) +'\n')
start_file.close()
print("start written")

goal_file=open('goal.txt', 'w+')
goal_file.truncate(0)
goal=move_random(start,0)
for i in goal:
    goal_file.write(' '.join(i) +'\n')
goal_file.close()
print("goal written")