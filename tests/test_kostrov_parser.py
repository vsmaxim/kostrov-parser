from kostrov_parser import __version__


def test_version():
    if __version__ != '0.1.0':
        raise AssertionError
