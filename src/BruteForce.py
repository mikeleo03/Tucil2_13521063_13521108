# File pengimplementasian Algoritma Brute Force
# 0. Impor modul eksternal, termasuk file
import Point
   
# 1. Implementasi Strategi Bruteforce untuk titik 3 dimensi
def BruteForceDist(listOfPoints) :
    compare = 0  # Inisiasi jumlah perbandingan yang dilakukan
    shortest = Point.EuclideanDist3(listOfPoints[0], listOfPoints[1])

    for i in range (len(listOfPoints)) :
        for j in range(len(listOfPoints)) :
            if (i != j):
                compare += 1
                if (Point.EuclideanDist3(listOfPoints[i], listOfPoints[j]) <= shortest):
                    shortest = Point.EuclideanDist3(listOfPoints[i], listOfPoints[j])
                    a = listOfPoints[i]
                    b = listOfPoints[j]
                
    return a, b, shortest, compare

# 2. Implementasi Strategi Bruteforce untuk dimensi tergeneralisasi [BONUS]
def BruteForceDistGeneral(listOfPoints, dimention) :
    compare = 0  # Inisiasi jumlah perbandingan yang dilakukan
    shortest = Point.EuclideanDistGeneral(listOfPoints[0], listOfPoints[1], dimention)

    for i in range (len(listOfPoints)) :
        for j in range(len(listOfPoints)) :
            if (i != j):
                compare += 1
                if (Point.EuclideanDistGeneral(listOfPoints[i], listOfPoints[j], dimention) <= shortest):
                    shortest = Point.EuclideanDistGeneral(listOfPoints[i], listOfPoints[j], dimention)
                    a = listOfPoints[i]
                    b = listOfPoints[j]
                
    return a, b, shortest, compare