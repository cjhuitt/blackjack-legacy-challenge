import unittest
import main


class CommsStub():
    def __init__(self):
        self.sent_message = None

    def send(self, message):
        self.sent_message = message


class DbStub():
    def __init__(self):
        self.pass_auth = False
        self.auth_user = None
        self.auth_pass = None
        self.user_money = None

    def auth(self, user, passwd):
        self.auth_user = user
        self.auth_pass = passwd
        return self.pass_auth

    def money(self, param):
        return self.user_money


class GameStub():
    def __init__(self):
        self.began = False

    def begin(self):
        self.began = True


class HandleAuthTests(unittest.TestCase):
    def test_starts_game_on_valid_login(self):
        params = ['user', 'passwd']
        comms = CommsStub()
        db = DbStub()
        game = GameStub()

        db.pass_auth = True
        main.handle_auth(command='login', params=params, game=game, db=db, comms=comms)

        self.assertTrue(game.began)

    def test_returns_money_on_valid_login(self):
        params = ['user', 'passwd']
        comms = CommsStub()
        db = DbStub()
        game = GameStub()

        db.pass_auth = True
        db.user_money = 50
        main.handle_auth(command='login', params=params, game=game, db=db, comms=comms)

        self.assertTrue('50' in comms.sent_message)

    def test_returns_auth_fail_on_invalid_login(self):
        params = ['user', 'passwd']
        comms = CommsStub()
        db = DbStub()
        game = GameStub()

        db.pass_auth = False
        main.handle_auth(command='login', params=params, game=game, db=db, comms=comms)

        self.assertEqual(comms.sent_message, 'auth_fail')


if __name__ == '__main__':
    unittest.main()
