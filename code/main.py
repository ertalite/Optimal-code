import pygame, sys #Importation des modules
import commands as com
import misc, gates

#-----------------------------[ Initialisation ]------------------

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Apprends les portes logiques !')
clock = pygame.time.Clock()
pygame.display.set_icon(com.Affichage.chargementFichier('./graphics/lights/light-bulb-on.png'))

#-----------------------------[ Chargement des fichiers ]------------------

main_menu_surface = com.Affichage.chargementFichier('./graphics/backgrounds/esthetique-minimal-violet.jpg')

# Polices

Nexa = com.Affichage.chargementPolice('./font/Nexa-Heavy.ttf', 30)

# Textes 

title_surface = com.Affichage.creerTexte(Nexa, 'Apprends les portes logiques !', True, 'black')
title_rectangle = com.Collision.creerRectangle(title_surface, 'center', (640, 160))

cours_surface = com.Affichage.creerTexte(Nexa, "Les portes logiques c'est quoi ?", True, 'black')
cours_rectangle = com.Collision.creerRectangle(cours_surface, 'center', (640, 120))

and_surface = com.Affichage.creerTexte(Nexa, 'AND', True, 'black')
and_rectangle = com.Collision.creerRectangle(and_surface, 'center', (640, 160))

or_surface = com.Affichage.creerTexte(Nexa, 'OR', True, 'black')
or_rectangle = com.Collision.creerRectangle(or_surface, 'center', (640, 160))

not_surface = com.Affichage.creerTexte(Nexa, 'NOT', True, 'black')
not_rectangle = com.Collision.creerRectangle(not_surface, 'center', (640, 160))

xor_surface = com.Affichage.creerTexte(Nexa, 'XOR', True, 'black')
xor_rectangle = com.Collision.creerRectangle(xor_surface, 'center', (640, 160))

nand_surface = com.Affichage.creerTexte(Nexa, 'NAND', True, 'black')
nand_rectangle = com.Collision.creerRectangle(nand_surface, 'center', (640, 160))

nor_surface = com.Affichage.creerTexte(Nexa, 'NOR', True, 'black')
nor_rectangle = com.Collision.creerRectangle(nor_surface, 'center', (640, 160))

xnor_surface = com.Affichage.creerTexte(Nexa, 'XNOR', True, 'black')
xnor_rectangle = com.Collision.creerRectangle(xnor_surface, 'center', (640, 160))

# Boutons de menu

cours_img = com.Affichage.chargementFichier('./graphics/buttons/menu_buttons/button_cours.png')
cours_button = misc.Bouton(640, 280, cours_img, 1)

circuit_img = com.Affichage.chargementFichier('./graphics/buttons/menu_buttons/button_circuit.png')
circuit_button = misc.Bouton(640, 400, circuit_img, 1)

quitter_img = com.Affichage.chargementFichier('./graphics/buttons/menu_buttons/button_quitter.png')
quitter_button = misc.Bouton(640, 520, quitter_img, 1)

retour_img = com.Affichage.chargementFichier('./graphics/buttons/menu_buttons/button_retour.png')
retour_button = misc.Bouton(150, 620, retour_img, 1)

propos_img = com.Affichage.chargementFichier('./graphics/buttons/menu_buttons/button_propos.png')
propos_button = misc.Bouton(1150, 610, propos_img, 1)

# Boutons de circuit

a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a.png')
a_button = misc.Bouton(280, 300, a_button_img, 1)

a_button_pressed_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a_pressed.png')
a_button_pressed = misc.Bouton(280, 300, a_button_pressed_img, 1)

b_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b.png')
b_button = misc.Bouton(280, 480, b_button_img, 1)

b_button_pressed_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b_pressed.png')
b_button_pressed = misc.Bouton(280, 480, b_button_pressed_img, 1)

fleche_de_droite_button_img = com.Affichage.chargementFichier('./graphics/buttons/cours_buttons/fleche-droite.png')
fleche_de_droite_button = misc.Bouton(1180, 360, fleche_de_droite_button_img, 0.1)

fleche_de_gauche_button_img = com.Affichage.chargementFichier('./graphics/buttons/cours_buttons/fleche-gauche.png')
fleche_de_gauche_button = misc.Bouton(100, 360, fleche_de_gauche_button_img, 0.1)

