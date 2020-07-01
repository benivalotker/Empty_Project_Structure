'''
    log rotation configuration
'''
win_log_path = "./logging_pkg/logs/"

unix_log_path = "/opt/logs/"

log_format = "%(asctime)s - %(levelname)s - %(message)s"

log_level = "INFO"

file_size = 10*1024*1024 # 10mb

file_num = 5