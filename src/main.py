# Implementasi Algoritma Utama
# Importing modules
import os
import math
import random
import matplotlib.pyplot as plt

# 0.1. Pembangkit titik koordinat acak
def RandomPoint(dimention) :
    return [random.randint(-100, 100) for i in range (dimention)]

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

# 1.2. Persamaan Euclidean distance (Tergeneralisasi) [BONUS]
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
def lineCenterClosest(lineCenter, size, minimum, am, bm, dimention):
    # Pendefinisian nilai dari parameter, sebagai handler kalau nilainya sama
    min_dist = minimum
    min_p1 = am
    min_p2 = bm
    
    # Membuat lineCenter dengan melakukan pengurutan berdasarkan nilai koordinat [1]
    lineCenter = sorted(lineCenter, key=lambda point: point[1])

    # Melakukan pengujian jarak terdekat dari titik disekitar pusat dalam batas toleransi
    for i in range(size):
        for j in range(i+1, size):
            # Kalau ukurannya lebih besar dari delta, lewati
            if (lineCenter[j][1] - lineCenter[i][1]) >= min_dist:
                break

            # Kalau lebih kecil, update nilai terkecilnya dan titik yang berkoresponden
            if EuclideanDistGeneral(lineCenter[i], lineCenter[j], dimention) < min_dist:
                min_dist = EuclideanDistGeneral(lineCenter[i], lineCenter[j], dimention)
                min_p1 = lineCenter[i]
                min_p2 = lineCenter[j]
    
    # Pengembalian dua titik terdekat dalam batas lineCenter dan jaraknya
    return min_p1, min_p2, min_dist

# 5.1. Implementasi rekursif cari kanan kiri (3 dimensi)
def ClosestPairPoint3(listOfPoints, numbers) :
    # Kondisi pemberhenti rekursifitas, saat jumlah elemen partisi sudah terbatas
    if numbers <= 3:
        a, b, dist = bruteForceDist(listOfPoints)
        # Mengembalikan 2 titik dan nilai jaraknya
        return a, b, dist
    
    # Sebelum melakukan pemrosesan, titik diurutkan menaik menggunakan fungsi sortPoints
    sorted = SortPoints(listOfPoints)
    
    # Ambil titik tengah partisi
    midPoint = numbers // 2
    
    # Mencari titik dengan jarak terdekat di kanan dan kiri lineCenter secara rekursif
    a1, b1, dist_left = ClosestPairPoint3(sorted[:midPoint], midPoint)
    a2, b2, dist_right = ClosestPairPoint3(sorted[midPoint:], numbers - midPoint)
    
    # Mengambil nilai minimum dari jarak terdekat bagian kanan dan kiri serta titiknya
    min = minimum(dist_left, dist_right)
    if (min == dist_left) :
        am = a1
        bm = b1
    else :
        am = a2
        bm = b2
        
    # Mendefinisikan lineCenters, mengisi elemen linecenter dengan batas nilai delta, yaitu min
    lineCenter = []
    for i in range(numbers):
        if abs(sorted[i][0] - sorted[midPoint][0]) < min:
            lineCenter.append(sorted[i])
    
    # Mengambil nilai terkecuil disekitar lineCenter
    p1, p2, val = lineCenterClosest(lineCenter, len(lineCenter), min, am, bm, 3)
    
    # Membandingkan nilai sekitar lineCenter dengan nilai minimum partisi dan ambil titiknya
    min_pol = minimum(min, val)
    if (min_pol == min) :
        a_min = am
        b_min = bm
    else :
        a_min = p1
        b_min = p2
    
    # mengembalikan hasil final, yaitu kedua titik dengan jarak terdekat dan jaraknya
    return a_min, b_min, min_pol

