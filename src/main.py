# File pengimplementasi Program Utama
# Impor modul eksternal, termasuk file
import os
import time
import Point
import DnC
import BruteForce
import Visual

# Program Utama
os.system('cls') # Clear screen
print('''
                 = Tugas Kecil 2 Strategi Algoritma  =                                                
   _|_|_|  _|                                            _|      
 _|        _|    _|_|      _|_|_|    _|_|      _|_|_|  _|_|_|_|  
 _|        _|  _|    _|  _|_|      _|_|_|_|  _|_|        _|      
 _|        _|  _|    _|      _|_|  _|            _|_|    _|      
   _|_|_|  _|    _|_|    _|_|_|      _|_|_|  _|_|_|        _|_|  
                                                                                                 
 _|_|_|              _|              Points Detector -
 _|    _|    _|_|_|      _|  _|_|    Divide and Conquer Algorithm
 _|_|_|    _|    _|  _|  _|_|           
 _|        _|    _|  _|  _|          Made by :
 _|          _|_|_|  _|  _|          13521063 / 13521108
      ''')

# Tampilan pilihan menu
print("============================  INPUT  ============================")
print("Data titik seperti apa yang kamu pilih ?")
print("1. Tiga dimensi")
print("2. N dimensi")
print("Masukkan pilihanmu [1/2]")
pilihan = int(input(">> "))

# Validasi masukan
while (pilihan != 1 and pilihan != 2):
    print("> Pilihan tidak valid, ulangi!")
    print("-----------------------------------------------------------------")
    print("Data titik seperti apa yang kamu pilih ?")
    print("1. Tiga dimensi")
    print("2. N dimensi")
    print("Masukkan pilihanmu [1/2]")
    pilihan = int(input(">> "))
    
# Pemrosesan berdasarkan pilihan
if (pilihan == 1):
    print("\n=====================  PASANGAN 3 DIMENSI  ======================")
    print("Masukkan jumlah titik")
    titik = int(input(">> "))
    pointMatrix = Point.ListRandomPoint(3, titik)
    
    print("\n===================  PEMBANGKITAN TITIK ACAK  ===================")
    print("Daftar kumpulan titik")
    
    # Case handling untuk masukan diatas 50
    if titik <= 50 :
        Visual.printPointMatrix(pointMatrix)
        print("")
    else :
        print("Karena jumlah titik yang banyak, maka data titik akan disimpan pada Result.txt")
        with open('Result.txt', 'w') as f:
            print('Daftar titik yang dibangkitkan :\n', file=f)
            Visual.printPointMatrixFile(pointMatrix, f)
            
    print("\n=======================  HASIL ALGORITMA  =======================")
    start_bf = time.time()
    pts1, pts2, shortest1, compare1 = BruteForce.BruteForceDist(pointMatrix)
    finish_bf = time.time()
    start_dc = time.time()
    pts3, pts4, shortestcln1, compare2 = DnC.ClosestPairPoint3(pointMatrix, titik)
    finish_dc = time.time()
    print("Algoritma BruteForce --")
    print('Pasangan titik terdekat : ', end="") 
    Visual.printPoint(pts1)
    print(", ", end= "")
    Visual.printPoint(pts2) 
    print(f"\nJarak                   : {shortest1}")
    print("\nAlgoritma Divide and Conquer --")
    print('Pasangan titik terdekat : ', end="") 
    Visual.printPoint(pts3)
    print(", ", end= "")
    Visual.printPoint(pts4) 
    print(f"\nJarak                   : {shortestcln1}")
    
    print("\n==========================  STATISTIK  ==========================")
    print("Algoritma BruteForce --")
    print(f'Jumlah perbandingan : {compare1}')
    print(f'Waktu Eksekusi      : {finish_bf - start_bf} sekon\n')
    print("Algoritma Divide and Conquer --")
    print(f'Jumlah perbandingan : {compare2}')
    print(f'Waktu Eksekusi      : {finish_dc - start_dc} sekon')
    
    # Penampilan grafik
    print("\n======================  PENAMPILAN GRAFIK  ======================")
    print("Apakah ingin menampilkan hasil ilustrasi titik ?")
    print("Masukkan pilihanmu [Y/n]")
    pilihan = input(">> ")
    
    # Validasi masukan
    while (pilihan != "Y" and pilihan != "y" and pilihan != "N" and pilihan != "n"):
        print("> Pilihan tidak valid, ulangi!")
        print("-----------------------------------------------------------------")
        print("Apakah ingin menampilkan hasil ilustrasi titik ?")
        print("Masukkan pilihanmu [Y/n]")
        pilihan = input(">> ")
        
    # Pemrosesan masukan
    if (pilihan == "Y" or pilihan == "y"):
        print("\nPemrosesan sedang berlangsung....")
        Visual.VisualizeMinimum(pointMatrix, pts1, pts2)
        print(" ")
    else :
        print(" ")
        
else :
    print("\n=====================  PASANGAN N DIMENSI  ======================")
    print("Masukkan jumlah dimensi")
    dimensi = int(input(">> "))
    print("Masukkan jumlah titik")
    titik = int(input(">> "))
    pointMatrix = Point.ListRandomPoint(dimensi, titik)
    
    print("\n===================  PEMBANGKITAN TITIK ACAK  ===================")
    print("Daftar kumpulan titik")
    
    # Case handling untuk masukan diatas 50
    if titik <= 50 :
        Visual.printPointMatrix(pointMatrix)
        print("")
    else :
        print("Karena jumlah titik yang banyak, maka data titik akan disimpan pada Result.txt")
        with open('Result.txt', 'w') as f:
            print('Daftar titik yang dibangkitkan :\n', file=f)
            Visual.printPointMatrixFile(pointMatrix, f)
            
    print("\n=======================  HASIL ALGORITMA  =======================")
    start_bf = time.time()
    pts1, pts2, shortest1, compare1 = BruteForce.BruteForceDistGeneral(pointMatrix, dimensi)
    finish_bf = time.time()
    start_dc = time.time()
    pts3, pts4, shortestcln1, compare2 = DnC.ClosestPairPointGeneral(pointMatrix, titik, dimensi)
    finish_dc = time.time()
    print("Algoritma BruteForce --")
    print('Pasangan titik terdekat : ', end="") 
    Visual.printPoint(pts1)
    print(", ", end= "")
    Visual.printPoint(pts2) 
    print(f"\nJarak                   : {shortest1}")
    print("\nAlgoritma Divide and Conquer --")
    print('Pasangan titik terdekat : ', end="") 
    Visual.printPoint(pts3)
    print(", ", end= "")
    Visual.printPoint(pts4) 
    print(f"\nJarak                   : {shortestcln1}")
    
    print("\n==========================  STATISTIK  ==========================")
    print("Algoritma BruteForce --")
    print(f'Jumlah perbandingan : {compare1}')
    print(f'Waktu Eksekusi      : {finish_bf - start_bf} sekon\n')
    print("Algoritma Divide and Conquer --")
    print(f'Jumlah perbandingan : {compare2}')
    print(f'Waktu Eksekusi      : {finish_dc - start_dc} sekon\n')