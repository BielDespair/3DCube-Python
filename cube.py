from numpy import cross, array
from pygame import draw
from tools import *

class Cube3D():
    def __init__(self, size, scale=250, origin=(0, 0, 0), angle=45,color=(255, 255, 255)):
        
        #Display Properties
        self.size = size
        self.color = color
        self.scale = self.size * scale
        
        #Geometric Properties
        self.origin = array(origin)
        self.tetha = angle
        self.vertices = self.initializeVertices()
        
        #Update Properties
        self.speed = 1
        self.ax_speed = 0
        self.ay_speed = 0
        self.az_speed = 0
        
        
        #Debug Properties
        self.x_axis_angle = 0
        self.y_axis_angle = 0
        self.z_axis_angle = 0
    
    def display(self, screen):
        vertexRadius = self.size * self.scale * 0.025
        
        projected_vertices = self.projectVertices()
        
        for i, vertex in enumerate(projected_vertices):
            coord = convertPygame(screen, self.scale, vertex)
            draw.circle(screen, self.verticesColor[i], coord, vertexRadius)
        
        #Xy Plane
        self.connectVertices(screen, projected_vertices[0], projected_vertices[1])
        self.connectVertices(screen, projected_vertices[0], projected_vertices[2])
        self.connectVertices(screen, projected_vertices[2], projected_vertices[3])
        self.connectVertices(screen, projected_vertices[1], projected_vertices[3])
        
        #Xy + Z Plane
        self.connectVertices(screen, projected_vertices[4], projected_vertices[5])
        self.connectVertices(screen, projected_vertices[4], projected_vertices[6])
        self.connectVertices(screen, projected_vertices[6], projected_vertices[7])
        self.connectVertices(screen, projected_vertices[5], projected_vertices[7])
        
        #Xz + Y Plane
        self.connectVertices(screen, projected_vertices[0], projected_vertices[4])
        self.connectVertices(screen, projected_vertices[1], projected_vertices[5])
        self.connectVertices(screen, projected_vertices[2], projected_vertices[6])
        self.connectVertices(screen, projected_vertices[3], projected_vertices[7])
        

            

        
            
    def connectVertices(self, screen, vertex1, vertex2):
        start = convertPygame(screen, self.scale, vertex1)
        end = convertPygame(screen, self.scale, vertex2)
        draw.line(screen, self.color, start, end)
        
        
        
    
    def update(self):
        ax_speed = self.ax_speed * self.speed
        ay_speed = self.ay_speed * self.speed
        az_speed = self.az_speed * self.speed
        
        if self.x_axis_angle > radians(360):
            self.x_axis_angle = 0
        elif self.x_axis_angle < radians(-360):
            self.x_axis_angle = 0
            self.ax_speed *= -1
        if self.y_axis_angle > radians(360):
            self.y_axis_angle = 0
        elif self.y_axis_angle < radians(-360):
            self.y_axis_angle = 0
            self.ay_speed *= -1
        if self.z_axis_angle > radians(360):
            self.z_axis_angle = 0
        elif self.z_axis_angle < radians(-360):
            self.z_axis_angle = 0
            self.az_speed *= -1
            
            
        self.x_axis_angle = self.x_axis_angle + radians(ax_speed)
        self.y_axis_angle = self.y_axis_angle + radians(ay_speed)
        self.z_axis_angle = self.z_axis_angle + radians(az_speed)
        #Update vertices
        for i in range(1, len(self.vertices)):
            vertex = self.vertices[i]
            vertex = rotate3D(vertex, ax_speed, 'y')
            vertex = rotate3D(vertex, ay_speed, 'x')
            vertex = rotate3D(vertex, az_speed, 'z')
            self.vertices[i] = vertex
            
            
            
        
    def debug(self, screen, renders):
        for i, text in enumerate(renders):
            screen.blit(text, (0, 0 + (i*20)))

    
    def initializeVertices(self):
        vertices = []
        
        #Point 0 - Origin
        vec = self.origin
        vertices.append(array((vec[0], vec[1], vec[2])))
        
        #Point 1 - ax
        ax = vec + array((1, 0, 0))
        vertices.append(array((ax)))
        
        #Point 2 - ay
        ay = vec + array((0, 1, 0))
        vertices.append(array((ay)))
        
        #Point 3 - sum of vectors ax and ay
        vertices.append(ax + ay)
        
        #Points 4 to 7: above xy plane
        
        #Point 4 - az (ax and ay orthogonal, so az = cross product of ax and ay)
        u = (ax[0], ax[1], ax[2])
        v = (ay[0], ay[1], ay[2])
        az = cross(u, v)

        vertices.append(az)
        
        #Point 5 - sum of vectors ax and az
        vertices.append(ax + az)
        
        #Point 6 - sum of vectors ay and az
        vertices.append(ay + az)
        
        #Point 7 - Sum of all vectors
        vertices.append(ax + ay + az)
        
        for i, vertex in enumerate(vertices):
            vertex = rotate3D(vertex, self.tetha, 'x')
            vertex = rotate3D(vertex, self.tetha/2, 'y')
            vertices[i] = vertex
            
        self.verticesColor = ((255, 255, 255), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (150, 150, 150), (255, 25, 25))
        return vertices
        

            
    def projectVertices(self):
        projected_vectors = []

        for vertex in self.vertices:
            projection = projectTo2D(vertex)
            projected_vectors.append(array ( (projection[0], projection[1]) ) )

        return projected_vectors
    
    def getVertices(self):
        string = ''
        for i, vertex in enumerate(self.vertices):
            appending = f"Vertex {i}: ({vertex[0]}, {vertex[1]}, {vertex[2]})\n"
            string += appending
        return string





