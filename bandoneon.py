import pygame
import os

# 音源フォルダの絶対パス（takenagaユーザーに対応）
SOUND_FOLDER = "./data"

# キーと音源ファイルの対応（自由に追加できます）
key_sound_map = {
    pygame.K_a: "C4.wav",
    pygame.K_s: "D4.wav",
    pygame.K_d: "E4.wav",
    pygame.K_f: "F4.wav",
    pygame.K_g: "G4.wav",
    pygame.K_h: "A4.wav",
    pygame.K_j: "B4.wav",
    pygame.K_k: "C5.wav"
}

# 初期化
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((500, 150))
pygame.display.set_caption("Bandoneon Keyboard")

print("Bandoneon ready! Press A〜K to play notes. Press [X] to quit.")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key in key_sound_map:
                sound_path = os.path.join(SOUND_FOLDER, key_sound_map[event.key])
                if os.path.exists(sound_path):
                    sound = pygame.mixer.Sound(sound_path)
                    sound.play()
                    print(f"Playing: {key_sound_map[event.key]}")
                else:
                    print(f"Sound file not found: {sound_path}")

pygame.quit()
