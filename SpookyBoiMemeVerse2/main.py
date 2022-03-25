from ursina import * 

def update():
    e.rotation_y += .1

app = Ursina()

e = Entity(
    model = 'assets/gameobj/lowptree.obj',
    color = color.red,
    texture = 'assets/gamemtl/Lowpoly_tree_sample.mtl',
    position = Vec3(0 ,0 , 0),
    rotation = Vec3(0 ,0 , 0),
    scale = 1,
)

EditorCamera()

app.run()