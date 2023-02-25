# File pengimplementasian Algoritma Divide and Conquer
# 0. Impor modul eksternal, termasuk file
import Point
import BruteForce

# 1. Definisi nilai minimum dari 2 nilai masukan
def Minimum(x, y):
    if (x > y) :
        return y
    else :
        return x
    
# 2. Pencarian titik terdekat yang berada di tengah dengan batas toleransi delta
def LineCenterClosest(lineCenter, size, minimum, am, bm, dimention):
    # Pendefinisian nilai dari parameter, sebagai handler kalau nilainya sama
    min_dist = minimum
    min_p1 = am
    min_p2 = bm
    
    # Membuat lineCenter dengan melakukan pengurutan berdasarkan nilai koordinat [1]
    # lineCenter = sorted(lineCenter, key=lambda point: point[1])
    lineCenter = Point.QuickSort(lineCenter, 0, len(lineCenter) - 1, 1)

    # Melakukan pengujian jarak terdekat dari titik disekitar pusat dalam batas toleransi
    count = 0
    for i in range(size):
        for j in range(i+1, size):
            # Kalau ukurannya lebih besar dari delta, lewati
            if (lineCenter[j][1] - lineCenter[i][1]) >= min_dist:
                break
            else :
                count += 1
                # Kalau lebih kecil, update nilai terkecilnya dan titik yang berkoresponden
                if Point.EuclideanDistGeneral(lineCenter[i], lineCenter[j], dimention) < min_dist:
                    min_dist = Point.EuclideanDistGeneral(lineCenter[i], lineCenter[j], dimention)
                    min_p1 = lineCenter[i]
                    min_p2 = lineCenter[j]
    
    # Pengembalian dua titik terdekat dalam batas lineCenter dan jaraknya
    return min_p1, min_p2, min_dist, count

# 3. Implementasi rekursif cari kanan kiri (3 dimensi)
def ClosestPairPoint3(listOfPoints, numbers) :
    # Kondisi pemberhenti rekursifitas, saat jumlah elemen partisi sudah terbatas
    if numbers <= 3:
        a, b, dist, count = BruteForce.BruteForceDist(listOfPoints)
        # Mengembalikan 2 titik dan nilai jaraknya
        return a, b, dist, count
    
    # Sebelum melakukan pemrosesan, titik diurutkan menaik berdasarkan nilai koordinat [0]
    # sorted = Point.SortPoints(listOfPoints)
    sorted = Point.QuickSort(listOfPoints, 0, len(listOfPoints) - 1, 0)
    
    # Ambil titik tengah partisi
    midPoint = numbers // 2
    
    # Mencari titik dengan jarak terdekat di kanan dan kiri lineCenter secara rekursif
    a1, b1, dist_left, count1 = ClosestPairPoint3(sorted[:midPoint], midPoint)
    a2, b2, dist_right, count2 = ClosestPairPoint3(sorted[midPoint:], numbers - midPoint)
    
    # Mengambil nilai minimum dari jarak terdekat bagian kanan dan kiri serta titiknya
    min = Minimum(dist_left, dist_right)
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
    p1, p2, val, count3 = LineCenterClosest(lineCenter, len(lineCenter), min, am, bm, 3)
    
    # Membandingkan nilai sekitar lineCenter dengan nilai minimum partisi dan ambil titiknya
    min_pol = Minimum(min, val)
    if (min_pol == min) :
        a_min = am
        b_min = bm
    else :
        a_min = p1
        b_min = p2
        
    count_total = count1 + count2 + count3
    
    # mengembalikan hasil final, yaitu kedua titik dengan jarak terdekat dan jaraknya
    return a_min, b_min, min_pol, count_total

# 4. Implementasi rekursif cari kanan kiri (Tergeneralisasi) [BONUS]
def ClosestPairPointGeneral(listOfPoints, numbers, dimention) :
    # Kondisi pemberhenti rekursifitas, saat jumlah elemen partisi sudah terbatas
    if numbers <= 3:
        a, b, dist, count = BruteForce.BruteForceDistGeneral(listOfPoints, dimention)
        # Mengembalikan 2 titik dan nilai jaraknya
        return a, b, dist, count
    
    # Sebelum melakukan pemrosesan, titik diurutkan menaik berdasarkan nilai koordinat [0]
    # sorted = Point.SortPoints(listOfPoints)
    sorted = Point.QuickSort(listOfPoints, 0, len(listOfPoints) - 1, 0)
    
    # Ambil titik tengah partisi
    midPoint = numbers // 2
    
    # Mencari titik dengan jarak terdekat di kanan dan kiri lineCenter secara rekursif
    a1, b1, dist_left, count1 = ClosestPairPointGeneral(sorted[:midPoint], midPoint, dimention)
    a2, b2, dist_right, count2 = ClosestPairPointGeneral(sorted[midPoint:], numbers - midPoint, dimention)
    
    # Mengambil nilai minimum dari jarak terdekat bagian kanan dan kiri serta titiknya
    min = Minimum(dist_left, dist_right)
    if (min == dist_left) :
        am = a1
        bm = b1
    else :
        am = a2
        bm = b2
        
    # Mendefinisikan lineCenters, mengisi elemen linecenter dengan batas nilai delta, yaitu min
    lineCenter = []
    if (dimention > 1):
        for i in range(numbers):
            if abs(sorted[i][0] - sorted[midPoint][0]) < min:
                lineCenter.append(sorted[i])
    
    # Mengambil nilai terkecuil disekitar lineCenter
    p1, p2, val, count3 = LineCenterClosest(lineCenter, len(lineCenter), min, am, bm, dimention)
    
    # Membandingkan nilai sekitar lineCenter dengan nilai minimum partisi dan ambil titiknya
    min_pol = Minimum(min, val)
    if (min_pol == min) :
        a_min = am
        b_min = bm
    else :
        a_min = p1
        b_min = p2
        
    count_total = count1 + count2 + count3
    
    # mengembalikan hasil final, yaitu kedua titik dengan jarak terdekat dan jaraknya
    return a_min, b_min, min_pol, count_total