#============= Lisiting of States =============#
INIT = 0
MUSIC = 1
GAME = 2
WIN = 3
QUIT = 4
LOSE = 5

#======= Parameters =======#
width = 800
height = 600

fps = 60

white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
yellow = (255,255,0)
blue = (0,0,255)
orange = (255,122,0)
transparent = (0,0,0,0)

third = int(width/3)
sixth = int(third/6)

linha_e_i = (third, 0)
linha_e_f = (third, height)

linw_d_i = (2*third, 0)
line_d_f = (2*third, height)

y_teclas = int(height * 15/17)


#========== Music timestoppings ==========#
dic = {'assets/music/riptide_vance-joy.mp3':198, 'assets/music/grapejuice-harry.mp3':190, 'assets/music/jose_gonzalez-killing_for_love.mp3':181, 'assets/music/clairo_flamin-hot-cheetos.mp3':125, 'assets/music/a-drowning_how-to-destroy-angels.mp3':391, 'assets/music/eyen_plaid.mp3':260}