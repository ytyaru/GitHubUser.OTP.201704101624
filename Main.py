#!python3
#encoding:utf-8
import argparse
import AGitHubUser
import BasicAuthenticationUser
import OAuthNonWebApplicationUser
import TwoFactorAuthenticationUser
class Main:
    def __init__(self):
        pass

    def Run(self):
        parser = argparse.ArgumentParser(
            description='GitHub Authentication User Create Test.',
        )
        parser.add_argument('-u', '--username')
        parser.add_argument('-p', '--password')
        parser.add_argument('-t', '--token')
        parser.add_argument('-s', '--two-factor-secret')
        args = parser.parse_args()

        user = None
        if (None is not args.token):
            user = OAuthNonWebApplicationUser.OAuthNonWebApplicationUser(args.token)
        elif (None is not args.username) and (None is not args.password) and (None is not args.two_factor_secret):
            user = TwoFactorAuthenticationUser.TwoFactorAuthenticationUser(args.username, args.password, args.two_factor_secret)
        elif (None is not args.username) and (None is not args.password):
            user = BasicAuthenticationUser.BasicAuthenticationUser(args.username, args.password)
        else:
            raise Exception('認証データ生成エラー。以下の組合せのみ有効です。Basic: username, password, TwoFactor: username, password, two-factor-secret, OAuthNonWebApp: token')
        self.__RunApi(user)

    def __RunApi(self, user):
        params = {}
        headers = {
            "Time-Zone": "Asia/Tokyo"
        }
        headers.update(user.CreateHeaders())
        params['headers'] = headers
        if isinstance(user, BasicAuthenticationUser.BasicAuthenticationUser):
            params['auth'] = (user.Username, user.Password)
        print(params)
        # requests.get(url, **params)
        # requests.get(url, headers=params['headers'], auth=params['auth'])

if __name__ == '__main__':
    main = Main()
    main.Run()