# Portes logiques

ANDgate_img = com.Affichage.chargementFichier('./graphics/gates/ANDgate.png')
ANDgate_img = com.Affichage.redimensionner(ANDgate_img, 0.65)
ANDgate_rectangle = com.Collision.creerRectangle(ANDgate_img, 'center', (640, 370))

NANDgate_img = com.Affichage.chargementFichier('./graphics/gates/NANDgate.png')
NANDgate_img = com.Affichage.redimensionner(NANDgate_img, 0.55)
NANDgate_rectangle = com.Collision.creerRectangle(NANDgate_img, 'center', (640, 360))

NORgate_img = com.Affichage.chargementFichier('./graphics/gates/NORgate.png')
NORgate_img = com.Affichage.redimensionner(NORgate_img, 0.518)
NORgate_rectangle = com.Collision.creerRectangle(NORgate_img, 'center', (640, 360))

NOTgate_img = com.Affichage.chargementFichier('./graphics/gates/NOTgate.png')
NOTgate_img = com.Affichage.redimensionner(NOTgate_img, 0.35)
NOTgate_rectangle = com.Collision.creerRectangle(NOTgate_img, 'center', (640, 360))

ORgate_img = com.Affichage.chargementFichier('./graphics/gates/ORgate.png')
ORgate_img = com.Affichage.redimensionner(ORgate_img, 0.65)
ORgate_rectangle = com.Collision.creerRectangle(ORgate_img, 'center', (640, 360))

XNORgate_img = com.Affichage.chargementFichier('./graphics/gates/XNORgate.png')
XNORgate_img = com.Affichage.redimensionner(XNORgate_img, 0.7)
XNORgate_rectangle = com.Collision.creerRectangle(XNORgate_img, 'center', (640, 360))

XORgate_img = com.Affichage.chargementFichier('./graphics/gates/XORgate.png')
XORgate_img = com.Affichage.redimensionner(XORgate_img, 0.325)
XORgate_rectangle = com.Collision.creerRectangle(XORgate_img, 'center', (640, 360))

# Portes logique menu circuit

ANDgate = gates.ANDgate(1200, 50, 0.1)
NANDgate = gates.NANDgate(1200, 150, 0.08)
NORgate = gates.NORgate(1200, 250, 0.08)
NOTgate = gates.NOTgate(1200, 350, 0.05)
ORgate = gates.ORgate(1200, 450, 0.1)
XNORgate = gates.XNORgate(1200, 550, 0.1)
XORgate = gates.XORgate(1200, 650, 0.05)

# Lumières

light_on = misc.Light(1025, 360,'./graphics/lights/light-bulb-on.png', 0.1)

light_off = misc.Light(1025, 360, './graphics/lights/light-bulb-off.png', 0.1)

light_group = pygame.sprite.Group()

light_group.add(light_on, light_off)

# Circuit


blank_circuit_menu_surface = pygame.Surface([300, 720])
blank_circuit_menu_surface.fill('white')
blank_circuit_menu_surface.set_alpha(125)

fleche_gauche_menu_circuit = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/icone-fleche-gauche-grise.png')
fleche_gauche_menu_circuit = misc.Bouton(1210, 50, fleche_gauche_menu_circuit, 0.2)

fleche_droite_menu_circuit = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/icone-fleche-droite-grise.png')
fleche_droite_menu_circuit = misc.Bouton(1070, 50, fleche_droite_menu_circuit, 0.2)

#-----------------------------[ Game Loop ]------------------

SYSTEM_STATE ='main' #Initialisation du menu principal au démarage du programme
COURS_STATE = 'cours_un' #Initalisation du menu "cours" sur la page "cours_un"
light_bool = True
fleche_bool = True

run = True 
while run:

    com.Affichage.afficher(screen, main_menu_surface, (0, 0), 1) #Affichage du fond 

# Menu principal

    if SYSTEM_STATE == 'main': 

        com.Affichage.afficher(screen, title_surface, title_rectangle, 1)

        if cours_button.afficher(screen) == True:
            
            SYSTEM_STATE = 'cours'

        if circuit_button.afficher(screen) == True:
            
            SYSTEM_STATE = 'circuit'

        if quitter_button.afficher(screen) == True:
            run = False

        if propos_button.afficher(screen) == True:

            SYSTEM_STATE = 'propos'

