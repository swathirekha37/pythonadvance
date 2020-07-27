import random
import os
#creating grid
cells=[
    (0,0),(1,0),(2,0),(3,0),
    (0,1),(1,1),(2,1),(3,1),
    (0,2),(1,2),(2,2),(3,2),
    (0,3),(1,3),(2,3),(3,3)
]

def clearscreen():
    os.system('cls' if os.name=='nt' else 'clear')
    

def getLocation():
    return random.sample(cells,3)




def moveplayer(player,move):
    #get players location
    x,y=player

    if move=='left':
        x=x-1
    if move=='right':
        x=x+1
    if move=='up':
        y=y-1
    if move=='down':
        y=y+1

    return x,y

def getmove(player):
    moves=['left','right','up','down']
    x,y=player

    if y==0:
        moves.remove('up')
        #you cant move up
    if y==3:
        moves.remove('down')
        #print("you cant move down")
    if x==0:
        moves.remove('left')
        #print("you cant move left")
    if x==3:
        moves.remove('right')
       # print("you cant move right")
    return moves

def drawmap(player):
    print(' _ '*4)
    tile="|{}|"
    for cell in cells:
        x,y = cell
        if x<3:
            line_end=""
            if cell==player:
                output=tile.format('x')
            else:
                output=tile.format("_")
        else:
            line_end="\n"
            if cell==player:
                output=tile.format('X')
            else:
                output=tile.format("_")
        print(output,end=line_end)


def gameloop():
    monster,door,player = getLocation()
    playing=True

    while playing:
        clearscreen()
        drawmap(player)
        validmoves=getmove(player)
        print("enter quit to quit the game")
        print("now you are in {} positon.".format(player))

        validmoves=getmove(player)
        print("you can move {}.".format(",".join(validmoves)))
        move=input("enter the move : >")

        if move == 'quit':
            break
        
        if move in validmoves:
            player=moveplayer(player,move)

            if player==monster:
                print("Oh No! monster caught you. better luck next time.\n")
                playing=False
            if player==door:
                print("\n** You escaped ! congrats **\n")
                playing=False 
        else:
            print("\n** be careful\n**")
            continue
        clearscreen()
    else:
        if input('play again?(Y/N)').lower()!='n':
            gameloop()

clearscreen()
print('welcome to the dungeon game')
input("press 'return' to start!")
clearscreen()
gameloop()