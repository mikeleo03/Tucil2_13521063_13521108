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
import visual
import matplotlib.pyplot as plt

# 0.1. Pembangkit titik koordinat acak
def RandomPoint(dimention) :
    return [random.randint(-10, 10) for i in range (dimention)]

# 0.2. Inisialisasi senarai hasil pembangkit titik koordinat acak
def ListRandomPoint(dimention, numbers) :
    return [RandomPoint(dimention) for i in range (numbers)]

# 1.1. Persamaan Euclidean distance (3 dimensi)
def EuclideanDist3(point1, point2) :
    # Persamaan : sqrt((x1-x2)^2 + (y1-y2)^2 + (z1-z2)^2)
    xdist = pow(point1[0] - point2[0], 2)
    ydist = pow(point1[1] - point2[1], 2)
    zdist = pow(point1[2] - point2[2], 2)
    return math.sqrt(xdist + ydist + zdist)

# 1.2. Persamaan Euclidean distance (Tergeneralisasi)
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

# 2. Melakukan pengurutan titik berdasarkan nilai koordinat [0]
def SortPoints(listOfPoints) :
    listOfPoints.sort(key = lambda point : point[0])
    return listOfPoints

# 3. Definisi nilai minimum dari 2 nilai masukan
def minimum(x, y):
    if (x > y) :
        return y
    else :
        return x

# 4. Pencarian titik terdekat yang berada di tengah dengan batas toleransi delta
def stripClosest(strip, size, minimum, am, bm, dimention):
    # Pendefinisian nilai dari parameter, sebagai handler kalau nilainya sama
    min_dist = minimum
    min_p1 = am
    min_p2 = bm
    
    # Membuat strip dengan melakukan pengurutan berdasarkan nilai koordinat [1]
    strip = sorted(strip, key=lambda point: point[1])

    # Melakukan pengujian jarak terdekat dari titik disekitar pusat dalam batas toleransi
    for i in range(size):
        for j in range(i+1, size):
            # Kalau ukurannya lebih besar dari delta, lewati
            if (strip[j][1] - strip[i][1]) >= min_dist:
                break

            # Kalau lebih kecil, update nilai terkecilnya dan titik yang berkoresponden
            if EuclideanDistGeneral(strip[i], strip[j], dimention) < min_dist:
                min_dist = EuclideanDistGeneral(strip[i], strip[j], dimention)
                min_p1 = strip[i]
                min_p2 = strip[j]
    
    # Pengembalian dua titik terdekat dalam batas strip dan jaraknya
    return min_p1, min_p2, min_dist

# 5.1. Implementasi rekursif cari kanan kiri (3 dimensi)
def ClosestPairPoint3(listOfPoints, numbers, dimention) :
    # Kondisi pemberhenti rekursifitas, saat jumlah elemen partisi sudah terbatas
    if numbers <= 3:
        a, b, dist = bruteForceDistGeneral(listOfPoints, dimention)
        # Mengembalikan 2 titik dan nilai jaraknya
        return a, b, dist
    
    # Sebelum melakukan pemrosesan, titik diurutkan menaik menggunakan fungsi sortPoints
    sorted = SortPoints(listOfPoints)
    midPoint = numbers // 2
    
    # Recursively find distance to left and right
    a1, b1, dist_left = ClosestPairPointGeneral(sorted[:midPoint], midPoint, dimention)
    a2, b2, dist_right = ClosestPairPointGeneral(sorted[midPoint:], numbers - midPoint, dimention)
    
    # minimum both
    min = minimum(dist_left, dist_right)
    if (min == dist_left) :
        am = a1
        bm = b1
    else :
        am = a2
        bm = b2
        
    # defining strips
    strip = []
    for i in range(numbers):
        if abs(sorted[i][0] - sorted[midPoint][0]) < min:
            strip.append(sorted[i])
    
    # Finishing
    p1, p2, val = stripClosest(strip, len(strip), min, am, bm, dimention)
    min_pol = minimum(min, val)
    if (min_pol == min) :
        a_min = am
        b_min = bm
    else :
        a_min = p1
        b_min = p2
    
    return a_min, b_min, min_pol

