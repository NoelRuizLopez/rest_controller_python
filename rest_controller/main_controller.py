'''
Created on 1 de dic. de 2016

@author: Asgard Team.Altran
'''
import json
from flask import Flask, request

from syntactic_analyzer.services import Services
from syntactic_analyzer.configuration.entry_points_URI import *

from rest_controller.configuration.read_config_file import *
from rest_controller.configuration.error_codes import *

from rest_controller.daemon_tool.rest_daemon import RestDaemon
from rest_controller.daemon_tool.runner import Runner

from rest_controller.log.logger import Logger
from rest_controller.output import response


_cfg = None
#_validator = None
app = Flask(__name__)
#####
#
#  ENTRY POINTS
#
#####


@app.route(SERVICE_1, methods=['GET'])
def tokenize():
    # schema = sys._getframe().f_code.co_name + _cfg.schema_suffix
    return context(Services.tokenizer, request.data)


@app.route(SERVICE_2, methods=['POST'])
def tokenize_2():
    # schema = sys._getframe().f_code.co_name + _cfg.schema_suffix
    texto = None

    try:
        texto = str(request.get_json()["text"])
    except  ValueError, e:
        app.logger.info("Sorry, this seems not to be a valid JSON")

    return context(Services.get_sentences, texto)

#####
#
#  Exceptions & Strategy Pattern
#
#####

def dump(exception):
    return json.dumps({'errors': str(exception)})

def context(function, request, *kargs):
    try:
        return function(request, *kargs)
    except Exception, e:
        return response(dump(e), CODE_SERVER_ERROR)
    finally:
        pass

#####
#
#   RUN MODE
#
#####


def debug(args):
    app.run(_cfg.DEBUG_HOST, _cfg.DEBUG_PORT, debug=True, use_reloader=False)

ACTIONS = {'start': [Runner.start, 'Server starting.'],
           'stop': [Runner.stop, 'Server stopping.'],
           'restart': [Runner.restart, 'Server restating.'],
           'status': [Runner.status, 'Service status request.'],
           'debug': [debug, 'Server stating in debug mode.']}

#####
#
#   MAIN
#
#####

def main():
    if len(sys.argv) == 2:
        global _cfg
        _cfg = get_config()
#        global _validator
#        _validator = r_config.get_validator(_cfg)
        Logger.init_logs(_cfg, app)
        daemon = RestDaemon(_cfg.pid_file_full_path,
                            _cfg.ip,
                            int(_cfg.port),
                            app)
        function = ACTIONS.get(sys.argv[1])
        if function is not None:
            try:
                app.logger.info(function[1])
                function[0](daemon)
            except SystemExit:
                pass
            except:
                app.logger.error(traceback.format_exc())
        else:
            print 'Unknown option', sys.argv[1]
            sys.exit(2)
        sys.exit(0)
    else:
        print "Usage of REST API Server: %s start|stop|restart|status|debug" % sys.argv[0]
        sys.exit(2)


if __name__ == "__main__":
    sys.exit(main())
