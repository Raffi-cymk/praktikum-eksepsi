# SyntaxError: Jika Anda lupa titik dua atau tanda lainnya
# if x < 5
#     print(x)

# ZeroDivisionError
try:
    # Kode yang bisa menimbulkan kesalahan
    print(10 / 0)
except ZeroDivisionError as e:
    # Menangani kesalahan
    print(f"Terjadi kesalahan: {e}")

print("Program tetap berjalan tanpa error.")


# FileNotFoundError
try:
    # Mencoba membuka file
    with open("tidak_ada_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError as e:
    # Menangani kesalahan file tidak ditemukan
    print(f"Kesalahan: File tidak ditemukan. Detail: {e}")

print("Program tetap berjalan tanpa error.")


try:
    hasil = 10 / 0
except ZeroDivisionError as e:
    print(f"Terjadi kesalahan: {e}")

def cek_angka(x):
    if x > 5:
        raise ValueError(f"Angka tidak boleh lebih dari 5, tapi nilai adalah {x}")
    print(f"Angka valid: {x}")

try:
    cek_angka(10)
except ValueError as e:
    print(e)

try:
    with open("contoh.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File tidak ditemukan!")

with open("contoh.txt", "a") as file:
    file.write("Ini baris tambahan.\n")

try:
    with open("latihan.txt", "r") as file:
        content = file.read()
        if not content:
            raise ValueError("File kosong!")
        print(content)
except FileNotFoundError:
    print("File tidak ditemukan, membuat file baru...")
    with open("latihan.txt", "w") as file:
        file.write("Baris pertama file.\n")
except ValueError as e:
    print(e)

# Tambahkan data ke file
with open("latihan.txt", "a") as file:
    file.write("Baris tambahan.\n")