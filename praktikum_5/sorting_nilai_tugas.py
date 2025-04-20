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

def selecttionsort(S):
    n= len(S)
    for i in range(n-1):
        smallest = i
        for j in range(i+1,n):
            if S[j][1] < S[smallest][1]:
                smallest = j
        S[i], S[smallest] = S[smallest], S[i]

    return S

hasil_selection_sort = selecttionsort(data_mahasiswa)

# Menampilkan hasil bubble sort
print("\nHasil Pengurutan dengan Selection Sort:")
print("=========================================================")
print("No. | Nama\t\t| Nilai")
print("-----------------------------------------")
for i, mahasiswa in enumerate(hasil_selection_sort, 1):
    if len(mahasiswa[0]) < 10:
        print(f"{i}   | {mahasiswa[0]}\t\t| {mahasiswa[1]}")
    else:
        print(f"{i}   | {mahasiswa[0]}\t| {mahasiswa[1]}")