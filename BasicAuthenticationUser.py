#!python3
#encoding:utf-8
from abc import ABCMeta, abstractmethod
import AGitHubUser
class BasicAuthenticationUser(AGitHubUser.AGitHubUser):
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
    
    @property    
    def Username(self):
        return self.__username
    
    @property    
    def Password(self):
        return self.__password
    
    def CreateHeaders(self):
        return {}
