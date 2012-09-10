'''
Created on Sep 2, 2012

@author: anthony
'''
from cocos.director import director
from pyglet import resource

resource.path = ['../assets']
resource.path = ['../assets/textures']
resource.reindex()

director.init()

from Game.Config import LoadCongurationFile, SaveConfigurationFile, Configuration
from Game.DebugMenu import g_DebugMenue

LoadCongurationFile('../assets/Config.json')
g_DebugMenue.AddObject(Configuration, None)

from Game import g_GameInstance

if __name__ == '__main__':
    director.run(g_GameInstance)
    SaveConfigurationFile('../assets/Config.json')