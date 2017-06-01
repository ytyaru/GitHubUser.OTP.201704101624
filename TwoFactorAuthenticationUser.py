#!python3
#encoding:utf-8
from abc import ABCMeta, abstractmethod
import AGitHubUser
import BasicAuthenticationUser
import pyotp
class TwoFactorAuthenticationUser(BasicAuthenticationUser.BasicAuthenticationUser):
    def __init__(self, username, password, secret):
        super().__init__(username, password)
        self.__secret = secret
        self.__totp = pyotp.TOTP(self.__secret)
    
    @property
    def OneTimePassword(self):
        return self.__totp.now()
    
    def CreateHeaders(self):
        return {"X-GitHub-OTP": self.OneTimePassword}
