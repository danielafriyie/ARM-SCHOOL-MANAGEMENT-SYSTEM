from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mbx
from Main_Window import database
from datetime import datetime as dt

A_S_M_S_D = database.ArmDatabase('armdata.db')


class ReportModuleWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # Fonts
        self.TTF = ('algerian', 30)
        self.CUF = ('MV Boli', 15)
        self.LFF = ('Arial', 13, 'bold')
        self.ALG = ("News701 BT", 10, 'bold')

        # Main Frame
        self.main_frame = Frame(self.master, bg='light green')
        self.main_frame.pack(expand=True, fill=BOTH)

        # Tool bar frame
        self.toolbar_frame = Frame(self.main_frame, bg='green')
        self.toolbar_frame.pack(side=TOP, fill=X)

        # Interaction Frame
        self.int_frame = Frame(self.main_frame, bg='light green')
        self.int_frame.pack(expand=True, fill=BOTH, pady=5)
        self.font = ('Times New Roman', 15)

        # Active button
        self.__active_btn = {'active_btn': ''}

        ##########################
        # Toolbar Buttons
        ##########################
        self.btn_frame = Frame(self.toolbar_frame)
        self.btn_frame.pack(fill=X)
        # self.sub_btn = Button(self.btn_frame, text='Subject', font=self.ALG, activebackground='black',
        #                       activeforeground='#b7f731', relief=FLAT, bd=1, bg='green', fg='white',
        #                       command=self.sub_btn_command)
        # self.sub_btn.pack(side=LEFT, expand=True, fill=X)

        self.std_btn = Button(self.btn_frame, text='Student', font=self.ALG, activebackground='black',
                              activeforeground='#b7f731', relief=FLAT, bd=1, bg='green', fg='white',
                              command=self.std_btn_command)
        self.std_btn.pack(side=LEFT, expand=True, fill=X)

        self.cls_btn = Button(self.btn_frame, text='Class', font=self.ALG, activebackground='black',
                              activeforeground='#b7f731', relief=FLAT, bd=1, bg='green', fg='white',
                              command=self.cls_btn_command)
        self.cls_btn.pack(side=LEFT, expand=True, fill=X)

    # ======== Subject Button Command =================
    # def sub_btn_command(self):
    #     self.__active_btn['active_btn'] = 'subject'
    #
    #     for widgets in self.int_frame.winfo_children():
    #         widgets.destroy()
    #     SubjectWindow(self.int_frame)
    #
    #     self.active_btn_func()

    # ======== Student Button Command =================
    def std_btn_command(self):
        self.__active_btn['active_btn'] = 'student'
        for widgets in self.int_frame.winfo_children():
            widgets.destroy()

        StudentWindow(self.int_frame)

        self.active_btn_func()

    # ======== Class Button Command =================
    def cls_btn_command(self):
        self.__active_btn['active_btn'] = 'class'

        for widgets in self.int_frame.winfo_children():
            widgets.destroy()

        ClassWindow(self.int_frame)

        self.active_btn_func()

    # Active button function
    def active_btn_func(self):

        # def sub_btn():
        #     if self.__active_btn['active_btn'] == 'subject':
        #         self.sub_btn.config(bg='white', fg='green')
        #     else:
        #         self.sub_btn.config(bg='green', fg='white')

        # sub_btn()

        def cls_btn():
            if self.__active_btn['active_btn'] == 'class':
                self.cls_btn.config(bg='white', fg='green')
            else:
                self.cls_btn.config(bg='green', fg='white')

        cls_btn()

        def std_btn():
            if self.__active_btn['active_btn'] == 'student':
                self.std_btn.config(bg='white', fg='green')
            else:
                self.std_btn.config(bg='green', fg='white')

        std_btn()