# 5.2. Implementasi rekursif cari kanan kiri (Tergeneralisasi) [BONUS]
def ClosestPairPointGeneral(listOfPoints, numbers, dimention) :
    # Kondisi pemberhenti rekursifitas, saat jumlah elemen partisi sudah terbatas
    if numbers <= 3:
        a, b, dist = bruteForceDistGeneral(listOfPoints, dimention)
        # Mengembalikan 2 titik dan nilai jaraknya
        return a, b, dist
    
    # Sebelum melakukan pemrosesan, titik diurutkan menaik menggunakan fungsi sortPoints
    sorted = SortPoints(listOfPoints)
    
    # Ambil titik tengah partisi
    midPoint = numbers // 2
    
    # Mencari titik dengan jarak terdekat di kanan dan kiri lineCenter secara rekursif
    a1, b1, dist_left = ClosestPairPointGeneral(sorted[:midPoint], midPoint, dimention)
    a2, b2, dist_right = ClosestPairPointGeneral(sorted[midPoint:], numbers - midPoint, dimention)
    
    # Mengambil nilai minimum dari jarak terdekat bagian kanan dan kiri serta titiknya
    min = minimum(dist_left, dist_right)
    if (min == dist_left) :
        am = a1
        bm = b1
    else :
        am = a2
        bm = b2
        
    # Mendefinisikan lineCenters, mengisi elemen linecenter dengan batas nilai delta, yaitu min
    lineCenter = []
    for i in range(numbers):
        if abs(sorted[i][0] - sorted[midPoint][0]) < min:
            lineCenter.append(sorted[i])
    
    # Mengambil nilai terkecuil disekitar lineCenter
    p1, p2, val = lineCenterClosest(lineCenter, len(lineCenter), min, am, bm, dimention)
    
    # Membandingkan nilai sekitar lineCenter dengan nilai minimum partisi dan ambil titiknya
    min_pol = minimum(min, val)
    if (min_pol == min) :
        a_min = am
        b_min = bm
    else :
        a_min = p1
        b_min = p2
    
    # mengembalikan hasil final, yaitu kedua titik dengan jarak terdekat dan jaraknya
    return a_min, b_min, min_pol
    
# 6.1. Implementasi Strategi Bruteforce untuk titik 3 dimensi
def bruteForceDist(listOfPoints) :
    shortest = EuclideanDist3(listOfPoints[0], listOfPoints[1])

    for i in range (len(listOfPoints)) :
        for j in range(len(listOfPoints)) :
            if (i != j) and (EuclideanDist3(listOfPoints[i], listOfPoints[j]) <= shortest):
                shortest = EuclideanDist3(listOfPoints[i], listOfPoints[j])
                a = listOfPoints[i]
                b = listOfPoints[j]
                
    return a, b, shortest

# 6.2. Implementasi Strategi Bruteforce untuk dimensi tergeneralisasi [BONUS]
def bruteForceDistGeneral(listOfPoints, dimention) :
    shortest = EuclideanDistGeneral(listOfPoints[0], listOfPoints[1], dimention)

    for i in range (len(listOfPoints)) :
        for j in range(len(listOfPoints)) :
            if (i != j) and (EuclideanDistGeneral(listOfPoints[i], listOfPoints[j], dimention) <= shortest):
                shortest = EuclideanDistGeneral(listOfPoints[i], listOfPoints[j], dimention)
                a = listOfPoints[i]
                b = listOfPoints[j]
                
    return a, b, shortest

# 7.1. Visualisasi titik dalam bidang 3 Dimensi - Normal
def visualize(listOfPoints) :
    fig = plt.figure(figsize=(11,7))
    ax = fig.add_subplot(111, projection='3d')

    for i in range (len(listOfPoints)) :
        x = listOfPoints[i][0]
        y = listOfPoints[i][1]
        z = listOfPoints[i][2]

        ax.scatter(x,y,z, color='red')
    
    plt.show()

# 7.2. Visualisasi titik dalam bidang 3 Dimensi - Perjelas Minimum [BONUS]
def visualizeMinimum(listOfPoints, point1, point2) :
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

# 8. Cetak titik dalam bentuk kurung
def printPoint(Point) :
    n = len(Point) - 1
    a = "("
    for i in range (len(Point) - 1) :
        a += str(Point[i])
        a += ", "
    a += str(Point[n])
    a += ")"
    print(a)

