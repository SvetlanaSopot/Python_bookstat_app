# Imports for Watcher

from statistics_calculator import StatisticsCalculator
import os
import shutil
import time


class Watcher:   # Scanning input directory for new .fb2 files, moving incorrect files into incorrect_input directory
    def rchop(self, string, ending):
        if string.endswith(ending):
            return string[:-len(ending)]
        return string

    # Moving not .fb2 files into incorrect_input directory
    def watch(self, directory, wrong_files_directory):
        statistics_calculator = StatisticsCalculator()
        processed_files = []

        #  Process of scanning repeated in 5 second
        while True:
            print('Scanning directory ' + directory + ' for new fb2 files...')

            for node in os.listdir(directory):
                if not node.endswith(".fb2"):
                    print('Wrong file detected' + node + ', trying to move wrong file into directory '
                          + wrong_files_directory)
                    shutil.move(os.path.join(directory, node),
                                os.path.join(wrong_files_directory, node))
                elif node not in processed_files:

                    print('New .fb2 file detected ' + node)

                    statistics_calculator.calculate_book_statistic(directory + '/' + node)
                    statistics_calculator.calculate_book_word_count(self.rchop(node, '.fb2'), directory + '/' + node)
                    processed_files.append(node)

            time.sleep(5)

