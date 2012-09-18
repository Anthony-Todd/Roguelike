import cocos
from cocos import tiles, actions, layer, collision_model
import cocos.euclid as eu
import ast
import pyglet

def load_level(tilemap):
    layers = []
    cm = cocos.collision_model.CollisionManagerGrid(0,40*16,0,40*16,16*1.25,16*1.25)
    #cm = None
    
    for k in sorted(tilemap.__dict__['contents'].keys()):
        if 'background' in k:
            layers.append(tilemap[k])

        elif 'blocks' in k:
            new_layer,cm = collision_layer(tilemap[k], cm)
            layers.append(new_layer)
            
    #print type(cm)
    return layers, cm

def collision_layer(tilelayer, cm, alt_tilelayer=None):

    def collision_sprite(img, pos):
        sprite = cocos.sprite.Sprite(img)
        sprite.cshape = cocos.collision_model.AARectShape(pos, 8,8)
        sprite.position = pos
        return sprite

    toggle_objs = {}

    layer = cocos.layer.ScrollableLayer()
    im = pyglet.image.Texture.create(40*16, 40*16)
    #print type(tilelayer)
    for i in range(40):
        for j in range(40):
            cell = tilelayer.get_cell(i,j)
            if cell.tile != None:
                img = cell.tile.image.get_image_data()
                sprite = collision_sprite(img.texture, cell.center)
                im.blit_into(img, i*16, j*16, 0)
                cm.add(sprite)
    spr = cocos.sprite.Sprite(im)
    spr.position = (20*16,20*16)
    layer.add(spr)

    '''
    batch = cocos.batch.BatchNode()
    #layer.add(batch)
    for col in tilelayer.cells:
        for cell in col:
            if cell.tile != None:
                
                img = cell.tile.image.get_image_data().texture
                sprite = collision_sprite(img, cell.center)
                print cell.topright
                #sprite.position = cell.center

                if cell.get('type') == 'block':
                    pass
                    #batch.add(sprite)
        
                elif cell.get('type') == 'toggle':
                    sprite.norm = img

                    # image to swap to when 'toggled'
                    alt_coords = c['alternate']
                    cell = alt_tilemap.get_cell(*(ast.literal_eval(alt_coords)))
                    sprite.alt = cell.tile.image.get_image_data().texture
                    sprite.toggled = False

                    batch.add(sprite)
                    toggle_objs[sprite.position] = sprite
                
                #cm.add(sprite)
    '''                         
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