# 3.2. Implementasi rekursif cari kanan kiri (General)
def ClosestPairPointGeneral(listOfPoints, numbers, dimention) :
    if numbers <= 3:
        a, b, dist = bruteForceDistGeneral(listOfPoints, dimention)
        return a, b, dist
    
    sorted = SortPoints(listOfPoints)
    midPoint = numbers // 2
    
    # Recursively find distance to left and right
    a1, b1, dist_left = ClosestPairPointGeneral(sorted[:midPoint], midPoint, dimention)
    a2, b2, dist_right = ClosestPairPointGeneral(sorted[midPoint:], numbers - midPoint, dimention)
    
    # minimum both
    min = minimum(dist_left, dist_right)
    if (min == dist_left) :
        am = a1
        bm = b1
    else :
        am = a2
        bm = b2
        
    # defining strips
    strip = []
    for i in range(numbers):
        if abs(sorted[i][0] - sorted[midPoint][0]) < min:
            strip.append(sorted[i])
    
    # Finishing
    p1, p2, val = stripClosest(strip, len(strip), min, am, bm, dimention)
    min_pol = minimum(min, val)
    if (min_pol == min) :
        a_min = am
        b_min = bm
    else :
        a_min = p1
        b_min = p2
    
    return a_min, b_min, min_pol
    
# 5.1. Bruteforce 3 Points
def bruteForce(listOfPoints) :
    shortest = EuclideanDist3(listOfPoints[0], listOfPoints[1])

    for i in range (len(listOfPoints)) :
        for j in range(len(listOfPoints)) :
            if (i != j) and (EuclideanDist3(listOfPoints[i], listOfPoints[j]) <= shortest):
                shortest = EuclideanDist3(listOfPoints[i], listOfPoints[j])
                a = listOfPoints[i]
                b = listOfPoints[j]
                
    return a, b, shortest

# 5.2. Generalized bruteFirce
def bruteForceDistGeneral(listOfPoints, dimention) :
    shortest = EuclideanDistGeneral(listOfPoints[0], listOfPoints[1], dimention)

    for i in range (len(listOfPoints)) :
        for j in range(len(listOfPoints)) :
            if (i != j) and (EuclideanDistGeneral(listOfPoints[i], listOfPoints[j], dimention) <= shortest):
                shortest = EuclideanDistGeneral(listOfPoints[i], listOfPoints[j], dimention)
                a = listOfPoints[i]
                b = listOfPoints[j]
                
    return a, b, shortest

# Visualizing
def visualizeMinimum(listOfPoints) :
    fig = plt.figure(figsize=(11,7))
    ax = fig.add_subplot(111, projection='3d')

    for i in range (len(listOfPoints)) :
        x = listOfPoints[i][0]
        y = listOfPoints[i][1]
        z = listOfPoints[i][2]

        ax.scatter(x,y,z, color='black')
    
    point1, point2, dist = bruteForce(listOfPoints)

    ax.scatter(point1[0],point1[1],point1[2], color='red')
    ax.scatter(point2[0],point2[1],point2[2], color='red')

    plt.show()

# 5. Main program
""" b = ListRandomPoint(3, 100)
print("Daftar kumpulan titik")
print(b)
c = SortPoints(b)
print(c)
print("Euclidean distance 2 titik pertama")
print(EuclideanDist3(b[0],b[1]))
pt1, pt2, shortest = bruteForce(b)
print(f'Dua titik terdekat yaitu {pt1} dan {pt2} menurut BruteForce dengan jarak {shortest}')
shortestcln = ClosestPairPoint3(b, 100, 3)
print(f'Dua titik terdekat yaitu menurut DnC dengan jarak {shortestcln}') """
# visualizeMinimum(b)

""" b = ListRandomPoint(2, 10)
print("Daftar kumpulan titik")
print(b)
c = SortPoints(b)
print(c)
print("Euclidean distance 2 titik pertama")
print(EuclideanDistGeneral(b[0],b[1],2))
pt1, pt2, shortest = bruteForceDistGeneral(b, 2)
print(f'Dua titik terdekat yaitu {pt1} dan {pt2} menurut BruteForce dengan jarak {shortest}')
shortestcln = ClosestPairPoint3(b, 10)
print(f'Dua titik terdekat yaitu menurut DnC dengan jarak {shortestcln}') """

p = ListRandomPoint(5, 100)
print("Daftar kumpulan titik")
print(p)
pts1, pts2, shortest1 = bruteForceDistGeneral(p, 5)
print(f'Dua titik terdekat yaitu {pts1} dan {pts2} menurut BruteForce dengan jarak {shortest1}')
pts3, pts4, shortestcln1 = ClosestPairPointGeneral(p, 100, 5)
print(f'Dua titik terdekat yaitu {pts3} dan {pts4} menurut DnC dengan jarak {shortestcln1}')

# Note : implement bonus ilustrasi dan generalized R^n point di file terpisah aja okeng