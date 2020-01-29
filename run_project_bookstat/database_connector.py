# Imports for Database class
import sqlite3


# Bookstatbase connection, create and populate tables
class Database:
    database_name = 'C:/Users/sviatlana_sopat/PycharmProjects/run_project_bookstat/bookstatbase.db'

    def connection(self):
        conn = sqlite3.connect(self.database_name)

        return conn

    def add_book_word_counts(self, book_id, counts, counts_upp):   # Insert calculated data into a new table
        self.initialize_book_new_table(book_id)

        conn = self.connection()
        cursor = conn.cursor()

        for words in counts.keys():
            if words in counts_upp.keys():
                for word_q in words:
                    st = counts_upp[word_q]
                    #print(words, counts[words])
                    add_counts = [(words, counts[words], st)]
                    cursor.executemany("INSERT INTO \"" + book_id + "\" VALUES (?,?,?)", add_counts)

        conn.commit()

    def initialize_book_new_table(self, table_name):   # initialize of new table
        print('Create books new table with name ' + table_name)

        conn = self.connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""CREATE TABLE \"""" + table_name + """\" (word text, count INT, count_uppercase INT)""")
            conn.commit()
            print('Table ' + table_name + ' successfully created!')
        except sqlite3.OperationalError:
            print('Table ' + table_name + ' is already created!')



    def initialize(self):   # create tables in Bookststbase
        print('Initializing database structure...')

        conn = self.connection()
        cursor = conn.cursor()

        print('Create books info table')

        try:
            cursor.execute("""CREATE TABLE BOOKSINFO
                                   (book_name text, number_of_paragraph INT, number_of_words INT,
                                   number_of_letters INT, words_with_capital_letters INT, words_in_lowercase INT)
                                   """)
            conn.commit()
            cursor.execute("CREATE UNIQUE INDEX User ON BOOKSINFO(book_name, number_of_paragraph)")
            conn.commit()
            print('Initialization completed')
        except sqlite3.OperationalError:
            cursor.execute("SELECT * FROM BOOKSINFO")

    #  calculate and insert statistics
    def add_book_statistics(self, book_name, amount_of_paragraphs, number_of_words, number_of_letters,
                            words_with_capital_letters, words_in_lowercase):
        conn = self.connection()
        cursor = conn.cursor()

        cursor.execute('SELECT book_name FROM BOOKSINFO')
        book_stat = [(book_name, amount_of_paragraphs, number_of_words, number_of_letters, words_with_capital_letters,
                      words_in_lowercase)]
        try:
            cursor.executemany("INSERT INTO BOOKSINFO VALUES (?,?,?,?,?,?)", book_stat)
            conn.commit()
        except sqlite3.IntegrityError:
            pass
            print('Unique constraint: This book statistic is already exist')