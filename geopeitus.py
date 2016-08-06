import logging
import requests

from collections import namedtuple

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')
AuthDetails = namedtuple('AuthDetails', 'username password')

class Site:
    SITENAME = '.'

    def __init__(self, authDetails):
        self.authDetails = authDetails
        self.cookies = requests.cookies.RequestsCookieJar()
        self.isLoggedIn = False

    def login(self):
        # Subclass
        logging.info("Logged into {} as {}.".format(self.SITENAME, self.authDetails.username))
        self.isLoggedIn = True

    def listCaches(self):
        if not self.isLoggedIn:
            raise RuntimeError("User is not logged in to {}.".format(self.SITENAME))


class GeoCaching(Site):
    SITENAME = "geocaching.com"

    def login(self):
        super().login()

engSite = GeoCaching(AuthDetails("styx0", "123"))
engSite.login()
