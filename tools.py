from matrixMultiplication import matrixMultiplication
from math import cos, sin, radians


def transform(transformationMatrix, matrix):
    result = matrixMultiplication(transformationMatrix, matrix)
    return result


def rotate2D(tetha, vector) -> tuple[float, float]:
    if not type(vector) == tuple:
        print(f"Watch out! 2D Rotations requires a R² vector. The Vector was extended to R²: ({vector}) -> ({vector},0) ")
        vector = (vector, 0)
        
    elif len(vector) != 2:
        raise Exception("Vector must be a R² vector")
    
        
    rotationMatrix = [
        
        [cos(tetha), -sin(tetha)],
        [sin(tetha),  cos(tetha)]
        
        ]
    matrix = columnMatrix(vector)
    
    result = transform(rotationMatrix, matrix)
    
    return matrixToVector(result)

def projectTo2D(vector):
    matrix = columnMatrix(vector)

    projectionMatrix = [
        
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
        
        ]
    
    return matrixToVector(transform(projectionMatrix, matrix))

def rotate3D(vector, tetha, axis='x'):
    tetha = radians(tetha)
    matrix = columnMatrix(tuple(vector))
    Rx = [
        
        [1,      0,           0    ],
        [0, cos(tetha), -sin(tetha)],
        [0, sin(tetha), cos(tetha) ]
        
        ]
    
    Ry = [
        
        [cos(tetha), 0, sin(tetha)],
        [0,           1,      0    ],
        [-sin(tetha), 0, cos(tetha)]
        
        ]
    
    Rz = [
        
        [cos(tetha), -sin(tetha), 0],
        [sin(tetha), cos(tetha),  0],
        [0,           0,           1]
        
        ]
    
    match axis:
        case 'x':
            result = transform(Rx, matrix)
        case 'y':
            result = transform(Ry, matrix)
        case 'z':
            result = transform(Rz, matrix)
            
    return matrixToVector(result)
    
def columnMatrix(vector):
    matrix = []
    for i in range(0, len(vector)):
        line = [vector[i]]
        matrix.append(line)
    return matrix
        
def matrixToVector(matrix):
    vector = []
    for i in range(0, len(matrix)):
        vector.append(matrix[i][0])
    return tuple(vector)

def convertPygame(screen, scale, coordinates):
    width, height = screen.get_size()
    coordinates = (coordinates * scale)

    x, y = coordinates
    x_pos, y_pos = (width/2 + x, height / 2 + y)
    x_pos = x_pos - (width*0.075)
    
    pos = (x_pos, y_pos)
    return (pos)

def centerPygameMouse(screen, mouse_pos):
    width, height = screen.get_size()
    return (mouse_pos[0] - (width/2), mouse_pos[1] - (height/2))