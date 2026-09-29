import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    img = pg.image.load("fig/3.png")
    img = pg.transform.flip(img, True, False)
    tmr = 0
    kk_rct = img.get_rect()
    kk_rct.center = 300, 200
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed()
        kx, ky= -1, 0
        if key_lst[pg.K_UP]:
            ky -= 1
        if key_lst[pg.K_DOWN]:
            ky += 1 
        if key_lst[pg.K_RIGHT]:
            kx += 2 
        kk_rct.move_ip((kx, ky))

        x = tmr%3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(img, kk_rct)
        pg.display.update()
        tmr += 1
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()