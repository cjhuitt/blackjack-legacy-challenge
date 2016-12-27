supported_features = ['base']


def handle_features_request(comms):
    supported = ' '.join(supported_features)
    comms.send('supported_features: {}'.format(supported))
