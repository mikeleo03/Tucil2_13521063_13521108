# Implementasi Algoritma Utama
'''
Algorithm (basic scheme)
Input : Array of points represented using x and y coordinates

Step 0: Create an sorted array px which is sorted array of original array by x coordinate.
Create a sorted array py which is sorted array of original array by y coordinate.
Initialize low to 0 and high to n-1 (where n is length of the array)
Step 1: Find middle point of the px using (low+high)/2
Step 2: Divide px array into two halves, The first subarray containts from px[low] to px[mid] and second array contains from px[mid+1] to p[high]
Step 3: Recursively compute smallest distance from both left and right sub arrays leftMin and rightMin and then compute minimum of LeftMin and right which is called min.
Step 4: Create a strip of coordinates from py array whose distance is less than min, and compute minValue from strip of coordinates which is calles minFromStrip
Step 5: Finally the minimum is minimum of leftMin, rightMin and minFromStrip

Output : Pair of points which are closer in the plane

References :
https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorithm/
https://blog.devgenius.io/closest-pair-of-points-on-a-plane-divide-and-conquer-ea622870a9a7
https://itzsyboo.medium.com/algorithms-studynote-4-divide-and-conquer-closest-pair-49ba679ce3c7

'''
# Importing modules
import math
import random

# 0.1. Random Point Generator
def RandomPoint(dimention) :
    return [random.randint(-2, 2) for i in range (dimention)]

# 0.2. List of Random Point Generator
def ListRandomPoint(dimention, numbers) :
    return [RandomPoint(dimention) for i in range (numbers)]

# 1. Persamaan Euclidean distance (3 dimensi)
def EuclideanDist3(point1, point2) :
    # Persamaan : sqrt((x1-x2)^2 + (y1-y2)^2 + (z1-z2)^2)
    xdist = pow(point1[0] - point2[0], 2)
    ydist = pow(point1[1] - point2[1], 2)
    zdist = pow(point1[2] - point2[2], 2)
    return math.sqrt(xdist + ydist + zdist)

# 2. Jarak terdekat ke tengah lintas titik

# 3. Implementasi rekursif cari kanan kiri

# 4. Definisi terdekat

# 5. Main program
b = ListRandomPoint(3, 10)
print("Daftar kumpulan titik")
print(b)
print("Euclidean distance 2 titik pertama")
print(EuclideanDist3(b[0],b[1]))

# Note : implement bonus ilustrasi dan generalized R^n point di file terpisah aja okeng