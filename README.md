Nama : Aditya Dinata

NIM  : 2209116062

Kelas : Sistem Informasi B 2022


Program Pengelolaan Stok Barang Toko Kelontong
Program ini dibuat untuk membantu pengelolaan stok barang pada suatu toko kelontong. Program ini berfungsi untuk menambah, menghapus, memperbarui, serta melihat stok barang dan riwayat perubahan stok barang.

Program menggunakan menggunakan jenis linked list singly linked list (linked list satu arah), karena setiap node hanya menunjuk ke node selanjutnya, dan tidak memiliki pointer yang menunjuk ke node sebelumnya. setiap kali pengguna melakukan operasi (mengubah atau menghapus barang), program akan menyimpan riwayat operasi pada atribut history di objek linked list.

cara kerja program :
Program ini adalah sebuah program pengelolaan stok barang. Pada awal program, akan ditampilkan menu yang terdiri dari 6 pilihan:

Lihat Barang: Menampilkan seluruh stok barang yang tersedia pada program
Tambah Barang: Menambahkan barang baru pada stok barang
Perbarui Barang: Memperbarui stok dan harga barang yang ada
Hapus Barang: Menghapus barang yang sudah tidak ada pada stok barang
Lihat History Barang: Menampilkan riwayat perubahan stok barang
Exit: Keluar dari program
Setelah memilih salah satu pilihan, program akan mengeksekusi fungsi yang sesuai dengan pilihan tersebut.

Program ini menggunakan linked list untuk menyimpan data stok barang. Setiap item dalam linked list direpresentasikan oleh kelas Item, yang memiliki atribut nama barang, stok, harga, dan pointer ke item sebelum dan sesudahnya. Linked list sendiri direpresentasikan oleh kelas Stok1, yang memiliki atribut pointer ke head dan tail dari linked list, serta daftar riwayat aksi yang dilakukan pada barang.

Berikut adalah penjelasan singkat dari setiap fungsi dalam program ini:

add_item(name, stock, price): Menambahkan item baru ke linked list.
remove_item(name): Menghapus item dari linked list berdasarkan nama barang.
update_item(name, stock, price): Memperbarui item dalam linked list berdasarkan nama barang.
display_Stok1(): Menampilkan seluruh item dalam linked list beserta detailnya.
display_history(): Menampilkan riwayat aksi yang dilakukan pada barang.
Program ini juga menggunakan modul os dan time
untuk membersihkan layar console dan memberikan jeda antar aksi.

Bagaimana Apliksi/Program Berjalan:
 Pada bagian awal program, terdapat pembuatan class Item dan class Stok1 yang masing-masing berfungsi sebagai blue print dari objek node (barang) dan linked list dari objek node tersebut.

Class Item memiliki atribut name (nama barang), stock (jumlah stok barang), price (harga barang), next (pointer ke node berikutnya pada linked list), dan prev (pointer ke node sebelumnya pada linked list).

Class Stok1 memiliki atribut head (pointer ke node pertama pada linked list), tail (pointer ke node terakhir pada linked list), dan history (list yang digunakan untuk menyimpan riwayat operasi yang dilakukan pada linked list).

Setelah itu, program menambahkan beberapa node (barang) awal pada linked list dengan menggunakan method add_item pada class Stok1.

Fungsi login digunakan untuk menampilkan menu utama dan memanggil method dari class Stok1 sesuai dengan pilihan pengguna. Pilihan yang tersedia meliputi menampilkan seluruh barang, menambahkan barang baru, mengupdate barang, menghapus barang, dan menampilkan riwayat operasi yang telah dilakukan.

Pada bagian akhir program, fungsi login dipanggil untuk memulai program.


Struktur Kode/ Element Penting pada program
Program ini menggunakan class dan method sebagai berikut:

Class Item
__init__(self, name, stock, price): Method untuk membuat object item baru dengan property name, stock, price, next, dan prev
Class Stok1

__init__(self): Method untuk membuat object stok baru dengan property head, tail, dan history

add_item(self, name, stock, price): Method untuk menambahkan item baru ke stok

remove_item(self, name): Method untuk menghapus item dari stok berdasarkan nama

update_item(self, name, stock, price): Method untuk memperbarui stok dan harga barang pada stok berdasarkan nama

display_Stok1(self): Method untuk menampilkan seluruh stok barang yang tersedia

display_history(self): Method untuk menampilkan riwayat perubahan stok barang

Function login()
login(): Fungsi utama yang digunakan untuk menampilkan menu, memproses input, dan menampilkan output yang sesuai dengan pilihan yang dipilih

Output Program :
![1](https://user-images.githubusercontent.com/126496425/225896846-3a811f92-69d9-44f3-881c-de294a4e0cee.png)
![2](https://user-images.githubusercontent.com/126496425/225897450-e5eae64a-3f5a-4051-9978-ce39a6794f65.png)
![3](https://user-images.githubusercontent.com/126496425/225899012-7d7e579c-e1e9-4442-9a86-de492d2c2062.png)
![4](https://user-images.githubusercontent.com/126496425/225899071-e2e05bff-407c-4a0a-b6d5-50c9147ebb82.png)
![5](https://user-images.githubusercontent.com/126496425/225899138-9bc8c54c-a82a-47f7-8c86-6d7ed5e0289b.png)
![6](https://user-images.githubusercontent.com/126496425/225899169-4fd23210-04ed-4185-9ba2-6aefd6f89d1c.png)
![7](https://user-images.githubusercontent.com/126496425/225899191-9fc28cea-c9bb-4e0c-9aca-6184111e3647.png)
![8](https://user-images.githubusercontent.com/126496425/225899228-a202ca2e-b216-41c5-b680-2c28982222ce.png)
![9](https://user-images.githubusercontent.com/126496425/225899265-4b9b15e0-668d-4006-b535-1073d0653cda.png)







