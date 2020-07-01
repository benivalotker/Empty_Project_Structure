import os
import time
import logging
from logging_pkg import log_config
from logging.handlers import RotatingFileHandler


def init_log(service_name):
    log_message = f"{service_name} restart"

    logs = RotatingLog(f"{service_name}.log")
    logs.info(log_message)
    print(log_message)

    return logs


class RotatingLog():
    def __init__(self, file_name):
        if os.name == "nt":
            if not os.path.exists(log_config.win_log_path):
                os.mkdir(log_config.win_log_path)
            log_path = log_config.win_log_path
        else:
            if not os.path.exists(log_config.unix_log_path):
                os.mkdir(log_config.unix_log_path)
            log_path = log_config.unix_log_path

        # initial logging class
        self.logger = logging.getLogger(file_name)

        # set rotatating handler setting
        self.handler = RotatingFileHandler(log_path + file_name, maxBytes=log_config.file_size , backupCount=log_config.file_num)

        # rotatating log format.
        self.formatter = logging.Formatter(log_config.log_format)
        self.handler.setFormatter(self.formatter)

        # logging level
        self.logger.setLevel(log_config.log_level)

        # set handler
        self.logger.addHandler(self.handler)

    
    def info(self, info_text):
        self.logger.info(info_text)
    
    
    def error(self, error_text):
        self.logger.error(error_text)

    
    def debug(self, debug_text):
        self.logger.debug(debug_text)

    
    def warning(self, warning_text):
        self.logger.warning(warning_text)

    
    def critical(self, critical):
        self.logger.critical(critical)

