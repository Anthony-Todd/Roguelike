'''
Created on Sep 2, 2012

@author: anthony
'''
from cocos.director import director
from pyglet import resource

resource.path = ['../assets']
resource.path = ['../assets/textures']
resource.reindex()


from Game import LoadConfigurationFile, SaveConfigurationFile, AppendProperty, Game, Configuration

if __name__ == '__main__':
    LoadConfigurationFile('../assets/Config.json')
    AppendProperty(Configuration, None)
    
    director.init(do_not_scale=True, resizable=True)
    director.run(Game())
    SaveConfigurationFile('../assets/Config.json')    

    
