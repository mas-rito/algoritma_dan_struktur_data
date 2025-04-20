# Insertion Sort in Python

def insertionSort(array):
    # Iterasi melalui setiap elemen array dimulai dari indeks 1
    for i in range(1, len(array)):
        # Perulangan ke-1
        # i = 1
        # Menyimpan nilai saat ini sebagai key
        key = array[i]
        # key = 6
        # Menyimpan indeks sebelumnya
        j = i - 1
        # j = 1-1
        # j = 0

        # Iterasi mundur untuk mencari posisi yang tepat bagi key
        while j >= 0 and key < array[j]:
            # j = 0
            # key = 6
            # array[0] = 1
            # 6 < 1
            # tidak terjadi perubahan
            
        
        # Menempatkan key pada posisi yang benar
        array[j + 1] = key
        # array[1] = 6
        
        # Menampilkan proses sorting setelah setiap iterasi utama
        print(f'Iterasi {i}: {array}')
        # Iterasi 1: [1, 6, 3, 29, 12]

        # Perulangan ke-2
        # i = 2
        # Menyimpan nilai saat ini sebagai key
        key = array[i]
        # key = 3
        # Menyimpan indeks sebelumnya
        j = i - 1
        # j = 2-1
        # j = 1

        # Iterasi mundur untuk mencari posisi yang tepat bagi key
        while j >= 0 and key < array[j]:
            # iterasi ke-1
            # j = 1
            # key = 3
            # array[1] = 6
            # 3 < 6
            array[j + 1] = array[j]  # Geser elemen ke kanan
            # array[2] = 6
            j -= 1  # Kurangi indeks
            # j = 0

            # iterasi ke-2
            # j = 0
            # key = 3
            # array[1] = 1
            # 3 < 3
            # tidak terjadi perubahan
        
        # Menempatkan key pada posisi yang benar
        array[j + 1] = key
        # array[1] = 3
        
        # Menampilkan proses sorting setelah setiap iterasi utama
        print(f'Iterasi {i}: {array}')
        # Iterasi 2: [1, 3, 6, 29, 12]

        # Perulangan ke-3
        # i = 3
        # Menyimpan nilai saat ini sebagai key
        key = array[i]
        # key = 29
        # Menyimpan indeks sebelumnya
        j = i - 1
        # j = 3-1
        # j = 2

        # Iterasi mundur untuk mencari posisi yang tepat bagi key
        while j >= 0 and key < array[j]:
            # iterasi ke-1
            # j = 2
            # key = 29
            # array[2] = 6
            # 29 < 6
            # tidak terjadi perubahan
        
        # Menempatkan key pada posisi yang benar
        array[j + 1] = key
        # array[3] = 29
        
        # Menampilkan proses sorting setelah setiap iterasi utama
        print(f'Iterasi {i}: {array}')
        # Iterasi 3: [1, 3, 6, 29, 12]

        # Perulangan ke-4
        # i = 4
        # Menyimpan nilai saat ini sebagai key
        key = array[i]
        # key = 12
        # Menyimpan indeks sebelumnya
        j = i - 1
        # j = 4-1
        # j = 3

        # Iterasi mundur untuk mencari posisi yang tepat bagi key
        while j >= 0 and key < array[j]:
            # iterasi ke-1
            # j = 3
            # key = 12
            # array[3] = 29
            # 12 < 29
            array[j + 1] = array[j]  # Geser elemen ke kanan
            # array[4] = 29
            j -= 1  # Kurangi indeks
            # j = 2

            # iterasi ke-2
            # j = 2
            # key = 12
            # array[2] = 6
            # 12 < 6
            # tidak terjadi perubahan
        
        # Menempatkan key pada posisi yang benar
        array[j + 1] = key
        # array[3] = 12
        
        # Menampilkan proses sorting setelah setiap iterasi utama
        print(f'Iterasi {i}: {array}')
        # Iterasi 4: [1, 3, 6, 12, 29]



# Data awal
data = [1, 6, 3, 29, 12]
print('Array sebelum sorting:', data)

# Panggil fungsi insertionSort
insertionSort(data)

print('Array setelah sorting:', data)
