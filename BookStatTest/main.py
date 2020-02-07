from sys import argv
from configurator import Configurator
from connector import Connector
from resulting import Result
from test_processor import TestProcessor


def run():
    config = Configurator(argv[1])  # получает на вход переменную окружения dev (параметр кот мы читаем при запуске приложения)

    database_url = config.get_database_url()  # переменная находит путь к базе

    connector = Connector(database_url)    # соединяемся с базой

    logger = Result()

    test_processor = TestProcessor(config, connector, logger)   # в питоне всё объекты и поэтому мы одному объекту отдаём в обработку другие объекты с которыми будем работать
    test_processor.process()

    logger.finish_test()

if __name__ == '__main__':  #используется если мы хотим что то запустить, только если запустим main с помощью питона будет выполняться
    run()
