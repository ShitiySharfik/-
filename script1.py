# Импорты
from customtkinter import *
import sounddevice as sd
from PIL import Image
import pygame
import scipy.io.wavfile as wav
# Настройки
fs = 44100
seconds = 10
data = None

original_pil = Image.open("Ragel_overworld_dancing.gif")
img = CTkImage(light_image=original_pil, size=(200, 320))
pygame.mixer.init()
pygame.mixer.music.load("snd_mushroomdance.ogg")


# Команды
def record():
    global data

    data = sd.rec(
        int(seconds * fs),
        samplerate=fs,
        channels=1,
        dtype='int16'
    )
    pygame.mixer.music.play(10)
    sd.wait()


def hear():
    if data is None:
        print("Че запись не зделал дурик?")
        return

    sd.play(data, fs)
    pygame.mixer.music.play(10)
    sd.wait()
def save():
    if data is None:
        print("Че запись не зделал дурик?")
        return

    wav.write("ТАНЕЦ ГРИБОЧКОВ🍄🍄🍄", fs, data)

# Окно
window = CTk()
window.title("КАРАКОЕ ДО ПОЛУНОЧИ🎤🎤🎤")
window.geometry("1700x450")

label = CTkLabel(window, image=img, text="")
label.place(x=250, y=120)

label2 = CTkLabel(window, image=img, text="")
label2.place(x=1250, y=120)

label3 = CTkLabel(window, image=img, text="")
label3.place(x=750, y=120)

button_sd = CTkButton(window,text="Начать танец гриба",command=record)

button_sd.pack(pady=5)

button_wt = CTkButton(window,text="Услышать танец гриба",command=hear)
button_wt.pack(pady=5)

button_ld = CTkButton(window,text="Сохранить танец гриба",command=save)
button_ld.pack(pady=5)

window.mainloop()

