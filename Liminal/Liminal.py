from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

Horror_song_1_liminal = Audio('Horror theme liminal game.wav', loop=True, autoplay=True)

Horror_song_1_liminal.volume = 0.4

class Sky(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = 'sphere'
        self.texture = 'assets/night.jpg'
        self.scale = 150
        self.double_sided = True

class Wall(Entity):
    def __init__(self, position=(0, 0, 0), model='cube', texture='assets/brick.jpg', rotation=(0, 0, 0), scale=(0.25, 5, 30)):
        super().__init__(
            parent=scene,
            position=position,
            model=model,
            texture=texture,
            collider='box',
            color=color.white,
            scale=scale,
            rotation=rotation,
        )

class NPC(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            position=(5, 0.5, 10),
            model='assets/NPC_1_Peter.glb',
            scale=(0.01, 0.01, 0.01),
        )

class Ground(Entity):
    def __init__(self, position=(0, 0, 0), model='cube', texture='assets/plancher.jpg'):
        super().__init__(
            parent=scene,
            position=position,
            model=model,
            texture=texture,
            collider='box',
            color=color.white,
            scale=(1, 0.5, 1),
        )

# Création du sol
for x in range(-16, 16):
    for z in range(-16, 16):
        Ground(position=(x, 0, z))

# Création du plafond
for x in range(-20, 20):
    for z in range(-20, 20):
        Ground(position=(x, 5, z), texture='assets/sol.jpg')

npc = NPC()

# Création des 4 murs
left_wall = Wall(position=(-15, 2, 0))                          # Mur gauche
right_wall = Wall(position=(14.875, 2, 0))                     # Mur droit
front_wall = Wall(position=(0, 2, -15), rotation=(0, 90, 0), scale=(0.25, 5, 30))  # Mur avant
back_wall = Wall(position=(0, 2, 14.875), rotation=(0, 90, 0), scale=(0.25, 5, 30))  # Mur arrière

# Joueur et ciel
player = FirstPersonController()
sky = Sky()

app.run()