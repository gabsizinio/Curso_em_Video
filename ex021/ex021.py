resp = (input("Você curte um John Mayer ? ")).capitalize()
if resp == "Sim" or resp == "S":
    print("Eu também, tamo junto !")
    import pygame
    pygame.init()
    pygame.mixer.music.load("whygeorgia.mp3")
    pygame.mixer.music.play()
    pygame.event.wait()
    input()
else:
    print("Então ouça imediatamente !")

