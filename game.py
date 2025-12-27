import classes
import random

grid_sizes = {1:(15,17),2:(9,10),3:(21,24)}
incompatible = {classes.UP:classes.DOWN,classes.LEFT:classes.RIGHT,classes.DOWN:classes.UP,classes.RIGHT:classes.LEFT}

grid = grid_sizes[int(input("Enter which grid size you want to play with:\n1. Standard Size (15x17)\n2. Small Size (9x10)\n3. Large Size (21x24)\nEnter your choice: "))]
game_end = False
invincible = int(input("Do you want wall colission? (1 for Yes, 0 for No) ")) == 0
start_col = int(grid[0]/2)
init_body = [(2,start_col),(3,start_col),(4,start_col),(5,start_col),(6,start_col)]
ourGame = classes.Game(grid[0],grid[1],init_body,classes.UP)
score = 0

while not game_end:
    ourGame.render()
    moves = {"W":classes.UP,"A":classes.LEFT,"S":classes.DOWN,"D":classes.RIGHT,'':ourGame.snake.direction}
    move = moves[input("W for UP, A for LEFT, S for DOWN, D for RIGHT, Nothing to keep going straight: ").upper()]
    while (move == incompatible[ourGame.snake.direction]):
        print("That is an incompatible move")
        move = moves[input("W for UP, A for LEFT, S for DOWN, D for RIGHT, Nothing to keep going straight: ").upper()]

    ourGame.snake.set_direction(move)
    ourGame.snake.make_move(move,invincible,grid)

    if ourGame.snake.head()==ourGame.apple.position:
        ourGame.grow_snake(invincible)
        score += 1

    if (not invincible):
        if ourGame.snake.head()[0]<0 or ourGame.snake.head()[0]>=grid[0] or ourGame.snake.head()[1]<0 or ourGame.snake.head()[1]>=grid[1]:
            game_end=True
            print(f"The snake has crashed into a wall. The game has ended.\nYou scored {score} points")
    
    for part in ourGame.snake.body[0:-1]:
        if ourGame.snake.head()==part:
            game_end=True
            print(f"The snake has crashed into itself. The game has ended.\nYou scored {score} points")
