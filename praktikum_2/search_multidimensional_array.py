def pencarian_sequential_2d(arr, nilai):
    # Looping untuk pencarian sequential pada array 2D
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == nilai:
                return True, i, j  # Nilai ditemukan, mengembalikan posisi
    
    # Jika nilai tidak ditemukan
    return False, -1, -1


baris = int(input("Masukkan jumlah baris: "))
kolom = int(input("Masukkan jumlah kolom: "))
    
# Membuat array 2 dimensi kosong
arr = []
    
# Input data array
print("Masukkan data array:")
for i in range(baris):
    baris_array = []
    for j in range(kolom):
        nilai = int(input(f"Data [{i}][{j}]: "))
        baris_array.append(nilai)
    arr.append(baris_array)
    
# Menampilkan array
print("\nArray yang dimasukkan:")
for baris in arr:
    for nilai in baris:
        print(nilai, end="\t")
    print()
    
# Menu pencarian data
while True:
    nilai_cari = int(input("\nNilai yang dicari: "))
    
    # Memanggil fungsi pencarian
    ketemu, posisi_baris, posisi_kolom = pencarian_sequential_2d(arr, nilai_cari)
    
    # Menampilkan hasil pencarian
    if ketemu:
        print(f"output: data {nilai_cari} berada pada posisi [{posisi_baris}][{posisi_kolom}]")
    else:
        print(f"output: data {nilai_cari} tidak ditemukan dalam array")
    break
    
print("Program selesai")

