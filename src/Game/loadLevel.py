import cocos
from cocos import tiles, actions, layer, collision_model
import cocos.euclid as eu
import ast

def load_level(tilemap):
    layers = []
    
    for k in sorted(tilemap.__dict__['contents'].keys()):
        if 'background' in k:
            layers.append(tilemap[k])

        elif 'blocks' in k:
            layers.append(CollisionLayer(tilemap[k]))

    return layers

class CollisionSprite(cocos.sprite.Sprite):
    def __init__(self, image, position):
        super(CollisionSprite, self).__init__(image)
        #self.cshape = cocos.collision_model.AARectShape(position, 16, 16)
        self.cshape = cocos.collision_model.AARectShape(eu.Vector2(0.0, 0.0), 4, 4)

class CollisionLayer(cocos.layer.ScrollableLayer):

    #is_event_handler = True

    def __init__(self,tilemap=None, alt_tilemap=None, z=0):
        super(CollisionLayer, self).__init__()
        self.cm = cocos.collision_model.CollisionManager()
        self.objects = {}
        self.tilemap = tilemap
        if tilemap:
            self.add_tilemap(tilemap,alt_tilemap, z=z)
        
    def add_tilemap(self,tilemap,alt_tilemap = None, z=0):
        for c in tilemap.find_cells(type='block'):
            sprite = CollisionSprite(c.tile.image.get_image_data().texture, c.center)
            sprite.position = c.center
            self.add(sprite)
            self.cm.add(sprite)

        for c in tilemap.find_cells(type='toggle'):
            image = c.tile.image.get_image_data().texture
            sprite = CollisionSprite(image, c.center)
            sprite.norm = image

            # image to swap to when 'toggled'
            alt_coords = c['alternate']
            cell = alt_tilemap.get_cell(*(ast.literal_eval(alt_coords)))
            sprite.alt = cell.tile.image.get_image_data().texture
            sprite.toggled = False
    
            sprite.position = c.center

            self.add(sprite)
            #self.cm.add(sprite)
            self.objects[sprite.position] = sprite
                    
    def on_mouse_press(self, x, y, buttons, modifiers):
        cell = self.tilemap.get_at_pixel(x,y)
        
        if cell.center in self.objects:
            pos = cell.center
            sprite = self.objects[pos]

            if sprite.toggled:
                sprite.toggled = False
                sprite.image = sprite.norm
            else:
                sprite.toggled = True
                sprite.image = sprite.alt

