import pygame
from cube import Cube3D


pygame.init()
pygame.font.init()

'''
pygame.mixer.init()
pygame.mixer.music.load('song.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.01)
'''

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720))
font = pygame.font.SysFont('Arial', 15)


cube = Cube3D(1, scale=150)


def handleKeys():
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
        cube.ax_speed = 1
    elif keys[pygame.K_d]:
        cube.ax_speed = -1
    else:
        cube.ax_speed = 0
    if keys[pygame.K_w]:
        cube.ay_speed = 1
    elif keys[pygame.K_s]:
        cube.ay_speed = -1
    else:
        cube.ay_speed = 0
        
    if keys[pygame.K_r]:
        cube.vertices = cube.initializeVertices()
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    handleKeys()
        
    screen.fill((0, 0, 0))
    cube.display(screen)
    cube.update()
    
        
    rotation_speed = font.render(f"Rotation Speed: {cube.speed}", True, (255, 255, 255))
    
    cube_x_axis = font.render(f"x_axis: ({cube.vertices[1][0]:.3f}, {cube.vertices[1][1]:.3f})", True, (255, 255, 255))
    cube_y_axis = font.render(f"y_axis: ({cube.vertices[2][0]:.3f}, {cube.vertices[2][1]:.3f})", True, (255, 255, 255))
    cube_z_axis = font.render(f"z_axis: ({cube.vertices[3][0]:.3f}, {cube.vertices[3][1]:.3f})", True, (255, 255, 255))
    
    
    renders = [rotation_speed, cube_x_axis, cube_y_axis, cube_z_axis]
    cube.debug(screen, renders)
    
    pygame.display.flip()
    
    pygame.display.update()
    clock.tick(60)

    
    
    
    
