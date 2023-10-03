import pygame
import math
from matrix_multiplication import matrix_multiplication


#variables
width , height = 800,600
black,white ,blue = (20,20,20),(230,230,230),(0,154,255)

pygame.init()
pygame.display.set_caption("cube projection")
screen=pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
fps = 60
run = True

index = 0
angle =  0
cube_position = [width/2 , height/2]
scale = 200
scale_variable=1
speed = 0.01

points = [n for n in range(8)]
projected_points = [n for n in range(8)]

points[0] = [[-1], [-1], [1]]  #5
points[1] = [[1], [-1], [1]]  #6
points[2] = [[1], [1], [1]]   #7
points[3] = [[-1], [1], [1]] #8
points[4] = [[-1], [-1], [-1]]  #1
points[5] = [[1], [-1], [-1]]   #2
points[6] = [[1], [1], [-1]]    #4
points[7] = [[-1], [1], [-1]]   #3
def draw_line(k):


    pygame.draw.line(screen, white, (k[4][0][0], k[4][1][0]), (k[5][0][0], k[5][1][0]), 2)  #2
    pygame.draw.line(screen, white, (k[4][0][0], k[4][1][0]), (k[7][0][0], k[7][1][0]), 2)  #3
    pygame.draw.line(screen, white, (k[4][0][0], k[4][1][0]), (k[0][0][0], k[0][1][0]), 2)  #5
    pygame.draw.line(screen, white, (k[5][0][0], k[5][1][0]), (k[6][0][0], k[6][1][0]), 2) #4
    pygame.draw.line(screen, white, (k[6][0][0], k[6][1][0]), (k[7][0][0], k[7][1][0]), 2) #3
    pygame.draw.line(screen, white, (k[5][0][0], k[5][1][0]), (k[1][0][0], k[1][1][0]), 2)  #6
    pygame.draw.line(screen, white, (k[6][0][0], k[6][1][0]), (k[2][0][0], k[2][1][0]), 2)
    pygame.draw.line(screen, white, (k[7][0][0], k[7][1][0]), (k[3][0][0], k[3][1][0]), 2)
    pygame.draw.line(screen, white, (k[0][0][0], k[0][1][0]), (k[3][0][0], k[3][1][0]), 2)
    pygame.draw.line(screen, white, (k[3][0][0], k[3][1][0]), (k[2][0][0], k[2][1][0]), 2)
    pygame.draw.line(screen, white, (k[2][0][0], k[2][1][0]), (k[1][0][0], k[1][1][0]), 2)
    pygame.draw.line(screen, white, (k[1][0][0], k[1][1][0]), (k[0][0][0], k[0][1][0]), 2)
    
    












projection_matrix =[[1,0,0],
                        [0,1,0]]




while run :
    clock.tick(fps)
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    
    rotation_x = [[1, 0, 0],
                [0, math.cos(angle), -math.sin(angle)],
                [0, math.sin(angle), math.cos(angle)]]

    rotation_y = [[math.cos(angle), 0, math.sin(angle)],
                [0, 1, 0],
                [-math.sin(angle), 0, math.cos(angle)]]

    rotation_z = [[math.cos(angle), -math.sin(angle), 0],
                    [math.sin(angle), math.cos(angle), 0],
                    [0, 0 ,1]]
    










    #print(projected_points)
    for i in range(len(points)):
        projected_points[i]=matrix_multiplication(rotation_x,points[i]) 
        projected_points[i]=matrix_multiplication(rotation_y,projected_points[i])
        projected_points[i]=matrix_multiplication(rotation_z,projected_points[i])
        projected_points[i]=matrix_multiplication(projection_matrix,projected_points[i])
        
    for i in range(len(points)):
        for j in range(len(points[i])):
            if j == 0:
                projected_points[i][j][0]=projected_points[i][j][0] * scale 
                projected_points[i][j][0]=projected_points[i][j][0] + cube_position[0]
                projected_points[i][j][0]=int(projected_points[i][j][0])
                
            elif j == 1:
                projected_points[i][j][0]=projected_points[i][j][0]*scale 
                projected_points[i][j][0]=projected_points[i][j][0]+cube_position[1]
                projected_points[i][j][0]=int(projected_points[i][j][0])
                
                
    draw_line(projected_points)
    angle = angle + speed

    
    scale=scale-scale_variable
    if scale > 400:
        scale_variable=scale_variable*(-1)
    elif scale < -400:
        scale_variable=scale_variable*(-1)
    
    
    

    pygame.display.update()
pygame.quit()





