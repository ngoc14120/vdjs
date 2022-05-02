import pygame, sys, os, random
from SlidePuzzle import*

def main():
    pygame.init()
    # os.environ['SDL_VIDEO_CENTERED'] = '1'
    w,h = 750,600; cx,cy = w//2,h//2
    screen = pygame.display.set_mode((w,h))
    pygame.display.set_caption('Slide Puzzle')
    fpsclock = pygame.time.Clock(); fps = 60
    puzzle = SlidePuzzle(screen,(3,3),120,2)
    puzzle.rect.center = 300,cy


    x,y = 600,70; size = 100,100
    buttons = {}
    buttons['solve']     = Button((x,y),     size, puzzle.solve,'Start')
    buttons['stop']      = Button((x,y),     size, puzzle.stop,'Stop')
    buttons['random'] = Button((x,y+120), size, puzzle.randomize, 'Random')

    bg = pygame.image.load("background.jpg")
    bg_w,bg_h = bg.get_size()

    while True:
        dt = fpsclock.tick(fps)/1000
        key = pygame.key.get_pressed(); mouse = pygame.mouse.get_pressed(); mpos = pygame.mouse.get_pos()

        solve = buttons['stop' if puzzle.solving else 'solve']
        collide = None
        for b in (solve,buttons['random']):
            if b.collide(mpos): collide = b; break

        for y in range(0,h,bg_h):
            for x in range(0,w,bg_w): screen.blit(bg,(x,y))

        puzzle.draw(screen)
        solve.draw(screen,(180,0,0) if puzzle.solving else (0,180,0))
        buttons['random'].draw(screen,(60,70,160))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4 and key[pygame.K_LALT]: pygame.quit(); sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if collide:
                    if collide is buttons['random']: collide(1000)
                    else: collide()
            puzzle.events(event)

        puzzle.update(dt,key,mouse,mpos)


if __name__ == '__main__':
    main()