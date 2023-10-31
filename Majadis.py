import pandas as pd
import os
def login():
    username = input("Masukkan nama pengguna: ")
    NIM = input("Masukkan kata NIM: ")

    daftar_pengguna = baca_daftar_pengguna()
    if username in daftar_pengguna.index:
        correct_NIM = daftar_pengguna.at[username, "NIM"]
        if NIM == str(correct_NIM):
            homepage(username,NIM)
        else:
            print("NIM salah")
            login()
    else:
        print("Nama pengguna tidak ditemukan")
        login()

def baca_daftar_pengguna():
    daftar_pengguna = "daftar_pengguna.csv"
    df = pd.read_csv(daftar_pengguna)
    df = df.set_index("Nama")
    return df

def menampilkan_jadwal(NIM):
    jadwal = str(NIM)+".csv"
    df = pd.read_csv(jadwal)
    df = df.set_index("jam")
    print(df)

def ubah_jadwal(NIM):
    menampilkan_jadwal(NIM)
    hari_diubah = input("masukan hari jadwal yang ingin diubah ")
    jam_diubah = input("masukan jam jadwal yang ingin diubah ")
    df = df.at[hari_diubah,jam_diubah]
    print(df)

def homepage(username,NIM):
    os.system('cls')
    print(f"selamat datang \n {username} \n Berikut jadwal anda minggu ini :")
    menampilkan_jadwal(NIM)
    print("apa yang ingin anda lakukan?\n1. Ubah jadwal\n2. Booking jadwal dengan mahasiswa lain\n3. keluar")
    A = input("pilihan = ")
    if A == "1":
        ubah_jadwal(NIM)


login()
