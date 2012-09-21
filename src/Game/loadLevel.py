import cocos
import cocos.euclid as eu
import ast
import pyglet
from Config import Configuration as Conf

def load_level(tilemap, cm):
    layers = []

    for k in sorted(tilemap.__dict__['contents'].keys()):
        if 'background' in k:
            layers.append(tilemap[k])

        elif 'blocks' in k:
            new_layer, cm = collision_layer(tilemap[k], cm)
            layers.append(new_layer)
            
    return layers, cm

def collision_layer(tilelayer, cm, alt_tilelayer=None):

    def collision_sprite(img, pos):
        sprite = cocos.sprite.Sprite(img)
        sprite.cshape = cocos.collision_model.AARectShape(pos, 8,8)
        sprite.position = pos
        return sprite

    toggle_objs = {}

    layer = cocos.layer.ScrollableLayer()
    large_img = pyglet.image.Texture.create(Conf.MapWidth * Conf.TileSize,
                                     Conf.MapHeight * Conf.TileSize)

    for i in range(40):
        for j in range(40):
            cell = tilelayer.get_cell(i,j)
            if cell.tile != None:
                img = cell.tile.image.get_image_data()
                sprite = collision_sprite(img.texture, cell.center)

                if cell.get('type') == 'block':   
                    # create one big background image
                    large_img.blit_into(img, i*16, j*16, 0)
                    cm.add(sprite)

                elif cell.get('type') == 'toggle':
                    # add to layer directly
                    sprite.norm = img.texture

                    # image to swap to when 'toggled' / clicked on
                    alt_coords = c['alternate']
                    acell = alt_tilemap.get_cell(*(ast.literal_eval(alt_coords)))
                    sprite.alt = acell.tile.image.get_image_data().texture
                    sprite.toggled = False

    backdrop = cocos.sprite.Sprite(large_img)
    backdrop.position = (Conf.MapWidth * Conf.TileSize / 2, 
                         Conf.MapHeight * Conf.TileSize / 2)
    layer.add(backdrop)
                        
    return layer,cm

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
