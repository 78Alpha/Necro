import pygame

#file = 'Necro.mp3'
#pygame.init()
pygame.mixer.init(48000, -16, 2, 4096)
pygame.mixer.music.load("Necro.mp3")
pygame.mixer.music.play(0)

clock = pygame.time.Clock()
clock.tick(10)
while pygame.mixer.music.get_busy():
    #pygame.event.poll()
    clock.tick(10)
#pygame.mixer.music.load(file)
#pygame.mixer.music.play()

#while pygame.mixer.music.get_busy():
#    pygame.time.Clock().tick(10)
