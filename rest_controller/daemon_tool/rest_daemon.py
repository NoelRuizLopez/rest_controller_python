from rest_controller.daemon_tool.daemon import Daemon


class RestDaemon(Daemon):
   _host = None
   _port = None
   _app = None

   def __init__(self, pid_file, host, port, app):
        super(RestDaemon, self).__init__(pid_file)
        self._host = host
        self._port = port
        self._app = app

   def run(self):
       self._app.run(self._host, self._port)



