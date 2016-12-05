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

    def auth(self, user, passwd):
        self.auth_user = user
        self.auth_pass = passwd
        return self.pass_auth

    def money(self, param):
        return None


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


if __name__ == '__main__':
    unittest.main()
