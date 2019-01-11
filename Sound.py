from openal import *
import time

# open our wave file
source = oalOpen("Necro.wav")

# and start playback
source.play()

# check if the file is still playing
while source.get_state() == AL_PLAYING:
	# wait until the file is done playing
	time.sleep(1)

# release resources (don't forget this)
oalQuit()
#pygame.init()
#pygame.display.set_mode((200,100))
#pygame.mixer.music.load("Necro.mp3")
#pygame.mixer.music.play(0)

#clock = pygame.time.Clock()
#clock.tick(10)
#while pygame.mixer.music.get_busy():
#    pygame.event.poll()
#    clock.tick(10)