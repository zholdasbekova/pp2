import pygame as pg
import os
import random

pg.init()

image_library = {}
def get_image(path):
    global image_library
    image = image_library.get(path)
    if image is None:
        canonicalized_path = path.replace("/", os.sep).replace("\\", os.sep)
        image = pg.image.load(path)
        image_library[canonicalized_path] = image
    return image

sounds_library = {}
def get_sound(path):
    global sounds_library
    sound = sounds_library.get(path)
    if sound is None:
        canonicalized_path = path.replace("\\", os.sep).replace("/", os.sep)
        sound = pg.mixer.music.load(canonicalized_path)
        sounds_library[canonicalized_path] = sound
    return sound

names = ["MY TREASURE", "HELLO", "VolKano", "JIKJIN", "I LOVE U"]
names_mp3 = [song + ".mp3" for song in names]
names_mp3_2 = [song + ".mp3" for song in names]

def play_song(order):
    global names_mp3, y
    if order == -1:
        names_mp3 = [names_mp3[-1]] + names_mp3[:5]
    elif order == 1:
        names_mp3 = names_mp3[1:] + [names_mp3[0]]
    path = names_mp3[0]
    for i in range(6):
        if path == names_mp3_2[i]:
            y = i * 100
    get_sound("music/" + names_mp3[0])
    pg.mixer.music.play()

def shuffle():
    global currently_playing_song, names_mp3, y
    next_song = random.choice(names_mp3)
    while next_song == currently_playing_song:
        next_song = random.choice(names_mp3)
    currently_playing_song = next_song
    for i in range(6):
        if currently_playing_song == names_mp3_2[i]:
            y = i * 100
    get_sound("C:\Users\Aidana Zholdasbekova\Desktop\pp\tsis7\music" + currently_playing_song)
    pg.mixer.music.play()

screen = pg.display.set_mode((600, 600))
pg.display.set_caption("Playlist")

dancing = get_image("C:/Users/Aidana Zholdasbekova/Desktop/pp/tsis7/pic/treasurepic.jpeg")

pos = 0
y = 0
currently_playing_song = None

done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    
    screen.fill((0, 66, 66))
    
    screen.blit(pg.transform.scale(dancing, (100, 100)), (350, y))
    if pos == 7:
        pos = 0
    else:
        pos += 1
    
    screen.blit(pg.transform.scale(get_image("C:/Users/Aidana Zholdasbekova/Desktop/pp/tsis7/pic/shuffling.png"), (60, 60)), (510, 50))
    screen.blit(pg.transform.scale(get_image("C:/Users/Aidana Zholdasbekova/Desktop/pp/tsis7/pic/prev_song.jpg"), (60, 60)), (480, 110))
    screen.blit(pg.transform.scale(get_image("C:/Users/Aidana Zholdasbekova/Desktop/pp/tsis7/pic/next_song.jpg"), (60, 60)), (540, 110))
    screen.blit(pg.transform.scale(get_image("C:/Users/Aidana Zholdasbekova/Desktop/pp/tsis7/pic/stop.jpg"), (60, 60)), (510, 170))
    
    pg.display.flip()

pg.quit()