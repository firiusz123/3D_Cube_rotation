import pygame
import os
import math
from matrix_multiplication import matrix_multiplication


#variables
os.environ["SDL_VIDEO_CENTERED"]="1"
width , height = 800,600
black,white ,blue = (20,20,20),(230,230,230),(0,154,255)

pygame.init()
pygame.display.set_caption("cube projection")
screen=pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
fps = 60

index = 0
angle = 7
cube_position = [width/2 , height/2]
scale = 200
scale_variable=1
speed = 0.01

points = [n for n in range(4)]
"""
points[0] = [[-1], [-1], [1]]
points[1] = [[1], [-1], [1]]
points[2] = [[1], [1], [1]]
points[3] = [[-1], [1], [1]]
points[4] = [[-1], [-1], [-1]]
points[5] = [[1], [-1], [-1]]
points[6] = [[1], [1], [-1]]
points[7] = [[-1], [1], [-1]]
"""












    







# all deffs 
def draw_line(k):
    pygame.draw.line(screen, white, (k[0][0][0], k[0][1][0]), (k[1][0][0], k[1][1][0]), 2)
    pygame.draw.line(screen, white, (k[1][0][0], k[1][1][0]), (k[2][0][0], k[2][1][0]), 2)
    pygame.draw.line(screen, white, (k[2][0][0], k[2][1][0]), (k[3][0][0], k[3][1][0]), 2)
    pygame.draw.line(screen, white, (k[3][0][0], k[3][1][0]), (k[0][0][0], k[0][1][0]), 2)

# core program


projected_points = [n for n in range(4)]
run = True


    
print(projected_points)
while run :
    clock.tick(fps)
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    
    points[0]=[[1],[1]]
    points[1]=[[-1],[1]]
    points[2]=[[-1],[-1]]
    points[3]=[[1],[- 1]]

    scale_matrix=[[[scale] , [0]],
                [[0], [scale]]]


    rotation=[[math.cos(angle) ,-math.sin(angle)],
            [math.sin(angle) ,math.cos(angle)]]
    for i in range(len(points)):
        points[i]=matrix_multiplication(rotation,points[i])
        print(matrix_multiplication(rotation,points[i]))

    for i in range(len(points)):
        for k in range(len(points[i])):
            
            if k == 1 :
                points[i][k][0] = points[i][k][0] * scale
                points[i][k][0] +=cube_position[1]
                points[i][k][0]=int(points[i][k][0])
            else:
                points[i][k][0] = points[i][k][0] * scale
                points[i][k][0] +=cube_position[0]
                points[i][k][0]=int(points[i][k][0])
            points[i][k][0]=int(points[i][k][0])
            
        # print(points[i][k][0])
    print(points)
    draw_line(points)
    angle=angle+speed
    scale=scale-scale_variable
    if scale > 200:
        scale_variable=scale_variable*(-1)
    elif scale < -200:
        scale_variable=scale_variable*(-1)
    
    
    
   
        

    
    
        
    

    pygame.display.update()
pygame.quit()