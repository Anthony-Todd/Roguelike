'''
Created on Sep 2, 2012

@author: anthony
'''
from cocos.director import director
from pyglet import resource
import pyglet.clock

resource.path = ['../assets']
resource.path = ['../assets/textures']
resource.reindex()


from Game import LoadConfigurationFile, SaveConfigurationFile, AppendProperty, Game
from Game.Config import Configuration as Conf

if __name__ == '__main__':
    LoadConfigurationFile('../assets/Config.json')
    AppendProperty(Conf, None)
    
    width = Conf.TileSize * Conf.WindowWidth
    height = Conf.TileSize * Conf.WindowHeight
    director.init(width=width, height=height, do_not_scale=True, resizable=True)
    #pyglet.clock.set_fps_limit(30)
    director.show_FPS = True
    director.run(Game())
    SaveConfigurationFile('../assets/Config.json')    

    
