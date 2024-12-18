# praktikum-eksepsi
1. Apa itu Eksepsi di Python?
Eksepsi (exception) adalah kesalahan yang terjadi saat program berjalan. Jika tidak ditangani, eksepsi dapat menyebabkan program berhenti mendadak. Beberapa contoh eksepsi umum:

ZeroDivisionError: Kesalahan saat membagi angka dengan nol.
FileNotFoundError: Kesalahan saat mencoba membuka file yang tidak ada.
ValueError: Kesalahan tipe data tidak valid.
Python memungkinkan kita menangani eksepsi agar program tetap berjalan dengan lancar.

2. Penanganan Eksepsi (Exception Handling)
Python menyediakan fitur blok try ... except untuk menangani eksepsi:

Blok try: Berisi kode yang mungkin menghasilkan kesalahan.
Blok except: Menangani kesalahan yang terjadi.
Jika kesalahan muncul di dalam try, Python akan langsung menjalankan blok except. Jika tidak ada kesalahan, blok except akan diabaikan.

3. Membangkitkan Eksepsi dengan raise
Kadang, kita ingin memaksa munculnya eksepsi. Python memungkinkan kita membangkitkan (raise) eksepsi secara manual menggunakan perintah raise.

Ini berguna untuk memvalidasi kondisi tertentu dalam program. Contohnya, jika nilai yang diberikan tidak sesuai dengan aturan tertentu, kita bisa memunculkan kesalahan untuk menghentikan proses.

4. Penanganan File (File Handling)
Dalam penanganan file, kita sering menghadapi kemungkinan terjadinya kesalahan, seperti:

File yang tidak ditemukan (FileNotFoundError).
File kosong atau konten tidak sesuai harapan.
Python menyediakan cara aman untuk bekerja dengan file menggunakan mode seperti:

r (read): Membuka file untuk membaca.
w (write): Membuka file untuk menulis (menghapus isi lama).
a (append): Membuka file untuk menambahkan konten.
Untuk mencegah program berhenti mendadak saat file tidak ada, kita dapat menangani kesalahan dengan try ... except.

5. Contoh Penanganan Kesalahan
ZeroDivisionError: Terjadi saat ada operasi pembagian dengan nol. Kita bisa menangani ini dengan memberikan pesan kesalahan kepada pengguna.

FileNotFoundError: Terjadi saat mencoba membuka file yang tidak ada. Kita dapat menangani ini dengan memberi opsi untuk membuat file baru.

ValueError: Terjadi saat tipe data tidak sesuai, misalnya memasukkan teks untuk operasi numerik. Kita dapat memvalidasi input pengguna untuk mencegah kesalahan.

6. Kesimpulan
Penanganan eksepsi sangat penting untuk membuat program lebih stabil dan user-friendly. Dengan fitur seperti try ... except dan raise, kita dapat:

Menangani kesalahan tanpa menghentikan program.
Membantu debugging dengan memberikan informasi kesalahan.
Membuat program lebih fleksibel dan aman.
