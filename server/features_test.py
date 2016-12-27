import unittest
import features


class CommsStub():
    def __init__(self):
        self.sent_message = None

    def send(self, message):
        self.sent_message = message


class HandleFeaturesTest(unittest.TestCase):
    def test_returns_features_if_requested(self):
        comms = CommsStub()

        features.handle_features_request(comms=comms)

        reply, *supported = comms.sent_message.split(' ')
        self.assertEqual(reply, 'supported_features:')
        self.assertIn('base', supported)


if __name__ == '__main__':
    unittest.main()
