pygame.init()
pygame.font.init()
font = pygame.font.SysFont("ArcadeClassic", 25)

text = font.render("SCORE: "+str(score),True,yellow)
    screen.blit(text,[30,380])