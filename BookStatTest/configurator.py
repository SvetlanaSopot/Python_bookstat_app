
class Configurator:  # конфигуратор связывается с конфигом и в нашем случае мы этот файл открываем, анализируем и в зависимости от метода возвращаем
    def __init__(self, environment):
        with open('config.json') as f:
            self.config = eval(f.read())  # представляет в виде словаря
        self.config = self.config[environment]

    def get_database_url(self):      # путь к базе
        return self.config['database']   # возвращает значение из конфига по ключу database

    def get_test_data_folder(self):    # путь к папке с тестами
        return self.config['test_data_folder']
