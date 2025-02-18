stringku = "Saya suka belajar struktur data"

karakter_set = set(stringku.lower())

karakter_set.discard(' ')

karakter_list = list(karakter_set)

karakter_list.sort()

print("String asli:", stringku)
print("\nKarakter unik (dalam set):", karakter_set)
print("\nKarakter unik (dalam list terurut):", karakter_list)
print("\nJumlah karakter unik:", len(karakter_list))