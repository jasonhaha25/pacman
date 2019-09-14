import pygame

pygame.init()
pygame.font.init()
font = pygame.font.SysFont("ArcadeClassic", 20)

black = 0, 0, 0
white = 255, 255, 255
blue = 0, 0, 255
yellow = 255, 255, 0

man0 = pygame.image.load("./man/man0.png")
man1 = pygame.image.load("./man/man1.png")
man2 = pygame.image.load("./man/man2.png")
man3 = pygame.image.load("./man/man3.png")
cookie0 = pygame.image.load("./cookie0.png")
cookie1 = pygame.image.load("./cookie1.png")
cookie2 = pygame.image.load("./cookie2.png")

down = pygame.image.load("./map/d.png")
top = pygame.image.load("./map/t.png")
left = pygame.image.load("./map/l.png")
right = pygame.image.load("./map/r.png")

bordertop = pygame.image.load("./map/bt.png")
borderdown = pygame.image.load("./map/bd.png")
borderleft = pygame.image.load("./map/bl.png")
borderright = pygame.image.load("./map/br.png")

border1 = pygame.image.load("./map/b1.png")
border2 = pygame.image.load("./map/b2.png")
border3 = pygame.image.load("./map/b3.png")
border4 = pygame.image.load("./map/b4.png")

turn1 = pygame.image.load("./map/1.png")
turn2 = pygame.image.load("./map/2.png")
turn3 = pygame.image.load("./map/3.png")
turn4 = pygame.image.load("./map/4.png")

lturn1 = pygame.image.load("./map/5.png")
lturn2 = pygame.image.load("./map/6.png")
lturn3 = pygame.image.load("./map/7.png")
lturn4 = pygame.image.load("./map/8.png")

u = pygame.image.load("./map/u.png")
v = pygame.image.load("./map/v.png")
w = pygame.image.load("./map/w.png")
x = pygame.image.load("./map/x.png")
y = pygame.image.load("./map/y.png")
z = pygame.image.load("./map/z.png")

door = pygame.image.load("./map/door.png")
cherry = pygame.image.load("./cherry.png")



def draw(i, j, s):
    i *= 12
    j = j * 12 + 32
    l = 3

    if "b" in s:
        if "bt" in s:
            screen.blit(bordertop, [j, i, 12, 12])
        elif "bl" in s:
            screen.blit(borderleft, [j, i, 12, 12])
        elif "br" in s:
            screen.blit(borderright, [j, i, 12, 12])
        elif "bd" in s:
            screen.blit(borderdown, [j, i, 12, 12])
        elif "b1" in s:  # border corner 1
            screen.blit(border1, [j, i, 12, 12])
        elif "b2" in s:  # border corner 2
            screen.blit(border2, [j, i, 12, 12])
        elif "b3" in s:  # border corner 3:
            screen.blit(border3, [j, i, 12, 12])
        elif "b4" in s:  # border corner 4:
            screen.blit(border4, [j, i, 12, 12])
    else:

        if "t" == s:
            screen.blit(top, [j, i, 12, 12])
        if "l" == s:
            screen.blit(left, [j, i, 12, 12])
        if "r" == s:
            screen.blit(right, [j, i, 12, 12])
        if "d" == s:
            screen.blit(down, [j, i, 12, 12])

        if "1" == s:
            screen.blit(turn1, [j, i, 12, 12])

        if "2" == s:  # bottom left
            screen.blit(turn2, [j, i, 12, 12])
        if "3" == s:  # top left
            screen.blit(turn3, [j, i, 12, 12])
        if "4" == s:  # top right
            screen.blit(turn4, [j, i, 12, 12])
        # ----------------------------------------------------
        if "5" == s:  # l-turn 1
            screen.blit(lturn1, [j, i, 12, 12])

        if "6" == s:  # l-turn 2
            screen.blit(lturn2, [j, i, 12, 12])

        if "7" == s:  # l-turn 3
            screen.blit(lturn3, [j, i, 12, 12])

        if "8" == s:  # l-turn 4
            screen.blit(lturn4, [j, i, 12, 12])

        if "u" == s:
            screen.blit(u, [j, i, 12, 12])
        if "v" == s:
            screen.blit(v, [j, i, 12, 12])
        if "w" == s:
            screen.blit(w, [j, i, 12, 12])

        if "x" == s:
            screen.blit(x, [j, i, 12, 12])

        if "y" == s:
            screen.blit(y, [j, i, 12, 12])

        if "z" == s:
            screen.blit(z, [j, i, 12, 12])

        if "oo" == s:
            screen.blit(door, [j, i, 12, 12])

        if s == "":
            screen.fill(white, [j + 5, i + 5, 2, 2])
        if 0 <= cookie_phase <= 2:
            cookie = cookie0
        elif 3 <= cookie_phase <= 5:
            cookie = cookie1
        elif 6 <= cookie_phase <= 8:
            cookie = cookie2
        elif 9 <= cookie_phase <= 11:
            cookie = cookie1
        if s == "c":
            screen.blit(cookie, [j, i, 12, 12])
        if s == "cherry":
            screen.blit(cherry, [j, i, 20, 20])

