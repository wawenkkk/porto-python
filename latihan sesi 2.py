import pygame
import sys

# Inisialisasi pygame
pygame.init()

# Ukuran layar
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Cursor Naga")

# Warna
black = (0, 0, 0)
green = (0, 255, 0)

# Muat gambar naga (pastikan Anda memiliki gambar naga)
# Ganti 'naga.png' dengan path ke gambar naga Anda
naga_image = pygame.image.load('naga.png')
naga_rect = naga_image.get_rect()

# Loop utama
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Ambil posisi mouse
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Update posisi kursor naga
    naga_rect.center = (mouse_x, mouse_y)

    # Gambar
    screen.fill(black)  # Bersihkan layar
    screen.blit(naga_image, naga_rect)  # Gambar kursor naga
    pygame.display.flip()  # Perbarui tampilan

    # Batasi frame rate
    pygame.time.Clock().tick(60)