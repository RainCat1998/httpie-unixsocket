"""
UNIX socket transport plugin for HTTPie.

"""
from httpie.plugins import TransportPlugin
from requests.compat import urlparse
from requests_unixsocket import UnixAdapter, Settings, DEFAULT_SCHEME


__version__ = '0.0.0'
__author__ = 'Marc Abramowitz'
__licence__ = 'BSD'

def custom_urlparse(url):
    parsed_url = urlparse(url)
    return Settings.ParseResult(
        sockpath=parsed_url.path,
        reqpath=parsed_url.fragment,
    )

class UnixSocketTransportPlugin(TransportPlugin):
    name = 'UNIX socket transport'

    prefix = DEFAULT_SCHEME

    def get_adapter(self):
        return UnixAdapter(settings=Settings(urlparse=custom_urlparse))
