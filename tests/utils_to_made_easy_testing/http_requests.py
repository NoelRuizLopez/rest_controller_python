import requests

class HTTPRequests(object):

    HOST = '127.0.0.1'
    PORT = '5000'
    URL = "http://%s:%s" % (HOST, PORT)

    @classmethod
    def set_host(cls, host):
        cls.HOST = host
        cls.URL = "http://%s:%s" % (host, cls.PORT)

    @classmethod
    def set_port(cls, port):
        cls.PORT = port
        cls.URL = "http://%s:%s" % (cls.HOST, port)

    @classmethod
    def set_url(cls, url):
        cls.URL = url

    @classmethod
    def POST(cls, endpoint, _json):
        with requests.Session() as session:
            session.trust_env = False
            uri = cls.URL + endpoint

            res = session.post(uri, None, _json)

            return res

    @classmethod
    def GET(cls, endpoint):
        with requests.Session() as session:
            session.trust_env = False
            uri = cls.URL + endpoint

            try:
                res = session.get(uri)
            except Exception as ex:
                raise Exception("REST Client Error: " + str(ex))

            return res

    @classmethod
    def PUT(cls, endpoint, _json):
        with requests.Session() as session:
            uri = cls.URL + endpoint
            try:
                res = session.put(uri, json=_json)

            except Exception as ex:
                raise Exception("REST Client Error: " + str(ex))

            return res

    @classmethod
    def DELETE(cls, endpoint, _json=None):
        with requests.Session() as session:
            session.trust_env = False
            uri = cls.URL + endpoint
            try:
                res = session.delete(uri, json=_json)
            except Exception:
                pass

            return res