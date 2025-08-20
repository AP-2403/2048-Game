import tkinter as tk
from tkinter import messagebox
import random
def start_game():
    mat=[]
    for i in range(4):
        mat.append([0]*4)#create a new 4X4 matrix with all 0 initals
    print("Command are as follows:")
    print("'W' or 'w': Move up")
    print("'S' or 's' : Move down")
    print("'A' or 'a': Move Left")
    print("'D' or 'd': Move Right")
    add_new_2(mat)
    return mat
def find_empty(mat):
    for i in range(4):
        for j in range(4):
            if(mat[i][j]==0):
                return i,j
    return None,None
def add_new_2(mat):
    if all(all(cell !=0 for cell in row) for row in mat):
        return
    tries=0
    while(tries<30):
        r=random.randint(0,3)
        c=random.randint(0,3)
        if mat[r][c]==0:
            mat[r][c]=2
            return
        tries+=1
    r,c=find_empty(mat)
    if r is not None and c is not None:
        mat[r][c]=2
def get_current_state(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return 'WON'

    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return 'Game Not Over'

    for i in range(4):
        for j in range(4):
            if i < 3 and mat[i][j] == mat[i+1][j]:  
                return 'Game Not Over'
            if j < 3 and mat[i][j] == mat[i][j+1]:  
                return 'Game Not Over'

    return 'LOST'


def compress(mat):
    changed=False
    new_mat=[]
    for i in range(4):
        new_mat.append([0]*4)
    for i in range(4):
        pos=0
        for j in range(4):
            if(mat[i][j]!=0):
                new_mat[i][pos]=mat[i][j]
                if(j!=pos):
                    changed=True
                pos+=1
    return new_mat,changed
def merge(mat):
    changed=False
    for i in range(4):
        for j in range(3):
            if(mat[i][j]==mat[i][j+1] and mat[i][j]!=0):
                mat[i][j]=mat[i][j]*2
                mat[i][j+1]=0 
                changed =True

    return mat,changed
def reverse(mat):
    new_mat=[]
    for i in range(4):
        new_mat.append([])
        for j in  range(4):
            new_mat[i].append(mat[i][3-j])
    return new_mat
def transpose(mat):
    new_mat=[]
    for i in range(4):  
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat
def move_left(grid):
    new_grid,changed1=compress(grid)
    new_grid,changed2=merge(new_grid)
    changed=changed1 or changed2
    new_grid,temp=compress(new_grid)
    return new_grid,changed
def move_right(grid):
    new_grid=reverse(grid)
    new_grid,changed=move_left(new_grid)
    new_grid=reverse(new_grid)
    return new_grid,changed
def move_up(grid):
    new_grid=transpose(grid)
    new_grid,changed=move_left(new_grid)
    new_grid=transpose(new_grid)
    return new_grid,changed
def move_down(grid):
    new_grid=transpose(grid)
    new_grid,changed=move_right(new_grid)
    new_grid=transpose(new_grid)
    return new_grid,changed

    
      
class Game2048:
    COLORS={
        0: ("#cdc1b4", "#776e65"),
        2: ("#eee4da", "#776e65"),
        4: ("#ede0c8", "#776e65"),
        8: ("#f2b179", "#f9f6f2"),
        16: ("#f59563", "#f9f6f2"),
        32: ("#f67c5f", "#f9f6f2"),
        64: ("#f65e3b", "#f9f6f2"),
        128: ("#edcf72", "#f9f6f2"),
        256: ("#edcc61", "#f9f6f2"),
        512: ("#edc850", "#f9f6f2"),
        1024: ("#edc53f", "#f9f6f2"),
        2048: ("#edc22e", "#f9f6f2"),
    }
    def __init__(self,root):
        self.root=root
        self.root.title("2048 Game")
        self.board=start_game()
        self.game_over=False

        self.frame=tk.Frame(self.root,bg="#bbada0")
        self.frame.grid()
        self.titles=[[None]*4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                label=tk.Label(self.frame,text="",width=4,height=2,font=("Helvetica",24,"bold"))
                label.grid(row=i,column=j,padx=5,pady=5,sticky="nsew")
                self.titles[i][j]=label
        
        self.update_board()

        self.root.bind("<Up>",lambda e: self.move("up"))
        self.root.bind("<Down>",lambda e: self.move("down"))
        self.root.bind("<Left>",lambda e: self.move("left"))
        self.root.bind("<Right>",lambda e: self.move("right"))
    def update_board(self):
        for i in range(4):
            for j in range(4):
                value=self.board[i][j]
                bg, fg=self.COLORS.get(value,("#3c3a32","#f9f6f2"))
                self.titles[i][j].config(text=str(value) if value!=0 else "", bg=bg,fg=fg)
    def move(self,direction):
        if self.game_over:
            return

        moved=False
        if direction=="up":
            self.board,moved=move_up(self.board)
        elif direction=="down":
            self.board,moved=move_down(self.board)
        elif direction=="left":
            self.board,moved=move_left(self.board)
        elif direction=="right":
            self.board,moved=move_right(self.board)
        
        if moved:
            add_new_2(self.board)
            self.update_board()

            state=get_current_state(self.board)
            if state=="Won":
                self.game_over=True
                messagebox.showinfo("2048","YOU WIN!")
            elif state=="LOST":
                self.game_over=True
                messagebox.showinfo("2048","GAME OVER!")


if __name__=="__main__":
    root=tk.Tk()
    Game2048(root)
    root.mainloop()
            
        
