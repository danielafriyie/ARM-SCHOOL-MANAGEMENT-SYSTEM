"""

MAIN APPLICATION INTERFACE

"""

__app_name__ = "ARM School Management System"
__version__ = "1.0"
__author__ = "Afriyie Daniel"
__email__ = "afriyiedaniel1@outlook.com"
__status__ = "Development"
__description__ = "School Management System Project"

from tkinter import *
from tkinter import messagebox as mbx
from Admin.TeachersModule import teachers_module
from Admin.StudentModule import student_module
from Admin.ClassModule import class_module
from Admin.TimeTableModule import time_table_module
from Admin.SubjectModule import subject_module
from Teacher.ClassList import class_list_module
from Teacher.ClassSchedule import class_schedule_module
from Teacher.Subject import subject_module_teacher
from Teacher.Scores import scores_module
from Teacher.Report import report_module
from . import database
from datetime import datetime as dt

A_S_M_S_D = database.ArmDatabase('.\\armdata.db')


class ArmSchoolMgtSys(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title(__app_name__ + " " + __version__)
        self.master.iconbitmap(default="images\\favicon.ico")
        self.master.state('zoomed')
        self.master.protocol('WM_DELETE_WINDOW', self.exit_command)

        # Fonts
        self.ALG = ("News701 BT", 10, 'bold')
        self.TTF = ('algerian', 30)
        self.CUF = ('MV Boli', 15)
        self.LFF = ('Arial', 10)
        self.BGL = ('News701 BT', 50)

        # Toolbar Frame
        self.toolbar = Frame(master, bg='green')
        self.toolbar.pack(fill=X)

        # School Name
        self.toolbar_title = Label(self.toolbar, text=__app_name__,
                                   bg='green', font=self.TTF, fg='white')
        self.toolbar_title.pack(anchor=N, pady=20)

        # Modules Frame
        self.__modules = LabelFrame(master, text='Modules', font=self.LFF, bg="light green")
        self.__modules.pack(anchor=W, side=LEFT, fill=Y)

        # Navigation Pane Frame
        self.nav_pane = Frame(self.__modules)
        self.nav_pane.pack(anchor=W, side=LEFT, fill=Y)

        # Interaction Window Frame
        self.interaction_window = LabelFrame(master, bg='light green', font=self.LFF)
        self.interaction_window.pack(side=LEFT, anchor=W, expand=True, fill=BOTH)
        # Set Subject as the default home module
        self.interaction_window.config(text='Subject Module')
        subject_module.SubjectModuleWindow(self.interaction_window)
        self.__active_module = {'current-module': ''}

        # Background Image / Label
        # self.main_image = PhotoImage(file='Main_Window\\t_logo.png').subsample(1, 1)
        # self.window_frame = Frame(self.interaction_window)
        # self.window_frame.pack(expand=True, fill=BOTH)
        # self.background_image = Label(self.window_frame, text="Background Image", image=self.main_image)
        # self.background_image.image = self.main_image
        # self.background_image.pack(expand=True, fill=BOTH)
        # self.background_label = Label(self.window_frame,
        #                               text='ARM SCHOOL MANAGEMENT SYSTEM\n\nINFUSED WITH\n\n'
        #                                    'ABOVE\n\nTOMORROW\n\nAND BEYOND',
        #                               bg='green', fg='white', font=self.BGL)
        # self.background_label.pack(expand=True, fill=BOTH)

        # Admin Panel Frame
        self.admin_frame = LabelFrame(self.nav_pane, font=self.LFF,
                                      bg='light green', fg='black')
        self.admin_frame.pack(expand=True, fill=Y)

        # Teacher Panel Frame
        self.teacher_frame = LabelFrame(self.nav_pane, font=self.LFF,
                                        bg='light green', fg='black')
        self.teacher_frame.pack(expand=True, fill=Y)

        # Accountant Panel Frame
        # self.accountant_frame = LabelFrame(self.nav_pane, text='Accountant', font=self.LFF,
        #                                    bg='light green', fg='black')
        # self.accountant_frame.pack(expand=True, fill=Y)

        # About and Log Out Frame
        self.help_frame = LabelFrame(self.nav_pane, text='Help', font=self.LFF,
                                     bg='light green', fg='black')
        self.help_frame.pack(fill=Y, ipady=20)

        # Toolbar Buttons
        # self.teacher = Button(self.toolbar, text="Teacher", width=35, height=3)
        # self.teacher.grid(row=0, column=0)
        #
        # self.accountant = Button(self.toolbar, text="Accountant", width=35, height=3)
        # self.accountant.grid(row=0, column=1)
        #
        # self.admin = Button(self.toolbar, text="Administrator", width=35, height=3)
        # self.admin.grid(row=0, column=2)

        ''' Navigation Pane Buttons '''
        # Admin Panel
        self.teachers = Button(self.admin_frame, text='Teachers', width=14, font=self.ALG, activebackground='black',
                               activeforeground='#b7f731', relief=FLAT, bd=1, command=self.teachers_module_window,
                               bg='green', fg='white')
        # self.users.bind("<Button-1>", self.active_module_func)
        self.teachers.pack(expand=True, fill=Y)

        self.students = Button(self.admin_frame, text='Students', width=14, font=self.ALG,
                               bg='green', fg='white', activebackground='black',
                               activeforeground='#b7f731', relief=FLAT, bd=1, command=self.student_module_window)
        self.students.pack(expand=True, fill=Y)

        self.clss = Button(self.admin_frame, text='Add/Edit Class', width=14, font=self.ALG,
                           bg='green', fg='white', activebackground='black',
                           activeforeground='#b7f731', relief=FLAT, bd=1, command=self.class_module_window)
        self.clss.pack(expand=True, fill=Y)

        self.time_table = Button(self.admin_frame, text='Time Table', width=14, font=self.ALG,
                                 bg='green', fg='white', activebackground='black',
                                 activeforeground='#b7f731', relief=FLAT, bd=1, command=self.time_table_module_window)
        self.time_table.pack(expand=True, fill=Y)

        self.subjects = Button(self.admin_frame, text='Add/Edit Subjects', width=14, font=self.ALG,
                               bg='white', fg='green', activebackground='black',
                               activeforeground='#b7f731', relief=FLAT, bd=1, command=self.subject_module_window)
        self.subjects.pack(expand=True, fill=Y)

        # Teacher Panel
        self.class_list = Button(self.teacher_frame, text='Class List', width=14, font=self.ALG,
                                 bg='green', fg='white', activebackground='black',
                                 activeforeground='#b7f731', relief=FLAT, bd=1, command=self.class_list_module_window)
        self.class_list.pack(expand=True, fill=Y)
        self.scores = Button(self.teacher_frame, text='Scores', width=14, font=self.ALG,
                             bg='green', fg='white', activebackground='black',
                             command=self.scores_module_window,
                             activeforeground='#b7f731', relief=FLAT, bd=1)
        self.scores.pack(expand=True, fill=Y)
        self.class_schedule = Button(self.teacher_frame, text='Class Schedule', width=14, font=self.ALG,
                                     bg='green', fg='white', activebackground='black',
                                     command=self.class_schedule_module_window,
                                     activeforeground='#b7f731', relief=FLAT, bd=1)
        self.class_schedule.pack(expand=True, fill=Y)
        self.teacher_subject = Button(self.teacher_frame, text='Subject', width=14, font=self.ALG,
                                      bg='green', fg='white', activebackground='black',
                                      command=self.subject_module_window_teacher,
                                      activeforeground='#b7f731', relief=FLAT, bd=1)
        self.teacher_subject.pack(expand=True, fill=Y)
        self.teacher_report = Button(self.teacher_frame, text='Report', width=14, font=self.ALG,
                                     bg='green', fg='white', activebackground='black',
                                     command=self.report_module_window,
                                     activeforeground='#b7f731', relief=FLAT, bd=1)
        self.teacher_report.pack(expand=True, fill=Y)

        '''# Accountant Panel
        self.std_list = Button(self.accountant_frame, text='Student List', width=14, font=self.ALG,
                               bg='green', fg='white')
        self.std_list.pack(expand=True, fill=Y)
        self.fee_payment = Button(self.accountant_frame, text='Fee Payment', width=14, font=self.ALG,
                                  bg='green', fg='white')
        self.fee_payment.pack(expand=True, fill=Y)
        self.acc_report = Button(self.accountant_frame, text='Report', width=14, font=self.ALG,
                                 bg='green', fg='white')
        self.acc_report.pack(expand=True, fill=Y)'''

        # Help Panel
        # self.log_out = Button(self.a_l_frame, text='Log Out', width=14, font=self.ALG,
        #                       bg='green', fg='white', activebackground='black',
        #                       activeforeground='#b7f731', relief=FLAT, bd=1)
        # self.log_out.pack(expand=True, fill=Y)
        self.about = Button(self.help_frame, text='About', width=14, font=self.ALG,
                            bg='green', fg='white', activebackground='black',
                            activeforeground='#b7f731', relief=FLAT, bd=1, command=self.about_window)
        self.about.pack(expand=True, fill=Y)

    def exit_command(self):
        query = mbx.askyesno("Confirm Exit", "Do you want to exit Arm School Management System")
        if query is True:
            A_S_M_S_D.close_database()
            self.master.destroy()

    def about_window(self):
        """ About Window """
        window = Toplevel()
        window.title("About")
        window.resizable(height=False, width=False)
        window.config(background='green')
        window.grab_set()

        about_label = Label(window, font=("Times New Roman", 16),
                            text="Arm School Management System 1.0\nMade by: Afriyie Daniel"
                                 "\n\n\nEmail: afriyiedaniel1@outlook.com\nTel: 0543833501 / 0502155025\n"
                                 "The Drive to Develop\n\nYou can send your reviews\nAnd recommendations to\n"
                                 "afriyiedaniel1@outlook.com\n\n", bg='green', fg='white').grid(row=1, column=1)

        about_label_2 = Label(window, text=f"© Copyright 2019 - {dt.today().year} GranSec Technologies",
                              font=("Monotype Corsiva", 12), bg='green', fg='white').grid(row=2, column=1)

        # about_btn = Button(window, text="Ok", width=15, relief=FLAT, command=window.destroy, bg='green', fg='white')
        # about_btn.grid(row=3, column=1)

    ###########################################
    #           ADMIN MODULE
    ##########################################
    def teachers_module_window(self):
        for widgets in self.interaction_window.winfo_children():
            widgets.destroy()
        self.interaction_window.config(text='Teachers Module')
        self.__active_module['current-module'] = 'Teachers Module'
        teachers_module.TeachersModuleWindow(self.interaction_window)
        self.active_module_func()

    def student_module_window(self):
        for widgets in self.interaction_window.winfo_children():
            widgets.destroy()
        self.interaction_window.config(text='Student Module')
        self.__active_module['current-module'] = 'Student Module'
        student_module.StudentModuleWindow(self.interaction_window)
        self.active_module_func()

    def class_module_window(self):
        for widgets in self.interaction_window.winfo_children():
            widgets.destroy()
        self.interaction_window.config(text='Class Module')
        self.__active_module['current-module'] = 'Class Module'
        class_module.ClassModuleWindow(self.interaction_window)
        self.active_module_func()

    def time_table_module_window(self):
        for widgets in self.interaction_window.winfo_children():
            widgets.destroy()
        self.interaction_window.config(text='Time Table Module')
        self.__active_module['current-module'] = 'Time Table Module'
        time_table_module.TimeTableModuleWindow(self.interaction_window)
        self.active_module_func()

    def subject_module_window(self):
        for widgets in self.interaction_window.winfo_children():
            widgets.destroy()
        self.interaction_window.config(text='Subject Module')
        self.__active_module['current-module'] = 'Subject Module'
        subject_module.SubjectModuleWindow(self.interaction_window)
        self.active_module_func()

    ##########################################
    #           TEACHERS MODULE
    ##########################################
    def class_list_module_window(self):
        for widgets in self.interaction_window.winfo_children():
            widgets.destroy()
        self.interaction_window.config(text='Class List Module')
        self.__active_module['current-module'] = 'Class List Module'
        class_list_module.ClassListModuleWindow(self.interaction_window)
        self.active_module_func()

    def class_schedule_module_window(self):
        for widgets in self.interaction_window.winfo_children():
            widgets.destroy()
        self.interaction_window.config(text='Class Schedule Module')
        self.__active_module['current-module'] = 'Class Schedule Module'
        class_schedule_module.ClassScheduleModuleWindow(self.interaction_window)
        self.active_module_func()

    def subject_module_window_teacher(self):
        for widgets in self.interaction_window.winfo_children():
            widgets.destroy()
        self.interaction_window.config(text='Subject (Teacher) Module')
        self.__active_module['current-module'] = 'Subject (Teacher) Module'
        subject_module_teacher.SubjectModuleWindow(self.interaction_window)
        self.active_module_func()

    def scores_module_window(self):
        for widgets in self.interaction_window.winfo_children():
            widgets.destroy()
        self.interaction_window.config(text='Scores Module')
        self.__active_module['current-module'] = 'Scores Module'
        scores_module.ScoresModuleWindow(self.interaction_window)
        self.active_module_func()

    def report_module_window(self):
        for widgets in self.interaction_window.winfo_children():
            widgets.destroy()
        self.interaction_window.config(text='Report Module')
        self.__active_module['current-module'] = 'Report Module'
        report_module.ReportModuleWindow(self.interaction_window)
        self.active_module_func()

    ''' ACTIVE MODULE FUNCTION '''

    def active_module_func(self):
        """

            ACTIVE MODULE FUNCTION, MAKES CURRENT MODULE BUTTON BACKGROUND
            WHITE AND FOREGROUND GREEN

        """

        def teachers_module_func():
            if self.__active_module['current-module'] == 'Teachers Module':
                self.teachers.config(bg='white', fg='green')
            else:
                self.teachers.config(bg='green', fg='white')

        teachers_module_func()

        def students_module_func():
            if self.__active_module['current-module'] == 'Student Module':
                self.students.config(bg='white', fg='green')
            else:
                self.students.config(bg='green', fg='white')

        students_module_func()

        def class_module_func():
            if self.__active_module['current-module'] == 'Class Module':
                self.clss.config(bg='white', fg='green')
            else:
                self.clss.config(bg='green', fg='white')

        class_module_func()

        def time_module_func():
            if self.__active_module['current-module'] == 'Time Table Module':
                self.time_table.config(bg='white', fg='green')
            else:
                self.time_table.config(bg='green', fg='white')

        time_module_func()

        def subject_module_func():
            if self.__active_module['current-module'] == 'Subject Module':
                self.subjects.config(bg='white', fg='green')
            else:
                self.subjects.config(bg='green', fg='white')

        subject_module_func()

        def class_list_module_func():
            if self.__active_module['current-module'] == 'Class List Module':
                self.class_list.config(bg='white', fg='green')
            else:
                self.class_list.config(bg='green', fg='white')

        class_list_module_func()

        def class_schedule_module_func():
            if self.__active_module['current-module'] == 'Class Schedule Module':
                self.class_schedule.config(bg='white', fg='green')
            else:
                self.class_schedule.config(bg='green', fg='white')

        class_schedule_module_func()

        def subject_module_func_teacher():
            if self.__active_module['current-module'] == 'Subject (Teacher) Module':
                self.teacher_subject.config(bg='white', fg='green')
            else:
                self.teacher_subject.config(bg='green', fg='white')

        subject_module_func_teacher()

        def scores_module_func():
            if self.__active_module['current-module'] == 'Scores Module':
                self.scores.config(bg='white', fg='green')
            else:
                self.scores.config(bg='green', fg='white')

        scores_module_func()

        def report_module_func():
            if self.__active_module['current-module'] == 'Report Module':
                self.teacher_report.config(bg='white', fg='green')
            else:
                self.teacher_report.config(bg='green', fg='white')

        report_module_func()
