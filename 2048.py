#2022年11月20日11:21:29
#Python

#变量
xy=[0,0,0,0,\
    0,0,0,0,\
    0,0,0,0,\
    0,0,0,0]
return_direction=False
temp_xy=0

def mobile(direction):
    global xy
#//////////ERROR//////////
    if direction =='a'or'w':
        temp_xy=0
    elif direction =='s'or'd':
        temp_xy=15
    else:
        temp_xy=False
#//////////ERROR//////////        
    if temp_xy:
        if xy[temp_xy] == 0:
            if xy[temp_xy+1] == 0:
                if xy[temp_xy+2] == 0:
                    xy[temp_xy+2]=xy[temp_xy+3]
                    xy[temp_xy+3]=0
            else:
                xy[temp_xy+1]=xy[temp_xy+3]
                xy[temp_xy+3]=0
        else:
            xy[temp_xy]=xy[temp_xy+3]
            xy[temp_xy+3]=0
    else:
        print('无效的输入')

def merge():
    pass
mobile('w')