# Menu cours           

    if SYSTEM_STATE == 'cours':

        

    # Onglet "cours_un"

        if COURS_STATE == 'cours_un':
    

            com.Affichage.afficher(screen, cours_surface, cours_rectangle, 1)
            
            phrase_cours = """Une porte logique (gate) est un circuit électronique réalisant
des opérations logiques (booléennes) sur une séquence de bits. 
Cette séquence est donnée par un signal d'entrée modulé en créneau 
(signal carré) et cadencé de façon précise par un circuit d'horloge, 
ou quartz. Les opérations logiques sont réalisées électriquement par 
une combinaison de bascules ou inverseurs, à base de transistors.
Étant donné les capacités d'intégration en électronique, un circuit 
intégré comporte généralement plusieurs portes à la fois."""

            phrase_cours_rectangle = com.Collision.creerRectangle(screen, 'center', (125, 220))

            x, y =phrase_cours_rectangle.center

            for ligne in phrase_cours.splitlines():

                x,y = screen.blit(Nexa.render(ligne, 1, "black"), (x,y)).bottomleft
 

            if fleche_de_droite_button.afficher(screen) == True and clicked == False:
                clicked = True
                COURS_STATE = 'and'

    # Onglet "and"

        if COURS_STATE == 'and':

            com.Affichage.afficher(screen, and_surface, and_rectangle, 1)
        
            com.Affichage.afficher(screen, ANDgate_img, ANDgate_rectangle, 1)

            light_off.afficher(screen)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] and keys[pygame.K_b]:
                  
                  light_on.afficher(screen)

            if keys[pygame.K_a]:

                a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a_pressed.png')
                a_button = misc.Bouton(280, 300, a_button_img, 1)

            if keys[pygame.K_b]:

                b_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b_pressed.png')
                b_button = misc.Bouton(280, 435, b_button_img, 1)

            a_button.afficher(screen)
   
            b_button.afficher(screen)

            a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a.png')
            a_button = misc.Bouton(280, 300, a_button_img, 1)

            b_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b.png')
            b_button = misc.Bouton(280, 435, b_button_img, 1)

            if fleche_de_gauche_button.afficher(screen) == True and clicked == False:
                clicked = True
                COURS_STATE = 'cours_un'

            if fleche_de_droite_button.afficher(screen) == True and clicked == False:
                clicked = True
                COURS_STATE = 'or'

    # Onglet "or"

        if COURS_STATE == 'or':

            com.Affichage.afficher(screen, or_surface, or_rectangle, 1)

            com.Affichage.afficher(screen, ORgate_img, ORgate_rectangle, 1)

            light_off.afficher(screen)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] or keys[pygame.K_b]:
                  
                light_on.afficher(screen)

            if keys[pygame.K_a]:

                a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a_pressed.png')
                a_button = misc.Bouton(280, 300, a_button_img, 1)

            if keys[pygame.K_b]:

                b_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b_pressed.png')
                b_button = misc.Bouton(280, 435, b_button_img, 1)

            a_button.afficher(screen)
   
            b_button.afficher(screen)

            a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a.png')
            a_button = misc.Bouton(280, 300, a_button_img, 1)

            b_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b.png')
            b_button = misc.Bouton(280, 435, b_button_img, 1)

            if fleche_de_gauche_button.afficher(screen) == True and clicked == False:

                COURS_STATE = 'and'
                clicked = True

            if fleche_de_droite_button.afficher(screen) == True and clicked == False:

                COURS_STATE = 'not'
                clicked = True

    # Onglet "not"

        if COURS_STATE == 'not':

            com.Affichage.afficher(screen, not_surface, not_rectangle, 1)

            com.Affichage.afficher(screen, NOTgate_img, NOTgate_rectangle, 1)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_a]:

                light_bool = False
                light_off.afficher(screen)
                a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a_pressed.png')
                a_button = misc.Bouton(280, 360, a_button_img, 1)

            a_button.afficher(screen)

            a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a.png')
            a_button = misc.Bouton(280, 360, a_button_img, 1)

            if fleche_de_gauche_button.afficher(screen) == True and clicked == False:

                COURS_STATE = 'or'
                clicked = True

            if fleche_de_droite_button.afficher(screen) == True and clicked == False:

                COURS_STATE = 'xor'
                clicked = True

            if light_bool:

                light_on.afficher(screen)

            light_bool = True

            

    # Onglet "xor"

        if COURS_STATE == 'xor':

            light_bool = False

            com.Affichage.afficher(screen, xor_surface, xor_rectangle, 1)

            com.Affichage.afficher(screen, XORgate_img, XORgate_rectangle, 1)

            light_off.afficher(screen)

            light_bool = False

            keys = pygame.key.get_pressed()

            if not(keys[pygame.K_a] and keys[pygame.K_b]):    

                light_bool = False
                  
            if keys[pygame.K_a]:

                light_bool = True
                a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a_pressed.png')
                a_button = misc.Bouton(280, 300, a_button_img, 1)

                if keys[pygame.K_b]:

                    light_bool = False
                    light_off.afficher(screen)

            if keys[pygame.K_b]:

                light_bool = True
                b_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b_pressed.png')
                b_button = misc.Bouton(280, 435, b_button_img, 1)

                if keys[pygame.K_a]:

                    light_bool = False
                    light_off.afficher(screen)

            a_button.afficher(screen)
   
            b_button.afficher(screen)

            a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a.png')
            a_button = misc.Bouton(280, 300, a_button_img, 1)

            b_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b.png')
            b_button = misc.Bouton(280, 435, b_button_img, 1)

            if fleche_de_gauche_button.afficher(screen) == True and clicked == False:

                COURS_STATE = 'not'
                clicked = True

            if fleche_de_droite_button.afficher(screen) == True and clicked == False:

                COURS_STATE = 'nand'
                clicked = True

            if light_bool:
                
                light_on.afficher(screen)


    # Onglet "nand"

        if COURS_STATE == 'nand':

            com.Affichage.afficher(screen, nand_surface, nand_rectangle, 1)

            com.Affichage.afficher(screen, NANDgate_img, NANDgate_rectangle, 1)

            keys = pygame.key.get_pressed()

            if not(keys[pygame.K_a] and keys[pygame.K_b]):

                light_on.afficher(screen)

            if keys[pygame.K_a]:

                a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a_pressed.png')
                a_button = misc.Bouton(280, 300, a_button_img, 1)

            if keys[pygame.K_b]:

                b_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b_pressed.png')
                b_button = misc.Bouton(280, 435, b_button_img, 1)

            a_button.afficher(screen)
   
            b_button.afficher(screen)

            a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a.png')
            a_button = misc.Bouton(280, 300, a_button_img, 1)

            b_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b.png')
            b_button = misc.Bouton(280, 435, b_button_img, 1)

            if fleche_de_gauche_button.afficher(screen) == True and clicked == False:

                COURS_STATE = 'xor'
                clicked = True

            if fleche_de_droite_button.afficher(screen) == True and clicked == False:

                COURS_STATE = 'nor'
                clicked = True

            light_bool = True

            if light_bool:
 
                light_off.afficher(screen)

        # Onglet "nor"

        if COURS_STATE == 'nor':

            com.Affichage.afficher(screen, nor_surface, nor_rectangle, 1)

            com.Affichage.afficher(screen, NORgate_img, NORgate_rectangle, 1)

            light_bool = True

            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] and keys[pygame.K_b]:
                  
                light_bool = False
                light_off.afficher(screen)

            if keys[pygame.K_a]:

                light_bool = False
                light_off.afficher(screen)

                a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a_pressed.png')
                a_button = misc.Bouton(280, 300, a_button_img, 1)

            if keys[pygame.K_b]:

                light_bool = False
                light_off.afficher(screen)

                b_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b_pressed.png')
                b_button = misc.Bouton(280, 435, b_button_img, 1)

            a_button.afficher(screen)
   
            b_button.afficher(screen)

            a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a.png')
            a_button = misc.Bouton(280, 300, a_button_img, 1)

            b_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b.png')
            b_button = misc.Bouton(280, 435, b_button_img, 1)

            if fleche_de_gauche_button.afficher(screen) == True and clicked == False:

                COURS_STATE = 'nand'
                clicked = True

            if fleche_de_droite_button.afficher(screen) == True and clicked == False:

                COURS_STATE = 'xnor'
                clicked = True

            if light_bool:

                light_on.afficher(screen)

         # Onglet "xnor"

        if COURS_STATE == 'xnor':

            com.Affichage.afficher(screen, xnor_surface, xnor_rectangle, 1)

            com.Affichage.afficher(screen, XNORgate_img, XNORgate_rectangle, 1)

            light_bool = True

            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] and keys[pygame.K_b]:
                  
                light_bool = True
                light_on.afficher(screen)

            if keys[pygame.K_a]:

                light_bool = False
                light_off.afficher(screen)

                a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a_pressed.png')
                a_button = misc.Bouton(280, 300, a_button_img, 1)

            if keys[pygame.K_b]:

                light_bool = False
                light_off.afficher(screen)

                b_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b_pressed.png')
                b_button = misc.Bouton(280, 435, b_button_img, 1)

            a_button.afficher(screen)
   
            b_button.afficher(screen)

            a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a.png')
            a_button = misc.Bouton(280, 300, a_button_img, 1)

            b_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b.png')
            b_button = misc.Bouton(280, 435, b_button_img, 1)

            if fleche_de_gauche_button.afficher(screen) == True and clicked == False:

                COURS_STATE = 'nor'
                clicked = True


            if fleche_de_droite_button.afficher(screen) == True and clicked == False:

                COURS_STATE = 'resume'
                clicked = True

            if light_bool:

                light_on.afficher(screen)

        # Onglet "resume"

        if COURS_STATE == 'resume':

            com.Affichage.afficher(screen, xnor_surface, xnor_rectangle, 1)

            com.Affichage.afficher(screen, XNORgate_img, XNORgate_rectangle, 1)

            com.Affichage.afficher(screen, light_off_img, light_off_rectangle, 1)

            if fleche_de_gauche_button.afficher(screen) == True and clicked == False:

                COURS_STATE = 'xnor'
                clicked = True

            light_bool = True

            if light_bool:

                light_off.afficher(screen)
        
        if retour_button.afficher(screen):

            COURS_STATE = 'cours_un'
            SYSTEM_STATE = 'main'


    # Menu circuit

    if SYSTEM_STATE == 'circuit':


        if fleche_bool:

            if fleche_gauche_menu_circuit.afficher(screen) == True:

                fleche_bool = False
            
        if not fleche_bool:

            com.Affichage.afficher(screen, blank_circuit_menu_surface, (980, 0), 1)

            if ANDgate.afficher(screen):
                ANDgate.rectangle.center = pygame.mouse.get_pos()
            if NANDgate.afficher(screen):
                NANDgate.rectangle.center = pygame.mouse.get_pos()
            if NORgate.afficher(screen):
                NORgate.rectangle.center = pygame.mouse.get_pos()
            if NOTgate.afficher(screen):
                NOTgate.rectangle.center = pygame.mouse.get_pos()
            if ORgate.afficher(screen):
                ORgate.rectangle.center = pygame.mouse.get_pos()
            if XNORgate.afficher(screen):
                XNORgate.rectangle.center = pygame.mouse.get_pos()
            if XORgate.afficher(screen):
                XORgate.rectangle.center = pygame.mouse.get_pos()

            if fleche_droite_menu_circuit.afficher(screen) == True:

                fleche_bool = True


        if retour_button.afficher(screen) == True:

            SYSTEM_STATE = 'main'

    # Menu à propos

    if SYSTEM_STATE == 'propos':

        phrase_propos = """'Apprends les portes logiques !' est un projet réalisé dans
le cadre des trophées NSI."""

        phrase_propos_rectangle = com.Collision.creerRectangle(screen, 'center', (100, 150))
        x, y = phrase_propos_rectangle.center

        for ligne in phrase_propos.splitlines():

            x,y = screen.blit(Nexa.render(ligne, 1, "black"), (x,y)).bottomleft

        if retour_button.afficher(screen) == True:
     

            SYSTEM_STATE = 'main'



    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False

    pygame.display.update()
    clock.tick(60)