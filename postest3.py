import os
import time

#Item = Node
#Stok1 = LinkedList


class Item:
    def __init__(self, name, stock, price):
        self.name = name
        self.stock = stock
        self.price = price
        self.next = None
        self.prev = None


class Stok1:
    def __init__(self):
        self.head = None
        self.tail = None
        self.history = []

    def add_item(self, name, stock, price):
        new_item = Item(name, stock, price)

        if not self.head:
            self.head = new_item
            self.tail = new_item
        else:
            new_item.prev = self.tail
            self.tail.next = new_item
            self.tail = new_item

    def remove_item(self, name):
        current = self.head

        while current:
            if current.name == name:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                del current

                self.history.append(f"Barang Yang Telah Dihapus {name}")
                return True

            current = current.next

        return False

    def update_item(self, name, stock, price):
        current = self.head

        while current:
            if current.name == name:
                current.stock = stock
                current.price = price

                self.history.append(
                    f"Barang Yang Diperbarui {name} Stok Baru {stock} Harga Baru {price}")
                return True

            current = current.next

        return False

    def display_Stok1(self):
        current = self.head

        if not current:
            print("Stok kosong!")
        else:
            print("{:<20} {:<10} {:<10}".format(
                "Nama Barang :", "Stok :", "Harga :"))

            while current:
                print("{:<20} {:<10} {:<10}".format(
                    current.name, current.stock, current.price))
                current = current.next

    def display_history(self):
        if not self.history:
            print("Tidak ada riwayat")
        else:
            print("Riwayat:")
            for i in self.history:
                print(i)


Stok1 = Stok1()
Stok1.add_item("Minyak goreng", 10, 20000)
Stok1.add_item("Beras", 5, 360000)
Stok1.add_item("Telur", 30, 2000)
Stok1.add_item("Tepung terigu", 10, 18000)
Stok1.add_item("Mi Instan", 42, 3000)
Stok1.add_item("Pasta gigi", 25, 12000)
Stok1.add_item("Makanan kalengan", 32, 17000)
Stok1.add_item("Pembalut", 8, 25000)


def login():
    os.system("cls")
    while True:
        try:
            Pilihan = int(input(
                "Selamat Datang Di Program Pengelolaan Barang \n TOKO KELONTONG \nPilih Mana menu yang anda ingin lakukan \n1.Lihat Barang\n2.Tambah Barang\n3.Perbarui Barang \n4.Hapus Barang \n5.Lihat History Barang\n6.Exit\n:"))
            if Pilihan == 1:
                os.system("cls")
                Stok1.display_Stok1()
                input("\nEnter Untuk Balik Ke Menu Utama:")
                os.system("cls")
                login()
                break
            elif Pilihan == 2:
                os.system("cls")
                name = input(
                    "\nMasukan Nama Barang Yang Anda ingin Tambahkan :\n")
                while True:
                    try:
                        stock = int(input("Masukan Jumlah Stok Barang :\n"))
                        price = int(input("Masukan Harga Barang :\n"))
                        break
                    except:
                        print("HARUS BERUPA ANGKA")
                Stok1.add_item(name, stock, price)
                print(f"Barang {name} berhasil ditambahkan")
                input("\nEnter Untuk Balik Ke Menu Utama:")
                os.system("cls")
                login()
                break
            elif Pilihan == 3:
                os.system("cls")
                Stok1.display_Stok1()
                name = input("\nMasukan Nama Barang Yang Ingin Diperbarui:\n")
                stock = int(input("Masukan Jumlah Stok Baru:\n"))
                price = int(input("Masukan Harga Barang Baru:\n"))
                if Stok1.update_item(name, stock, price):
                    os.system("cls")
                    print(f"Barang {name} berhasil diperbarui!")
                    Stok1.display_Stok1()
                    input("\nEnter Untuk Balik Ke Menu Utama:")
                    login()
                else:
                    print(f"Tidak ditemukan barang dengan nama {name}")
                    time.sleep(1)
                    login()
                break
            elif Pilihan == 4:
                os.system("cls")
                Stok1.display_Stok1()
                name = input("\nMasukan Barang Yang Anda ingin Hapus :\n")
                if Stok1.remove_item(name):
                    os.system("cls")
                    time.sleep(1)
                    print(f"Barang {name} berhasil dihapus!")
                    Stok1.display_Stok1()
                    input("\nEnter Untuk Balik Ke Menu Utama:")
                    login()
                else:
                    print(f"Tidak ditemukan barang dengan nama {name}")
                    time.sleep(1)
                    login()
                break
            elif Pilihan == 5:
                os.system("cls")
                Stok1.display_history()
                input("\nEnter Untuk Balik Ke Menu Utama:")
                login()
                break
            elif Pilihan == 6:
                break
            else:
                print("MASUKAN PILIHAN DENGAN BENAR!!")
        except:
            print("MASUKAN PILIHAN DENGAN BENAR!!")


login()
