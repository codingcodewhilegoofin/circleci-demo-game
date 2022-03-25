# Import the Add function, and assert that it works correctly.
from ursina import *
from main import update

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

if __name__ == '__main__':
        update()