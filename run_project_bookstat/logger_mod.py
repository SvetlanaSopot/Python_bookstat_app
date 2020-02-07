import logging
# настройка логгера
logging.basicConfig(filename="file_log.log", filemode='w',
                    format='%(asctime)s-%(process)d-%(levelname)s-%(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
