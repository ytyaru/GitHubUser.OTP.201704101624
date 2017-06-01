#!python3
#encoding:utf-8
from abc import ABCMeta, abstractmethod
class AGitHubUser(metaclass=ABCMeta):
    @abstractmethod
    def CreateHeaders(self):
        pass

