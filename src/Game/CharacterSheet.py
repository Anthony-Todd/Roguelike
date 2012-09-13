'''
Created on Sep 9, 2012

@author: anthony
'''
import json
import pyglet.resource

class CharacterSheet(object):
    
    def __init__(self, image=None, x=1, y=1, characters=None):
        self.image = pyglet.resource.image(image)
        self.animations = {}
        animations = pyglet.image.ImageGrid(self.image, y, x)
        animations  = animations.get_texture_sequence()

        for c in characters:
            name = c.get('name')
            self.animations[name] = {}

            for anime in c['animations']:
                animeID = anime.get('id')
                seq = []
                
                for frame in anime['sequence']:
                    seq.append(animations[frame])

                self.animations[name][animeID] = \
                     pyglet.image.Animation.from_image_sequence(seq, anime.get('speed'), anime.get('loop'))

        #testAnimation = testAnimation.get_texture_sequence()

    def GetCharacterAnimationDict(self, key):
        return self.animations[key]
    
def DecodeCharacterSheet(filename):
    jsonFile = open(filename)
    d = json.loads(jsonFile.read())
    args = dict((key.encode('ascii'), value) for key, value in d.items())

    return CharacterSheet(**args)
