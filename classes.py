import random

#Constants:
UP = (1, 0)
DOWN = (-1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

#Classes:
class Snake:
    #PUBLIC direction : TUPLE
    #PUBLIC body : TUPLE

    def __init__(self,initial_body, initial_direction):
        self.body = initial_body
        self.direction = initial_direction
    
    def take_step(self, position):
        self.body = self.body[1:] + [position]

    def set_direction(self,direction):
        self.direction = direction

    def head(self):
        return self.body[-1]
    
    def make_move(self,move,invincible,grid):
        new_row = self.head()[0]+move[0]
        new_col = self.head()[1]+move[1]
        if invincible:
            if new_row>=grid[0]:
                new_row = 0
            elif new_row<0:
                new_row = grid[0]-1
            if new_col>=grid[1]:
                new_col = 0
            elif new_col<0:
                new_col = grid[1]-1

        new_head = (new_row,new_col)
        self.take_step(new_head)

    def grow(self,invincible,grid):
        new_row = self.body[0][0]-(self.body[1][0]-self.body[0][0])
        new_col = self.body[0][1]-(self.body[1][1]-self.body[0][1])
        
        new_tail = (new_row,new_col)
        self.body = [new_tail] + self.body

class Apple:
    #PUBLIC position : TUPLE

    def __init__(self, position):
        self.position = position

class Game:
    #PUBLIC height, width: INTEGER
    #PUBLIC snake: Snake

    def __init__(self, height, width, init_body, init_direction):
        self.height = height
        self.width = width
        self.snake = Snake(init_body, init_direction)
        self.apple = Apple((random.randint(0,height-1),random.randint(0,width-1)))

    def board_matrix(self):
        matrix = [[None for _ in range(self.width)] for _ in range(self.height)]
        return matrix

    def render(self):
        matrix = self.board_matrix()
        width = self.width
        height = self.height

        print('+','-'*width,'+',sep="") #top border

        for row in range(height): #row loop
            print('|',end="")
            for col in range(width): #col loop
                printed = False
                if (height-1-row,col) == self.snake.head(): #if this is head position print X
                    print('X',end='')
                    printed=True
                else:
                    if (height-1-row,col) == self.apple.position and printed==False:
                        print('*',end="")
                        printed = True
                    for part in self.snake.body: #check if body position and print O
                        if(height-1-row,col) == part and printed==False:
                            print('O',end='')
                            printed = True
                if printed==False: #if neither print blank space
                    print(' ',end='')
            print('|') 

        print('+','-'*width,'+',sep="") #bottom border

    def grow_snake(self,invincible):
        self.snake.grow(invincible,(self.height,self.width))
        self.apple.position = (random.randint(0,self.height-1),random.randint(0,self.width-1))
        while self.apple.position == self.snake.head():
            self.apple.position = (random.randint(0,self.height-1),random.randint(0,self.width-1))