pygame.init()

size = width, height = 400, 400
screen = pygame.display.set_mode(size)

FPS = 30
clock = pygame.time.Clock()

maze = []
for i in range(31):
    maze.append([""] * 28)

def maze2():
    global maze
    maze[0][0] = "b1"
    for i in range(1, 13):
        maze[0][i] = "bt"
    maze[0][13] = "u"
    maze[0][14] = "v"
    for i in range(15, 27):
        maze[0][i] = "bt"
    maze[0][27] = "b2"

    maze[1][0] = "bl"
    maze[1][27] = "br"

    maze[1][13] = "r"
    maze[1][14] = "l"
    maze[2][13] = "r"
    maze[2][14] = "l"
    maze[3][13] = "r"
    maze[3][14] = "l"
    maze[4][13] = "4"
    maze[4][14] = "3"

    maze[2][0] = "bl"
    maze[2][2] = "1"
    maze[2][3] = "d"
    maze[2][4] = "d"
    maze[2][5] = "2"

    maze[2][7] = "1"
    maze[2][8] = "d"
    maze[2][9] = "d"
    maze[2][10] = "d"
    maze[2][11] = "2"

    maze[2][16] = "1"
    maze[2][17] = "d"
    maze[2][18] = "d"
    maze[2][19] = "d"
    maze[2][20] = "2"

    maze[2][22] = "1"
    maze[2][23] = "d"
    maze[2][24] = "d"
    maze[2][25] = "2"
    maze[2][27] = "br"

    maze[3][0] = "bl"
    maze[3][2] = "r"
    maze[3][7] = "r"
    maze[3][5] = "l"
    maze[3][11] = "l"
    maze[3][16] = "r"
    maze[3][20] = "l"
    maze[3][22] = "r"
    maze[3][25] = "l"
    maze[3][27] = "br"

    maze[4][0] = "bl"
    maze[4][27] = "br"

    maze[4][2] = "4"
    maze[4][3] = "t"
    maze[4][4] = "t"
    maze[4][5] = "3"

    maze[4][7] = "4"
    maze[4][8] = "t"
    maze[4][9] = "t"
    maze[4][10] = "t"
    maze[4][11] = "3"

    maze[4][16] = "4"
    maze[4][17] = "t"
    maze[4][18] = "t"
    maze[4][19] = "t"
    maze[4][20] = "3"

    maze[4][22] = "4"
    maze[4][23] = "t"
    maze[4][24] = "t"
    maze[4][25] = "3"

    maze[5][0] = "bl"
    maze[5][27] = "br"
    maze[6][0] = "bl"
    maze[6][27] = "br"
    maze[7][0] = "bl"
    maze[7][27] = "br"

    maze[6][2] = "1"
    maze[7][2] = "4"
    maze[6][3] = "d"
    maze[6][4] = "d"
    maze[7][3] = "t"
    maze[7][4] = "t"
    maze[6][5] = "2"
    maze[7][5] = "3"

    maze[6][7] = "1"
    maze[6][8] = "2"
    for i in range(7, 13):
        maze[i][7] = "r"
        maze[i][8] = "l"
    maze[9][8] = "8"
    maze[10][8] = "5"
    maze[9][9] = "d"
    maze[9][10] = "d"
    maze[10][9] = "t"
    maze[10][10] = "t"
    maze[9][11] = "2"
    maze[10][11] = "3"

    maze[8][0] = "bl"
    maze[9][0] = "b4"
    for i in range(1, 5):
        maze[9][i] = "bd"
    maze[9][5] = "2"

    for i in range(10, 13):
        maze[i][5] = "bl"

    maze[8][27] = "br"
    maze[9][27] = "b3"
    for i in range(22, 27):
        maze[9][i] = "bd"
    maze[9][22] = "1"

    for i in range(10, 13):
        maze[i][22] = "br"

    maze[12][10] = "1"
    maze[12][11] = "bd"
    maze[12][12] = "bd"
    maze[12][13] = "oo"
    maze[12][14] = "oo"
    maze[12][15] = "bd"
    maze[12][16] = "bd"
    maze[12][17] = "2"

    maze[6][19] = "1"
    maze[6][20] = "2"
    for i in range(7, 13):
        maze[i][20] = "l"
    maze[7][19] = "r"
    maze[8][19] = "r"
    maze[11][19] = "r"
    maze[12][19] = "r"
    maze[9][19] = "7"
    maze[10][19] = "6"
    maze[9][18] = "d"
    maze[10][18] = "t"
    maze[9][17] = "d"
    maze[10][17] = "t"
    maze[9][16] = "1"
    maze[10][16] = "4"

    maze[6][25] = "2"
    maze[7][25] = "3"
    maze[6][24] = "d"
    maze[7][24] = "t"
    maze[6][23] = "d"
    maze[7][23] = "t"
    maze[6][22] = "1"
    maze[7][22] = "4"

    # _Joanna's part ______________________________________________________________
    maze[13][0] = "bt"
    maze[13][1] = "bt"
    maze[13][2] = "bt"
    maze[13][3] = "bt"
    maze[13][4] = "bt"
    maze[13][5] = "3"

    maze[13][7] = "4"
    maze[13][8] = "3"

    maze[13][10] = "br"
    maze[13][17] = "bl"

    maze[13][19] = "4"
    maze[13][20] = "3"

    maze[13][22] = "4"
    maze[13][23] = "bt"
    maze[13][24] = "bt"
    maze[13][25] = "bt"
    maze[13][26] = "bt"
    maze[13][27] = "bt"

    maze[14][10] = "br"
    maze[14][17] = "bl"

    maze[15][0] = "bd"
    maze[15][1] = "bd"
    maze[15][2] = "bd"
    maze[15][3] = "bd"
    maze[15][4] = "bd"
    maze[15][5] = "2"

    maze[15][7] = "1"
    maze[15][8] = "2"

    maze[15][10] = "br"
    maze[15][17] = "bl"

    maze[15][19] = "1"
    maze[15][20] = "2"

    maze[15][22] = "1"
    maze[15][23] = "bd"
    maze[15][24] = "bd"
    maze[15][25] = "bd"
    maze[15][26] = "bd"
    maze[15][27] = "bd"

    maze[16][5] = "bl"

    maze[16][7] = "r"
    maze[16][8] = "l"

    maze[16][10] = "4"
    maze[16][11] = "bt"
    maze[16][12] = "bt"
    maze[16][13] = "bt"
    maze[16][14] = "bt"
    maze[16][15] = "bt"
    maze[16][16] = "bt"
    maze[16][17] = "3"

    maze[16][19] = "r"
    maze[16][20] = "l"

    maze[16][22] = "br"

    maze[17][5] = "bl"

    maze[17][7] = "r"
    maze[17][8] = "l"

    maze[17][19] = "r"
    maze[17][20] = "l"

    maze[17][22] = "br"

    maze[18][5] = "bl"

    maze[18][7] = "r"
    maze[18][8] = "l"

    maze[18][10] = "1"
    maze[18][11] = "d"
    maze[18][12] = "d"
    maze[18][13] = "d"
    maze[18][14] = "d"
    maze[18][15] = "d"
    maze[18][16] = "d"
    maze[18][17] = "2"

    maze[18][19] = "r"
    maze[18][20] = "l"

    maze[18][22] = "br"

    maze[19][0] = "b1"
    maze[19][1] = "bt"
    maze[19][2] = "bt"
    maze[19][3] = "bt"
    maze[19][4] = "bt"
    maze[19][5] = "3"

    maze[19][7] = "4"
    maze[19][8] = "3"

    maze[19][10] = "4"
    maze[19][11] = "t"
    maze[19][12] = "t"
    maze[19][13] = "6"
    maze[19][14] = "5"
    maze[19][15] = "t"
    maze[19][16] = "t"
    maze[19][17] = "3"

    maze[19][19] = "4"
    maze[19][20] = "3"

    maze[19][22] = "4"
    maze[19][23] = "bt"
    maze[19][24] = "bt"
    maze[19][25] = "bt"
    maze[19][26] = "bt"
    maze[19][27] = "b2"

    maze[20][0] = "bl"
    maze[20][13] = "r"
    maze[20][14] = "l"

    maze[20][27] = "br"
    maze[21][13] = "r"
    maze[21][14] = "l"
    maze[22][13] = "4"
    maze[22][14] = "3"

    # --------Jason Lee--------
    maze[6][10] = "1"
    for i in range(11, 17):
        maze[6][i] = "d"
    maze[6][17] = "2"
    maze[7][17] = "3"
    maze[7][16] = "t"
    maze[7][15] = "t"
    maze[7][14] = "5"
    maze[8][14] = "l"
    maze[9][14] = "l"
    maze[10][14] = "3"
    maze[10][13] = "4"
    maze[9][13] = "r"
    maze[8][13] = "r"
    maze[7][13] = "6"
    maze[7][12] = "t"
    maze[7][11] = "t"
    maze[7][10] = "4"

    maze[30][0] = "b4"
    for i in range(1, 28):
        maze[30][i] = "bd"
    maze[30][27] = "b3"

    # bottom left obstacle
    maze[28][2] = "4"
    maze[27][2] = "1"
    maze[27][3] = "d"
    maze[27][4] = "d"
    maze[27][5] = "d"
    maze[27][6] = "d"
    maze[27][7] = "7"
    maze[26][7] = "r"
    maze[25][7] = "r"
    maze[24][7] = "1"
    maze[24][8] = "2"
    maze[25][8] = "l"
    maze[26][8] = "l"
    maze[27][8] = "8"
    maze[27][9] = "d"
    maze[27][10] = "d"
    maze[27][11] = "2"
    maze[28][11] = "3"
    for i in range(3, 11):
        maze[28][i] = "t"

    # obstacle no. 19
    maze[28][14] = "3"
    maze[28][13] = "4"
    maze[27][13] = "r"
    maze[26][13] = "r"
    maze[25][13] = "6"
    maze[25][12] = "t"
    maze[25][11] = "t"
    maze[25][10] = "4"
    maze[24][10] = "1"
    for i in range(11, 17):
        maze[24][i] = "d"
    maze[24][17] = "2"
    maze[25][17] = "3"
    maze[25][16] = "t"
    maze[25][15] = "t"
    maze[25][14] = "5"
    maze[26][14] = "l"
    maze[27][14] = "l"

    # bottom right obstacle
    maze[28][16] = "4"
    maze[27][16] = "1"
    maze[27][17] = "d"
    maze[27][18] = "d"
    maze[27][19] = "7"
    maze[26][19] = "r"
    maze[25][19] = "r"
    maze[24][19] = "1"
    maze[24][20] = "2"
    maze[25][20] = "l"
    maze[26][20] = "l"
    maze[27][20] = "8"
    maze[27][21] = "d"
    maze[27][22] = "d"
    maze[27][23] = "d"
    maze[27][24] = "d"
    maze[27][25] = "2"
    maze[28][25] = "3"
    for i in range(17, 25):
        maze[28][i] = "t"

    # obstacle no.14
    maze[25][5] = "3"
    maze[25][4] = "4"
    maze[24][4] = "r"
    maze[23][4] = "r"
    maze[22][4] = "6"
    maze[22][3] = "t"
    maze[22][2] = "4"
    maze[21][2] = "1"
    maze[21][3] = "d"
    maze[21][4] = "d"
    maze[21][5] = "2"
    maze[22][5] = "l"
    maze[23][5] = "l"
    maze[24][5] = "l"

    # obstacle no.15
    maze[22][7] = "4"
    maze[21][7] = "1"
    maze[21][8] = "d"
    maze[21][9] = "d"
    maze[21][10] = "d"
    maze[21][11] = "2"
    maze[22][11] = "3"
    maze[22][8] = "t"
    maze[22][9] = "t"
    maze[22][10] = "t"

    # obstacle no.16
    maze[22][16] = "4"
    maze[21][16] = "1"
    maze[21][17] = "d"
    maze[21][18] = "d"
    maze[21][19] = "d"
    maze[21][20] = "2"
    maze[22][20] = "3"
    maze[22][17] = "t"
    maze[22][18] = "t"
    maze[22][19] = "t"

    # obstacle no. 17
    maze[25][23] = "3"
    maze[25][22] = "4"
    maze[24][22] = "r"
    maze[23][22] = "r"
    maze[22][22] = "r"
    maze[21][22] = "1"
    maze[21][23] = "d"
    maze[21][24] = "d"
    maze[21][25] = "2"
    maze[22][25] = "3"
    maze[22][24] = "t"
    maze[22][23] = "5"
    maze[23][23] = "l"
    maze[24][23] = "l"

    maze[29][0] = "bl"
    maze[28][0] = "bl"
    maze[27][0] = "bl"
    maze[26][0] = "bl"
    maze[25][0] = "x"
    maze[25][1] = "t"
    maze[25][2] = "3"
    maze[24][2] = "2"
    maze[24][1] = "d"
    maze[24][0] = "w"
    maze[23][0] = "bl"
    maze[22][0] = "bl"
    maze[21][0] = "bl"
    maze[20][0] = "bl"

    maze[29][27] = "br"
    maze[28][27] = "br"
    maze[27][27] = "br"
    maze[26][27] = "br"
    maze[25][27] = "z"
    maze[25][26] = "t"
    maze[25][25] = "4"
    maze[24][25] = "1"
    maze[24][26] = "d"
    maze[24][27] = "y"
    maze[23][27] = "br"
    maze[22][27] = "br"
    maze[21][27] = "br"
    maze[20][27] = "br"
    #--------------
    maze[12][13] = "oo"
    maze[12][14] = "oo"

    maze[3][3] = "xx"
    maze[3][4] = "xx"

    maze[3][8] = "xx"
    maze[3][9] = "xx"
    maze[3][10] = "xx"

    maze[3][17] = "xx"
    maze[3][18] = "xx"
    maze[3][19] = "xx"

    maze[3][23] = "xx"
    maze[3][24] = "xx"
    for i in range(10, 13):
        for j in range(0, 5):
            maze[i][j] = "xx"
    for i in range(10, 13):
        for j in range(23, 28):
            maze[i][j] = "xx"
    for i in range(16, 19):
        for j in range(0, 5):
            maze[i][j] = "xx"
    for i in range(16, 19):
        for j in range(23, 28):
            maze[i][j] = "xx"

    for i in range(13, 16):
        for j in range(11, 17):
            maze[i][j] = "ooo"

    for i in range(9, 19):
        maze[11][i] = "-"
    for i in range(12, 20):
        maze[i][9] = "-"
        maze[i][18] = "-"
    for i in range(10, 18):
        maze[17][i] = "-"
    maze[9][12] = "-"
    maze[10][12] = "-"
    maze[9][15] = "-"
    maze[10][15] = "-"
    maze[14][7] = "-"
    maze[14][8] = "-"
    maze[14][19] = "-"
    maze[14][20] = "-"
    for i in range(0, 6):
        maze[14][i] = "-"
    for i in range(22, 28):
        maze[14][i] = "-"
    maze[23][14] = "-"
    maze[23][13] = "-"

    maze[3][1] = "c"
    maze[3][26] = "c"
    maze[23][1] = "c"
    maze[23][26] = "c"

