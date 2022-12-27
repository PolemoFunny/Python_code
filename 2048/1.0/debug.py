#2022年11月20日11:21:29
#Python

#变量
xy = [0, 1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

return_direction=False
operational_parameters = False

def mobile(direction):
    global xy
    if (direction in ['a','w']):
        operational_parameters = [15, -1]
    if (direction in ['s', 'd']):
        operational_parameters = [0, 1]
    print(('operational_parameters=' + str(operational_parameters)))
    print(('direction=' + direction))
    if operational_parameters != False:
        print('Ln:21 True')
        if (xy[operational_parameters[0]+operational_parameters[1]] == 0):
            print('Ln:23 True')
            if (xy[operational_parameters[0]+operational_parameters[1]] == 0):
                print('Ln:25 True')
                if (xy[(operational_parameters[0]+operational_parameters[1] * 2)] == 0):
                    xy[operational_parameters[0]+operational_parameters[1]*2]=xy[operational_parameters[1]*3]
                    xy[operational_parameters[0]+operational_parameters[1]*3]=0
            else :
                print('Ln:25 False')
                xy[operational_parameters[0]+operational_parameters[1]]=xy[operational_parameters[0]+operational_parameters[1]*3]
                xy[operational_parameters[0]+operational_parameters[1]*3]=0
        else :
            print('Ln:23 False')
            print(operational_parameters)
            xy[operational_parameters[0]+operational_parameters[1]]=xy[operational_parameters[0]+operational_parameters[1]*3]
            xy[operational_parameters[0]+operational_parameters[1]*3]=0
    else :
        print('Ln:21 False')

def merge():

    pass

mobile('a')
print(('xy=' + str(xy)))
