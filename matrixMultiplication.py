def matrixMultiplication(m1, m2):
   #Checa se a quantidade de colunas da primeira matriz é igual a quantidade linhas da segunda.
    if len(m1[0]) != len(m2):
        raise Exception("The number of columns in the first matrix must be equal to the number of lines in the second matrix.")
    #Faz a transposta da segunda matriz.
    m2 = transpose(m2)
    m3 = []
    for lines in m1:
        #Inicializa a linha da nova matriz
        new_line = []
        for columns in m2:
            #Calcula a multiplicação de cada linha da primeira com cada coluna da segunda e adiciona na linha da nova matriz
            new_line.append(dotProduct(lines, columns))
           
        m3.append(new_line)
       
    return m3
 
 
#Calcula o produto escalar de dois vetores
def dotProduct(l1, l2):
    sum = 0
    for i in range(0, len(l1)):
        sum += l1[i] * l2[i]
    return sum
#Faz a transposta de uma matriz
def transpose(m):
    mT = []
    for i in range(0, len(m[0])):
        line = []
        for j in range(0, len(m)):
            line.append(m[j][i])
        mT.append(line)
    return mT