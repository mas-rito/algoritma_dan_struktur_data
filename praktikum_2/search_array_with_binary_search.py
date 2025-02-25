def input_data ():
    arr = []
    while True:
        angka = input("Masukkan angka (ketikan 'n' untuk berhenti): ")
        if angka == 'n':
            break
        arr.append(int(angka))

    print("Array yang dimasukkan:", arr)
    arr.sort()
    return arr

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def main():
    arr = input_data()
    target = int(input("Masukkan angka yang dicari: "))
    result = binary_search(arr, target)
    if result != -1:
        print(f"Angka {target} ditemukan di indeks {result}.")
    else:
        print(f"Angka {target} tidak ditemukan dalam array.")

main()