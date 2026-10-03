# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3 (.mp3).

import pygame

pygame.mixer.init()
pygame.mixer.music.load("exercicios\\ex021\\demo.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)


# pygame.init()
# pygame.mixer.music.load('C:\\Users\\Guilherme\\Documents\\Cursos\\Tecnologia da Informação\\Curso de Python 3\\estudos\\scripts-py\\exercicios\\ex021\\demo.mp3')
# pygame.mixer.music.play()
# pygame.event.wait()
