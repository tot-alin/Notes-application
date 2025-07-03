
import sqlite3 as sql


class Function_sql:

    def __init__(self):
        self.test_db()
        #self.log
        # self.password = password

    def test_db(self):
        try:
            self.open_sql()
            self.curs.execute('''CREATE TABLE users (username TEXT, password TEXT)''')
            self.conn.commit()
            self.close_sql()
        except:
            self.close_sql()

    def open_sql(self):
        self.conn = sql.connect('note_db.db')
        #with self.conn:
        self.curs = self.conn.cursor()

    def close_sql(self):
        self.curs.close()
        self.conn.close()

    def insert_user(self, username, password, re_password):

        self.open_sql()
        sql_statement = 'SELECT username FROM users WHERE username=?'
        self.curs.execute(sql_statement, (username,))  # cauta in baza de date dupa parametri de inregistrare
        user_ver = self.curs.fetchall()
        self.close_sql()

        if len(user_ver) != 0 or len(username) == 0:
            return 'user invalid'
        elif password != re_password:
            return 'password != re_password'
        else:
            self.open_sql()
            sql_statement = f'CREATE TABLE {username} (date_reg TEXT, date_ref TEXT, notes_title TEXT, notes TEXT)'
            self.curs.execute(sql_statement,)
            sql_statement = 'INSERT INTO users(username, password) VALUES (?, ?)'
            self.curs.execute(sql_statement, (username, password))
            self.conn.commit()
            self.close_sql()
            return ''

    def ver_user_password(self, username, password):
        self.open_sql()
        sql_statement = f'SELECT username FROM users WHERE username = ? AND Password = ?'
        ver_user = self.curs.execute(sql_statement, (username, password)).fetchall()
        self.close_sql()
        if not ver_user:
            return ''
        else:
            return ver_user[0][0]

    def save_data(self, user_name, date_reg, date_ref, notes_title, notes):
        self.open_sql()
        sql_statement = f'INSERT INTO {user_name} (date_reg, date_ref, notes_title, notes) VALUES (?, ?, ?, ?)'
        self.curs.execute(sql_statement, (date_reg, date_ref, notes_title, notes))
        self.conn.commit()
        self.close_sql()

    def in_sort(self, user_name, sort_radio):
        if sort_radio == 'sort_regis':
            self.sql_statement_sort = f'SELECT * FROM {user_name} ORDER BY date_reg ASC'
        elif sort_radio == 'sort_date':
            self.sql_statement_sort = f'SELECT * FROM {user_name} ORDER BY date_ref ASC'
        else:
            self.sql_statement_sort = f'SELECT * FROM {user_name} ORDER BY notes_title ASC'
        self.refresh_list_box()

    def refresh_list_box(self):
        self.open_sql()
        self.curs.execute(self.sql_statement_sort)
        list_box_sql = self.curs.fetchall()
        self.close_sql()
        return list_box_sql

    def get_data_db(self, user_name, select_reg):
        sql_statement = f"SELECT * FROM {user_name} where date_reg = ?"
        self.open_sql()
        self.curs.execute(sql_statement, (select_reg,))  # cauta in baza de date dupa parametri de inregistrare
        data = self.curs.fetchall()
        self.close_sql()
        return data

    def del_record(self, user_name, select_reg):
        sql_statement = f"DELETE FROM {user_name} where date_reg = ?"
        self.open_sql()
        self.curs.execute(sql_statement, (select_reg,))
        self.conn.commit()
        self.close_sql()

    def up_record(self, user_name, select_reg, notes_title, notes):
        sql_statement = f'UPDATE {user_name} SET notes_title=?, notes=? WHERE date_reg = ?'
        self.open_sql()
        self.curs.execute(sql_statement, (notes_title, notes, select_reg))
        self.conn.commit()
        self.close_sql()



# x = Function()
# x.insert_user('lasal', 'tra', 'tra')
# print(x.ver_user_password('lasal', 'tra'))
