import matplotlib.pyplot as plt
import pandas as pd
import random
import networkx as nx
import time

def warshall_standard(matrix):
    n = len(matrix)
    closure = [row[:] for row in matrix]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                closure[i][j] = closure[i][j] or (closure[i][k] and closure[k][j])
    return closure


def warshall_by_definition(matrix):
    n = len(matrix)
    closure = [row[:] for row in matrix]
    changed = True
    while changed:
        changed = False
        for i in range(n):
            for j in range(n):
                if closure[i][j] == 1:
                    for k in range(n):
                        if closure[j][k] == 1 and closure[i][k] == 0:
                            closure[i][k] = 1
                            changed = True
    return closure


def compare_warshall_speeds(matrix):
    start = time.time()
    result_standard = warshall_standard(matrix)
    end = time.time()
    standard_time = end - start

    start = time.time()
    result_definition = warshall_by_definition(matrix)
    end = time.time()
    definition_time = end - start

    print("زمان اجرای وارشال استاندارد: {:.6f} ثانیه".format(standard_time))
    print("زمان اجرای وارشال بر اساس تعریف: {:.6f} ثانیه".format(definition_time))

    return result_standard, result_definition


def generate_random_matrix_to_csv(n, filename="matrix.csv"):

    matrix = [[random.randint(0, 1) for _ in range(n)] for _ in range(n)]
    df = pd.DataFrame(matrix)
    df.to_csv(filename, index=False, header=False)
    return matrix, n, n


def read_matrix_from_csv(filename="matrix.csv"):

    df = pd.read_csv(filename, header=None)
    matrix = df.values.tolist()
    return matrix, len(matrix), len(matrix[0])

def matrix():
    # matrix: Az karbar size matrix migire (mesl 3x3), va meghdare an ra be sorat 0 ya 1 daryaft mikone
    try :
        matrixsize = input("Please enter matrix input like this ( 2x2 , 3x3 , ...): ")
        satr1, soton1 = matrixsize.lower().split("x")
        satr1 , soton1 = int(satr1), int(soton1)
        matrixarray = []

        for i in range (satr1):
            matrixarray.append([])

        for satr in range (0,satr1) : 
            for soton in range(0,soton1) :
                while True :
                    try:
                        index = int(input(f"Enter Satr({satr}), Soton({soton}) : "))
                        if index in [0, 1]:    
                            matrixarray[satr].append(index)
                            break
                        else:
                            print("Only Enter 0 / 1")
                    except ValueError:
                        print("Please enter only 0 / 1")
                                
        return matrixarray , satr1 , soton1
    
    except ValueError:
        print("Enter correct size !")
        return matrix()

def zarb_boli(array1,satr1,soton1,array2,satr2,soton2) : # 4
# zarb_boli: Zarb-e Boolean do ta matrix ro anjam mide. (or ba and mesle zarb riyazi vali ba 0/1)
    if soton1 == satr2 :
        
        result = []

        for satr in range(satr1) :
            row = []
            for soton in range(soton2) :
                value = 0 
                for indx in range(soton1):

                    value = value or (array1[satr][indx] and array2[indx][soton])
                row.append(int(value))
            result.append(row)

        return result,len(result),len(result[0])
    else : 
        print("2 ta matrix shoma ghabeliat zarb boli nadarand")
        return

def show_graph(array1) : # 2
# show_graph: Matrixe voroodi ro be soorat graph ba networkx rasm mikone
# az tarighe edge ha va node ha graph neshoon mide ke az matrix rabete sakhte shode

    n = len(array1)
    graph = nx.DiGraph()

    for i in range(n):
        graph.add_node(i)
        for j in range(len(array1[i])):  
            if array1[i][j] == 1:
                graph.add_edge(i, j)

    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=800, arrows=True)
    plt.title("showing graph")
    plt.show()

    return graph

def vast_rasand(array1,array2): # 3
# vast_rasand: do matrix ba ham moghayese mishe
# vast = AND / rasand = OR  --> har element ba ham moghayese mishe
    choice = input("vast or rasand :").lower()
    if choice not in ("vast" , "rasand"):
        print("Entekhab Eshtebah")
        return 
    result = []
    for i in range(len(array1)):
        row = []
        for j in range(len(array1[0])):
            if choice == "vast" :
                v = int(array1[i][j] and array2[i][j])
            elif choice == "rasand" :
                v = int(array1[i][j] or array2[i][j])
            row.append(v)
        result.append(row)
    return result

def Khasiat(matrix,x,y): #  6
# Khasiat: tagharoni = matrix[i][j] == matrix[j][i]
# pad-tagharoni = agar i != j va har 2 taraf rabete dashte bashan pas pad-tagharon nist
# tarayayi = agar rabete mostaghim nist vali do rabete peyo pey bashe ke be on berese, bayad bashe
    Tagharoni = True
    Pad_Tagharoni = True
    Tarayayi = True
    for i in range(x) : 
        for j in  range(y) :
            if matrix[i][j] != matrix[j][i] :
                Tagharoni = False
            if i != j and matrix[i][j] == 1 and matrix[j][i] == 1 :
                Pad_Tagharoni = False
            if matrix[i][j]:
                for k in range(len(matrix)) :
                    if matrix[i][k] and matrix[k][j] and  matrix[i][j] == 0 :
                        Tarayayi = False
    print(f"Tagharoni : {Tagharoni}\nPad_Tagharoni : {Pad_Tagharoni}\nTarayayi : {Tarayayi}")


