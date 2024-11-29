import pygame
import random

# Inisialisasi pygame
pygame.init()

# Warna
putih = (255, 255, 255)
kuning = (255, 255, 102)
hitam = (0, 0, 0)
merah = (213, 50, 80)
hijau = (0, 255, 0)
biru = (50, 153, 213)
abu_abu = (100, 100, 100)

# Ukuran layar
lebar_layar = 800
tinggi_layar = 600

layar = pygame.display.set_mode((lebar_layar, tinggi_layar))
pygame.display.set_caption('Snake Game - kelompok 6')

jam = pygame.time.Clock()

ukuran_ular = 10
kecepatan_ular = 15

font_gaya = pygame.font.SysFont("bahnschrift", 25)
font_skor = pygame.font.SysFont("comicsansms", 35)

# Fungsi untuk menampilkan skor
def skor_pemain(skor):
    nilai = font_skor.render("Skor Anda: " + str(skor), True, kuning)
    layar.blit(nilai, [0, 0])

# Fungsi untuk menggambar ular
def gambar_ular(ukuran_ular, daftar_ular):
    for x in daftar_ular:
        pygame.draw.rect(layar, hitam, [x[0], x[1], ukuran_ular, ukuran_ular])

# Fungsi untuk menampilkan pesan
def pesan(teks, warna, pos_x, pos_y):
    teks_pesan = font_gaya.render(teks, True, warna)
    layar.blit(teks_pesan, [pos_x, pos_y])

# Fungsi untuk menu utama
def menu_utama():
    menu_selesai = False
    while not menu_selesai:
        layar.fill(abu_abu)
        pesan("Snake Game - kelompok 6", putih, lebar_layar / 3, tinggi_layar / 4)
        pesan("Tekan Play untuk memulai atau Quit untuk keluar", kuning, lebar_layar / 6, tinggi_layar / 3)

        # Tombol Play
        tombol_play = pygame.Rect(lebar_layar / 3, tinggi_layar / 2, 150, 50)
        pygame.draw.rect(layar, hijau, tombol_play)
        pesan("Play", hitam, lebar_layar / 3 + 45, tinggi_layar / 2 + 10)

        # Tombol Quit
        tombol_quit = pygame.Rect(lebar_layar / 3 + 200, tinggi_layar / 2, 150, 50)
        pygame.draw.rect(layar, merah, tombol_quit)
        pesan("Quit", putih, lebar_layar / 3 + 245, tinggi_layar / 2 + 10)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tombol_play.collidepoint(event.pos):
                    menu_selesai = True
                if tombol_quit.collidepoint(event.pos):
                    pygame.quit()
                    quit()

# Loop utama permainan
def permainan():
    permainan_selesai = False
    permainan_tutup = False

    x1 = lebar_layar / 2
    y1 = tinggi_layar / 2

    perubahan_x1 = 0
    perubahan_y1 = 0

    daftar_ular = []
    panjang_ular = 1

    makanan_x = round(random.randrange(0, lebar_layar - ukuran_ular) / 10.0) * 10.0
    makanan_y = round(random.randrange(0, tinggi_layar - ukuran_ular) / 10.0) * 10.0

    while not permainan_selesai:

        while permainan_tutup == True:
            layar.fill(biru)
            pesan("Kamu Kalah! Tekan C-Ulangi atau Q-Keluar", merah, lebar_layar / 6, tinggi_layar / 3)
            skor_pemain(panjang_ular - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        permainan_selesai = True
                        permainan_tutup = False
                    if event.key == pygame.K_c:
                        permainan()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                permainan_selesai = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    perubahan_x1 = -ukuran_ular
                    perubahan_y1 = 0
                elif event.key == pygame.K_RIGHT:
                    perubahan_x1 = ukuran_ular
                    perubahan_y1 = 0
                elif event.key == pygame.K_UP:
                    perubahan_y1 = -ukuran_ular
                    perubahan_x1 = 0
                elif event.key == pygame.K_DOWN:
                    perubahan_y1 = ukuran_ular
                    perubahan_x1 = 0

        if x1 >= lebar_layar or x1 < 0 or y1 >= tinggi_layar or y1 < 0:
            permainan_tutup = True
        x1 += perubahan_x1
        y1 += perubahan_y1
        layar.fill(biru)
        pygame.draw.rect(layar, hijau, [makanan_x, makanan_y, ukuran_ular, ukuran_ular])
        kepala_ular = []
        kepala_ular.append(x1)
        kepala_ular.append(y1)
        daftar_ular.append(kepala_ular)
        if len(daftar_ular) > panjang_ular:
            del daftar_ular[0]

        for bagian in daftar_ular[:-1]:
            if bagian == kepala_ular:
                permainan_tutup = True

        gambar_ular(ukuran_ular, daftar_ular)
        skor_pemain(panjang_ular - 1)

        pygame.display.update()

        if x1 == makanan_x and y1 == makanan_y:
            makanan_x = round(random.randrange(0, lebar_layar - ukuran_ular) / 10.0) * 10.0
            makanan_y = round(random.randrange(0, tinggi_layar - ukuran_ular) / 10.0) * 10.0
            panjang_ular += 1

        jam.tick(kecepatan_ular)

    pygame.quit()
    quit()


# Panggil menu utama sebelum memulai permainan
menu_utama()
permainan()
