# File pengimplementasian Visualisasi Grafik dan Pencetakan Layar
# 0. Impor modul eksternal
import matplotlib.pyplot as plt

# 1. Visualisasi titik dalam bidang 3 Dimensi - Perjelas Minimum [BONUS]
def VisualizeMinimum(listOfPoints, point1, point2) :
    fig = plt.figure(figsize=(11,7))
    ax = fig.add_subplot(111, projection='3d')

    for i in range (len(listOfPoints)) :
        x = listOfPoints[i][0]
        y = listOfPoints[i][1]
        z = listOfPoints[i][2]

        ax.scatter(x,y,z, color='black')

    ax.scatter(point1[0],point1[1],point1[2], color='red')
    ax.scatter(point2[0],point2[1],point2[2], color='red')

    plt.show()

# 2. Cetak titik dalam bentuk kurung di terminal
def printPoint(Point) :
    n = len(Point) - 1
    a = "("
    for i in range (len(Point) - 1) :
        a += str(Point[i])
        a += ", "
    a += str(Point[n])
    a += ")"
    print('\033[92m' + a + '\033[0m', end="")
    
# 3. Cetak titik dalam bentuk kurung di file
def printPointFile(Point, f) :
    n = len(Point) - 1
    a = "("
    for i in range (len(Point) - 1) :
        a += str(Point[i])
        a += ", "
    a += str(Point[n])
    a += ")"
    print(a, file=f)

# 4. Cetak titik dari matriks di terminal
def printPointMatrix(ListOfPoint) :
    long = len(ListOfPoint)
    
    for i in range (long) :
        n = len(ListOfPoint[i]) - 1
        a = "("

        for j in range (len(ListOfPoint[i]) - 1) :
            a += str(ListOfPoint[i][j])
            a += ", "
        a += str(ListOfPoint[i][n])
        
        if (i != long - 1):
            a += "),"
        else :
            a += ")"

        print("\033[34m" + a + '\033[0m')
    
# 5. Cetak titik dari matriks di file
def printPointMatrixFile(ListOfPoint, f) :
    long = len(ListOfPoint) - 1
    
    for i in range (long) :
        n = len(ListOfPoint[i]) - 1
        a = "("

        for j in range (len(ListOfPoint[i]) - 1) :
            a += str(ListOfPoint[i][j])
            a += ", "
        a += str(ListOfPoint[i][n])
        a += "),"

        print(a, file=f)
    
    printPointFile(ListOfPoint[long], f)