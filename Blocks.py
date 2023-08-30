import random

import pygame

class Blocks():

    # make ele_block
    blocks = [
        [[0,0],[0,-1],[0,1],[0,2]],             # I
        [[0,0],[0,-1],[-1,0],[-1,1]],           # Z
        [[0,0],[0,1],[1,1],[1,0]],              # squre
        [[0,0],[0,1],[-1,1],[-1,0]],            # rev_Z
        [[0,0],[0,1],[1,0],[0,-1]],             # T
        [[0,0],[1,0],[-1,0],[1,-1]],            # L
        [[0,0],[1,0],[-1,0],[1,1]]              # rev_L
    ]

    # background block setting
    background = [[0 for clo in range(10)] for row in range(23)]  # create back ground
    background[0] = [1 for gr in range(10)]  # make a ground, stop blocks fall below the ground
    print(background)
    # initial fall-down position: row  21, clo 5
    block_ini_position = [22, 5]

    block_size = 1.5

    # socre
    score = [0]
    # elim line
    complete_row_counts = 0

    Next_Block = random.choice(blocks)
    select_Block = []
    gameOver = False

    def block_down_move(self):
        #if not self.select_Block:
            #self.select_Block = list(random.choice(self.blocks))     # because sometimes there is no new blocks (bugs)
        y_drop = self.block_ini_position[0]
        x_move = self.block_ini_position[1]
        y_drop -= 1


        for row, col in self.select_Block:
            row += y_drop
            col += x_move
            print(self.background,"row=",row)
            if self.background[row+1][col] == 1:
                # the block hit the gournd
                break
        else:
            self.block_ini_position.clear()
            self.block_ini_position.extend([y_drop,x_move])
            print("in the loop",'2222')
            return
        print("come here3")
        y_drop,x_move = self.block_ini_position
        for row,col in self.select_Block:
            self.background[row+y_drop][col+x_move] = 1     # set the touched-ground block become 1
        print("come here1")
        # elim line
        complete_row = []
        for row in range(0,21):
            if 0 not in self.background[row]:       # this line is full
                complete_row.append(row)
        complete_row.sort(reverse=True)

        for row in complete_row:
            self.background.pop(row)
            self.background.append([0 for i in range(10)])
        # SCORE
        match len(complete_row):    #The correspondence between points and the number of lines
            case 1:
                self.score[0] += 100
            case 2:
                self.score[0] += 300
            case 3:
                self.score[0] += 600
            case 4:
                self.score[0] += 1000

        # recored the number of lines eliminated in the session
        self.complete_row_counts += len(complete_row)

        # new blcoks chosen
        #self.select_Block.clear()
        #self.select_Block.extend(list(random.choice(self.blocks)))
        self.select_Block = self.Next_Block
        self.Next_Block = list(random.choice(self.blocks))

        # new position set
        self.block_ini_position.clear()
        self.block_ini_position.extend([20,5])

        y_drop,x_move = self.block_ini_position
        # if it is the last element block
        for row,col in self.select_Block:
            row += y_drop
            col += x_move
            if self.background[row][col]:
                self.gameOver = True

    def draw_block(self,screen):
            y_drop, x_move = self.block_ini_position


            for row,col in self.select_Block: # loop the random blocks we chosen
                row += y_drop
                col += x_move

                #xy transport, each block should be 25*25
                point = [col * 23, 500 - row*23]

                pygame.draw.rect(screen, (172, 250, 233),   #232,255,206
                             (point[0]*self.block_size, point[1]*self.block_size,
                              23*self.block_size, 23*self.block_size))


            for row in range(20):
                for col in range(10):
                    bottom = self.background[row][col]
                    if bottom:
                        pygame.draw.rect(screen,(148,173,215),
                                         (col*25*self.block_size, (500-row*25)*self.block_size,
                                          23*self.block_size, 23*self.block_size))



    def movement(self,n):       # move left -1 and right +1,
        y_drop, x_move = self.block_ini_position
        x_move += n
        for row, col in self.select_Block:
            row += y_drop
            col += x_move

            # boundery
            if col < 0 or col > 9 or self.background[row][col]:
                break
        else:   # update position
            self.block_ini_position.clear()
            self.block_ini_position.extend([y_drop,x_move])

    def rotate(self):       # rotate blocks
        y_drop, x_move = self.block_ini_position
        rotate_position = [(-col,row) for row, col in self.select_Block]
        for row, col in rotate_position:
            row += y_drop
            col += x_move
            if col < 0 or col > 9 or self.background[row][col]:     # if rotate out of boundary, beak
                break
        else:
            #update postion
            self.select_Block.clear()
            self.select_Block.extend(rotate_position)