def Bastar(matrix,x,y):  # 7 ,8,9


    if x != y :
        print("Bastar Morabaei Nist")
        return
    Baztabi = [row[:] for row in matrix]
    Tagharoni = [row[:] for row in matrix]
    Tarayayi = [row[:] for row in matrix]
    for i in range(x) : 
        Baztabi[i][i] = 1

    for i in range(x) : 
        for j in range(y) : 
            if Tagharoni[i][j] == 1 :
                Tagharoni[j][i] = 1


    for i in range(x) :
        for j in range(x) : 
            for k in range(y)  :
                if Tarayayi[i][k] and Tarayayi[k][j] :
                    Tarayayi[i][j] = 1
    return Baztabi , Tagharoni , Tarayayi

def Warshall(matrix, x, y):
    """
    Warshall's algorithm to find transitive closure of a matrix
    Returns the transitive closure matrix
    """
    # Create a copy of the input matrix
    warsh = [row[:] for row in matrix]
    
    # Warshall's algorithm: for each vertex k, check if there's a path from i to j through k
    for k in range(x):  # k is the intermediate vertex
        for i in range(x):  # i is the source vertex
            for j in range(x):  # j is the destination vertex
                # If there's a path from i to k AND from k to j, then there's a path from i to j
                if warsh[i][k] and warsh[k][j]:
                    warsh[i][j] = 1
    
    return warsh
    


def RoS(matrix1,x1,y1,matrix2,x2,y2): # 10 matrix1 o matrix2
# RoS: Rabete az matrix2 be matrix1 ro mohasebe mikone (ba estefade az or va and)
# masalan baraye checking reachability ya enteghal rabete estefade mishe
    if y1 != x2 :
        print("Abaad Matrix nasazegar ast")
        return
    result = []
    for i in range(x2) :
        row= []
        for k in range(y1) :
            value = 0
            for j in range(y2) :
                if matrix2[i][j] == 1 and matrix1[j][k] == 1 :
                    value = 1
                    break
            row.append(value)
        result.append(row)
    return result

def printMatrix(matrix):
# printMatrix: matrix ro ghashang tabdil be print koni (satr be satr + tab)
    for row in matrix :
        for num in row :
            print(num,"\t",end="")
        print()

def GMatrixMojavaret(matrix): #11
# GMatrixMojavaret: matrixe rabete ro be soorat graph bi-samt (nx.Graph) neshoon mide
    graph = nx.Graph()

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):  
            if matrix[i][j] == 1: #and i < j   # vali age ham nabashe moshkeli nadare
                graph.add_edge(i, j)
    G = GMatrixMojavaret(matrix)
    nx.draw(G, with_labels=True)
    plt.show() 



def Daraje(matrix) : # 12
# baraye har satr jam mizane ke chand rabete dare
    darajeha = [] 
    for row in matrix : 
        darajeha.append(sum(row))
    return darajeha

def MotamamMatrix(matrix):
# MotamamMatrix: tamam khane ha ro baraks mikone (1 -> 0, 0 -> 1)
    Motamam = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                row.append(0)
            else :
                row.append(1)
        Motamam.append(row)
    return Motamam

def ZirGraph(g1,g2) : #14
# ZirGraph: check mikone aya matrix1 zirgraph matrix2 hast ya na
# yani har rabete dar g1, bayad dar g2 ham vojood dashte bashe
    Zir_Graph = True
    for i in range(len(g1)) :
        for j in range(len(g1)) :
            if g1[i][j] == 1 and g2[i][j] != 1 :
                Zir_Graph = False
    return Zir_Graph

def DFS(node, matrix, visited): #Depth Main Search
    visited[node] = True
    for neighbor in range(len(matrix)):
        if matrix[node][neighbor] == 1 and not visited[neighbor]:
            DFS(neighbor, matrix, visited)

def HamBand(matrix):
# HamBand: check mikone aya hame node ha be ham vasl hastan (bar asas DFS)
# agar hame true beshan pas ham-band hast
    visited = [False] * len(matrix) #15
    DFS(0, matrix, visited)
    return all(visited)

def show_menu():
    print("+" + "-"*40 + "+")
    print("|{:^40}|".format("MATRIX OPERATIONS PANEL"))
    print("+" + "-"*40 + "+")
    print("| {:<2} {:<36}|".format("2.", "Zarb boli Marix Ha"))
    print("| {:<2} {:<36}|".format("3.", "Graph matrix rabete"))
    print("| {:<2} {:<36}|".format("4.", "Vast va Rasand"))
    print("| {:<2} {:<36}|".format("5.", "Matrix Rn"))
    print("| {:<2} {:<36}|".format("6.", "Khasiat "))
    print("| {:<2} {:<36}|".format("7.", "Bastar ")) # 7 8 9
    print("| {:<2} {:<35}|".format("10.", "RoS"))
    print("| {:<2} {:<35}|".format("11.", "Graph Matrix Mojaverat"))
    print("| {:<2} {:<35}|".format("12.", "Daraje"))
    print("| {:<2} {:<35}|".format("13.", "MotamamMatrix"))
    print("| {:<2} {:<35}|".format("14.", "ZirGraph"))
    print("| {:<2} {:<35}|".format("15.", "HamBand"))
    print("| {:<2} {:<33}|".format("exit.", "Exit"))
    print("+" + "-"*40 + "+")