# File pengimplementasian Pemrosesan Titik
# 0. Impor modul eksternal
import random
import math

# 1. Pembangkit titik koordinat acak
def RandomPoint(dimention) :
    return [round(random.uniform(-1000, 1000), 2) for i in range (dimention)]

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

# 5. Implementasi QuickSort
# 5.1. Partisi untuk performasi QuicSort
def Partition(listOfPoints, min, max, target):
    pivot = listOfPoints[max]  # menentukan pivot
    i = min - 1  # penunjuk i

    # bandingkan nilai dengan pivot
    for j in range(min, max):
        if listOfPoints[j][target] <= pivot[target]:
            # kalau lebih kecil, pindah penunjuk i ke elemen selanjutnya
            i = i + 1
            # Prosedur swap
            temp = listOfPoints[i]
            listOfPoints[i] = listOfPoints[j]
            listOfPoints[j] = temp

    # jangan lupa swap yang terakhir
    temp = listOfPoints[i + 1]
    listOfPoints[i + 1] = listOfPoints[max]
    listOfPoints[max] = temp

    # kembalikan posisi partisi
    return i + 1

# 5.2. Algoritma utama QuickSort
def QuickSort(listOfPoints, min, max, target):
    if min < max:
        # menentukan letak partisi berdasarkan prosedur sebelumnya
        pos = Partition(listOfPoints, min, max, target)
        # Jalankan rekursifitas untuk bagian kanan dan kiri pivot
        QuickSort(listOfPoints, min, pos - 1, target)
        QuickSort(listOfPoints, pos + 1, max, target)
    
    # Kembalikan hasil sort
    return listOfPoints