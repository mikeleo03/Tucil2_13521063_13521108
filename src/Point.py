# File pengimplementasian Pemrosesan Titik
# 0. Impor modul eksternal
import random
import math

# 1. Pembangkit titik koordinat acak
def RandomPoint(dimention) :
    return [random.randint(-100, 100) for i in range (dimention)]

# 2. Inisialisasi senarai hasil pembangkit titik koordinat acak
def ListRandomPoint(dimention, numbers) :
    return [RandomPoint(dimention) for i in range (numbers)]

# 3. Persamaan Euclidean distance (3 dimensi)
def EuclideanDist3(point1, point2) :
    # Persamaan : sqrt((x1-x2)^2 + (y1-y2)^2 + (z1-z2)^2)
    xdist = pow(point1[0] - point2[0], 2)
    ydist = pow(point1[1] - point2[1], 2)
    zdist = pow(point1[2] - point2[2], 2)
    return math.sqrt(xdist + ydist + zdist)

# 4. Persamaan Euclidean distance (Tergeneralisasi) [BONUS]
def EuclideanDistGeneral(point1, point2, dimention) :
    # Persamaan : sqrt((x1-x2)^2 + (y1-y2)^2 + (z1-z2)^2 + ...)
    # Inisialisasi senarai hasil
    hasil = [0 for i in range (dimention)]
    
    # Melakukan pemrosesan per subdimensi dan kalkulasi hasil total
    result = 0
    for i in range (dimention) :
        hasil[i] = pow(point1[i] - point2[i], 2)
        result += hasil[i]
        
    # Finalisasi hasil
    return math.sqrt(result)

# 5. Melakukan pengurutan titik berdasarkan nilai koordinat [0]
def SortPoints(listOfPoints) :
    listOfPoints.sort(key = lambda point : point[0])
    return listOfPoints