def check_path(s):
    return s == "" or s == "-" or s == "c" or s == "cherry"

maze2()

me_i = 23
me_j = 14
me_i_change = 0
me_j_change = 0
me_move = "stop"
me_dir = "stop"
next_move = "empty"

speed = 0.25
man_phase = 0
cookie_phase = 0

score = 0

frame = 0


while True:
    screen.fill(black)
    for i in range(31):
        for j in range(28):
            if maze[i][j] != " ":
                draw(i, j, maze[i][j])

    me_ai = int(me_i)
    me_aj = int(me_j)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                next_move = "left"
            if event.key == pygame.K_RIGHT:
                next_move = "right"
            if event.key == pygame.K_UP:
                next_move = "up"
            if event.key == pygame.K_DOWN:
                next_move = "down"
    if next_move == "empty":
        me_move = "stop"

    if me_move == "left" and me_i == 14 and me_j == -1 + speed:
        me_j = 28 - speed
    if me_move == "right" and me_i == 14 and me_j == 28 - speed:
        me_j = -1 + speed

    if score % 700 == 0 and score != 0:
        maze[17][13] = "cherry"


    if me_i == me_ai and me_j == me_aj:
        if maze[me_ai][me_aj] == "":
            score += 10
        elif maze[me_ai][me_aj] == "c":
            score += 50
        maze[me_ai][me_aj] = "-"
        if next_move == "left":
            if me_aj == 0 or check_path(maze[me_ai][me_aj - 1]):
                me_j_change = -speed
                me_i_change = 0
                me_move = "left"
                me_dir = "left"
        if next_move == "right":
            if me_aj == 27 or check_path(maze[me_ai][me_aj + 1]):
                me_j_change = speed
                me_i_change = 0
                me_move = "right"
                me_dir = "right"
        if next_move == "up":
            if check_path(maze[me_ai - 1][me_aj]):
                me_j_change = 0
                me_i_change = -speed
                me_move = "up"
                me_dir = "up"
        if next_move == "down":
            if check_path(maze[me_ai + 1][me_aj]):
                me_j_change = 0
                me_i_change = speed
                me_move = "down"
                me_dir = "down"

        if me_move == "left" and (me_aj != 0 and not check_path(maze[me_ai][me_aj-1])):
            me_move = "stop"
        if me_move == "right" and (me_aj != 27 and not check_path(maze[me_ai][me_aj+1])):
            me_move = "stop"
        if me_move == "up" and not check_path(maze[me_ai-1][me_aj]):
            me_move = "stop"
        if me_move == "down" and not check_path(maze[me_ai+1][me_aj]):
            me_move = "stop"

        if me_move == "stop":
            me_j_change = 0
            me_i_change = 0

    me_j += me_j_change
    me_i += me_i_change
    # screen.fill(yellow, [me_j * 12 + 32, me_i * 12, 12, 12])

    if man_phase == 0:
        man = man0
    elif man_phase == 2:
        man = man1
    elif man_phase == 4:
        man = man2
    elif man_phase == 6:
        man = man3
    man_phase += 1
    if me_move == "stop":
        man_phase -= 1
    elif man_phase == 8:
        man_phase = 1

    if me_dir == "right":
        man_blit = man
    elif me_dir == "left":
        man_blit = pygame.transform.rotate(man, 180)
    elif me_dir == "up":
        man_blit = pygame.transform.rotate(man, 90)
    elif me_dir == "down":
        man_blit = pygame.transform.rotate(man, 270)
    else:
        man_blit = man0

    cookie_phase += 1
    if cookie_phase == 12:
        cookie_phase = 0
    man_rect = man_blit.get_rect()
    man_rect.center = (me_j * 12 + 32 + 6, me_i * 12 + 6)
    screen.blit(man_blit, man_rect)

    lives = 2
    text = font.render("LIVES: ",True,yellow)
    screen.blit(text,[160,380])
    man4 = pygame.transform.flip(man2,20,20)
    if lives == 2: 
        screen.blit(man4,[210,376])
        screen.blit(man4,[230,376])
    if lives ==1: 
        screen.blit(man4,[210,376])

    pygame.display.update()
    clock.tick(FPS)
    frame += 1
