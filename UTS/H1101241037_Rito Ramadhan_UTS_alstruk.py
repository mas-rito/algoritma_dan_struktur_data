# Insertion Sort in Python

def insertion_sort(array):
    # Iterasi melalui setiap elemen array dimulai dari indeks 1
    for i in range(1, len(array)):
        # Perulangan ke-1
        # i = 1
        # Menyimpan nilai saat ini sebagai key
        key = array[i]
        # key = 10
        # Menyimpan indeks sebelumnya
        j = i - 1
        # j = 1-1
        # j = 0

        # Iterasi mundur untuk mencari posisi yang tepat bagi key
        while j >= 0 and key < array[j]:
            # j = 0
            # key = 10
            # array[0] = 64
            # 10 < 64
            array[j + 1] = array[j]  # Geser elemen ke kanan
            # array[1] = 64
            j -= 1  # Kurangi indeks
            # j = -1
            
        
        # Menempatkan key pada posisi yang benar
        array[j + 1] = key
        # array[0] = 10
        
        # Menampilkan proses sorting setelah setiap iterasi utama
        print(f'Iterasi {i}: {array}')
        # Iterasi 1: [10, 64, 12, 15, 8]

        # Perulangan ke-2
        # i = 2
        # Menyimpan nilai saat ini sebagai key
        key = array[i]
        # key = 12
        # Menyimpan indeks sebelumnya
        j = i - 1
        # j = 2-1
        # j = 1

        # Iterasi mundur untuk mencari posisi yang tepat bagi key
        while j >= 0 and key < array[j]:
            # iterasi ke-1
            # j = 1
            # key = 12
            # array[1] = 64
            # 12 < 64
            array[j + 1] = array[j]  # Geser elemen ke kanan
            # array[2] = 64
            j -= 1  # Kurangi indeks
            # j = 0

            # iterasi ke-2
            # j = 0
            # key = 12
            # array[0] = 10
            # 12 < 10
            # tidak terjadi perubahan
        
        # Menempatkan key pada posisi yang benar
        array[j + 1] = key
        # array[1] = 12
        
        # Menampilkan proses sorting setelah setiap iterasi utama
        print(f'Iterasi {i}: {array}')
        # Iterasi 2: [10, 12, 64, 15, 8]

        # Perulangan ke-3
        # i = 3
        # Menyimpan nilai saat ini sebagai key
        key = array[i]
        # key = 15
        # Menyimpan indeks sebelumnya
        j = i - 1
        # j = 3-1
        # j = 2

        # Iterasi mundur untuk mencari posisi yang tepat bagi key
        while j >= 0 and key < array[j]:
            # iterasi ke-1
            # j = 2
            # key = 15
            # array[2] = 64
            # 15 < 64
            array[j + 1] = array[j]  # Geser elemen ke kanan
            # array[3] = 64
            j -= 1  # Kurangi indeks
            # j = 1

            # iterasi ke-2
            # j = 1
            # key = 15
            # array[1] = 12
            # 15 < 12
            # tidak terjadi perubahan
        
        # Menempatkan key pada posisi yang benar
        array[j + 1] = key
        # array[2] = 15 
        
        # Menampilkan proses sorting setelah setiap iterasi utama
        print(f'Iterasi {i}: {array}')
        # Iterasi 3: [10, 12, 15, 64, 8]

        # Perulangan ke-4
        # i = 4
        # Menyimpan nilai saat ini sebagai key
        key = array[i]
        # key = 8
        # Menyimpan indeks sebelumnya
        j = i - 1
        # j = 4-1
        # j = 3

        # Iterasi mundur untuk mencari posisi yang tepat bagi key
        while j >= 0 and key < array[j]:
            # iterasi ke-1
            # j = 3
            # key = 8
            # array[3] = 64
            # 8 < 64
            array[j + 1] = array[j]  # Geser elemen ke kanan
            # array[4] = 64
            j -= 1  # Kurangi indeks
            # j = 2

            # iterasi ke-2
            # j = 2
            # key = 8
            # array[2] = 15
            # 8 < 15
            array[j + 1] = array[j]  # Geser elemen ke kanan
            # array[3] = 15
            j -= 1  # Kurangi indeks
            # j = 1

            # iterasi ke-3
            # j = 1
            # key = 8
            # array[1] = 12
            # 8 < 12
            array[j + 1] = array[j]  # Geser elemen ke kanan
            # array[2] = 12
            j -= 1  # Kurangi indeks
            # j = 0
        
            # iterasi ke-4
            # j = 0
            # key = 8
            # array[0] = 10
            # 8 < 10
            array[j + 1] = array[j]  # Geser elemen ke kanan
            # array[1] = 10
            j -= 1  # Kurangi indeks
            # j = -1

        # Menempatkan key pada posisi yang benar
        array[j + 1] = key
        # array[0] = 0
        
        # Menampilkan proses sorting setelah setiap iterasi utama
        print(f'Iterasi {i}: {array}')
        # Iterasi 4: [8, 10, 12, 15, 64]



# Data awal
data = [64, 10, 12, 15, 8]
insertion_sort(data)
print("Sorted arra: ")
for i in range(len(data)):
    print(data[i], end=" ")

# Data setelah di sortir
# data = [8, 10, 12, 15, 64]