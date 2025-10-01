# Function untuk input data
def input_data():
    data = []
    jumlah = int(input("Masukkan jumlah mahasiswa: "))
    for i in range(jumlah):
        nama = input(f"Nama mahasiswa ke-{i+1}: ")
        nilai = float(input(f"Nilai {nama}: "))
        data.append([nama, nilai])
    return data

# Function untuk menghitung rata-rata
def hitung_rata(data):
    total = 0
    for mhs in data:
        total += mhs[1]
    return total / len(data)

# Function untuk mencari nilai tertinggi
def nilai_tertinggi(data):
    tertinggi = data[0]
    for mhs in data:
        if mhs[1] > tertinggi[1]:
            tertinggi = mhs
    return tertinggi

# Function untuk mencari nilai terendah
def nilai_terendah(data):
    terendah = data[0]
    for mhs in data:
        if mhs[1] < terendah[1]:
            terendah = mhs
    return terendah

# Main Program
def main():
    data = input_data()
    print("\n=== HASIL ===")
    print(f"Rata-rata nilai: {hitung_rata(data):.2f}")
    print(f"Nilai tertinggi: {nilai_tertinggi(data)[0]} ({nilai_tertinggi(data)[1]})")
    print(f"Nilai terendah : {nilai_terendah(data)[0]} ({nilai_terendah(data)[1]})")

# Jalankan
main()
