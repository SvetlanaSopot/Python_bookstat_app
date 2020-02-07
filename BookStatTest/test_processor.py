import glob  # модуль glob находит все пути совпадающие с шаблоном, в нашем случае '/*.json'

class TestProcessor:   # основной исполняющий класс, сердце фреймворка
    def __init__(self, config, connector, logger):   # отдаём объекты с которыми будем работать и сохраняем их в переменные
        self.config = config
        self.connector = connector
        self.logger = logger

    def process(self):  #  мы хотим получить список всех файлов с тестовыми датами - возвращает список всех файлов для процесса тестирования
        test_data_files = self.check_test_folder()

        for f in test_data_files:
            self.do_testing(f)

    def check_test_folder(self):
        test_data_folder = self.config.get_test_data_folder()
        return [f for f in glob.glob(test_data_folder + '/*.json', recursive=True)]

    def do_testing(self, file_name):   # процесс тестинга, принимает на вход имя файла
        self.logger.start_test(file_name)

        with open(file_name) as f:
            test_data = eval(f.read())

        for test in test_data['tests']:
            self.logger.start_case(test['name'])  # читаем имя теста, когда записываем в резалт

            query = test['query']
            expected_result = test['expected']
            actual_result = self.connector.execute(query)

            if actual_result == expected_result:
                self.logger.add_pass(query, actual_result)
            else:
                self.logger.add_fail(query, actual_result, expected_result)


