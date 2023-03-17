import os
import time
import math
# data list
arr = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]


def jump():

    def jump_search(arr, x):
        panjang = len(arr)
        jump = int(math.sqrt(panjang))
        kiri, kanan = 0, 0
        while kiri < panjang and arr[kiri] <= x:
            kanan = min(panjang - 1, kiri + jump)
            if arr[kiri] <= x and arr[kanan] >= x:
                break
            kiri += jump
        if kiri >= panjang or arr[kiri] > x:
            return -1
        kanan = min(panjang - 1, kanan)
        i = kiri
        while i <= kanan and arr[i] <= x:
            if arr[i] == x:
                return i
            i += 1
        return -1

    print("\n   Daftar Data: ", arr)
    time.sleep(1)

    # Cari Arsel
    idx_arsel = jump_search(arr, "Arsel")
    if idx_arsel != -1:
        print("Arsel di Index", idx_arsel)

    # Cari Avivah
    idx_avivah = jump_search(arr, "Avivah")
    if idx_avivah != -1:
        print("Avivah di Index", idx_avivah)

    # Cari Daiva
    idx_daiva = jump_search(arr, "Daiva")
    if idx_daiva != -1:
        print("Daiva di Index", idx_daiva)

    # Cari Wahyu
    idx_wahyu = jump_search(arr[3], "Wahyu")
    if idx_wahyu != -1:
        print("Wahyu di Index 3 pada kolom 0")

    # Cari Wibi
    idx_wibi = jump_search(arr[3], "Wibi")
    if idx_wibi != -1:
        print("Wibi di Index 3 pada kolom 1")

    input("\n   Tekan Enter untuk melihat data satu per satu")
    os.system("cls")
    time.sleep(1)
    print("\n   Daftar Data:")
    for i in arr:
        time.sleep(1)
        print("\n   ", i)
    input("\n   Tekan Enter untuk kembali")


def fib():

    def fibonacci_search(arr, x):
        fib2 = 0
        fib1 = 1
        fib = fib2 + fib1
        n = len(arr)

        while (fib < n):
            fib2 = fib1
            fib1 = fib
            fib = fib2 + fib1

        offset = -1

        while (fib > 1):
            i = min(offset + fib2, n - 1)

            if (arr[i] < x):
                fib = fib1
                fib1 = fib2
                fib2 = fib - fib1
                offset = i
            elif (arr[i] > x):
                fib = fib2
                fib1 = fib1 - fib2
                fib2 = fib - fib1
            else:
                return i

        if (fib1 and arr[offset + 1] == x):
            return offset + 1

        return -1

    # list data

    input("\n   Tekan Enter untuk melihat data satu per satu")
    os.system("cls")
    time.sleep(1)
    print("\n   Daftar Data:")
    for i in arr:
        time.sleep(1)
        print("\n   ", i)
    input("\n   Tekan Enter untuk kembali")

    # Cari Arsel
    idx_arsel = fibonacci_search(arr, "Arsel")
    if idx_arsel != -1:
        print("Arsel di Index", idx_arsel)

    # Cari Avivah
    idx_avivah = fibonacci_search(arr, "Avivah")
    if idx_avivah != -1:
        print("Avivah di Index", idx_avivah)

    # Cari Daiva
    idx_daiva = fibonacci_search(arr, "Daiva")
    if idx_daiva != -1:
        print("Daiva di Index", idx_daiva)

    # Cari Wahyu
    idx_wahyu = fibonacci_search(arr[3], "Wahyu")
    if idx_wahyu != -1:
        print("Wahyu di Index 3 pada kolom 0")

    # Cari Wibi
    idx_wibi = fibonacci_search(arr[3], "Wibi")
    if idx_wibi != -1:
        print("Wibi di Index 3 pada kolom 1")


def mulai():
    while True:
        os.system("cls")
        print("\tSelamat Di Program Searching Aditya Dinata")
        print("\tIni adalah data data yang akan dicari indeksnya:\n\tArsel, Avivah, Daiva, Wahyu, Wibi\n ")
        print("\tSilahkan plih metode searchingnya")
        i = input(
            "\tPilih \n1.JumpSearch\n2.FibSearch\n3.Exit\n:")
        if i == "1":
            jump()
            input("Tekan Enter untuk kembali")
            os.system("cls")
            mulai()
            break

        elif i == "2":
            fib()
            input("Tekan Enter untuk kembali")
            os.system("cls")
            mulai()
            break
        elif i == "3":
            break
        else:
            print("Masukan Pilihan dengan Benar")


mulai()
