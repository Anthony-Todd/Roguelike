'''
Created on Sep 2, 2012

@author: anthony
'''
import cocos

cocos.director.director.init()

from Game import g_GameInstance

if __name__ == '__main__':
    cocos.director.director.run (g_GameInstance)