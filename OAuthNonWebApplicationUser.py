#!python3
#encoding:utf-8
from abc import ABCMeta, abstractmethod
import AGitHubUser
class OAuthNonWebApplicationUser(AGitHubUser.AGitHubUser):
    def __init__(self, token):
        self.__token = token
    
    @property
    def AccessToken(self):
        return self.__token
    
    def CreateHeaders(self):
        return {"Authorization": "token " + self.AccessToken}
