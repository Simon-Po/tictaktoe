import random
class Board:
    
    board = [[],[],[]]
    player_turn= 1
    player1_won = False
    player2_won = False
    
    def __init__(self):
        self.fill_board()        
        
        
        
        
        
    def fill_board(self):
        for arr in self.board:
            for i in range(3):
                arr.append(" ")
                
    def print(self):
        print("-"*5)
        for arr in self.board:
            print(f"{arr[0]}|{arr[1]}|{arr[2]}")
            print("-"*5)
            
    def update(self,cord):
        x,y = cord
        
        if self.player_turn == 1 and self.board[x][y] == " ":
            self.board[x][y] = "x"
            self.player_turn = 2
        elif  self.board[x][y] == " ":
            self.board[x][y] = "o"
            self.player_turn = 1
        
        
    def message(self):
        out = f"Player {self.player_turn} it is your turn!"
        if self.player_turn == 1:
            self.player_turn = 2
        else:
            self.player_turn = 1
        return out
    
    def evaluate(self):
        for arr in self.board:
            if arr == ["x","x","x"]:
                self.player1_won = True
            elif arr == ["o","o","o"]:
                self.player2_won = True
        for i in range(len(self.board[0])):
            if self.board[0][i] == "x" and self.board[1][i] == "x" and self.board[2][i] == "x":
                self.player1_won = True
            if self.board[0][i] == "o" and self.board[1][i] == "o" and self.board[2][i] == "o":
                self.player2_won = True
        if self.board[0][0] == "x" and self.board[1][1] == "x" and self.board[2][2] == "x":
            self.player1_won = True
        elif self.board[0][0] == "o" and self.board[1][1] == "o" and self.board[2][2] == "o":
            self.player2_won = True
        elif self.board[0][2] == "x" and self.board[1][1] == "x" and self.board[2][0] == "x":
            self.player1_won = True
        elif self.board[0][2] == "o" and self.board[1][1] == "o" and self.board[2][0] == "0":
            self.player2_won = True
    
    
    def clear(self):
        for arr in self.board:
            arr = [" "," "," "]
    
    def make_move(self):
        if self.player_turn == 1:
            return
        empty_squares = []
        for x in range(len(self.board)):
            for y in range(len(self.board)):
                if self.board[x][y] == " ":
                    empty_squares.append((x,y))
        self.update(random.choice(empty_squares))