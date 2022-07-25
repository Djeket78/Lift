from imp import is_frozen
from os import system
from pickle import FALSE
from random import randrange

##### LIFT state #####
DIR_UP          = -1
DIR_DOWN        =  1
DIR_STOPED      =  0

building_roof    = False
building_floors  = 9
building_parking = False

lift_floor      = 5
lift_open       = True
lift_dir        = DIR_STOPED


human_floor     = 5
human_in_lift   = True
#############  RENDER FRAME ########
system('cls')

############ roof #################
if building_roof:
    print(        '---|-----|----')
    print(        ' R |     |    ')



############ bulding ##############
for floor in range(9,0,-1):
    ########### roof  top ######
    if building_roof==False and floor==9:
        b = '-----'
    else:
        b = '     '

 ################# lift top ####
    if floor==lift_floor:
        b = '-----'

################# lift d ####
    if floor==lift_floor-1:
        b = '-----'

    print(        f'---|{b}|----')
########### human #######
    if floor == human_floor and not human_in_lift:
        h = '  H  '
    else:
        h = '     '



############ lift  ##########
    if floor == lift_floor and not human_in_lift:
        l = '|   |'
    elif floor == human_floor and human_in_lift:
        l = '| H |' 
    else:
        l = '     '
############# ind ###########
    if floor == lift_floor+1:
        if lift_open:
            l = ' < > '
        else:
            if lift_dir==DIR_UP:
               l = '  ^  '
            if lift_dir==DIR_DOWN:
               l = '  v  '
          

    print(f'{floor:^3}|{l}|{h}')

######### parking##############
if building_parking:
    print(        '---|-----|----')
    print(        ' P |     |    ')
    print(        '---|-----|----')
else:
    print(        '---|-----|----')

#############  ######### ##############




