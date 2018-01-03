import requests


class RestClient(object):
    session = requests.Session()
    session.trust_env = False

    @classmethod
    def do_request(self, method, uri, **kwargs):
        try:
            return getattr(self.session, method)(uri, **kwargs)
        except Exception as ex:
            raise Exception("REST Client Error: " + str(ex))
