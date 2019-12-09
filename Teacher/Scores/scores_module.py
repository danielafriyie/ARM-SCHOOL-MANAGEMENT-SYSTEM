from tkinter import *
from tkinter import ttk
from datetime import datetime as dt
from Main_Window import database
from tkinter import messagebox as mbx

A_S_M_S_D = database.ArmDatabase('armdata.db')


class ScoresModuleWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.frame = Frame(self.master)
        self.frame.pack(expand=True, fill=BOTH)
        self.font = ('Times New Roman', 15)
        self.TNF = ('Times New Roman', 14)
        self.ENF = ('courier', 12, 'bold')

        # List box frame and list box
        self.box_frame = LabelFrame(self.frame, text='Students', bg='green', fg='white', font=self.font)
        self.box_frame.pack(fill=BOTH, side=LEFT)

        self.search_entry = ttk.Entry(self.box_frame, width=29, font=self.ENF)
        self.search_entry.pack(ipady=5)
        self.search_entry.bind('<Return>', self.search)

        self.list_box = ttk.Treeview(self.box_frame, )
        self.list_box_col = ('s_name',)
        self.list_box.config(columns=self.list_box_col)
        self.list_box.column('s_name', width=180, anchor=CENTER)
        self.list_box.heading('s_name', text='Student Name')
        self.list_box.column('#0', width=90)
        self.list_box.heading("#0", text="Student No")
        self.list_box.pack(expand=True, fill=BOTH, side=LEFT)
        self.list_box.bind('<<TreeviewSelect>>', self.get_selected_row)

        self.scroll = ttk.Scrollbar(self.box_frame, command=self.list_box.yview)
        self.list_box.config(yscrollcommand=self.scroll.set)
        self.scroll.pack(fill=Y, side=LEFT)

        for children in self.list_box.get_children():
            self.list_box.delete(children)
        for std in A_S_M_S_D.sco_all_students():
            self.list_box.insert('', END, std[0], text=std[0])
            self.list_box.set(std[0], self.list_box_col[0], std[1])

        # Credentials frame
        self.credentials_frame = LabelFrame(self.frame, text='Score', bg='green', fg='white', font=self.font)
        self.credentials_frame.pack(fill=X)

        # Buttons Frame
        self.btn_font = ("Times New Roman", 12, 'bold')
        self.btn_frame = LabelFrame(self.frame, text='Buttons', bg='green', fg='white', font=self.font)
        self.btn_frame.pack(fill=X)

        self.btn_frame2 = Frame(self.btn_frame, bg='green')
        self.btn_frame2.pack()

        self.add_btn = Button(self.btn_frame2, text='Add New', relief=FLAT, bg='#000000', fg='#b7f731', width=10,
                              font=self.btn_font, pady=5, activebackground='black',
                              activeforeground='white', command=self.add_new_btn_command)
        self.add_btn.pack(padx=5, side=LEFT, pady=5)

        self.update_btn = Button(self.btn_frame2, text='Update', relief=FLAT, bg='#000000', fg='#b7f731', width=10,
                                 height=1, font=self.btn_font, pady=5, activebackground='black',
                                 activeforeground='white', command=self.update_btn_command)
        self.update_btn.pack(padx=5, side=LEFT)

        # self.edit_btn = Button(self.details_frame, text='Edit', relief=FLAT, bg='#000000', fg='#b7f731', width=10,
        #                        height=1, font=self.btn_font, pady=5, activebackground='black',
        #                        activeforeground='white')
        # self.edit_btn.pack()

        self.refresh_btn = Button(self.btn_frame2, text='Refresh', relief=FLAT, bg='#000000', fg='#b7f731', width=10,
                                  height=1, font=self.btn_font, pady=5, activebackground='black',
                                  activeforeground='white', command=self.refresh_btn_command)
        self.refresh_btn.pack(padx=5, side=LEFT)

        self.clear_btn = Button(self.btn_frame2, text='Clear', relief=FLAT, bg='#000000', fg='#b7f731', width=10,
                                height=1, font=self.btn_font, pady=5, activebackground='black',
                                activeforeground='white', command=self.clear_btn_command)
        self.clear_btn.pack(padx=5, side=LEFT)

        self.delete_btn = Button(self.btn_frame2, text='Delete', relief=FLAT, bg='#000000', fg='#b7f731', width=10,
                                 height=1, font=self.btn_font, pady=5, activebackground='black',
                                 activeforeground='white', command=self.delete_btn_command)
        self.delete_btn.pack(padx=5, side=LEFT)

        self.convert_btn = Button(self.btn_frame2, text='Convert to 70%', relief=FLAT, bg='#000000', fg='#b7f731',
                                  width=13, height=1, font=self.btn_font, pady=5, activebackground='black',
                                  activeforeground='white', command=self.convert_btn_command)
        self.convert_btn.pack(padx=5, side=LEFT)

        # Student details frame
        self.details_frame = LabelFrame(self.frame, text='Student Details', bg='green', fg='white', font=self.font)
        self.details_frame.pack(fill=BOTH, expand=True)

        # Student credentials
        self.image = PhotoImage(
            file='Teacher\\Scores\\img.png')
        self.image_label = Label(self.credentials_frame, image=self.image, bg='green')
        self.image_label.grid(row=0, column=0, rowspan=9)

        self.date = Label(self.credentials_frame, text='Date', font=self.TNF, bg='green', fg='white')
        self.date.grid(row=1, column=1, sticky=NW, padx=20)
        self.date_entry = ttk.Entry(self.credentials_frame, font=self.ENF)
        self.date_entry.delete(0, END)
        self.date_entry.insert(END, dt.today().date())
        self.date_entry.grid(row=1, column=2, sticky=NW)

        self.year = Label(self.credentials_frame, text='Year', font=self.TNF, bg='green', fg='white')
        self.year.grid(row=2, column=1, sticky=NW, padx=20)
        self.year_entry = ttk.Entry(self.credentials_frame, font=self.ENF)
        self.year_entry.delete(0, END)
        self.year_entry.insert(END, dt.today().date().year)
        self.year_entry.grid(row=2, column=2, sticky=NW)

        self.name = Label(self.credentials_frame, text='Student Name', font=self.TNF, bg='green', fg='white')
        self.name.grid(row=3, column=1, sticky=NW, padx=20)
        self.name_entry = ttk.Entry(self.credentials_frame, font=self.ENF, width=35)
        self.name_entry.grid(row=3, column=2, sticky=NW)

        self.s_no = Label(self.credentials_frame, text='Student Number', font=self.TNF, bg='green', fg='white')
        self.s_no.grid(row=4, column=1, sticky=NW, padx=20)
        self.s_no_entry = ttk.Entry(self.credentials_frame, width=35, font=self.ENF)
        self.s_no_entry.grid(row=4, column=2, sticky=NW)

        self.cls = Label(self.credentials_frame, text='Class', font=self.TNF, bg='green', fg='white')
        self.cls.grid(row=5, column=1, sticky=NW, padx=20)
        self.cls_entry = ttk.Combobox(self.credentials_frame, state='readonly', font=self.ENF, width=33)
        cls = A_S_M_S_D.std_cls()
        cls.insert(0, '')
        self.cls_entry.config(values=cls)
        self.cls_entry.current(0)
        self.cls_entry.grid(row=5, column=2, sticky=NW)

        self.subject = Label(self.credentials_frame, text='Subject', font=self.TNF, bg='green', fg='white')
        self.subject.grid(row=6, column=1, sticky=NW, padx=20)
        self.subject_entry = ttk.Combobox(self.credentials_frame, state='readonly', font=self.ENF, width=33)
        sub = A_S_M_S_D.sub_select()
        sub.insert(0, '')
        self.subject_entry.config(values=sub)
        self.subject_entry.current(0)
        self.subject_entry.grid(row=6, column=2, sticky=NW)

        self.term = Label(self.credentials_frame, text='Term', font=self.TNF, bg='green', fg='white')
        self.term.grid(row=7, column=1, sticky=NW, padx=20)
        self.term_entry = ttk.Combobox(self.credentials_frame, state='readonly', font=self.ENF, width=33)
        self.term_entry.config(values=['', 'Term 1', 'Term 2', 'Term 3'])
        self.term_entry.current(0)
        self.term_entry.grid(row=7, column=2, sticky=NW)

        self.c_score = Label(self.credentials_frame, text='Class Score', font=self.TNF, bg='green', fg='white')
        self.c_score.grid(row=8, column=1, sticky=NW, padx=20)
        self.c_score_entry = ttk.Entry(self.credentials_frame, font=self.ENF, width=35)
        self.c_score_entry.grid(row=8, column=2, sticky=NW)

        self.e_score = Label(self.credentials_frame, text='Exam Score', font=self.TNF, bg='green', fg='white')
        self.e_score.grid(row=9, column=1, sticky=NW, padx=20)
        self.e_score_entry = ttk.Entry(self.credentials_frame, font=self.ENF, width=15)
        self.e_score_entry.grid(row=9, column=2, sticky=NW)

        self.e_score_entry_70 = Listbox(self.credentials_frame, font=self.ENF, width=15, relief=FLAT, height=1)
        self.e_score_entry_70.grid(row=9, column=2, sticky=NE)

        # self.score_type = Label(self.credentials_frame, text='Score Type', font=self.TNF, bg='green', fg='white')
        # self.score_type.grid(row=8, column=1, sticky=NW, padx=20)
        # self.score_type_entry = ttk.Combobox(self.credentials_frame, state='readonly', font=self.ENF, width=33)
        # self.score_type_entry.config(values=['', 'Class Score', 'Exam Score'])
        # self.score_type_entry.current(0)
        # self.score_type_entry.grid(row=8, column=2, sticky=NW)

        # Class details display
        self.details = ttk.Treeview(self.details_frame)
        self.details.pack(side=LEFT, expand=True, fill=BOTH)
        self.details.bind('<<TreeviewSelect>>', self.scores_row)

        # ================= Treeview Column names and headings ===============
        self.columns = ('date', 'year', 'name', 's_no', 'cls', 'subj', 'term', 'c_score', 'e_score', 't_score')
        self.headings = ('Date', 'Year', 'Student Name', 'Student Number', 'Class', 'Subject', 'Term', 'Class Score',
                         'Exam Score', 'Total Score')
        self.details.config(columns=self.columns)
        for col in self.columns:
            if col == 'date':
                self.col_width = 70
            elif col == 'year':
                self.col_width = 50
            elif col == "name":
                self.col_width = 200
            elif col == "s_no":
                self.col_width = 75
            elif col == "cls":
                self.col_width = 40
            elif col == 'subj':
                self.col_width = 100
            elif col == 'term':
                self.col_width = 75
            elif col == "c_score":
                self.col_width = 75
            elif col == 'e_score':
                self.col_width = 75
            elif col == 't_score':
                self.col_width = 75
            self.details.column(col, width=self.col_width, anchor=CENTER)
        counter = 0
        for col in self.columns:
            self.details.heading(col, text=self.headings[counter])
            counter += 1
        self.details.column('#0', width=50, anchor=CENTER)
        self.details.heading("#0", text="ID")

        self.details_scroll = ttk.Scrollbar(self.details_frame)
        self.details_scroll.pack(side=LEFT, fill=Y)
        self.details.config(yscrollcommand=self.details_scroll.set)
        self.details_scroll.config(command=self.details.yview)

    def search(self, event):
        try:
            for children in self.list_box.get_children():
                self.list_box.delete(children)

            # class code search
            if A_S_M_S_D.sco_cls_search(self.search_entry.get()):
                for data in A_S_M_S_D.sco_cls_search(self.search_entry.get()):
                    self.list_box.insert('', END, data[0], text=data[0])
                    self.list_box.set(data[0], self.list_box_col[0], data[1])

            # student number search
            elif A_S_M_S_D.sco_s_no_search(self.search_entry.get()):
                for data in A_S_M_S_D.sco_s_no_search(self.search_entry.get().title()):
                    self.list_box.insert('', END, data[0], text=data[0])
                    self.list_box.set(data[0], self.list_box_col[0], data[1])

            # student name search
            elif A_S_M_S_D.sco_s_name_search(self.search_entry.get()):
                for data in A_S_M_S_D.sco_s_name_search(self.search_entry.get().title()):
                    self.list_box.insert('', END, data[0], text=data[0])
                    self.list_box.set(data[0], self.list_box_col[0], data[1])

            else:
                mbx.showinfo('', 'What you searched does not exist in the database!!')
        except Exception:
            mbx.showinfo('Error', "Unexpected error, please try again!!")
            raise

    def add_new_btn_command(self):
        try:
            if self.date_entry.get() == '' or \
                    self.name_entry.get() == '' or \
                    self.s_no_entry.get() == '' or \
                    self.cls_entry.get() == '' or \
                    self.subject_entry.get() == '' or \
                    self.term_entry.get() == '' or \
                    self.c_score_entry.get() == '' or \
                    self.e_score_entry.get() == '' or self.year_entry.get() == '':
                mbx.showinfo('Incomplete data', 'Incomplete data, please fill all the necessary entries')
            else:
                if mbx.askyesno('Confirm Score', 'Do you want to add this score?') is True:
                    A_S_M_S_D.sco_add_new(
                        self.date_entry.get(),
                        self.name_entry.get(),
                        self.s_no_entry.get(),
                        self.cls_entry.get(),
                        self.subject_entry.get(),
                        self.term_entry.get(),
                        self.c_score_entry.get(),
                        self.e_score_entry.get(),
                        (float(self.c_score_entry.get()) + float(self.e_score_entry.get())),
                        self.year_entry.get()
                    )
                    mbx.showinfo('', 'Score added successfully')
                    self.date_entry.delete(0, END)
                    self.name_entry.delete(0, END)
                    self.s_no_entry.delete(0, END)
                    self.cls_entry.current(0)
                    self.subject_entry.current(0)
                    self.term_entry.current(0)
                    self.e_score_entry.delete(0, END)
                    self.e_score_entry_70.delete(0, END)
                    self.c_score_entry.delete(0, END)
                    self.year_entry.delete(0, END)
                    self.year_entry.insert(END, dt.today().date().year)
                    self.date_entry.insert(END, dt.today().date())
                else:
                    pass
        except Exception:
            mbx.showinfo('Error', 'Unexpected error, please try again!!')
            raise

    def update_btn_command(self):
        try:
            index = self.details.selection()
            if mbx.askyesno('Confirm Update', 'Do you want to update this score') is True:
                A_S_M_S_D.sco_update(
                    index[0],
                    self.subject_entry.get(),
                    self.term_entry.get(),
                    self.c_score_entry.get(),
                    self.e_score_entry.get(),
                    (float(self.c_score_entry.get()) + float(self.e_score_entry.get())),
                    self.year_entry.get()
                )
                mbx.showinfo('', 'Updated successfully')
                self.date_entry.delete(0, END)
                self.name_entry.delete(0, END)
                self.s_no_entry.delete(0, END)
                self.cls_entry.current(0)
                self.subject_entry.current(0)
                self.term_entry.current(0)
                self.e_score_entry.delete(0, END)
                self.e_score_entry_70.delete(0, END)
                self.c_score_entry.delete(0, END)
                self.year_entry.delete(0, END)
                self.year_entry.insert(END, dt.today().date().year)
                self.date_entry.insert(END, dt.today().date())
            else:
                pass
        except Exception:
            mbx.showinfo('Error', 'Unexpected error, please try again!!')
            raise

    def refresh_btn_command(self):
        try:
            for children in self.details.get_children():
                self.details.delete(children)
            for data in A_S_M_S_D.sco_refresh():
                self.details.insert('', END, data[0], text=data[0])
                self.details.set(data[0], self.columns[0], data[1])
                self.details.set(data[0], self.columns[1], data[10])
                self.details.set(data[0], self.columns[2], data[2])
                self.details.set(data[0], self.columns[3], data[3])
                self.details.set(data[0], self.columns[4], data[4])
                self.details.set(data[0], self.columns[5], data[5])
                self.details.set(data[0], self.columns[6], data[6])
                self.details.set(data[0], self.columns[7], data[7])
                self.details.set(data[0], self.columns[8], data[8])
                self.details.set(data[0], self.columns[9], data[9])
                # for sub in A_S_M_S_D.tim_sub_name(data[5]):
                #     self.details.set(data[0], self.columns[4], sub[0])
        except Exception:
            mbx.showinfo('Error', 'Unexpected error, please try again!!')
            raise

    def clear_btn_command(self):
        self.date_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.s_no_entry.delete(0, END)
        self.cls_entry.current(0)
        self.subject_entry.current(0)
        self.term_entry.current(0)
        self.e_score_entry.delete(0, END)
        self.e_score_entry_70.delete(0, END)
        self.c_score_entry.delete(0, END)
        self.year_entry.delete(0, END)
        self.year_entry.insert(END, dt.today().date().year)
        self.date_entry.insert(END, dt.today().date())

    def delete_btn_command(self):
        try:
            index = self.details.selection()
            if mbx.askyesno('Confirm Delete', 'Do you want to delete this score?') is True:
                A_S_M_S_D.sco_delete(index[0])
                mbx.showinfo('', 'Deleted successfully')
                self.date_entry.delete(0, END)
                self.name_entry.delete(0, END)
                self.s_no_entry.delete(0, END)
                self.cls_entry.current(0)
                self.subject_entry.current(0)
                self.term_entry.current(0)
                self.e_score_entry.delete(0, END)
                self.e_score_entry_70.delete(0, END)
                self.c_score_entry.delete(0, END)
                self.year_entry.delete(0, END)
                self.year_entry.insert(END, dt.today().date().year)
                self.date_entry.insert(END, dt.today().date())
            else:
                pass
        except Exception:
            mbx.showinfo('Error', 'Unexpected error, please try again!!')
            raise

    def convert_btn_command(self):
        try:
            self.e_score_entry_70.delete(0, END)
            self.e_score_entry_70.insert(END, self.e_score_entry.get())
            s_70 = ((float(self.e_score_entry.get()) * 70) / 100)
            self.e_score_entry.delete(0, END)
            self.e_score_entry.insert(END, s_70)
        except Exception:
            mbx.showinfo('Error', 'Unexpected error, please try again!!')
            raise

    def get_selected_row(self, event):
        try:
            self.name_entry.delete(0, END)
            self.s_no_entry.delete(0, END)
            self.cls_entry.current(0)
            self.subject_entry.current(0)
            self.term_entry.current(0)
            self.e_score_entry.delete(0, END)
            self.e_score_entry_70.delete(0, END)
            self.c_score_entry.delete(0, END)
            index = self.list_box.selection()
            for children in self.details.get_children():
                self.details.delete(children)
            for data in A_S_M_S_D.sco_std_row(index[0]):
                self.name_entry.insert(END, data[0])
                self.s_no_entry.insert(END, data[1])
                self.cls_entry.set(data[2])
            for s_data in A_S_M_S_D.sco_std_data(index[0]):
                self.details.insert('', END, s_data[0], text=s_data[0])
                self.details.set(s_data[0], self.columns[0], s_data[1])
                self.details.set(s_data[0], self.columns[1], s_data[10])
                self.details.set(s_data[0], self.columns[2], s_data[2])
                self.details.set(s_data[0], self.columns[3], s_data[3])
                self.details.set(s_data[0], self.columns[4], s_data[4])
                self.details.set(s_data[0], self.columns[5], s_data[5])
                self.details.set(s_data[0], self.columns[6], s_data[6])
                self.details.set(s_data[0], self.columns[7], s_data[7])
                self.details.set(s_data[0], self.columns[8], s_data[8])
                self.details.set(s_data[0], self.columns[9], s_data[9])
        except Exception:
            mbx.showinfo('Error', 'Unexpected error, please try again!!')
            raise

    def scores_row(self, event):
        try:
            self.date_entry.delete(0, END)
            self.name_entry.delete(0, END)
            self.s_no_entry.delete(0, END)
            self.cls_entry.current(0)
            self.subject_entry.current(0)
            self.term_entry.current(0)
            self.e_score_entry.delete(0, END)
            self.e_score_entry_70.delete(0, END)
            self.c_score_entry.delete(0, END)
            self.year_entry.delete(0, END)
            index = self.details.selection()
            for data in A_S_M_S_D.scores_row(index[0]):
                self.date_entry.insert(END, data[1])
                self.name_entry.insert(END, data[2])
                self.s_no_entry.insert(END, data[3])
                self.cls_entry.set(data[4])
                self.subject_entry.set(data[5])
                self.term_entry.set(data[6])
                self.e_score_entry.insert(END, data[8])
                self.c_score_entry.insert(END, data[7])
                self.year_entry.insert(END, data[10])

        except Exception:
            mbx.showinfo('Error', 'Unexpected error, please try again!!')
            raise