# 9. Cetak titik dari matriks
def printPointMatrix(ListOfPoint) :
    long = len(ListOfPoint) - 1
    
    for i in range (long) :
        n = len(ListOfPoint[i]) - 1
        a = "("

        for j in range (len(ListOfPoint[i]) - 1) :
            a += str(ListOfPoint[i][j])
            a += ", "
        a += str(ListOfPoint[i][n])
        a += "),"

        print(a)
    
    printPoint(ListOfPoint[long])
        

# 10. Program Utama
os.system('cls') # Clear screen
print("Selamat Datang di Program Closest-Pair Points Detector!\n")

# Tampilan pilihan menu
print("====================  INPUT  ====================")
print("Data titik seperti apa yang kamu pilih ?")
print("1. Tiga dimensi")
print("2. N dimensi")
pilihan = int(input("Masukkan pilihanmu (1/2) : "))

# Validasi masukan
while (pilihan != 1 and pilihan != 2):
    print("Pilihan tidak valid, ulangi!")
    print("-------------------------------------------------\n")
    print("Data titik seperti apa yang kamu pilih ?")
    print("1. Tiga dimensi")
    print("2. N dimensi")
    pilihan = int(input("Masukkan pilihanmu (1/2) : "))
    
# Pemrosesan berdasarkan pilihan
if (pilihan == 1):
    print("\n=============  PASANGAN 3 DIMENSI  ==============")
    titik = int(input("Masukkan jumlah titik : "))
    pointMatrix = ListRandomPoint(3, titik)
    print("\n===========  PEMBANGKITAN TITIK ACAK  ===========")
    print("Daftar kumpulan titik")
    printPointMatrix(pointMatrix)
    print("\n===============  HASIL ALGORITMA  ===============")
    pts1, pts2, shortest1 = bruteForceDist(pointMatrix)
    print("Menurut Algoritma BruteForce --")
    print(f'Dua titik terdekat yaitu {pts1} dan {pts2} dengan jarak {shortest1}')
    pts3, pts4, shortestcln1 = ClosestPairPoint3(pointMatrix, titik)
    print("Menurut Algoritma Divide and Conquer --")
    print(f'Dua titik terdekat yaitu {pts3} dan {pts4} dengan jarak {shortestcln1}')
    
    # Penampilan grafik
    print("\n==============  PENAMPILAN GRAFIK  ==============")
    print("Apakah ingin menampilkan hasil ilustrasi titik ?")
    pilihan = input("Masukkan pilihanmu (Y/n) : ")
    
    # Validasi masukan
    while (pilihan != "Y" and pilihan != "y" and pilihan != "N" and pilihan != "n"):
        print("Pilihan tidak valid, ulangi!")
        print("-------------------------------------------------\n")
        print("Apakah ingin menampilkan hasil ilustrasi titik ?")
        pilihan = input("Masukkan pilihanmu (Y/n) : ")
        
    # Pemrosesan masukan
    if (pilihan == "Y" or pilihan == "y"):
        print("\nPemrosesan sedang berlangsung....")
        visualizeMinimum(pointMatrix, pts1, pts2)
        print(" ")
        
else :
    print("\n=============  PASANGAN N DIMENSI  ==============")
    dimensi = int(input("Masukkan jumlah dimensi : "))
    titik = int(input("Masukkan jumlah titik : "))
    pointMatrix = ListRandomPoint(dimensi, titik)
    print("\n===========  PEMBANGKITAN TITIK ACAK  ===========")
    print("Daftar kumpulan titik")
    printPointMatrix(pointMatrix)
    print("\n===============  HASIL ALGORITMA  ===============")
    pts1, pts2, shortest1 = bruteForceDistGeneral(pointMatrix, dimensi)
    print("Menurut Algoritma BruteForce --")
    print(f'Dua titik terdekat yaitu {pts1} dan {pts2} dengan jarak {shortest1}')
    pts3, pts4, shortestcln1 = ClosestPairPointGeneral(pointMatrix, titik, dimensi)
    print("Menurut Algoritma Divide and Conquer --")
    print(f'Dua titik terdekat yaitu {pts3} dan {pts4} dengan jarak {shortestcln1}\n')