from Board import Board
import pygame
import sys
WIDTH = 800
HEIGHT = 800
COLOR_BACKGROUND = (242, 233, 228)
COLOR_LINES = (74, 78, 105)
COLOR_PLAYERS = (34, 34, 59)
LINE_THICKNESS = 12
MARGIN = ((WIDTH + HEIGHT) / 2) / 16

#Setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TicTacToe")
board = Board()


def draw_board():
    pygame.draw.line(screen, COLOR_LINES, (screen.get_width() / 3,MARGIN) , (screen.get_width() / 3,HEIGHT - MARGIN),LINE_THICKNESS)
    pygame.draw.line(screen, COLOR_LINES, (screen.get_width() / 1.5,MARGIN) , (screen.get_width() / 1.5,HEIGHT - MARGIN),LINE_THICKNESS)
    pygame.draw.line(screen, COLOR_LINES, (MARGIN,screen.get_height() / 3) , (WIDTH - MARGIN ,screen.get_height() / 3),LINE_THICKNESS)
    pygame.draw.line(screen, COLOR_LINES, (MARGIN,screen.get_height() / 1.5) , (WIDTH - MARGIN, screen.get_height() / 1.5),LINE_THICKNESS)
    
    
def evaluate_mouse_pos(x,y):
    print(x," ",y)
    if x < WIDTH / 3:
        if y < HEIGHT / 3:
            return (0,0)
        elif y > HEIGHT / 3  and y < (HEIGHT / 3) * 2:
            return (1,0)
        elif y > (WIDTH / 3) * 2:
            return (2,0)
    elif x > WIDTH / 3 and x < WIDTH and x < (WIDTH / 3) * 2:
        if y < HEIGHT / 3:
            return (0,1)
        elif y > HEIGHT /  y < HEIGHT and y < (HEIGHT / 3) * 2:
            return (1,1)
        elif y > (WIDTH / 3) * 2:
            return (2,1)
    elif x > (WIDTH / 3) * 2:
        if y < HEIGHT / 3:
            return (0,2)
        elif y > HEIGHT / 3 and y < (HEIGHT / 3) * 2:
            return (1,2)
        elif y > (WIDTH / 3) * 2:
            return (2,2)
        
def display_players(b):
    current_board = b.board
    b.print()
    for x in range(len(current_board)):
        for y in range(len(current_board[x])):
            if current_board[x][y] == "x":
                draw_x(x,y)
            elif current_board[x][y] == "o":
                draw_o(x,y)


def draw_x(x,y):
    pygame.draw.line(screen, COLOR_PLAYERS,(MARGIN + (screen.get_width() / 3) * y ,MARGIN + (screen.get_height() / 3) * x),(MARGIN + (screen.get_width() / 3) * y + 170,MARGIN + (screen.get_height() / 3) * x + 170),10 )
    pygame.draw.line(screen, COLOR_PLAYERS,(MARGIN + (screen.get_width() / 3) * y ,MARGIN + (screen.get_height() / 3) * x + 170),(MARGIN + (screen.get_width() / 3) * y +170,MARGIN + (screen.get_height() / 3) * x ),10 )

def draw_o(x,y):
    pygame.draw.circle(screen, COLOR_PLAYERS, (MARGIN + (screen.get_width() / 3) * y + 80, MARGIN + (screen.get_height() / 3) * x + 100), 90,10)

board.print()

screen.fill(COLOR_BACKGROUND)
draw_board()
display_players(board)
pygame.display.update()
#Gameloop
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Get the position of the mouse click
            mouse_x, mouse_y = pygame.mouse.get_pos()
            board.update(evaluate_mouse_pos(mouse_x,mouse_y))
            board.evaluate()
            screen.fill(COLOR_BACKGROUND)
            draw_board()
            display_players(board)
            pygame.display.update()
            board.evaluate()
            if board.player1_won :
                print("Player 1 Won")
                pygame.quit()
                sys.exit()
                
            elif board.player2_won :
                print("Player 2 Won") 
                pygame.quit()
                sys.exit()
                
                
    

