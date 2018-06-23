try:
    from urllib.parse import urlencode  # noqa: F401
    from urllib.request import urlopen  # noqa: F401
except ImportError:
    from urllib import urlencode  # noqa: F401
    from urllib2 import urlopen  # noqa: F401
