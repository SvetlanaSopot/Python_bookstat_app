from watcher import Watcher
from database_connector import Database


database = Database()
database.initialize()
watcher = Watcher()
watcher.watch("C:/Users/sviatlana_sopat/PycharmProjects/run_project_bookstat/input",
              "C:/Users/sviatlana_sopat/PycharmProjects/run_project_bookstat/incorrect_input")
