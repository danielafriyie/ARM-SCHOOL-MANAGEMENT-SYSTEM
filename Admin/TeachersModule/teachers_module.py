from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mbx
from datetime import datetime as dt
from Main_Window import database
from sqlite3 import IntegrityError

A_S_M_S_D = database.ArmDatabase('armdata.db')


class TeachersModuleWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        # self.title('Users Module')
        self.font = ('Times New Roman', 15)

        self.frame = ttk.Frame(self.master)
        self.frame.pack(expand=True, fill=BOTH)

        self.frame_style = ttk.Style()
        self.frame_style.configure('TLabelframe', background='green')

        # List Box frame
        self.list_box_frame = LabelFrame(self.frame, text='Teachers', bg="green", fg='white', font=self.font)
        self.list_box_frame.pack(fill=Y, anchor=N, side=LEFT)

        # Credentials frame
        self.credentials_frame = LabelFrame(self.frame, text='Registration Form', bg="green", fg='white',
                                            font=self.font)
        self.credentials_frame.pack(anchor=N, fill=BOTH, expand=True)

        # Access Rights Frame
        # self.access_rights_frame =
        # LabelFrame(self.frame, text='Access Rights', bg="green", fg='white', font=self.font)
        # self.access_rights_frame.pack(fill=BOTH)

        # User Credentials
        self.teachers_image = PhotoImage(file='images\\teacher.png').subsample(3, 2)
        self.teachers_image_label = ttk.Label(self.credentials_frame, image=self.teachers_image, background='green',
                                              foreground='white')
        self.teachers_image_label.grid(row=0, column=0, rowspan=13, padx=20, )

        self.TNF = ('Times New Roman', 14)
        self.ENF = ('courier', 12, 'bold')

        # self.entry_style = ttk.Style()
        # self.entry_style.configure('TEntry', foreground='green', )

        self.date_label = ttk.Label(self.credentials_frame, text='Date', width=15, font=self.TNF, background='green',
                                    foreground='white')
        self.date_label.grid(row=1, column=1, sticky=NW, padx=20)
        self.date_entry = ttk.Entry(self.credentials_frame, font=('courier', 12, 'bold'))
        self.date_entry.delete(0, END)
        self.date_entry.insert(END, dt.today().date())
        self.date_entry.grid(row=1, column=2, sticky=NW, )

        self.name_label = ttk.Label(self.credentials_frame, text='Name', font=self.TNF, background='green',
                                    foreground='white')
        self.name_label.grid(row=2, column=1, sticky=NW, padx=20)
        self.name_entry = ttk.Entry(self.credentials_frame, width=35, font=('courier', 12, 'bold'))
        self.name_entry.grid(row=2, column=2, sticky=NW, )

        self.phone_label = ttk.Label(self.credentials_frame, text='Phone', font=self.TNF, background='green',
                                     foreground='white')
        self.phone_label.grid(row=3, column=1, sticky=NW, padx=20)
        self.phone_entry = ttk.Entry(self.credentials_frame, width=35, font=('courier', 12, 'bold'))
        self.phone_entry.grid(row=3, column=2, sticky=NW, )

        self.email_label = ttk.Label(self.credentials_frame, text='Email', font=self.TNF, background='green',
                                     foreground='white')
        self.email_label.grid(row=4, column=1, sticky=NW, padx=20)
        self.email_entry = ttk.Entry(self.credentials_frame, width=35, font=('courier', 12, 'bold'))
        self.email_entry.grid(row=4, column=2, sticky=NW, )

        # self.account_type_label = ttk.Label(self.credentials_frame, text='Account Type', font=self.TNF,
        #                                     background='green', foreground='white')
        # self.account_type_label.grid(row=5, column=1, sticky=NW, padx=20)
        # self.account_type_entry = ttk.Combobox(self.credentials_frame, state='readonly', width=25,
        #                                        font=('courier', 12, 'bold'))
        # self.account_type_entry['values'] = ['', 'Administrator', 'Teacher', 'SuperUser']
        # self.account_type_entry.current(0)
        # self.account_type_entry.grid(row=5, column=2, sticky=NW, )

        # self.username_label = ttk.Label(self.credentials_frame, text='Username', font=self.TNF, background='green',
        #                                 foreground='white')
        # self.username_label.grid(row=6, column=1, sticky=NW, padx=20)
        # self.username_entry = ttk.Entry(self.credentials_frame, width=35, font=('courier', 12, 'bold'))
        # self.username_entry.grid(row=6, column=2, sticky=NW, )

        # self.password_label = ttk.Label(self.credentials_frame, text='Password', font=self.TNF, background='green',
        #                                 foreground='white')
        # self.password_label.grid(row=7, column=1, sticky=NW, padx=20)
        # self.password_entry = ttk.Entry(self.credentials_frame, width=35, show='*', font=('courier', 12, 'bold'))
        # self.password_entry.grid(row=7, column=2, sticky=NW, )

        self.assign_sub_label = ttk.Label(self.credentials_frame, text='Assign Subject', font=self.TNF,
                                          background='green', foreground='white')
        self.assign_sub_label.grid(row=5, column=1, sticky=NW, padx=20)
        self.assign_sub_entry = ttk.Combobox(self.credentials_frame, width=25, font=('courier', 12, 'bold'),
                                             state='readonly', )
        # counter = 0
        # sub = A_S_M_S_D.sub_select()
        # try:
        #     while counter < len(sub):
        #         self.assign_sub_entry.config(values=sub)
        #         counter += 1
        # except IndexError:
        #     pass
        sub = A_S_M_S_D.sub_select()
        sub.insert(0, '')
        self.assign_sub_entry.config(values=sub)
        self.assign_sub_entry.current(0)
        self.assign_sub_entry.grid(row=5, column=2, sticky=NW, )

        self.subject_box = Listbox(self.credentials_frame, width=35, height=4, relief=FLAT, font=self.ENF)
        self.subject_box.grid(row=6, column=2, sticky=NW, )
        self.subject_box_add_btn = ttk.Button(self.credentials_frame, text="Add", width=9
                                              , command=self.subject_box_btn_command)
        self.subject_box_add_btn.grid(row=6, column=4, sticky=N, )
        self.subject_box_remove_btn = ttk.Button(self.credentials_frame, text="Remove", width=9
                                                 , command=self.subject_box_rev_command)
        self.subject_box_remove_btn.grid(row=6, column=4, )

        self.address = Label(self.credentials_frame, text='Address', font=self.TNF, bg='green', fg='white')
        self.address.grid(row=7, column=1, sticky=NW, padx=20)
        self.address_entry = ttk.Entry(self.credentials_frame, width=35, font=self.ENF)
        self.address_entry.grid(row=7, column=2, sticky=NW, )

        self.residence = Label(self.credentials_frame, text='Residence', font=self.TNF, bg='green', fg='white')
        self.residence.grid(row=8, column=1, sticky=NW, padx=20)
        self.residence_entry = ttk.Entry(self.credentials_frame, width=35, font=self.ENF)
        self.residence_entry.grid(row=8, column=2, sticky=NW, )

        self.loc = Label(self.credentials_frame, text='Location', font=self.TNF, bg='green', fg='white')
        self.loc.grid(row=9, column=1, sticky=NW, padx=20)
        self.loc_entry = ttk.Entry(self.credentials_frame, width=35, font=self.ENF)
        self.loc_entry.grid(row=9, column=2, sticky=NW, )

        self.l_mark = Label(self.credentials_frame, text='Land Mark', font=self.TNF, bg='green', fg='white')
        self.l_mark.grid(row=10, column=1, sticky=NW, padx=20)
        self.l_mark_entry = ttk.Entry(self.credentials_frame, width=35, font=self.ENF)
        self.l_mark_entry.grid(row=10, column=2, sticky=NW, )

        self.nationality = Label(self.credentials_frame, text='Nationality', font=self.TNF, bg='green', fg='white')
        self.nationality.grid(row=11, column=1, sticky=NW, padx=20)
        self.nationality_entry = ttk.Entry(self.credentials_frame, width=35, font=self.ENF)
        self.nationality_entry.grid(row=11, column=2, sticky=NW, )

        self.region = Label(self.credentials_frame, text='Region', font=self.TNF, bg='green', fg='white')
        self.region.grid(row=12, column=1, sticky=NW, padx=20)
        self.region_entry = ttk.Entry(self.credentials_frame, width=35, font=self.ENF)
        self.region_entry.grid(row=12, column=2, sticky=NW, )

        self.teacher_no = Button(self.credentials_frame, text='Teacher No.', font=self.TNF, bg='green', fg='white',
                                 relief=FLAT, activebackground='black', activeforeground='white',
                                 command=self.t_no_btn_command)
        self.teacher_no.grid(row=13, column=1, sticky=NW, padx=20)
        self.teacher_no_entry = ttk.Entry(self.credentials_frame, width=35, font=self.ENF)
        self.teacher_no_entry.grid(row=13, column=2, sticky=NW, )

        # Display Box
        self.search_entry = ttk.Entry(self.list_box_frame, width=36, font=('courier', 12, 'bold'))
        self.search_entry.pack(ipady=5)
        self.search_entry.bind("<Return>", self.search)

        self.display_box = ttk.Treeview(self.list_box_frame)
        self.display_box_col = ('t_name',)
        self.display_box.config(columns=self.display_box_col)
        self.display_box.column('t_name', width=250, anchor=CENTER)
        self.display_box.heading('t_name', text='Teacher Name')
        self.display_box.column('#0', width=90)
        self.display_box.heading("#0", text="Teacher No")
        self.display_box.pack(fill=BOTH, expand=True, side=LEFT)
        self.display_box.bind("<<TreeviewSelect>>", self.get_selected_row)

        self.scroll = ttk.Scrollbar(self.list_box_frame)
        self.scroll.pack(fill=Y, side=LEFT)
        self.display_box.configure(yscrollcommand=self.scroll.set)
        self.scroll.configure(command=self.display_box.yview)

        # Access Right Administrator frame
        # self.CBS = ttk.Style()
        # self.CBS.configure('TCheckbutton', background='green', )
        #
        # self.admin_frame = LabelFrame(self.access_rights_frame, text='Administrator', bg="green", fg='white',
        #                               font=self.font)
        # self.admin_frame.pack(side=LEFT, anchor=N, fill=BOTH, expand=True)
        #
        # # Access Right Teacher frame
        # self.teacher_frame = LabelFrame(self.access_rights_frame, text="Teacher", bg="green", fg='white',
        #                                 font=self.font)
        # self.teacher_frame.pack(side=LEFT, anchor=N, fill=BOTH, expand=True)
        #
        # # Administrator Access Right
        # self.admin_image = PhotoImage(file='Admin\\TeachersModule\\admin.png')
        # self.admin_image_label = ttk.Label(self.admin_frame, image=self.admin_image, background='green',
        #                                    foreground='white')
        # self.admin_image_label.grid(row=0, column=0, rowspan=7, padx=20, sticky=NSEW)
        #
        # self.users_label = ttk.Label(self.admin_frame, text="Users", background='green', foreground='white',
        #                              font=self.TNF)
        # self.users_label.grid(row=1, column=1, sticky=NSEW, padx=20)
        # self.users_check_var = IntVar()
        # self.users_check = ttk.Checkbutton(self.admin_frame, onvalue=1, offvalue=0, variable=self.users_check_var)
        # self.users_check.grid(row=1, column=2, padx=30, sticky=NSEW)
        #
        # self.students_label = ttk.Label(self.admin_frame, text="Students", background='green', foreground='white',
        #                                 font=self.TNF)
        # self.students_label.grid(row=2, column=1, sticky=NSEW, padx=20)
        # self.students_check_var = IntVar()
        # self.students_check = ttk.Checkbutton(self.admin_frame, onvalue=1, offvalue=0, variable=self.students_check_var)
        # self.students_check.grid(row=2, column=2, padx=30, sticky=NSEW)
        #
        # self.class_label = ttk.Label(self.admin_frame, text="Add / Edit Class", background='green', foreground='white',
        #                              font=self.TNF)
        # self.class_label.grid(row=3, column=1, sticky=NSEW, padx=20)
        # self.class_check_var = IntVar()
        # self.class_check = ttk.Checkbutton(self.admin_frame, onvalue=1, offvalue=0, variable=self.class_check_var)
        # self.class_check.grid(row=3, column=2, padx=30, sticky=NSEW)
        #
        # self.time_table_label = ttk.Label(self.admin_frame, text="Time Table", background='green', foreground='white',
        #                                   font=self.TNF)
        # self.time_table_label.grid(row=4, column=1, sticky=NSEW, padx=20)
        # self.time_table_check_var = IntVar()
        # self.time_table_check = ttk.Checkbutton(self.admin_frame, onvalue=1, offvalue=0,
        #                                         variable=self.time_table_check_var)
        # self.time_table_check.grid(row=4, column=2, padx=30, sticky=NSEW)
        #
        # self.sub_label = ttk.Label(self.admin_frame, text="Add / Edit Subjects", background='green', foreground='white',
        #                            font=self.TNF)
        # self.sub_label.grid(row=5, column=1, sticky=NSEW, padx=20)
        # self.sub_check_var = IntVar()
        # self.sub_check = ttk.Checkbutton(self.admin_frame, onvalue=1, offvalue=0, variable=self.sub_check_var)
        # self.sub_check.grid(row=5, column=2, padx=30, sticky=NSEW)
        #
        # # Teacher Access Right
        # self.teacher_image = PhotoImage(file='Admin\\TeachersModule\\teacher2.png')
        # self.teacher_image_label = ttk.Label(self.teacher_frame, image=self.teacher_image, background='green',
        #                                      foreground='white')
        # self.teacher_image_label.grid(row=0, column=0, rowspan=7, padx=20)
        #
        # self.class_list_label = ttk.Label(self.teacher_frame, text="Class List", background='green', foreground='white',
        #                                   font=self.TNF)
        # self.class_list_label.grid(row=1, column=1, sticky=W, padx=20)
        # self.class_list_check_var = IntVar()
        # self.class_list_check = ttk.Checkbutton(self.teacher_frame, onvalue=1, offvalue=0,
        #                                         variable=self.class_list_check_var)
        # self.class_list_check.grid(row=1, column=2, padx=30)
        #
        # self.scores_label = ttk.Label(self.teacher_frame, text="Scores", background='green', foreground='white',
        #                               font=self.TNF)
        # self.scores_label.grid(row=2, column=1, sticky=W, padx=20)
        # self.scores_check_var = IntVar()
        # self.scores_check = ttk.Checkbutton(self.teacher_frame, onvalue=1, offvalue=0, variable=self.scores_check_var)
        # self.scores_check.grid(row=2, column=2, padx=30)
        #
        # self.class_schedule_label = ttk.Label(self.teacher_frame, text="Class Schedule", background='green',
        #                                       foreground='white', font=self.TNF)
        # self.class_schedule_label.grid(row=3, column=1, sticky=W, padx=20)
        # self.class_schedule_check_var = IntVar()
        # self.class_schedule_check = ttk.Checkbutton(self.teacher_frame, onvalue=1, offvalue=0,
        #                                             variable=self.class_schedule_check_var)
        # self.class_schedule_check.grid(row=3, column=2, padx=30)
        #
        # self.subjects_label = ttk.Label(self.teacher_frame, text="Subjects", background='green', foreground='white',
        #                                 font=self.TNF)
        # self.subjects_label.grid(row=4, column=1, sticky=W, padx=20)
        # self.subjects_check_var = IntVar()
        # self.subjects_check = ttk.Checkbutton(self.teacher_frame, onvalue=1, offvalue=0,
        #                                       variable=self.subjects_check_var)
        # self.subjects_check.grid(row=4, column=2, padx=30)
        #
        # self.report_label = ttk.Label(self.teacher_frame, text="Reports", background='green', foreground='white',
        #                               font=self.TNF)
        # self.report_label.grid(row=5, column=1, sticky=W, padx=20)
        # self.report_check_var = IntVar()
        # self.report_check = ttk.Checkbutton(self.teacher_frame, onvalue=1, offvalue=0, variable=self.report_check_var)
        # self.report_check.grid(row=5, column=2, padx=30)

        # Buttons Frame
        self.buttons_frame = LabelFrame(self.frame, text='Buttons', bg="green", fg='white', font=self.font)
        self.buttons_frame.pack(fill=X)

        # Buttons
        self.btn_frame = Frame(self.buttons_frame, bg="green")
        self.btn_frame.pack()

        self.btn_font = ("Times New Roman", 12, 'bold')
        self.btn_style = ttk.Style()
        self.btn_style.configure("TButton", background='green', height='10', font=self.btn_font,
                                 color='green', pressed='pink')

        self.add_new_btn = Button(self.btn_frame, text='Add New', relief=FLAT, bg='#000000', fg='#b7f731', width=10,
                                  height=1, font=self.btn_font, activebackground='black',
                                  activeforeground='white', command=self.add_new_btn_command)
        self.add_new_btn.pack(side=LEFT, padx=10, pady=3)

        self.update_btn = Button(self.btn_frame, text='Update', relief=FLAT, bg='#000000', fg='#b7f731', width=10,
                                 height=1, font=self.btn_font, activebackground='black',
                                 activeforeground='white', command=self.update_btn_command)
        self.update_btn.pack(side=LEFT, padx=10)

        # self.edit_btn = Button(self.btn_frame, text='Edit', relief=FLAT, bg='#000000', fg='#b7f731', width=10,
        #                        height=1, font=self.btn_font, activebackground='black',
        #                        activeforeground='white')
        # self.edit_btn.pack(side=LEFT, padx=10)

        self.refresh_btn = Button(self.btn_frame, text='Refresh', relief=FLAT, bg='#000000', fg='#b7f731', width=10,
                                  height=1, font=self.btn_font, activebackground='black',
                                  activeforeground='white', command=self.refresh_btn_command)
        self.refresh_btn.pack(side=LEFT, padx=10)

        self.clear_btn = Button(self.btn_frame, text='Clear', relief=FLAT, bg='#000000', fg='#b7f731', width=10,
                                height=1, font=self.btn_font, activebackground='black',
                                activeforeground='white', command=self.clear_btn_command)
        self.clear_btn.pack(side=LEFT, padx=10)

        self.delete_btn = Button(self.btn_frame, text='Delete', relief=FLAT, bg='#000000', fg='#b7f731', width=10,
                                 height=1, font=self.btn_font, activebackground='black',
                                 activeforeground='white', command=self.delete_btn_command)
        self.delete_btn.pack(side=LEFT, padx=10)

        # Status Bar
        # self.status_bar_frame = LabelFrame(self.frame, bg='green', )
        # self.status_bar_frame.pack(expand=True, fill=BOTH)
        # self.status_bar = "STATUS BAR"
        # self.status_bar_label = Label(self.status_bar_frame, text=self.status_bar, bg="green", fg="white",
        #                               font=("Algerian", 15))
        # self.status_bar_label.pack(expand=True, fill=BOTH, )

    ###############################################
    #       BUTTON COMMANDS
    ##############################################
    def add_new_btn_command(self):
        try:
            if self.date_entry.get() == '' or \
                    self.name_entry.get() == '' or \
                    self.phone_entry.get() == '' or \
                    self.email_entry.get() == '' or \
                    self.subject_box.get(0) == '' or \
                    self.address_entry.get() == '' or \
                    self.residence_entry.get() == '' or \
                    self.loc_entry.get() == '' or \
                    self.l_mark_entry.get() == '' or \
                    self.nationality_entry.get() == '' or \
                    self.region_entry.get() == '' or \
                    self.teacher_no_entry.get() == '':
                mbx.showinfo('Incomplete registration', 'Please fill all the necessary entries')
            else:
                query = mbx.askyesno('Confirm Teacher', 'Do you want to add this teacher?')
                if query is True:
                    A_S_M_S_D.tea_add_new(
                        self.date_entry.get(),
                        self.name_entry.get(),
                        self.phone_entry.get(),
                        self.email_entry.get(),
                        str(self.subject_box.get(0, END)),
                        self.address_entry.get(),
                        self.residence_entry.get(),
                        self.loc_entry.get(),
                        self.l_mark_entry.get(),
                        self.nationality_entry.get(),
                        self.region_entry.get(),
                        self.teacher_no_entry.get()
                    )
                    mbx.showinfo('', 'Added successfully')
                    self.name_entry.delete(0, END)
                    self.phone_entry.delete(0, END)
                    self.email_entry.delete(0, END)
                    self.assign_sub_entry.current(0)
                    self.subject_box.delete(0, END)
                    self.address_entry.delete(0, END)
                    self.residence_entry.delete(0, END)
                    self.loc_entry.delete(0, END)
                    self.l_mark_entry.delete(0, END)
                    self.nationality_entry.delete(0, END)
                    self.region_entry.delete(0, END)
                    self.teacher_no_entry.delete(0, END)
                else:
                    pass
        except IntegrityError:
            print('Integrity Error << check add_new_btn_command >>')
            mbx.showinfo('Error', "Unexpected error, couldn't add teacher!!")
            raise IntegrityError
        except Exception:
            print('Unexpected Error << check add_new_btn_command >>')
            mbx.showinfo('Error', "Unexpected error, couldn't add teacher, please try again\nor contact"
                                  " system administrator!!")
            raise Exception

    def t_no_btn_command(self):
        num = A_S_M_S_D.tea_t_no_gen()
        self.teacher_no_entry.delete(0, END)
        try:
            if len(str(num[0][0])) == 1:
                self.teacher_no_entry.insert(END, ('T' + '000' + str(num[0][0] + 1) + str(dt.today().year)))
            elif len(str(num[0][0])) == 2:
                self.teacher_no_entry.insert(END, ('T' + '00' + str(num[0][0] + 1) + str(dt.today().year)))
            elif len(str(num[0][0])) == 3:
                self.teacher_no_entry.insert(END, ('T' + '0' + str(num[0][0] + 1) + str(dt.today().year)))
            elif len(str(num[0][0])) >= 4:
                self.teacher_no_entry.insert(END, ('T' + str(num[0][0] + 1) + str(dt.today().year)))
        except IndexError:
            self.teacher_no_entry.insert(END, ('T' + '0001' + str(dt.today().year)))
        except:
            print('Unexpected Error << check t_no_btn_command >>')
            pass

    def subject_box_btn_command(self):
        # self.subject_box.delete(0, END)
        if self.assign_sub_entry.get() == '':
            mbx.showinfo('', 'You have not selected any subject!')
            pass
        elif self.assign_sub_entry.get() in self.subject_box.get(0, END):
            mbx.showinfo('', 'Subject Already exist!')
            pass
        else:
            self.subject_box.insert(END, self.assign_sub_entry.get())

    def subject_box_rev_command(self):
        try:
            index = self.subject_box.curselection()[0]
            self.subject_box.delete(index)
        except IndexError:
            pass

    def clear_btn_command(self):
        self.name_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.assign_sub_entry.current(0)
        self.subject_box.delete(0, END)
        self.address_entry.delete(0, END)
        self.residence_entry.delete(0, END)
        self.loc_entry.delete(0, END)
        self.l_mark_entry.delete(0, END)
        self.nationality_entry.delete(0, END)
        self.region_entry.delete(0, END)
        self.teacher_no_entry.delete(0, END)

    def refresh_btn_command(self):
        try:
            for children in self.display_box.get_children():
                self.display_box.delete(children)
            for std in A_S_M_S_D.tea_view_all():
                self.display_box.insert('', END, std[0], text=std[0])
                self.display_box.set(std[0], self.display_box_col[0], std[1])
        except Exception:
            mbx.showinfo('Error', "Unexpected error, couldn't fetch data from the database\nPlease try again!")
            raise

    def get_selected_row(self, event):
        try:
            selected_row = self.display_box.selection()
            self.name_entry.delete(0, END)
            self.phone_entry.delete(0, END)
            self.email_entry.delete(0, END)
            self.assign_sub_entry.current(0)
            self.subject_box.delete(0, END)
            self.address_entry.delete(0, END)
            self.residence_entry.delete(0, END)
            self.loc_entry.delete(0, END)
            self.l_mark_entry.delete(0, END)
            self.nationality_entry.delete(0, END)
            self.region_entry.delete(0, END)
            self.teacher_no_entry.delete(0, END)
            for data in A_S_M_S_D.tea_get_selected_row(selected_row[0]):
                self.name_entry.insert(END, data[2])
                self.phone_entry.insert(END, data[3])
                self.email_entry.insert(END, data[4])
                # self.subject_box.insert(END, data[5])
                self.address_entry.insert(END, data[6])
                self.residence_entry.insert(END, data[7])
                self.loc_entry.insert(END, data[8])
                self.l_mark_entry.insert(END, data[9])
                self.nationality_entry.insert(END, data[10])
                self.region_entry.insert(END, data[11])
                self.teacher_no_entry.insert(END, data[12])
                for sub in data[5].strip("()").replace("'", "").split(','):
                    # print(sub.strip(' '))
                    self.subject_box.insert(END, sub.strip(' '))
        except IndexError:
            pass

    def update_btn_command(self):
        try:
            query = mbx.askyesno('Confirm Update', 'Do you want to update selected teacher?')
            if query is True:
                A_S_M_S_D.tea_update(
                    self.name_entry.get(),
                    self.phone_entry.get(),
                    self.email_entry.get(),
                    str(self.subject_box.get(0, END)),
                    self.address_entry.get(),
                    self.residence_entry.get(),
                    self.loc_entry.get(),
                    self.l_mark_entry.get(),
                    self.nationality_entry.get(),
                    self.region_entry.get(),
                    self.teacher_no_entry.get()
                )
                mbx.showinfo('', 'Updated successfully')
            else:
                pass
        except Exception:
            mbx.showinfo('Error', "Unexpected error, couldn't update teacher!!")
            print('Unexpected Error << check update_btn_command >>')
            raise

    def delete_btn_command(self):
        try:
            query = mbx.askyesno('Confirm Delete', 'Do you want to delete this teacher?')
            if query is True:
                selected_row = self.display_box.selection()
                A_S_M_S_D.tea_delete(selected_row[0])
                mbx.showinfo('', 'Deleted successfully')
            else:
                pass
        except IndexError:
            pass
        except Exception:
            mbx.showinfo('Error', "Unexpected error, couldn't delete teacher!!")
            raise

    def search(self, event):
        try:
            self.display_box.delete(0, END)
            if len(A_S_M_S_D.tea_search(self.search_entry.get().title())) <= 0:
                mbx.showinfo('', "Couldn't find any teacher associated with your search\nPlease try again!")
            else:
                for tea in A_S_M_S_D.tea_search(self.search_entry.get().title()):
                    self.display_box.insert(END, tea)
        except Exception:
            mbx.showinfo('Error', "Unexpected error, couldn't find any teacher associated with your search"
                                  "\nPlease try again!")
            raise
