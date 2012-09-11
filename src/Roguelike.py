'''
Created on Sep 2, 2012

@author: anthony
'''
from cocos.director import director
from pyglet import resource

resource.path = ['../assets']
resource.path = ['../assets/textures']
resource.reindex()


from Game import LoadCongurationFile, SaveConfigurationFile, AppendProperty, Game, Configuration

if __name__ == '__main__':
    LoadCongurationFile('../assets/Config.json')
    AppendProperty( Configuration, None )
    
    director.init()
    director.run(Game())
    SaveConfigurationFile('../assets/Config.json')