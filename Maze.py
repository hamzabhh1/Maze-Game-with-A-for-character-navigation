import pygame
s = 0  # water
m = 1  # sand
g = 3  # grass
h = 4  # red
b = 5  # cadre

blue = (63, 72, 204)
yellow = (255, 242, 0)
green = (14, 209, 69)
brown = (255, 0, 0)
black = (0, 0, 0)
col_tiles = {s: blue, m: yellow, g: green, h: brown, b: black}
# sysfont=pygame.font.get_default_font()

bo = 20
# bo=10
# bo=2


map_tiles1 = [
    [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
    [b, m, s, g, g, g, s, s, g, g, g, g, g, g, b],
    [b, g, s, g, g, g, s, g, g, s, s, s, s, g, b],
    [b, g, s, g, g, g, s, g, s, s, s, s, s, g, b],
    [b, g, s, g, s, g, s, g, s, g, g, g, g, g, b],
    [b, g, s, g, s, g, s, g, g, g, s, s, s, s, b],
    [b, g, s, g, s, g, s, g, s, g, s, g, g, g, b],
    [b, g, s, g, s, g, s, g, s, g, s, g, s, g, b],
    [b, g, s, g, s, g, s, g, s, g, s, g, s, g, b],
    [b, g, g, g, s, g, g, g, s, g, g, g, s, g, b],
    [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b]
]


map_tiles3 = [
    [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
    [b, s, s, s, s, s, s, s, g, s, s, s, s, g, b],
    [b, g, g, g, g, g, g, s, g, s, s, s, s, g, b],
    [b, g, s, s, s, s, g, s, g, s, s, s, s, g, b],
    [b, g, g, g, g, s, g, g, g, s, s, s, s, g, b],
    [b, s, s, s, g, s, g, s, g, g, g, s, s, g, b],
    [b, m, g, s, g, s, g, s, s, s, g, s, s, g, b],
    [b, s, g, g, g, s, g, s, s, s, g, s, s, g, b],
    [b, s, g, s, s, s, g, g, s, s, g, g, g, g, b],
    [b, g, g, g, g, g, g, s, s, s, s, s, s, s, b],
    [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b]
]





disttx = 0
distty = 0
emchix=-1
emchiy=-1


map_tiles2 = [
    [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
    [b, s, s, g, g, g, g, g, g, h, h, h, h, h, b],
    [b, s, s, g, s, s, s, h, m, h, h, g, g, g, b],
    [b, g, s, g, g, s, s, h, h, h, h, g, h, g, b],
    [b, g, s, s, g, s, s, s, s, s, s, g, s, g, b],
    [b, g, s, s, g, g, g, g, g, g, g, g, s, g, b],
    [b, g, s, s, s, s, s, s, s, s, s, s, s, g, b],
    [b, g, g, g, g, g, g, g, g, g, g, g, g, g, b],
    [b, s, s, s, s, s, s, g, s, s, s, s, s, s, b],
    [b, s, s, s, s, s, s, g, s, s, s, s, s, s, b],
    [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b]
]




tiles_size = 70
mov = True
map_width = 15
map_height = 11

pygame.init()

keys = pygame.key.get_pressed()
dsurf = pygame.display.set_mode(((70 * 11) // 2, (70 * 15) // 2))
font = pygame.font.SysFont(None, 48)
img = font.render('GOOD JOB', True, black)
img1 = font.render('press R to restart', True, black)
img3 = font.render('you can jump using space key', True, black)
img2 = font.render('press t for a tip', True, black)
img21 = font.render('1', True, black)
img22 = font.render('2', True, black)
img23 = font.render('3', True, black)
DISPLAY = pygame.display.set_mode((map_width * tiles_size, map_height * tiles_size))
run = True
st = False
pos3x = tiles_size * 13 + tiles_size // 2
pos3y = tiles_size * 1 + tiles_size // 2

pos2x = tiles_size * 7 + tiles_size // 2
pos2y = tiles_size * 9 + tiles_size // 2

pos1x = tiles_size * 13 + tiles_size // 2
pos1y = tiles_size * 9 + tiles_size // 2


pos2xfinish = tiles_size * 8 + tiles_size // 2
pos2yfinish = tiles_size * 2 + tiles_size // 2
pos1xfinish = tiles_size * 1 + tiles_size // 2
pos1yfinish = tiles_size * 1 + tiles_size // 2
pos3xfinish = tiles_size * 1 + tiles_size // 2
pos3yfinish = tiles_size * 6 + tiles_size // 2
# x=tiles_size*7+tiles_size//2
# y=tiles_size*9+tiles_size//2
tiles_size2 = 15
f = tiles_size // 60
img5 = font.render('please select the map number', True, brown)
map_tiles=map_tiles2

#def map(map_tiles):
##############################################################################

def heuristique(x,y,finish):
    heur=((finish[0]-x)**2+(finish[1]-y)**2)**(1/2)
    return heur/70

def successeur(x,y,cout,a,pres):
    cout=cout+1
    pres=(x,y)
    sull=[]
    for i,j in [(0,1),(0,-1),(1,0),(-1,0)]:
        col1 = (x - 35) // 70 + i
        row1 = (y - 35) // 70 + j
        if (x + 70 * i) != pres[0] or (y + 70 * j) != pres[1]:
            if (map_tiles[row1][col1] == g or map_tiles[row1][col1] == m):
                sull.append(((x + 70 * i, y+70 * j), cout, heuristique(x+70 * i, y+70 * j,finish), pres))
    return sull

def AlgA(x1,y1,map,finish):
     ouvert=[]
     ferme=[]
     cout = 0
     pres=(-1,-1)
     ouvert.append(((x1,y1),cout,heuristique(x1,y1,finish),pres))
     print(ouvert)
     print(ferme)
     while ouvert :
         succL = successeur(ouvert[0][0][0],ouvert[0][0][1],ouvert[0][1],ouvert[0][2],ouvert[0][3])
         ferme.append(ouvert.pop(0))
         for a in succL:
             if a[2]<=0.5:
                 chemin=[]
                 chemin.append(a[0])
                 while a[3]!=(-1,-1) :
                     for b in ferme:
                         if b[0] == a[3]:
                             a = b
                             break
                     chemin.append(a[0])
                 chemin.reverse()
                 return chemin
         for a in succL:
             for b in ouvert:
                 if a[0] == b[0] :
                     if a[1] + a[2] <= b[1] + b[2]:
                         ouvert.remove(b)
                     else:
                         succL.remove(a)
         elements_to_remove = []
         for a in succL:
             for c in ferme:
                 if a[0] == c[0]:
                     if a[1] + a[2] <= c[1] + c[2]:
                         elements_to_remove.append(c)
                     else:
                         elements_to_remove.append(a)

         for element in elements_to_remove:
             if element in ferme:
                 ferme.remove(element)
             if element in succL:
                 succL.remove(element)

             '''for a in succL:
             for c in ferme:
                 if a[0] == c[0]:
                     if a[1] + a[2] <= c[1] + c[2]:
                         ferme.remove(c)
                     else:
                         succL.remove(a)'''
         ouvert = ouvert + succL
         sorted_list = sorted(ouvert, key=lambda x: x[1] + x[2])
         ouvert = sorted_list
         print("***************")
         print(ouvert)
         print(ferme)
     print("error <<coud not find path ")
#hedhi tetekhdem ki tbadel lmap
def exec():
    deb=(pos2x,pos2y)
    finish=(pos2xfinish,pos2yfinish)
    path=AlgA(deb[0],deb[1],map,finish)
    print("AND THE FINAL PATH IS ")
    print(path)
    khatwa=0
    '''for i in range(0,len(path)):
        emchix = path[khatwa + 1][0] - path[khatwa][0]
        emchiy = path[khatwa + 1][1] - path[khatwa][1]
        disttx=0
        distty=0
        while (disttx!=emchix):
            disttx+=1
            x+=1
        while (distty!=emchiy):
            distty+=1
            y += 1
'''

##############################################################################

hoppa=1
khatwa=0
#print(heuristique(3*70,5*70))
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for row2 in range(map_height):
        for col2 in range(map_width):
            pygame.draw.rect(DISPLAY, col_tiles[map_tiles1[row2][col2]],
                             (70 * 4 // 2 + col2 * tiles_size2, (70 * 8) // 2 + row2 * tiles_size2, tiles_size2,
                              tiles_size2))
            pygame.draw.rect(DISPLAY, col_tiles[map_tiles2[row2][col2]],
                             (70 * 11 // 2 + col2 * tiles_size2, (70 * 8) // 2 + row2 * tiles_size2, tiles_size2,
                              tiles_size2))
            pygame.draw.rect(DISPLAY, col_tiles[map_tiles3[row2][col2]],
                             (70 * 18 // 2 + col2 * tiles_size2, (70 * 8) // 2 + row2 * tiles_size2, tiles_size2,
                              tiles_size2))
    dsurf.blit(img5, ((70 * 7) // 2, (70 * 3) // 2))
    dsurf.blit(img21, ((70 * 4) // 2 + 50, (70 * 3) // 2 + 200))
    dsurf.blit(img22, ((70 * 11) // 2 + 50, (70 * 3) // 2 + 200))
    dsurf.blit(img23, ((70 * 18) // 2 + 50, (70 * 3) // 2 + 200))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        map_tiles = map_tiles1
        break
    if keys[pygame.K_2]:
        map_tiles = map_tiles2
        break
    if keys[pygame.K_3]:
        map_tiles = map_tiles3
        break
    pygame.display.update()

if map_tiles == map_tiles1:
    x = pos1x
    y = pos1y
    deb = (pos1x, pos1y)
    finish = (pos1xfinish, pos1yfinish)
    path = AlgA(deb[0], deb[1], map, finish)
elif map_tiles == map_tiles2:
    x = pos2x
    y = pos2y
    deb = (pos2x, pos2y)
    finish = (pos2xfinish, pos2yfinish)
    path = AlgA(deb[0], deb[1], map, finish)
elif map_tiles == map_tiles3:
    x = pos3x
    y = pos3y
    deb = (pos3x, pos3y)
    finish = (pos3xfinish, pos3yfinish)
    path = AlgA(deb[0], deb[1], map, finish)

if map_tiles == map_tiles1:
    jump = 1
elif map_tiles == map_tiles2:
    jump = 1
elif map_tiles == map_tiles3:
    jump = 1
pp = 0
mol = 0


path=AlgA(deb[0],deb[1],map,finish)
print("AND THE FINAL PATH IS ")
print(path)
print(len(path))




while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # elif event.type == KEYDOWN:
        #  tiles_size += 1
    keys = pygame.key.get_pressed()
    ccc = (255, 70, 90)



    for row in range(map_height):
        for col in range(map_width):
            pygame.draw.rect(DISPLAY, col_tiles[map_tiles[row][col]],
                             (col * tiles_size, row * tiles_size, tiles_size, tiles_size))

    if mov:
        if keys[pygame.K_LEFT]:
            x -= f
            if keys[pygame.K_SPACE] and not (jump == 0):
                x -= 2 * tiles_size + bo
                jump -= 1

        if keys[pygame.K_RIGHT]:
            x += f
            if keys[pygame.K_SPACE] and not (jump == 0):
                x += 2 * tiles_size + bo
                jump -= 1
        if keys[pygame.K_UP]:
            y -= f
            if keys[pygame.K_SPACE] and not (jump == 0):
                y -= 2 * tiles_size + bo
                jump -= 1

        if keys[pygame.K_DOWN]:
            y += f
            if keys[pygame.K_SPACE] and not (jump == 0):
                y += 2 * tiles_size + bo
                jump -= 1
        if keys[pygame.K_x] :

            if hoppa==1 and  khatwa < len(path) - 1:
                emchix = path[khatwa + 1][0] - path[khatwa][0]
                emchiy = path[khatwa + 1][1] - path[khatwa][1]
                disttx = 0
                distty = 0
                hoppa=0

            if mov:
                if disttx < emchix:
                    disttx += 1
                    x += 1
                if distty < emchiy:
                    distty += 1
                    y += 1
                if disttx > emchix:
                    disttx -= 1
                    x -= 1
                if distty > emchiy:
                    distty -= 1
                    y -= 1

            if disttx == emchix and distty == emchiy:
                khatwa = khatwa + 1
                hoppa = 1





    if jump == 0:
        pp += 1
    if jump == 0 and pp > 150:
        jump += 1
        pp = 0
    pygame.draw.circle(DISPLAY, (255, 70, 110), (x, y), 30)
    # for row1 in range(map_height):
    #   for col1 in range(map_width):
    # if (map_tiles[row1][col1]!=g )and ((col1)*(tiles_size)-30<=x<=(col1)*(tiles_size)+70+30) and ((col1)*(tiles_size)-30<=y<=((col1)*(tiles_size)+70+30)):
    #    map_tiles[row1] [col1]=b
    #   ccc=(255,0,0)

    for row1 in range(map_height):
        for col1 in range(map_width):
            x1 = (col1 * tiles_size) + 35
            y1 = (row1 * tiles_size) + 35
            if (map_tiles[row1][col1] != g and map_tiles[row1][col1] != m) and (
                    ((x - x1) ** 2 + (y - y1) ** 2) ** (1 / 2)) <= 65:
                # run = False
                dsurf.blit(img1, ((70 * 11) // 2, (70 * 10) // 2))
                dsurf.blit(img2, ((70 * 11) // 2, (70 * 11) // 2))
                mov = False
            if (map_tiles[row1][col1] == m) and (((x - x1) ** 2 + (y - y1) ** 2) ** (1 / 2)) <= 65:
                mov = False
                dsurf.blit(img, ((70 * 11) // 2, (70 * 15) // 2))
    if keys[pygame.K_r]:
        hoppa = 1
        khatwa = 0
        if map_tiles == map_tiles1:
            jump = 1
            x = pos1x
            y = pos1y

        elif map_tiles == map_tiles2:
            jump = 1
            x = pos2x
            y = pos2y
        elif map_tiles == map_tiles3 :
            jump = 1
            x = pos3x
            y = pos3y
        mov = True

    if keys[pygame.K_t]:
        dsurf.blit(img3, ((70 * 11) // 2, (70 * 13) // 2))

    pygame.display.update()


