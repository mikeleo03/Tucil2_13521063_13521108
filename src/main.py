# File pengimplementasi Program Utama
# Impor modul eksternal, termasuk file
import os
import time
import platform
import Point
import DnC
import BruteForce
import Visual

# Program Utama
os.system('cls') # Clear screen
print('''
                 = Tugas Kecil 2 Strategi Algoritma  =                                                
\033[31m   _|_|_|  _|             \033[33m                  \033[32m             _|      
\033[31m _|        _|    _|_|  \033[33m    _|_|_|    _|_| \033[32m     _|_|_|  _|_|_|_|  
\033[31m _|        _|  _|    \033[33m_|  _|_|      _|_|_\033[32m|_|  _|_|        _|      
\033[31m _|        _|  _|  \033[33m  _|      _|_|  _| \033[32m           _|_|    _| \033[34m     
\033[31m   _|_|_|  _|    _\033[33m|_|    _|_|_|   \033[32m   _|_|_|  _|_|_|       \033[34m _|_|  
\033[31m               \033[33m                \033[32m                         \033[34m                                         
\033[31m _|_|_|        \033[33m      _|     \033[32m         Points Detector \033[34m-
\033[31m _|    _|  \033[33m  _|_|_|      _|\033[32m  _|_|    Divide and \033[34mConquer Algorithm
\033[31m _|_|_|  \033[33m  _|    _|  _|  \033[32m_|_|                 \033[34m
\033[31m _|     \033[33m   _|    _|  _|\033[32m  _|          Made \033[34mby :
\033[31m _|  \033[33m        _|_|_| \033[32m _|  _|          \033[34m13521063 / 13521108 
\033[0m      ''')

# Tampilan pilihan menu
print("============================  INPUT  ============================")
print("Data titik seperti apa yang kamu pilih ?")
print("1. Tiga dimensi")
print("2. N dimensi")
print("Masukkan pilihanmu [1/2]")
pilihan = input(">> ")

# Validasi masukan
while (pilihan != "1" and pilihan != "2"):
    print('\033[93m' + f"> Pilihan tidak valid, ulangi!" + '\033[0m')
    print("-----------------------------------------------------------------")
    print("Data titik seperti apa yang kamu pilih ?")
    print("1. Tiga dimensi")
    print("2. N dimensi")
    print("Masukkan pilihanmu [1/2]")
    pilihan = input(">> ")
    
# Pemrosesan berdasarkan pilihan
if (pilihan == "1"):
    print("\n=====================  PASANGAN 3 DIMENSI  ======================")
    print("Masukkan jumlah titik")
    titik = int(input(">> "))
    while (titik < 2):
        print('\033[93m' + f"> Jumlah titik harus lebih dari 1!" + '\033[0m')
        print("-----------------------------------------------------------------")
        print("Masukkan jumlah titik")
        titik = int(input(">> "))
    pointMatrix = Point.ListRandomPoint(3, titik)
    
    print("\n===================  PEMBANGKITAN TITIK ACAK  ===================")
    print("Daftar kumpulan titik")
    
    # Case handling untuk masukan diatas 50
    if titik <= 50 :
        Visual.printPointMatrix(pointMatrix)
    else :
        print("Karena jumlah titik yang banyak, maka data titik akan disimpan pada doc/Result.txt")
        with open('doc/Result.txt', 'w') as f:
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
    print(f"\nJarak                   : \033[92m{shortest1}"  + '\033[0m')
    print("\nAlgoritma Divide and Conquer --")
    print('Pasangan titik terdekat : ', end="") 
    Visual.printPoint(pts3)
    print(", ", end= "")
    Visual.printPoint(pts4)
    print(f"\nJarak                   : \033[92m{shortestcln1}" + '\033[0m')
    
    print("\n==========================  STATISTIK  ==========================")
    print("Algoritma BruteForce --")
    print(f'Jumlah perbandingan : \033[92m{compare1}' + '\033[0m')
    print(f'Waktu Eksekusi      : \033[92m{finish_bf - start_bf} sekon\n' + '\033[0m')
    print("Algoritma Divide and Conquer --")
    print(f'Jumlah perbandingan : \033[92m{compare2}' + '\033[0m')
    print(f'Waktu Eksekusi      : \033[92m{finish_dc - start_dc} sekon' + '\033[0m')
    
    # Penampilan grafik
    print("\n======================  PENAMPILAN GRAFIK  ======================")
    print("Apakah ingin menampilkan hasil ilustrasi titik ?")
    print("Masukkan pilihanmu [Y/n]")
    pilihan = input(">> ")
    
    # Validasi masukan
    while (pilihan != "Y" and pilihan != "y" and pilihan != "N" and pilihan != "n"):
        print('\033[93m' + f"> Pilihan tidak valid, ulangi!" + '\033[0m')
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
    while (titik < 2):
        print('\033[93m' + f"> Jumlah titik harus lebih dari 1!" + '\033[0m')
        print("-----------------------------------------------------------------")
        print("Masukkan jumlah titik")
        titik = int(input(">> "))
    pointMatrix = Point.ListRandomPoint(dimensi, titik)
    
    print("\n===================  PEMBANGKITAN TITIK ACAK  ===================")
    print("Daftar kumpulan titik")
    
    # Case handling untuk masukan diatas 50
    if titik <= 50 :
        Visual.printPointMatrix(pointMatrix)
    else :
        print("Karena jumlah titik yang banyak, maka data titik akan disimpan pada doc/Result.txt")
        with open('doc/Result.txt', 'w') as f:
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
    print(f"\nJarak                   : \033[92m{shortest1}"  + '\033[0m')
    print("\nAlgoritma Divide and Conquer --")
    print('Pasangan titik terdekat : ', end="") 
    Visual.printPoint(pts3)
    print(", ", end= "")
    Visual.printPoint(pts4)
    print(f"\nJarak                   : \033[92m{shortestcln1}" + '\033[0m')
    
    print("\n==========================  STATISTIK  ==========================")
    print("Algoritma BruteForce --")
    print(f'Jumlah perbandingan : \033[92m{compare1}' + '\033[0m')
    print(f'Waktu Eksekusi      : \033[92m{finish_bf - start_bf} sekon\n' + '\033[0m')
    print("Algoritma Divide and Conquer --")
    print(f'Jumlah perbandingan : \033[92m{compare2}' + '\033[0m')
    print(f'Waktu Eksekusi      : \033[92m{finish_dc - start_dc} sekon\n' + '\033[0m')
    
print("=====================  SPESIFIKASI SISTEM  ======================")
print("Berikut adalah detail spesifikasi sistem Anda")
envi = platform.uname()
print(f"System: \033[34m{envi.system}" + '\033[0m')
print(f"Node Name: \033[34m{envi.node}" + '\033[0m')
print(f"Release: \033[34m{envi.release}" + '\033[0m')
print(f"Version: \033[34m{envi.version}" + '\033[0m')
print(f"Machine: \033[34m{envi.machine}" + '\033[0m')
print(f"Processor: \033[34m{envi.processor}\n" + '\033[0m')