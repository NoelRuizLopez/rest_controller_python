import logging
from logging.handlers import TimedRotatingFileHandler


class Logger():

    @staticmethod
    def init_logs(cfg, app):
        log_file_full_path = cfg.log_file_name
        MIDNIGHT = 'midnight'
        # Force werkzeug messages to appear also in our file
        werkzeug_hdlr = TimedRotatingFileHandler(log_file_full_path,
                                                 when=MIDNIGHT,
                                                 backupCount=cfg._MAX_NUM_LOGS)
        logging.getLogger('werkzeug').addHandler(werkzeug_hdlr)
        # Force app.log messages to appear also in our file
        our_hdlr = TimedRotatingFileHandler(log_file_full_path, when=MIDNIGHT,
                                            backupCount=cfg._MAX_NUM_LOGS)
        # If you want sized rotating file:
    #     our_hdlr = RotatingFileHandler(log_file_full_path,
    #                                    maxBytes=_MAX_LOG_SIZE,
    #                                    backupCount=_MAX_NUM_LOGS)

        our_hdlr.setFormatter(logging.Formatter('%(asctime)s - %(message)s',
                                                datefmt='%Y/%m/%d %H:%M:%S'))
        app.logger.addHandler(our_hdlr)
        app.logger.setLevel(logging.INFO)
