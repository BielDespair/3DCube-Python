# Cubo 3D com Matrizes de Rotação em Pygame

Este projeto utiliza a biblioteca Pygame para criar um cubo 3D interativo. A manipulação do cubo é feita através de matrizes de rotação, permitindo que o usuário controle a rotação do cubo em tempo real.

## Tecnologias Utilizadas

- **Pygame**: Biblioteca para criação de jogos e simulações gráficas em Python.
- **Numpy**: Para cálculos matemáticos e manipulação de matrizes.

## Funcionalidades

- **Rotação do Cubo**: Controle a rotação do cubo em tempo real usando as teclas `A`, `D`, `W` e `S`.
- **Reset do Cubo**: Pressione `R` para resetar o cubo à sua posição inicial.

## Como Executar

1. Certifique-se de ter o Python instalado na sua máquina.
2. Instale as bibliotecas necessárias:
    ```python
    pip install pygame numpy
    ```
3. Importe a pygame no seu arquivo principal:
    ```python
    import pygame
    ```
4. Importe o objeto cubo:
    ```python
    from cube import Cube3D
    ```
5. Inicialize um objeto Cube3D:
    ```python
    #Selecione o tamanho do cubo e a escala em relação a janela
    cube = Cube3D(1, scale=150)
    ```
6. Inicialize suas configurações de pygame e execute os seguintes métodos dentro do loop principal (siga na seção 'Código de Exemplo'):
    ```python

    #Dentro do loop pygame
    janela_pygame.fill((0, 0, 0))
    cube.display(janela_pygame)
    cube.update()

    pygame.display.flip()
    pygame.display.update()
    ```

## Classe `cube3D`

A classe `cube3D` é responsável por modelar e gerenciar o cubo 3D.

### Atributos

- `size`: Tamanho do cubo.
- `color`: Cor do cubo.
- `scale`: Escala do cubo.
- `origin`: Origem do cubo no espaço 3D.
- `tetha`: Ângulo inicial de rotação do cubo.
- `vertices`: Lista de vértices do cubo.
- `speed`: Velocidade de rotação.
- `ax_speed`, `ay_speed`, `az_speed`: Velocidades de rotação em torno dos eixos x, y e z.
- `x_axis_angle`, `y_axis_angle`, `z_axis_angle`: Ângulos atuais de rotação em torno dos eixos x, y e z.

### Métodos

- `__init__(self, size, scale=250, origin=(0, 0, 0), angle=45, color=(255, 255, 255))`: Inicializa o cubo com os parâmetros fornecidos.
- `display(self, screen)`: Exibe o cubo na tela.
- `connectVertices(self, screen, vertex1, vertex2)`: Conecta dois vértices com uma linha.
- `update(self)`: Atualiza a posição dos vértices com base nas rotações.
- `debug(self, screen, renders)`: Exibe informações de depuração na tela.
- `initializeVertices(self)`: Inicializa os vértices do cubo.
- `projectVertices(self)`: Projeta os vértices 3D em um plano 2D.
- `getVertices(self)`: Retorna uma string com as coordenadas dos vértices.

## Código de Exemplo

```python
#main

import pygame
from cube import Cube3D

#Inicializa o objeto
cube = Cube3D(1, scale=150)

#Inicializa as configurações do pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720))

#Para lidar com os inputs do usuário
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

#Loop principal pygame
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    handleKeys()
        
    screen.fill((0, 0, 0))
    cube.display(screen)
    cube.update()
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)
