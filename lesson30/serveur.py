import pygame
from grid import Grid
import os
os.environ['SDL_VIDEO-WINDOW_POST'] = ('400,100')

surface = pygame.display.set_mode((600, 600))
pygame.display.set_caption("TIC_TAC_TOE")
import threading

def create_thread(target):
    thread = threading.Thread(target=target)
    thread.daemon = True
    thread.start()



import socket
HOST = '127.0.0.1'
PORT = 65432
connection_established = False
conn , addr = None , None

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((HOST,PORT))
sock.listen(1)

def recive_data():
    global turn
    while True:
        data = conn.recv(1024).decode()
        data = data.split('-')
        x,y = int(data[0]) , int(data[1])
        if data[2] == 'yourturn':
            turn = True
        if data[3] == 'False':
            grid.game_over = True
        if grid.get_cell_value(x,y) == 0:
            grid.set_cell_value(x,y,"o")
        print(data)

def waiting_connection():
    global connection_established, conn , addr
    conn , addr = sock.accept()
    print('client is connected')
    connection_established = True
    recive_data()
create_thread(waiting_connection)
grid = Grid()


running = True
player ="x"
turn = True
playing = 'True'
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not grid.game_over:
            if pygame.mouse.get_pressed()[0]:
                if turn and not grid.game_over:
                    pos = pygame.mouse.get_pos()
                    cellx,celly = pos[0]//200,pos[1]//200
                    grid.get_mouse(cellx,celly,player)
                    if grid.game_over:
                        playing = 'False'
                    send_data = '{}-{}-{}-{}'.format(cellx,celly,'yourturn',playing).encode()
                    conn.send(send_data)
                    turn = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and grid.game_over:
                grid.clear_grid()
                grid.game_over = False
                playing = 'True'
            elif event.key == pygame.K_ESCAPE:
                running =False

                


    surface.fill((0, 0, 0))

    grid.draw(surface)

    pygame.display.flip()
