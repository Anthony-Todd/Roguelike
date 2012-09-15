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
            layers.append(collision_layer(tilemap[k]))

    return layers

def collision_layer(tilelayer, alt_tilelayer=None, layer=None):

    def collision_sprite(img):
        sprite = cocos.sprite.Sprite(img)
        sprite.cshape = cocos.collision_model.AARectShape(eu.Vector2(0.0,0.0),8,8)
        return sprite

    #cm = cocos.collision_model.CollisionManagerGrid(0,100,0,100,32,32)
    cm = cocos.collision_model.CollisionManager()
    toggle_objs = {}

    if layer == None:
        layer = cocos.layer.ScrollableLayer()
    
    for col in tilelayer.cells:
        for cell in col:
            if cell.tile != None:
                
                img = cell.tile.image.get_image_data().texture
                sprite = collision_sprite(img)
                sprite.position = cell.center

                if cell.get('type') == 'block':
                    layer.add(sprite)
        
                elif cell.get('type') == 'toggle':
                    sprite.norm = img

                    # image to swap to when 'toggled'
                    alt_coords = c['alternate']
                    cell = alt_tilemap.get_cell(*(ast.literal_eval(alt_coords)))
                    sprite.alt = cell.tile.image.get_image_data().texture
                    sprite.toggled = False

                    layer.add(sprite)
                    toggle_objs[sprite.position] = sprite

                #cm.add(sprite)
                               
    return layer
'''
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
'''
