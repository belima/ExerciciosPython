from tkinter import Tk
from tkinter.filedialog import askopenfilename
from pygame import mixer

Tk().withdraw()
filename = askopenfilename()

mixer.init()
mixer.music.load(filename)
mixer.music.play()

print('Tocando {}'.format(filename))
input('Pressiona uma tecla para encerrar')
