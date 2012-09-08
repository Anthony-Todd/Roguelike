'''
Created on Sep 2, 2012

@author: anthony
'''
import cocos.layer
import Entity
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
                self.animations[name][animeID] = pyglet.image.Animation.from_image_sequence(seq, anime.get('speed'), anime.get('loop'))
        #testAnimation = testAnimation.get_texture_sequence()

    def GetCharacterAnimationDict(self, key):
        return self.animations[key]
    
def DecodeCharacterSheet( filename ):
    jsonFile = open(filename)
    d = json.JSONDecoder().decode(jsonFile.read())
    args = dict( ( key.encode('ascii'), value) for key, value in d.items() )
    return CharacterSheet(**args)

class Level(cocos.layer.Layer):
    '''
    classdocs
    '''

    def __init__(self, *argv, **kwargv):
        '''
        Constructor
        '''
        self.parent = kwargv.get('parent')
        self.backGround = cocos.layer.Layer()
        self.foreGround  = cocos.layer.Layer()
        self.player     = cocos.layer.Layer()
        self.entityList = []
        super(Level, self).__init__()
        for l in [self.backGround, self.foreGround, self.player]:
            self.add(l)
        
        # the following is to test the performace of pyglet animations feelfree to delete when you need too
        self.charSheet = DecodeCharacterSheet('../assets/textures/Characters.json')
        self.charGeorge= DecodeCharacterSheet('../assets/textures/George.json')
        
        playerAnime = self.charSheet.GetCharacterAnimationDict('player')
        ai0Anime = self.charSheet.GetCharacterAnimationDict('AI0')
        npcAnime = self.charSheet.GetCharacterAnimationDict('NPC')
        ai1Anime = self.charSheet.GetCharacterAnimationDict('AI1')
        ai2Anime = self.charSheet.GetCharacterAnimationDict('AI2')
        ai3Anime = self.charSheet.GetCharacterAnimationDict('AI3')
        ai4Anime = self.charSheet.GetCharacterAnimationDict('AI4')
        ai5Anime = self.charSheet.GetCharacterAnimationDict('AI5')
        
        georgeAnime = self.charGeorge.GetCharacterAnimationDict('george')
        
        self.player.add(Entity.Factory.Create_AnimatedSprite(georgeAnime, 'walk_up',    (266,144)))
        self.player.add(Entity.Factory.Create_AnimatedSprite(georgeAnime, 'walk_left',  (298,144)))
        self.player.add(Entity.Factory.Create_AnimatedSprite(georgeAnime, 'walk_down',  (320,144)))
        self.player.add(Entity.Factory.Create_AnimatedSprite(georgeAnime, 'walk_right', (352,144)))        
        
        self.foreGround.add(Entity.Factory.Create_AnimatedSprite(ai5Anime, 'walk_up',    (266,400)))
        self.foreGround.add(Entity.Factory.Create_AnimatedSprite(ai5Anime, 'walk_left',  (298,400)))
        self.foreGround.add(Entity.Factory.Create_AnimatedSprite(ai5Anime, 'walk_down',  (320,400)))
        self.foreGround.add(Entity.Factory.Create_AnimatedSprite(ai5Anime, 'walk_right', (352,400)))
        
        self.foreGround.add(Entity.Factory.Create_AnimatedSprite(ai4Anime, 'walk_up',    (266,368)))
        self.foreGround.add(Entity.Factory.Create_AnimatedSprite(ai4Anime, 'walk_left',  (298,368)))
        self.foreGround.add(Entity.Factory.Create_AnimatedSprite(ai4Anime, 'walk_down',  (320,368)))
        self.foreGround.add(Entity.Factory.Create_AnimatedSprite(ai4Anime, 'walk_right', (352,368)))
        
        self.foreGround.add(Entity.Factory.Create_AnimatedSprite(ai3Anime, 'walk_up',    (266,336)))
        self.foreGround.add(Entity.Factory.Create_AnimatedSprite(ai3Anime, 'walk_left',  (298,336)))
        self.foreGround.add(Entity.Factory.Create_AnimatedSprite(ai3Anime, 'walk_down',  (320,336)))
        self.foreGround.add(Entity.Factory.Create_AnimatedSprite(ai3Anime, 'walk_right', (352,336)))
        
        self.foreGround.add(Entity.Factory.Create_AnimatedSprite(ai2Anime, 'walk_up',    (266,304)))
        self.foreGround.add(Entity.Factory.Create_AnimatedSprite(ai2Anime, 'walk_left',  (298,304)))
        self.foreGround.add(Entity.Factory.Create_AnimatedSprite(ai2Anime, 'walk_down',  (320,304)))
        self.foreGround.add(Entity.Factory.Create_AnimatedSprite(ai2Anime, 'walk_right', (352,304)))
        
        self.foreGround.add(Entity.Factory.Create_AnimatedSprite(ai1Anime, 'walk_up',    (266,272)))
        self.foreGround.add(Entity.Factory.Create_AnimatedSprite(ai1Anime, 'walk_left',  (298,272)))
        self.foreGround.add(Entity.Factory.Create_AnimatedSprite(ai1Anime, 'walk_down',  (320,272)))
        self.foreGround.add(Entity.Factory.Create_AnimatedSprite(ai1Anime, 'walk_right', (352,272)))
        
        self.foreGround.add(Entity.Factory.Create_AnimatedSprite(npcAnime, 'walk_up',    (266,176)))
        self.foreGround.add(Entity.Factory.Create_AnimatedSprite(npcAnime, 'walk_left',  (298,176)))
        self.foreGround.add(Entity.Factory.Create_AnimatedSprite(npcAnime, 'walk_down',  (320,176)))
        self.foreGround.add(Entity.Factory.Create_AnimatedSprite(npcAnime, 'walk_right', (352,176)))
        
        self.foreGround.add(Entity.Factory.Create_AnimatedSprite(ai0Anime, 'walk_up',    (266,208)))
        self.foreGround.add(Entity.Factory.Create_AnimatedSprite(ai0Anime, 'walk_left',  (298,208)))
        self.foreGround.add(Entity.Factory.Create_AnimatedSprite(ai0Anime, 'walk_down',  (320,208)))
        self.foreGround.add(Entity.Factory.Create_AnimatedSprite(ai0Anime, 'walk_right', (352,208)))
        
        self.player.add(Entity.Factory.Create_AnimatedSprite(playerAnime, 'walk_up',    (266,240)))
        self.player.add(Entity.Factory.Create_AnimatedSprite(playerAnime, 'walk_left',  (298,240)))
        self.player.add(Entity.Factory.Create_AnimatedSprite(playerAnime, 'walk_down',  (320,240)))
        self.player.add(Entity.Factory.Create_AnimatedSprite(playerAnime, 'walk_right', (352,240)))
        #end of test code
    
    def LoadLevel(self,Filename):
        pass
        # loaded the tiled level from assets levels directory.
    
    def GenerateEntitys(self):
        pass

    
        
