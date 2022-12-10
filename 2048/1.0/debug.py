#2022年11月20日11:21:29
#Python

#变量
xy=[0,1,2,3,\
    0,0,0,0,\
    0,0,0,0,\
    0,0,0,0]
return_direction=False
temp_xy=False

def mobile(direction):
    global xy
#//////////ERROR//////////#
    if direction =='a'or'w':
        temp_xy=15
    if direction =='s'or'd':
        temp_xy=0
#//////////ERROR//////////#
    print('temp_xy='+str(temp_xy))
    print('direction='+direction)
    if temp_xy != False:
        print('Ln:21 True')
        if xy[temp_xy] == 0:
            print('Ln:23 True')
            if xy[temp_xy+1] == 0:
                print('Ln:25 True')
                if xy[temp_xy+2] == 0:
                    xy[temp_xy+2]=xy[temp_xy+3]
                    xy[temp_xy+3]=0
            else:
                print('Ln:25 False')
                xy[temp_xy+1]=xy[temp_xy+3]
                xy[temp_xy+3]=0
        else:
            print('Ln:23 False')
            print(xy[temp_xy])
            xy[temp_xy]=xy[temp_xy+3]
            xy[temp_xy+3]=0
    else:
        print('Ln:21 False')
def merge():
    pass
mobile('a')
print('xy='+str(xy))