# class SubjectWindow(Frame):
#     def __init__(self, master):
#         Frame.__init__(self, master)
#
#         # Fonts
#         self.TTF = ('algerian', 30)
#         self.CUF = ('MV Boli', 15)
#         self.LFF = ('Arial', 13, 'bold')
#         self.ALG = ("News701 BT", 10, 'bold')
#         self.font = ('Times New Roman', 15)
#
#         # Images
#         self.sub_img = PhotoImage(file='Teacher\\Report\\reports.png')
#
#         self.frame = Frame(self.master, bg='light green')
#         self.frame.pack(expand=True, fill=BOTH)
#
#         self.sub_frame = Frame(self.frame, bg='green')
#         self.sub_frame.pack(expand=True, fill=BOTH)
#         self.c_frame = Frame(self.sub_frame, bg='green')
#         self.c_frame.pack(fill=X)
#         self.d_frame = Frame(self.sub_frame, bg='green')
#         self.d_frame.pack(expand=True, fill=BOTH)
#
#         self.img_label = Label(self.c_frame, image=self.sub_img, bg='green')
#         self.img_label.grid(row=0, column=0, rowspan=5)
#
#         self.term = Label(self.c_frame, text='Select Term', font=self.LFF, bg='green', fg='white')
#         self.term.grid(row=1, column=1, sticky=W)
#         self.term_entry = ttk.Combobox(self.c_frame, font=self.LFF, width=38, state='readonly')
#         self.term_entry['values'] = ['Term 1', 'Term 2', 'Term 3']
#         self.term_entry.grid(row=1, column=2, padx=5)
#
#         self.s_no = Label(self.c_frame, text='Enter Subject Code', font=self.LFF, bg='green', fg='white')
#         self.s_no.grid(row=2, column=1, sticky=W)
#         self.s_no_entry = ttk.Entry(self.c_frame, font=self.LFF, width=40)
#         self.s_no_entry.bind('<Return>', self.sub_search)
#         self.s_no_entry.grid(row=2, column=2, padx=5)
#
#         self.s_name = Label(self.c_frame, text='Subject Name', font=self.LFF, bg='green', fg='white')
#         self.s_name.grid(row=3, column=1, sticky=W)
#         self.s_name_entry = ttk.Entry(self.c_frame, font=self.LFF, width=40)
#         self.s_name_entry.grid(row=3, column=2, padx=5)
#
#         self.subjects = ttk.Treeview(self.d_frame)
#         self.subjects.pack(expand=True, fill=BOTH, side=LEFT)
#
#         self.subjects_scroll = ttk.Scrollbar(self.d_frame, command=self.subjects.yview)
#         self.subjects_scroll.pack(side=LEFT, fill=Y)
#         self.subjects.configure(yscrollcommand=self.subjects_scroll.set)
#
#         self.cols = ('s_name', 'c_s', 'e_s', 't_s', 'pos')
#         self.headings = ('Student Name', 'Class Score', 'Exams Score', 'Total Score', 'Position')
#         self.subjects.config(columns=self.cols)
#         for col in self.cols:
#             if col == 's_name':
#                 self.col_width = 200
#             elif col == 'c_s':
#                 self.col_width = 80
#             elif col == 'e_s':
#                 self.col_width = 80
#             elif col == 't_s':
#                 self.col_width = 100
#             elif col == 'pos':
#                 self.col_width = 100
#             self.subjects.column(col, width=self.col_width, anchor=CENTER)
#         counter = 0
#         for col in self.cols:
#             self.subjects.heading(col, text=self.headings[counter])
#             counter += 1
#         self.subjects.column('#0', width=100)
#         self.subjects.heading('#0', text='Student No')
#
#     # Subject search command
#     def sub_search(self, event):
#         for data in A_S_M_S_D.rep_subject(self.term_entry.get(), self.s_no_entry.get()):
#             print(data)


class ClassWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # Fonts
        self.TTF = ('algerian', 30)
        self.CUF = ('MV Boli', 15)
        self.LFF = ('Arial', 13, 'bold')
        self.ALG = ("News701 BT", 10, 'bold')
        self.font = ('Times New Roman', 15)

        # Images
        # self.cls_img = PhotoImage(file='Teacher\\Report\\class_image.png')

        self.frame = Frame(self.master, bg='light green')
        self.frame.pack(expand=True, fill=BOTH)

        self.cls_frame = Frame(self.frame, bg='green')
        self.cls_frame.pack(expand=True, fill=BOTH)
        self.c_frame = Frame(self.cls_frame, bg='green')
        self.c_frame.pack(fill=X)
        self.d_frame = Frame(self.cls_frame, bg='green')
        self.d_frame.pack(expand=True, fill=BOTH)

        # self.img_label = Label(self.c_frame, image=self.cls_img, bg='green')
        # self.img_label.grid(row=0, column=0, rowspan=5)

        self.year = Label(self.c_frame, text='Year', font=self.LFF, bg='green', fg='white')
        self.year.grid(row=1, column=0, sticky=W)
        self.year_entry = ttk.Entry(self.c_frame, font=self.LFF, width=5)
        self.year_entry.delete(0, END)
        self.year_entry.insert(END, dt.today().date().year)
        self.year_entry.grid(row=1, column=1, padx=5)

        self.term = Label(self.c_frame, text='Select Term', font=self.LFF, bg='green', fg='white')
        self.term.grid(row=1, column=2, sticky=W, pady=5)
        self.term_entry = ttk.Combobox(self.c_frame, font=self.LFF, width=8, state='readonly')
        self.term_entry['values'] = ['Term 1', 'Term 2', 'Term 3']
        self.term_entry.bind('<Return>', self.search_command)
        self.term_entry.grid(row=1, column=3, padx=5)

        cls = A_S_M_S_D.std_cls()
        cls.insert(0, '')
        self.c_code = Label(self.c_frame, text='Class', font=self.LFF, bg='green', fg='white')
        self.c_code.grid(row=1, column=4, sticky=W)
        self.c_code_entry = ttk.Combobox(self.c_frame, font=self.LFF, width=5, state='readonly')
        self.c_code_entry['values'] = cls
        self.c_code_entry.bind('<Return>', self.search_command)
        self.c_code_entry.grid(row=1, column=5, padx=5)

        self.search_btn = ttk.Button(self.c_frame, text='Search', width=10, command=self.search_btn_command)
        self.search_btn.grid(row=1, column=6, padx=5)

        self.cls_size = Label(self.c_frame, text='Class Size', font=self.LFF, bg='green', fg='white')
        self.cls_size.grid(row=1, column=7, sticky=W)
        self.cls_size_entry = ttk.Entry(self.c_frame, font=self.LFF, width=5)
        self.cls_size_entry.grid(row=1, column=8, padx=5)

        self.tea = Label(self.c_frame, text='Class Teacher', font=self.LFF, bg='green', fg='white')
        self.tea.grid(row=1, column=9, sticky=W)
        self.tea_entry = ttk.Entry(self.c_frame, font=self.LFF, width=40)
        self.tea_entry.grid(row=1, column=10, padx=5)

        self.subjects = ttk.Treeview(self.d_frame)
        self.subjects.pack(expand=True, fill=BOTH, side=LEFT)

        self.subjects_scroll = ttk.Scrollbar(self.d_frame, command=self.subjects.yview)
        self.subjects_scroll.pack(side=LEFT, fill=Y)
        self.subjects.configure(yscrollcommand=self.subjects_scroll.set)

        self.cols = ('s_name', 't_s', 'pos')
        self.headings = ('Student Name', 'Total Score', 'Position')
        self.subjects.config(columns=self.cols)
        for col in self.cols:
            # if col == 's_no':
            #     self.col_width = 100
            if col == 's_name':
                self.col_width = 200
            elif col == 't_s':
                self.col_width = 100
            elif col == 'pos':
                self.col_width = 100
            self.subjects.column(col, width=self.col_width, anchor=CENTER)
        counter = 0
        for col in self.cols:
            self.subjects.heading(col, text=self.headings[counter])
            counter += 1
        self.subjects.column('#0', width=100, anchor=CENTER)
        self.subjects.heading('#0', text='Student No')

    def search_btn_command(self):
        try:
            self.cls_size_entry.delete(0, END)
            self.tea_entry.delete(0, END)
            for d in A_S_M_S_D.rep_cls_tea(self.c_code_entry.get()):
                self.cls_size_entry.insert(END, d[1])
                for t in A_S_M_S_D.cls_teacher(d[0]):
                    self.tea_entry.insert(END, t[0])
            for children in self.subjects.get_children():
                self.subjects.delete(children)
            pos = 1
            results = A_S_M_S_D.rep_cls(self.c_code_entry.get(), self.term_entry.get(), self.year_entry.get())
            if results:
                for data in results:
                    # print(data)
                    self.subjects.insert('', END, data[1], text=data[1])
                    # self.subjects.set(data[0], self.cols[0], data[1])
                    self.subjects.set(data[1], self.cols[0], data[2])
                    self.subjects.set(data[1], self.cols[1], round(data[3], 2))
                    self.subjects.set(data[1], self.cols[2], pos)
                    pos += 1
            else:
                mbx.showinfo('Error', "What you searched for does not exist in the database!")
        except Exception:
            mbx.showinfo('Error', "Unexpected error, please try again!\nIf it persists, restart the program")
            raise

    def search_command(self, event):
        try:
            self.cls_size_entry.delete(0, END)
            self.tea_entry.delete(0, END)
            for d in A_S_M_S_D.rep_cls_tea(self.c_code_entry.get()):
                self.cls_size_entry.insert(END, d[1])
                for t in A_S_M_S_D.cls_teacher(d[0]):
                    self.tea_entry.insert(END, t[0])
            for children in self.subjects.get_children():
                self.subjects.delete(children)
            pos = 1
            results = A_S_M_S_D.rep_cls(self.c_code_entry.get(), self.term_entry.get(), self.year_entry.get())
            if results:
                for data in results:
                    # print(data)
                    self.subjects.insert('', END, data[1], text=data[1])
                    # self.subjects.set(data[0], self.cols[0], data[1])
                    self.subjects.set(data[1], self.cols[0], data[2])
                    self.subjects.set(data[1], self.cols[1], round(data[3], 2))
                    self.subjects.set(data[1], self.cols[2], pos)
                    pos += 1
            else:
                mbx.showinfo('Error', "What you searched for does not exist in the database!")
        except Exception:
            mbx.showinfo('Error', "Unexpected error, please try again!\nIf it persists, restart the program")
            raise


class StudentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # Fonts
        self.TTF = ('algerian', 30)
        self.CUF = ('MV Boli', 15)
        self.LFF = ('Arial', 13, 'bold')
        self.ALG = ("News701 BT", 10, 'bold')
        self.font = ('Times New Roman', 15)

        # Images
        self.std_img = PhotoImage(file='Teacher\\Report\\cls.jpg')

        self.frame = Frame(self.master, bg='light green')
        self.frame.pack(expand=True, fill=BOTH)

        self.std_frame = Frame(self.frame, bg='green')
        self.std_frame.pack(expand=True, fill=BOTH)
        self.c_frame = Frame(self.std_frame, bg='green')
        self.c_frame.pack(fill=X)
        self.d_frame = LabelFrame(self.std_frame, bg='light green', text='Subjects')
        self.d_frame.pack(expand=True, fill=BOTH)

        self.img_label = Label(self.c_frame, image=self.std_img, bg='green')
        self.img_label.grid(row=0, column=0, rowspan=6)

        self.term = Label(self.c_frame, text='Select Term', font=self.LFF, bg='green', fg='white')
        self.term.grid(row=1, column=1, sticky=W)
        self.term_entry = ttk.Combobox(self.c_frame, font=self.LFF, width=38, state='readonly')
        self.term_entry['values'] = ['Term 1', 'Term 2', 'Term 3']
        self.term_entry.grid(row=1, column=2, padx=5)

        self.year = Label(self.c_frame, text='Enter Year', font=self.LFF, bg='green', fg='white')
        self.year.grid(row=2, column=1, sticky=W)
        self.year_entry = ttk.Entry(self.c_frame, font=self.LFF, width=40)
        self.year_entry.delete(0, END)
        self.year_entry.insert(END, dt.today().date().year)
        self.year_entry.grid(row=2, column=2, padx=5)

        cls = A_S_M_S_D.std_cls()
        cls.insert(0, '')
        self.cls = Label(self.c_frame, text='Class', font=self.LFF, bg='green', fg='white')
        self.cls.grid(row=3, column=1, sticky=W)
        self.cls_entry = ttk.Combobox(self.c_frame, font=self.LFF, width=38, state='readonly')
        self.cls_entry['values'] = cls
        self.cls_entry.grid(row=3, column=2, padx=5)

        self.s_no = Label(self.c_frame, text='Enter Student No', font=self.LFF, bg='green', fg='white')
        self.s_no.grid(row=4, column=1, sticky=W)
        self.s_no_entry = ttk.Entry(self.c_frame, font=self.LFF, width=40)
        self.s_no_entry.bind('<Return>', self.search_command)
        self.s_no_entry.grid(row=4, column=2, padx=5)

        self.search_btn = ttk.Button(self.c_frame, text='Search', width=15, command=self.search_btn_command)
        self.search_btn.grid(row=4, column=3)

        self.s_name = Label(self.c_frame, text='Student Name', font=self.LFF, bg='green', fg='white')
        self.s_name.grid(row=5, column=1, sticky=W)
        self.s_name_entry = ttk.Entry(self.c_frame, font=self.LFF, width=40)
        self.s_name_entry.grid(row=5, column=2, padx=5)

        # pos = Label(c_frame, text='Position', font=self.LFF, bg='green', fg='white')
        # pos.grid(row=4, column=1, sticky=W)
        # pos_entry = ttk.Entry(c_frame, font=self.LFF, width=40)
        # pos_entry.grid(row=4, column=2, padx=5)

        self.subjects = ttk.Treeview(self.d_frame)
        self.subjects.pack(expand=True, fill=BOTH, side=LEFT)

        self.subjects_scroll = ttk.Scrollbar(self.d_frame, command=self.subjects.yview)
        self.subjects_scroll.pack(side=LEFT, fill=Y)
        self.subjects.configure(yscrollcommand=self.subjects_scroll.set)

        self.cols = ('code', 'name', 'c_s', 'e_s', 't_s', 'pos')
        self.headings = ('Subject Code', 'Subject Name', 'Class Score', 'Exams Score', 'Total Score', 'Position')
        self.subjects.config(columns=self.cols)
        for col in self.cols:
            if col == 'code':
                self.col_width = 100
            if col == 'name':
                self.col_width = 200
            elif col == 'c_s':
                self.col_width = 80
            elif col == 'e_s':
                self.col_width = 80
            elif col == 't_s':
                self.col_width = 100
            elif col == 'pos':
                self.col_width = 100
            self.subjects.column(col, width=self.col_width, anchor=CENTER)
        counter = 0
        for col in self.cols:
            self.subjects.heading(col, text=self.headings[counter])
            counter += 1
        self.subjects.column('#0', width=80, anchor=CENTER)
        self.subjects.heading('#0', text='ID')

    def search_command(self, event):
        try:
            self.s_name_entry.delete(0, END)
            # self.cls_entry.delete(0, END)
            for children in self.subjects.get_children():
                self.subjects.delete(children)
            if self.term_entry.get():
                for data in A_S_M_S_D.rep_std_details(self.s_no_entry.get().title()):
                    # self.cls_entry.insert(END, data[1])
                    self.s_name_entry.insert(END, data[0])
                for data in A_S_M_S_D.rep_std(
                        self.term_entry.get(), self.s_no_entry.get().title(),
                        self.year_entry.get(), self.cls_entry.get()
                ):
                    self.subjects.insert('', END, data[0], text=data[0])
                    self.subjects.set(data[0], self.cols[0], data[3])
                    self.subjects.set(data[0], self.cols[2], data[5])
                    self.subjects.set(data[0], self.cols[3], data[6])
                    self.subjects.set(data[0], self.cols[4], data[7])
                    self.subjects.set(data[0], self.cols[5], data[8])
                    for sub in A_S_M_S_D.rep_sub_name(data[3]):
                        self.subjects.set(data[0], self.cols[1], sub[0])
            else:
                mbx.showinfo('', "Select Term")
        except TclError:
            mbx.showinfo('Error', "Unexpected error, please try again")
            raise
        except Exception:
            mbx.showinfo('Error', "Unexpected error, please try again")
            raise

    def search_btn_command(self):
        try:
            self.s_name_entry.delete(0, END)
            # self.cls_entry.delete(0, END)
            for children in self.subjects.get_children():
                self.subjects.delete(children)
            if self.term_entry.get():
                for data in A_S_M_S_D.rep_std_details(self.s_no_entry.get().title()):
                    # self.cls_entry.insert(END, data[1])
                    self.s_name_entry.insert(END, data[0])
                for data in A_S_M_S_D.rep_std(
                        self.term_entry.get(), self.s_no_entry.get().title(),
                        self.year_entry.get(), self.cls_entry.get()
                ):
                    self.subjects.insert('', END, data[0], text=data[0])
                    self.subjects.set(data[0], self.cols[0], data[3])
                    self.subjects.set(data[0], self.cols[2], data[5])
                    self.subjects.set(data[0], self.cols[3], data[6])
                    self.subjects.set(data[0], self.cols[4], data[7])
                    self.subjects.set(data[0], self.cols[5], data[8])
                    for sub in A_S_M_S_D.rep_sub_name(data[3]):
                        self.subjects.set(data[0], self.cols[1], sub[0])
            else:
                mbx.showinfo('', "Select Term")
        except TclError:
            mbx.showinfo('Error', "Unexpected error, please try again")
            raise
        except Exception:
            mbx.showinfo('Error', "Unexpected error, please try again")
            raise
