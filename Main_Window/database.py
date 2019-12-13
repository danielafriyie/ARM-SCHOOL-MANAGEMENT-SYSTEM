import sqlite3 as sq
from sqlite3 import Error


class ArmDatabase:
    def __init__(self, db):
        self.connection = sq.connect(db)
        self.cursor = self.connection.cursor()
        try:
            # Teachers Table
            self.cursor.execute(
                'CREATE TABLE IF NOT EXISTS teachers(id INTEGER PRIMARY KEY AUTOINCREMENT, date DATE NOT NULL'
                ', name VARCHAR(200) NOT NULL'
                ', phone VARCHAR(20) NOT NULL UNIQUE, email VARCHAR(100) NOT NULL UNIQUE'
                ', assign_sub TEXT  NOT NULL, address VARCHAR(100) NOT NULL'
                ', res VARCHAR(100) NOT NULL, loc VARCHAR(100) NOT NULL, land_mrk VARCHAR(100)'
                ', nationality VARCHAR(100) NOT NULL'
                ', reg VARCHAR(100) NOT NULL, t_no VARCHAR(100) UNIQUE NOT NULL)'
            )
            # Students Table
            self.cursor.execute(
                'CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY AUTOINCREMENT, date DATE NOT NULL'
                ', name VARCHAR(200) NOT NULL'
                ', phone VARCHAR(20), email VARCHAR(100), gender TEXT NOT NULL, dob VARCHAR(100) NOT NULL'
                ', cls VARCHAR(100) REFERENCES class(code) NOT NULL'
                ', p_g VARCHAR(200) NOT NULL, p_g_phone VARCHAR(20) NOT NULL, address VARCHAR(100) NOT NULL'
                ', res VARCHAR(100) NOT NULL, loc VARCHAR(100) NOT NULL'
                ', land_mrk VARCHAR(100), nationality VARCHAR(100) NOT NULL, reg VARCHAR(100) NOT NULL'
                ', s_no VARCHAR(100) UNIQUE NOT NULL)'
            )
            # Class Table
            self.cursor.execute(
                'CREATE TABLE IF NOT EXISTS class(id INTEGER PRIMARY KEY AUTOINCREMENT, date DATE NOT NULL, '
                'name VARCHAR(200) NOT NULL'
                ', code VARCHAR(20) UNIQUE NOT NULL, a_teacher VARCHAR(200) REFERENCES teachers(t_no) NOT NULL'
                ', assistant_t TEXT, size DEFAULT 0 NOT NULL)'
            )
            # Time Table
            self.cursor.execute(
                'CREATE TABLE IF NOT EXISTS timetable(id INTEGER PRIMARY KEY AUTOINCREMENT, date DATE NOT NULL'
                ', a_teacher VARCHAR(200) REFERENCES teachers(t_no) NOT NULL'
                ', time TIME NOT NULL, day VARCHAR(15) NOT NULL'
                ', a_sub VARCHAR(100) REFERENCES subjects(code) NOT NULL'
                ', a_cls VARCHAR(100) REFERENCES class(code) NOT NULL)'
            )
            # Subject Table
            self.cursor.execute(
                'CREATE TABLE IF NOT EXISTS subjects(id INTEGER PRIMARY KEY AUTOINCREMENT, date DATE NOT NULL'
                ', name VARCHAR(200) NOT NULL'
                ', code VARCHAR(20) UNIQUE NOT NULL)'
            )
            # Scores Table
            self.cursor.execute(
                'CREATE TABLE IF NOT EXISTS scores(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, date DATE'
                ', s_name REFERENCES students(name) NOT NULL '
                ', s_no REFERENCES students(s_no) NOT NULL'
                ', cls REFERENCES class(code) NOT NULL'
                ', subject REFERENCES subjects(code) NOT NULL'
                ', term VARCHAR(20), c_score FLOAT, e_score FLOAT, t_score FLOAT, year)'
            )
        except Error:
            raise
        except Exception:
            raise

    try:
        #####################################
        #        SUBJECTS MODULE
        #####################################
        def sub_add_new(self, date, name, code):
            self.cursor.execute(
                'INSERT INTO subjects VALUES (NULL,?,?,?)', (date, name, code)
            )
            self.connection.commit()

        def sub_view_all(self):
            self.cursor.execute('SELECT * FROM subjects')
            return self.cursor.fetchall()

        def sub_delete(self, _id):
            self.cursor.execute('DELETE FROM subjects WHERE id=?', (_id,))
            self.connection.commit()

        def sub_highlight_select(self, _id):
            self.cursor.execute('SELECT * FROM subjects WHERE id=?', (_id,))
            return self.cursor.fetchall()

        def sub_update(self, __id, name, code):
            self.cursor.execute('UPDATE subjects SET name=?, code=? WHERE id=?', (name, code, __id))
            self.connection.commit()

        def sub_select(self):
            self.cursor.execute('SELECT code FROM subjects')
            return self.cursor.fetchall()

        #######################################
        #       TEACHERS MODULE
        #######################################
        def tea_add_new(self, date, name, phone, email, a_subject, address, res, loc, l_mrk, nat, reg, t_no):
            self.cursor.execute(
                'INSERT INTO teachers VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?)',
                (date, name, phone, email, a_subject, address, res, loc, l_mrk, nat, reg, t_no)
            )
            self.connection.commit()

        def tea_t_no_gen(self):
            self.cursor.execute('SELECT id FROM teachers ORDER BY id DESC LIMIT 1')
            return self.cursor.fetchall()

        def tea_view_all(self):
            self.cursor.execute('SELECT t_no, name FROM teachers ORDER BY name')
            return self.cursor.fetchall()

        def tea_delete(self, t_no):
            self.cursor.execute('DELETE FROM teachers WHERE t_no=?', (t_no,))
            self.connection.commit()

        def tea_get_selected_row(self, t_no):
            self.cursor.execute('SELECT * FROM teachers WHERE t_no=?', (t_no,))
            return self.cursor.fetchall()

        def tea_sub_select(self, t_no):
            self.cursor.execute('SELECT assign_sub FROM teachers WHERE t_no=?', (t_no,))
            return self.cursor.fetchall()

        def tea_update(self, name, phone, email, a_subject, address, res, loc, l_mrk, nat, reg, t_no):
            self.cursor.execute(
                'UPDATE teachers SET name=?, phone=?, email=?, assign_sub=?, address=?, res=?, loc=?, land_mrk=?'
                ', nationality=?, reg=? WHERE t_no=?',
                (name, phone, email, a_subject, address, res, loc, l_mrk, nat, reg, t_no)
            )
            self.connection.commit()

        def tea_t_no(self):
            self.cursor.execute('SELECT t_no FROM teachers')
            return self.cursor.fetchall()

        def tea_search(self, t_no):
            self.cursor.execute('SELECT t_no FROM teachers WHERE t_no=?', (t_no,))
            return self.cursor.fetchall()

        def tea_t_data(self, t_no):
            self.cursor.execute('SELECT * FROM teachers WHERE t_no=?', (t_no,))
            return self.cursor.fetchall()

        def tea_c_list(self, code):
            self.cursor.execute('SELECT * FROM class WHERE a_teacher=?', (code,))
            return self.cursor.fetchall()

        def tea_c_schedule(self, t_no):
            self.cursor.execute('SELECT * FROM timetable WHERE a_teacher=?', (t_no,))
            return self.cursor.fetchall()

        def tea_c_sub(self, code):
            self.cursor.execute('SELECT * FROM subjects WHERE code=?', (code,))
            return self.cursor.fetchall()

        ###################################################
        #           CLASS MODULE
        ###################################################
        def cls_add_new(self, date, name, code, a_t, as_t, size):
            self.cursor.execute('INSERT INTO class VALUES (NULL, ?,?,?,?,?,?)', (date, name, code, a_t, as_t, size))
            self.connection.commit()

        def cls_view_all(self):
            self.cursor.execute('SELECT * FROM class')
            return self.cursor.fetchall()

        def cls_teacher(self, t_no):
            self.cursor.execute('SELECT name FROM teachers WHERE t_no=?', (t_no,))
            return self.cursor.fetchall()

        def cls_get_selected_row(self, __id):
            self.cursor.execute('SELECT * FROM class WHERE id=?', (__id,))
            return self.cursor.fetchall()

        def cls_update(self, name, code, a_t, as_t, __id):
            self.cursor.execute('UPDATE class SET name=?, code=?, a_teacher=?, assistant_t=? WHERE id=?',
                                (name, code, a_t, as_t, __id))
            self.connection.commit()

        def cls_delete(self, __id):
            self.cursor.execute('DELETE FROM class WHERE id=?', (__id,))
            self.connection.commit()

        ##############################################
        #           STUDENTS MODULE
        ##############################################
        def std_cls(self):
            self.cursor.execute('SELECT code FROM class')
            return self.cursor.fetchall()

        def std_add_new(self, date, name, phone, email, gender, dob, cls, p_g, p_g_no, address, res, loc, l_mrk, nat,
                        reg, s_no):
            self.cursor.execute('INSERT INTO students VALUES (NULL, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                                (
                                    date, name, phone, email, gender, dob, cls, p_g, p_g_no, address, res, loc, l_mrk,
                                    nat, reg, s_no
                                ))
            self.connection.commit()

        def std_s_no(self):
            self.cursor.execute('SELECT id FROM students ORDER BY id DESC LIMIT 1')
            return self.cursor.fetchall()

        def std_view_all(self, s_no):
            self.cursor.execute('SELECT * FROM students WHERE s_no=?', (s_no,))
            return self.cursor.fetchall()

        def std_refresh(self):
            self.cursor.execute('SELECT s_no FROM students')
            return self.cursor.fetchall()

        def std_update(self, name, phone, email, gender, dob, cls, p_g, p_g_no, address, res, loc, l_mrk, nat,
                       reg, s_no):
            self.cursor.execute(
                'UPDATE students SET name=?, phone=?, email=?, gender=?, dob=?, cls=?, p_g=?, p_g_phone=?,'
                'address=?, res=?, loc=?, land_mrk=?, nationality=?, reg=? WHERE s_no=?',
                (name, phone, email, gender, dob, cls, p_g, p_g_no, address, res, loc, l_mrk, nat,
                 reg, s_no))
            self.connection.commit()

        def std_delete(self, s_no):
            self.cursor.execute('DELETE FROM students WHERE s_no=?', (s_no,))
            self.connection.commit()

        def std_search(self, s_no):
            self.cursor.execute('SELECT s_no FROM students WHERE s_no=?', (s_no,))
            return self.cursor.fetchall()

        def std_class_size_increase(self, c_code):
            self.cursor.execute('UPDATE class SET size=size+1 WHERE code=?', (c_code,))
            self.connection.commit()

        ##############################################
        #           TIME TABLE MODULE
        ##############################################
        def tim_add_new(self, date, tea, time, day, sub, cls):
            self.cursor.execute('INSERT INTO timetable VALUES (NULL, ?,?,?,?,?,?)', (date, tea, time, day, sub, cls))
            self.connection.commit()

        def tim_view_all(self):
            self.cursor.execute('SELECT * FROM timetable')
            return self.cursor.fetchall()

        def tim_teacher(self):
            self.cursor.execute('SELECT t_no FROM teachers')
            return self.cursor.fetchall()

        def tim_class(self):
            self.cursor.execute('SELECT code FROM class')
            return self.cursor.fetchall()

        def tim_subject(self):
            self.cursor.execute('SELECT code FROM subjects')
            return self.cursor.fetchall()

        def tim_sub_name(self, name):
            self.cursor.execute('SELECT name FROM subjects WHERE code=?', (name,))
            return self.cursor.fetchall()

        def tim_get_selected_row(self, __id):
            self.cursor.execute('SELECT * FROM timetable WHERE id=?', (__id,))
            return self.cursor.fetchall()

        def tim_update(self, tea, time, day, sub, cls, __id):
            self.cursor.execute('UPDATE timetable SET a_teacher=?, time=?, day=?, a_sub=?, a_cls=? WHERE id=?',
                                (tea, time, day, sub, cls, __id))
            self.connection.commit()

        def tim_delete(self, __id):
            self.cursor.execute('DELETE FROM timetable WHERE id=?', (__id,))
            self.connection.commit()

        ##############################################
        #           SCORES MODULE
        ##############################################
        def sco_all_students(self):
            self.cursor.execute('SELECT s_no, name FROM students ORDER BY name')
            return self.cursor.fetchall()

        def sco_cls_search(self, code):
            self.cursor.execute('SELECT s_no, name FROM students WHERE cls=?', (code,))
            return self.cursor.fetchall()

        def sco_s_no_search(self, s_no):
            self.cursor.execute('SELECT s_no, name FROM students WHERE s_no=?', (s_no,))
            return self.cursor.fetchall()

        def sco_s_name_search(self, name):
            self.cursor.execute('SELECT s_no, name FROM students WHERE name=?', (name,))
            return self.cursor.fetchall()

        def sco_add_new(self, date, s_name, s_no, cls, sub, term, c_score, e_score, t_score, year):
            self.cursor.execute('INSERT INTO scores VALUES(NULL, ?,?,?,?,?,?,?,?,?,?)', (
                date, s_name, s_no, cls, sub, term, c_score, e_score, t_score, year
            ))
            self.connection.commit()

        def sco_std_row(self, s_no):
            self.cursor.execute('SELECT name, s_no, cls FROM students WHERE s_no=?', (s_no,))
            return self.cursor.fetchall()

        def sco_refresh(self):
            self.cursor.execute('SELECT * FROM scores')
            return self.cursor.fetchall()

        def scores_row(self, __id):
            self.cursor.execute('SELECT * FROM scores WHERE id=?', (__id,))
            return self.cursor.fetchall()

        def sco_delete(self, __id):
            self.cursor.execute('DELETE FROM scores WHERE id=?', (__id,))
            self.connection.commit()

        def sco_update(self, __id, sub, term, c_score, e_score, t_score, year):
            self.cursor.execute('UPDATE scores SET subject=?, term=?, c_score=?, e_score=?, t_score=?, year=? '
                                'WHERE id=?', (
                                    sub, term, c_score, e_score, t_score, year, __id))
            self.connection.commit()

        def sco_std_data(self, s_no):
            self.cursor.execute('SELECT * FROM scores WHERE s_no=?', (s_no,))
            return self.cursor.fetchall()

        #############################################
        #           REPORT MODULE
        #############################################
        def rep_std(self, term, s_no, year, cls):
            # Temporary table for storing student results
            self.cursor.execute('DROP TABLE IF EXISTS s_results')
            self.cursor.execute(
                'CREATE TABLE s_results AS SELECT id, s_name, s_no, subject, term, c_score, e_score, t_score, '
                'RANK () OVER (PARTITION BY subject ORDER BY t_score DESC) position '
                'FROM scores WHERE year=? AND term=? AND cls=?'
                , (year, term, cls)
            )
            self.cursor.execute('SELECT * FROM s_results WHERE s_no=?', (s_no,))
            return self.cursor.fetchall()

        def rep_std_details(self, s_no):
            self.cursor.execute('SELECT name, cls FROM students WHERE s_no=?', (s_no,))
            return self.cursor.fetchall()

        def rep_sub_name(self, code):
            self.cursor.execute('SELECT name FROM subjects WHERE code=?', (code,))
            return self.cursor.fetchall()

        def rep_cls(self, code, term, year):
            self.cursor.execute(
                'SELECT id, s_no, s_name, sum(t_score) AS overall_score '
                'FROM scores GROUP BY s_no HAVING cls=? AND term=? AND year=? ORDER BY overall_score DESC',
                (code, term, year))
            return self.cursor.fetchall()

        def rep_cls_tea(self, code):
            self.cursor.execute('SELECT a_teacher, size FROM class WHERE code=?', (code,))
            return self.cursor.fetchall()

    except Exception:
        raise

    ##############################################
    #           CLOSES THE DATABASE
    ##############################################
    def close_database(self):
        self.connection.close()
