# Implementasi Algoritma Utama
# Importing modules
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
def visualizeMinimum(listOfPoints) :
    fig = plt.figure(figsize=(11,7))
    ax = fig.add_subplot(111, projection='3d')

    for i in range (len(listOfPoints)) :
        x = listOfPoints[i][0]
        y = listOfPoints[i][1]
        z = listOfPoints[i][2]

        ax.scatter(x,y,z, color='black')
    
    point1, point2, dist = bruteForceDist(listOfPoints)

    ax.scatter(point1[0],point1[1],point1[2], color='red')
    ax.scatter(point2[0],point2[1],point2[2], color='red')

    plt.show()

# 8. Cetak titik dalam bentuk kurung
def printPoint(Point) :
    # Contoh masukan : [2,3,4]
    # Keluaran : (2, 3, 4)
    # TODO : IMPLEMENT
    return Point

# 9. Cetak titik dari matriks
def printPointMatrix(ListOfPoint) :
    # Contoh masukan : [[2,3,4], [1,7,4], [2,11,-3]]
    # Keluaran : 
    # (2, 3, 4),
    # (1, 7, 4),
    # (2, 11, -3)
    # TODO : IMPLEMENT
    return ListOfPoint

# 10. Program Utama
print("Selamat Datang di Program ClesestPair Points!")

# Tampilan pilihan menu
print("Data titik seperti apa yang kamu pilih ?")
print("1. Tiga dimensi")
print("2. N dimensi")
pilihan = int(input("Masukkan pilihanmu : "))

# Validasi masukan
while (pilihan != 1 and pilihan != 2):
    print("Pilihan tidak valid, ulangi!")
    print("Data titik seperti apa yang kamu pilih ?")
    print("1. Tiga dimensi")
    print("2. N dimensi")
    pilihan = int(input("Masukkan pilihanmu : "))
    
# Pemrosesan berdasarkan pilihan
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

p = ListRandomPoint(3, 10)
print("Daftar kumpulan titik")
print(p)
pts1, pts2, shortest1 = bruteForceDistGeneral(p, 3)
print(f'Dua titik terdekat yaitu {pts1} dan {pts2} menurut BruteForce dengan jarak {shortest1}')
pts3, pts4, shortestcln1 = ClosestPairPointGeneral(p, 10, 3)
print(f'Dua titik terdekat yaitu {pts3} dan {pts4} menurut DnC dengan jarak {shortestcln1}')

# Note : implement bonus ilustrasi dan generalized R^n point di file terpisah aja okeng