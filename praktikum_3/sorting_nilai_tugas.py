data_mahasiswa = [
    ["Alan", 72],
    ["Rito", 82],
    ["Ramadhan", 84],
    ["Budi", 55],
    ["Kusuma", 82],
    ["Ardi", 61],
    ["Taufik", 95],
    ["Desi", 85],
    ["Mikel", 65],
    ["Desi", 63]
]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        
        for j in range(0, n-i-1):
            if arr[j][1] < arr[j+1][1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                
        if swapped == False:
            break
    
    return arr

hasil_bubble_sort = bubble_sort(data_mahasiswa)

# Menampilkan hasil bubble sort
print("\nHasil Pengurutan dengan Bubble Sort:")
print("=========================================================")
print("No. | Nama\t\t| Nilai")
print("-----------------------------------------")
for i, mahasiswa in enumerate(hasil_bubble_sort, 1):
    if len(mahasiswa[0]) < 10:
        print(f"{i}   | {mahasiswa[0]}\t\t| {mahasiswa[1]}")
    else:
        print(f"{i}   | {mahasiswa[0]}\t| {mahasiswa[1]}")