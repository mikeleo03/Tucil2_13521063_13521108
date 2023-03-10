# File pengimplementasian Algoritma Brute Force
# 0. Impor modul eksternal, termasuk file
import Point
   
# 1. Implementasi Strategi Bruteforce untuk titik 3 dimensi
def BruteForceDist(listOfPoints) :
    compare = 0  # Inisiasi jumlah perbandingan yang dilakukan
    shortest = Point.EuclideanDist3(listOfPoints[0], listOfPoints[1])

    for i in range (len(listOfPoints)) :
        for j in range(i+1, len(listOfPoints)) :
            compare += 1
            titik = Point.EuclideanDist3(listOfPoints[i], listOfPoints[j])
            if (titik <= shortest):
                shortest = titik
                a = listOfPoints[i]
                b = listOfPoints[j]
                
    return a, b, shortest, compare

# 2. Implementasi Strategi Bruteforce untuk dimensi tergeneralisasi [BONUS]
def BruteForceDistGeneral(listOfPoints, dimention) :
    compare = 0  # Inisiasi jumlah perbandingan yang dilakukan
    shortest = Point.EuclideanDistGeneral(listOfPoints[0], listOfPoints[1], dimention)

    for i in range (len(listOfPoints)) :
        for j in range(i+1, len(listOfPoints)) :
            compare += 1
            titik = Point.EuclideanDistGeneral(listOfPoints[i], listOfPoints[j], dimention)
            if (titik <= shortest):
                shortest = titik
                a = listOfPoints[i]
                b = listOfPoints[j]
                
    return a, b, shortest, compare