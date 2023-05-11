deret_angka = [64, 34, 25, 12, 22, 11, 90]
for i in range(len(deret_angka) - 1):
    for j in range(len(deret_angka) - i - 1):
        if deret_angka[j] > deret_angka[j + 1]:
            deret_angka[j], deret_angka[j + 1] = deret_angka[j + 1], deret_angka[j]
print("Deret angka setelah diurutkan:")
print(deret_angka)