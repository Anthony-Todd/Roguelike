'''
Created on Sep 2, 2012

@author: anthony
'''
import cocos
import pyglet.resource

pyglet.resource.path = ['../assets']
pyglet.resource.path = ['../assets/textures']
pyglet.resource.reindex()

cocos.director.director.init()

from Game import g_GameInstance
import Game.Config

Game.Config.LoadCongurationFile('../assets/Config.json')

if __name__ == '__main__':
    cocos.director.director.run(g_GameInstance)
    Game.Config.SaveConfigurationFile('../assets/Config.json')