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
# 0.1. Random Point generator

# 0.2. List of Random Point Generator

# 1. Membandingkan nilai x

# 2. Membandingkan nilai y

# 3. Persamaan Euclidean distance (3 dimensi)

# 4. Jarak terdekat ke tengah lintas titik

# 5. Implementasi rekursif cari kanan kiri

# 6. Definisi terdekat

# 7. Main program

# Note : implement bonus ilustrasi dan generalized R^n point di file terpisah aja okeng