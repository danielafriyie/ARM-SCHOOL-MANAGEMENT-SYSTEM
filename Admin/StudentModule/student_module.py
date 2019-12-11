from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mbx
from datetime import datetime as dt
from Main_Window import database
from PIL import Image, ImageTk

A_S_M_S_D = database.ArmDatabase('.\\armdata.db')


class StudentModuleWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        # self.title('Users Module')
        self.font = ('Times New Roman', 15)

        self.frame = ttk.Frame(self.master)
        self.frame.pack(expand=True, fill=BOTH)

        self.frame_style = ttk.Style()
        self.frame_style.configure('TLabelframe', background='green')

        # List Box frame
        self.list_box_frame = LabelFrame(self.frame, text='Students', bg="green", fg='white', font=self.font)
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
        self.image = Image.open('images\\image.png')
        self.image = self.image.resize((240, 560))
        self.photoImage = ImageTk.PhotoImage(self.image)
        self.image_label = ttk.Label(self.credentials_frame, image=self.photoImage, background='green',
                                     foreground='white')
        self.image_label.grid(row=0, column=0, rowspan=17,)

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
        self.date_entry.grid(row=1, column=2, sticky=NW, columnspan=6)

        self.name_label = ttk.Label(self.credentials_frame, text='Name', font=self.TNF, background='green',
                                    foreground='white')
        self.name_label.grid(row=2, column=1, sticky=NW, padx=20)
        self.name_entry = ttk.Entry(self.credentials_frame, width=35, font=('courier', 12, 'bold'))
        self.name_entry.grid(row=2, column=2, sticky=NW, columnspan=6)

        self.phone_label = ttk.Label(self.credentials_frame, text='Phone', font=self.TNF, background='green',
                                     foreground='white')
        self.phone_label.grid(row=3, column=1, sticky=NW, padx=20)
        self.phone_entry = ttk.Entry(self.credentials_frame, width=35, font=('courier', 12, 'bold'))
        self.phone_entry.grid(row=3, column=2, sticky=NW, columnspan=6)

        self.email_label = ttk.Label(self.credentials_frame, text='Email', font=self.TNF, background='green',
                                     foreground='white')
        self.email_label.grid(row=4, column=1, sticky=NW, padx=20)
        self.email_entry = ttk.Entry(self.credentials_frame, width=35, font=('courier', 12, 'bold'))
        self.email_entry.grid(row=4, column=2, sticky=NW, columnspan=6)

        self.gender = ttk.Label(self.credentials_frame, text='Gender', font=self.TNF,
                                background='green', foreground='white')
        self.gender.grid(row=5, column=1, sticky=NW, padx=20)
        self.gender_entry = ttk.Combobox(self.credentials_frame, width=25, font=('courier', 12, 'bold'),
                                         state='readonly', )
        self.gender_entry['values'] = ['', 'Male', 'Female']
        self.gender_entry.current(0)
        self.gender_entry.grid(row=5, column=2, sticky=NW, columnspan=6)

        self.dob = ttk.Label(self.credentials_frame, text='Date of Birth', font=self.TNF,
                             background='green', foreground='white')
        self.dob.grid(row=6, column=1, sticky=NW, padx=20)

        self.month_var = StringVar()
        self.month_entry = ttk.Combobox(self.credentials_frame, font=("Times New Roman", 13), state="readonly"
                                        , textvariable=self.month_var, width=10)
        self.month_entry["values"] = ("", "January", "February", "March", "April", "May", "June", "July", "August",
                                      "September", "October", "November", "December")
        self.month_entry.current(0)
        self.month_entry.grid(row=6, column=2, sticky=NW, )

        self.day_var = StringVar()
        self.day_entry = ttk.Combobox(self.credentials_frame, font=("Times New Roman", 13)
                                      , textvariable=self.day_var, width=3)
        self.day_entry["values"] = (
            "", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15",
            "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29",
            "30", "31")
        self.day_entry.current(0)
        self.day_entry.grid(row=6, column=3, sticky=NW, padx=2, )

        self.year_var = StringVar()
        self.year_entry = ttk.Combobox(self.credentials_frame, font=("Times New Roman", 13),
                                       textvariable=self.year_var, width=15)
        self.year_entry["values"] = [
            "", "1901", "1902", "1903", "1904", "1905", "1906", "1907", "1908", "1909", "1910",
            "1911", "1912", "1913", "1914", "1915", "1916", "1917", "1918", "1919", "1920",
            "1921",
            "1922", "1923", "1924", "1925", "1926", "1927", "1928", "1929", "1930", "1931",
            "1932",
            "1933", "1934", "1935", "1936", "1937", "1938", "1939", "1940", "1941", "1942",
            "1943",
            "1944", "1945", "1946", "1947", "1948", "1949", "1950", "1951", "1952", "1953",
            "1954",
            "1954", "1954", "1954", "1954", "1954", "1954", "1954", "1954", "1954", "1954",
            "1954"
            , "1955", "1956", "1957", "1958", "1959", "1960", "1961", "1962", "1963", "1964"
            , "1965", "1966", "1967", "1968", "1969", "1970", "1971", "1972", "1973", "1974"
            , "1975", "1976", "1977", "1978", "1979", "1980", "1981", "1982", "1983", "1984"
            , "1985", "1986", "1987", "1988", "1989", "1990", "1991", "1992", "1993", "1994"
            , "1995", "1996", "1997", "1998", "1999",
            "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010",
            "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2020", "2020",
            "2021",
            "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030", "2031",
            "2032",
            "2033", "2034", "2035", "2036", "2037", "2038", "2039", "2040", "2041", "2042",
            "2043",
            "2044", "2045", "2046", "2047", "2048", "2049", "2050", "2051", "2052", "2053",
            "2054",
            "2054", "2054", "2054", "2054", "2054", "2054", "2054", "2054", "2054", "2054",
            "2054"
            , "2055", "2056", "2057", "2058", "2059", "2060", "2061", "2062", "2063", "2064"
            , "2065", "2066", "2067", "2068", "2069", "2070", "2071", "2072", "2073", "2074"
            , "2075", "2076", "2077", "2078", "2079", "2080", "2081", "2082", "2083", "2084"
            , "2085", "2086", "2087", "2088", "2089", "2090", "2091", "2092", "2093", "2094"
            , "2095", "2096", "2097", "2098", "2099"]
        self.year_entry.current(0)
        self.year_entry.grid(row=6, column=4, sticky=NW, columnspan=10, )

        # self.account_type_label = ttk.Label(self.credentials_frame, text='Account Type', font=self.TNF,
        #                                     background='green', foreground='white')
        # self.account_type_label.grid(row=5, column=1, sticky=NW, padx=20)
        # self.account_type_entry = ttk.Combobox(self.credentials_frame, state='readonly', width=25,
        #                                        font=('courier', 12, 'bold'))
        # self.account_type_entry['values'] = ['', 'Administrator', 'Teacher', 'SuperUser']
        # self.account_type_entry.current(0)
        # self.account_type_entry.grid(row=5, column=2, sticky=NW, columnspan=3)

        # self.username_label = ttk.Label(self.credentials_frame, text='Username', font=self.TNF, background='green',
        #                                 foreground='white')
        # self.username_label.grid(row=6, column=1, sticky=NW, padx=20)
        # self.username_entry = ttk.Entry(self.credentials_frame, width=35, font=('courier', 12, 'bold'))
        # self.username_entry.grid(row=6, column=2, sticky=NW, columnspan=3)

        # self.password_label = ttk.Label(self.credentials_frame, text='Password', font=self.TNF, background='green',
        #                                 foreground='white')
        # self.password_label.grid(row=7, column=1, sticky=NW, padx=20)
        # self.password_entry = ttk.Entry(self.credentials_frame, width=35, show='*', font=('courier', 12, 'bold'))
        # self.password_entry.grid(row=7, column=2, sticky=NW, columnspan=3)

        self.assign_class = ttk.Label(self.credentials_frame, text='Assign Class', font=self.TNF,
                                      background='green', foreground='white')
        self.assign_class.grid(row=7, column=1, sticky=NW, padx=20)
        self.assign_class_entry = ttk.Combobox(self.credentials_frame, width=25, font=('courier', 12, 'bold'),
                                               state='readonly', )
        cls = A_S_M_S_D.std_cls()
        cls.insert(0, '')
        self.assign_class_entry['values'] = cls
        self.assign_class_entry.current(0)
        self.assign_class_entry.grid(row=7, column=2, sticky=NW, columnspan=3)

        self.parent_guardian = Label(self.credentials_frame, text='Parent / Guardian', font=self.TNF, bg='green',
                                     fg='white')
        self.parent_guardian.grid(row=8, column=1, sticky=NW, padx=20)
        self.parent_guardian_entry = ttk.Entry(self.credentials_frame, width=35, font=self.ENF)
        self.parent_guardian_entry.grid(row=8, column=2, sticky=NW, columnspan=3)

        self.parent_guardian_phone = Label(self.credentials_frame, text='Parent / Guardian Phone', font=self.TNF,
                                           bg='green', fg='white')
        self.parent_guardian_phone.grid(row=9, column=1, sticky=NW, padx=20)
        self.parent_guardian_phone_entry = ttk.Entry(self.credentials_frame, width=35, font=self.ENF)
        self.parent_guardian_phone_entry.grid(row=9, column=2, sticky=NW, columnspan=3)

        # self.subject_box = Listbox(self.credentials_frame, width=45, height=3, relief=FLAT)
        # self.subject_box.grid(row=6, column=2, sticky=NW, columnspan=3)
        # self.subject_box_btn = ttk.Button(self.credentials_frame, text="Add", width=9)
        # self.subject_box_btn.grid(row=6, column=4, sticky=NE, columnspan=3)

        self.address = Label(self.credentials_frame, text='Address', font=self.TNF, bg='green', fg='white')
        self.address.grid(row=10, column=1, sticky=NW, padx=20)
        self.address_entry = ttk.Entry(self.credentials_frame, width=35, font=self.ENF)
        self.address_entry.grid(row=10, column=2, sticky=NW, columnspan=6)

        self.residence = Label(self.credentials_frame, text='Residence', font=self.TNF, bg='green', fg='white')
        self.residence.grid(row=11, column=1, sticky=NW, padx=20)
        self.residence_entry = ttk.Entry(self.credentials_frame, width=35, font=self.ENF)
        self.residence_entry.grid(row=11, column=2, sticky=NW, columnspan=6)

        self.loc = Label(self.credentials_frame, text='Location', font=self.TNF, bg='green', fg='white')
        self.loc.grid(row=12, column=1, sticky=NW, padx=20)
        self.loc_entry = ttk.Entry(self.credentials_frame, width=35, font=self.ENF)
        self.loc_entry.grid(row=12, column=2, sticky=NW, columnspan=6)

        self.l_mark = Label(self.credentials_frame, text='Land Mark', font=self.TNF, bg='green', fg='white')
        self.l_mark.grid(row=13, column=1, sticky=NW, padx=20)
        self.l_mark_entry = ttk.Entry(self.credentials_frame, width=35, font=self.ENF)
        self.l_mark_entry.grid(row=13, column=2, sticky=NW, columnspan=6)

        self.nationality = Label(self.credentials_frame, text='Nationality', font=self.TNF, bg='green', fg='white')
        self.nationality.grid(row=14, column=1, sticky=NW, padx=20)
        self.nationality_entry = ttk.Entry(self.credentials_frame, width=35, font=self.ENF)
        self.nationality_entry.grid(row=14, column=2, sticky=NW, columnspan=6)

        self.region = Label(self.credentials_frame, text='Region', font=self.TNF, bg='green', fg='white')
        self.region.grid(row=15, column=1, sticky=NW, padx=20)
        self.region_entry = ttk.Entry(self.credentials_frame, width=35, font=self.ENF)
        self.region_entry.grid(row=15, column=2, sticky=NW, columnspan=6)

        self.student_no = Button(self.credentials_frame, text='Student No.', font=self.TNF, bg='green', fg='white',
                                 relief=FLAT, activebackground='black', activeforeground='white',
                                 command=self.std_no_btn_command)
        self.student_no.grid(row=16, column=1, sticky=NW, padx=20)
        self.student_no_entry = ttk.Entry(self.credentials_frame, width=35, font=self.ENF)
        self.student_no_entry.grid(row=16, column=2, sticky=NW, columnspan=3)

        # Display Box
        self.search_entry = ttk.Entry(self.list_box_frame, width=36, font=('courier', 12, 'bold'))
        self.search_entry.pack(ipady=5)
        self.search_entry.bind('<Return>', self.search)

        self.display_box = ttk.Treeview(self.list_box_frame)
        self.display_box_col = ('s_name',)
        self.display_box.config(columns=self.display_box_col)
        self.display_box.column('s_name', width=250, anchor=CENTER)
        self.display_box.heading('s_name', text='Student Name')
        self.display_box.column('#0', width=90)
        self.display_box.heading("#0", text="Student No")
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
        self.add_new_btn.pack(side=LEFT, padx=10)

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

    ##########################################
    #           BUTTON COMMANDS
    ##########################################
    def add_new_btn_command(self):
        # student date of birth
        std_dob = (self.day_entry.get() + '-' + self.month_entry.get() + '-' + self.year_entry.get())
        try:
            if self.name_entry.get() == '' or self.date_entry.get() == '' or self.gender_entry.get() == '' or \
                    self.assign_class_entry.get() == '' or self.parent_guardian_entry.get() == '' or \
                    self.parent_guardian_phone_entry.get() == '' or self.address_entry.get() == '' or \
                    self.residence_entry.get() == '' or self.loc_entry.get() == '' or self.l_mark_entry.get() == '' or \
                    self.nationality_entry.get() == '' or self.region_entry.get() == '' or \
                    self.student_no_entry.get() == '':
                mbx.showinfo('Incomplete registration', 'Please fill all the necessary entries!')
            else:
                query = mbx.askyesno('Confirm student', 'Do you want to add this student?')
                if query is True:
                    A_S_M_S_D.std_add_new(
                        self.date_entry.get(),
                        self.name_entry.get(),
                        self.phone_entry.get(),
                        self.email_entry.get(),
                        self.gender_entry.get(),
                        std_dob,
                        self.assign_class_entry.get(),
                        self.parent_guardian_entry.get(),
                        self.parent_guardian_phone_entry.get(),
                        self.address_entry.get(),
                        self.residence_entry.get(),
                        self.loc_entry.get(),
                        self.l_mark_entry.get(),
                        self.nationality_entry.get(),
                        self.region_entry.get(),
                        self.student_no_entry.get()
                    )
                    A_S_M_S_D.std_class_size_increase(self.assign_class_entry.get())
                    mbx.showinfo('', 'Added successfully')
                    self.date_entry.delete(0, END)
                    self.name_entry.delete(0, END)
                    self.phone_entry.delete(0, END)
                    self.email_entry.delete(0, END)
                    self.gender_entry.delete(0, END)
                    self.day_entry.set('')
                    self.month_entry.set('')
                    self.year_entry.set('')
                    self.assign_class_entry.delete(0, END)
                    self.parent_guardian_entry.delete(0, END)
                    self.parent_guardian_phone_entry.delete(0, END)
                    self.address_entry.delete(0, END)
                    self.residence_entry.delete(0, END)
                    self.loc_entry.delete(0, END)
                    self.l_mark_entry.delete(0, END)
                    self.nationality_entry.delete(0, END)
                    self.region_entry.delete(0, END)
                    self.student_no_entry.delete(0, END)
                    self.gender_entry.set('')
                    self.assign_class_entry.set('')
                    self.date_entry.insert(END, dt.today().date())
                else:
                    pass
        except Exception:
            mbx.showinfo('Error', "Unexpected error, couldn't add student\nPlease try again")
            raise

    def std_no_btn_command(self):
        self.student_no_entry.delete(0, END)
        try:
            num = A_S_M_S_D.std_s_no()
            if len(str(num[0][0])) == 1:
                self.student_no_entry.insert(END, ('S' + '000' + str(num[0][0] + 1) + str(dt.today().year)))
            elif len(str(num[0][0])) == 2:
                self.student_no_entry.insert(END, ('S' + '00' + str(num[0][0] + 1)) + str(dt.today().year))
            elif len(str(num[0][0])) == 3:
                self.student_no_entry.insert(END, ('S' + '0' + str(num[0][0] + 1)) + str(dt.today().year))
            elif len(str(num[0][0])) >= 4:
                self.student_no_entry.insert(END, ('S' + str(num[0][0] + 1)) + str(dt.today().year))
        except IndexError:
            self.student_no_entry.insert(END, 'S0001' + str(dt.today().year))
            pass
        except Exception:
            mbx.showinfo('Error', "Unexpected error, couldn't generate student number\nPlease try again!")
            raise

    def clear_btn_command(self):
        self.date_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.gender_entry.delete(0, END)
        self.day_entry.set('')
        self.month_entry.set('')
        self.year_entry.set('')
        self.assign_class_entry.delete(0, END)
        self.parent_guardian_entry.delete(0, END)
        self.parent_guardian_phone_entry.delete(0, END)
        self.address_entry.delete(0, END)
        self.residence_entry.delete(0, END)
        self.loc_entry.delete(0, END)
        self.l_mark_entry.delete(0, END)
        self.nationality_entry.delete(0, END)
        self.region_entry.delete(0, END)
        self.student_no_entry.delete(0, END)
        self.gender_entry.set('')
        self.assign_class_entry.set('')
        self.date_entry.insert(END, dt.today().date())

    def refresh_btn_command(self):
        try:
            for children in self.display_box.get_children():
                self.display_box.delete(children)
            for std in A_S_M_S_D.sco_all_students():
                self.display_box.insert('', END, std[0], text=std[0])
                self.display_box.set(std[0], self.display_box_col[0], std[1])
        except Exception:
            mbx.showinfo('Error', "Unexpected error, couldn't fetch data from the database\nPlease try again!")
            raise

    def delete_btn_command(self):
        try:
            selected_row = self.display_box.selection()
            query = mbx.askyesno('Confirm delete', 'Do you want to delete this student?')
            if query is True:
                A_S_M_S_D.std_delete(selected_row[0])
                mbx.showinfo('', 'Deleted successfully')
                self.date_entry.delete(0, END)
                self.name_entry.delete(0, END)
                self.phone_entry.delete(0, END)
                self.email_entry.delete(0, END)
                self.gender_entry.delete(0, END)
                self.day_entry.set('')
                self.month_entry.set('')
                self.year_entry.set('')
                self.assign_class_entry.delete(0, END)
                self.parent_guardian_entry.delete(0, END)
                self.parent_guardian_phone_entry.delete(0, END)
                self.address_entry.delete(0, END)
                self.residence_entry.delete(0, END)
                self.loc_entry.delete(0, END)
                self.l_mark_entry.delete(0, END)
                self.nationality_entry.delete(0, END)
                self.region_entry.delete(0, END)
                self.student_no_entry.delete(0, END)
                self.gender_entry.set('')
                self.assign_class_entry.set('')
                self.date_entry.insert(END, dt.today().date())
            else:
                pass

        except IndexError:
            pass
        except Exception:
            mbx.showinfo('Error', "Unexpected error, couldn't delete student\nPlease try again!")
            raise

    def update_btn_command(self):
        # student date of birth
        std_dob = (self.day_entry.get() + '-' + self.month_entry.get() + '-' + self.year_entry.get())
        try:
            if self.name_entry.get() == '' or self.date_entry.get() == '' or self.gender_entry.get() == '' or \
                    self.assign_class_entry.get() == '' or self.parent_guardian_entry.get() == '' or \
                    self.parent_guardian_phone_entry.get() == '' or self.address_entry.get() == '' or \
                    self.residence_entry.get() == '' or self.loc_entry.get() == '' or self.l_mark_entry.get() == '' or \
                    self.nationality_entry.get() == '' or self.region_entry.get() == '' or \
                    self.student_no_entry.get() == '':
                mbx.showinfo('Incomplete data', 'Please fill all the necessary entries!')
            else:
                query = mbx.askyesno('Confirm update', 'Do you want to update this student?')
                if query is True:
                    A_S_M_S_D.std_update(
                        self.name_entry.get(),
                        self.phone_entry.get(),
                        self.email_entry.get(),
                        self.gender_entry.get(),
                        std_dob,
                        self.assign_class_entry.get(),
                        self.parent_guardian_entry.get(),
                        self.parent_guardian_phone_entry.get(),
                        self.address_entry.get(),
                        self.residence_entry.get(),
                        self.loc_entry.get(),
                        self.l_mark_entry.get(),
                        self.nationality_entry.get(),
                        self.region_entry.get(),
                        self.student_no_entry.get()
                    )
                    mbx.showinfo('', 'Updated successfully')
                    self.date_entry.delete(0, END)
                    self.name_entry.delete(0, END)
                    self.phone_entry.delete(0, END)
                    self.email_entry.delete(0, END)
                    self.gender_entry.delete(0, END)
                    self.day_entry.set('')
                    self.month_entry.set('')
                    self.year_entry.set('')
                    self.assign_class_entry.delete(0, END)
                    self.parent_guardian_entry.delete(0, END)
                    self.parent_guardian_phone_entry.delete(0, END)
                    self.address_entry.delete(0, END)
                    self.residence_entry.delete(0, END)
                    self.loc_entry.delete(0, END)
                    self.l_mark_entry.delete(0, END)
                    self.nationality_entry.delete(0, END)
                    self.region_entry.delete(0, END)
                    self.student_no_entry.delete(0, END)
                    self.gender_entry.set('')
                    self.assign_class_entry.set('')
                    self.date_entry.insert(END, dt.today().date())
                else:
                    pass
        except Exception:
            mbx.showinfo('Error', "Unexpected error, couldn't Update student\nPlease try again")
            raise

    def get_selected_row(self, event):
        try:
            selected_row = self.display_box.selection()
            self.date_entry.delete(0, END)
            self.name_entry.delete(0, END)
            self.phone_entry.delete(0, END)
            self.email_entry.delete(0, END)
            self.gender_entry.delete(0, END)
            self.day_entry.set('')
            self.month_entry.set('')
            self.year_entry.set('')
            self.assign_class_entry.delete(0, END)
            self.parent_guardian_entry.delete(0, END)
            self.parent_guardian_phone_entry.delete(0, END)
            self.address_entry.delete(0, END)
            self.residence_entry.delete(0, END)
            self.loc_entry.delete(0, END)
            self.l_mark_entry.delete(0, END)
            self.nationality_entry.delete(0, END)
            self.region_entry.delete(0, END)
            self.student_no_entry.delete(0, END)
            self.gender_entry.set('')
            self.assign_class_entry.set('')
            for data in A_S_M_S_D.std_view_all(selected_row[0]):
                self.date_entry.insert(END, data[1])
                self.name_entry.insert(END, data[2])
                self.phone_entry.insert(END, data[3])
                self.email_entry.insert(END, data[4])
                self.gender_entry.set(data[5])
                self.assign_class_entry.set(data[7])
                self.parent_guardian_entry.insert(END, data[8])
                self.parent_guardian_phone_entry.insert(END, data[9])
                self.address_entry.insert(END, data[10])
                self.residence_entry.insert(END, data[11])
                self.loc_entry.insert(END, data[12])
                self.l_mark_entry.insert(END, data[13])
                self.nationality_entry.insert(END, data[14])
                self.region_entry.insert(END, data[15])
                self.student_no_entry.insert(END, data[16])
                dob = data[6].split('-')
                self.day_entry.set(dob[0])
                self.month_entry.set(dob[1])
                self.year_entry.set(dob[2])
        except IndexError:
            pass
        except Exception:
            raise

    def search(self, event):
        try:
            self.display_box.delete(0, END)
            if len(A_S_M_S_D.std_search(self.search_entry.get().title())) <= 0:
                mbx.showinfo('', "Couldn't find any student associated with your search\nPlease try again!")
            else:
                for tea in A_S_M_S_D.std_search(self.search_entry.get().title()):
                    self.display_box.insert(END, tea)
        except Exception:
            mbx.showinfo('Error', "Unexpected error, couldn't find any student associated with your search"
                                  "\nPlease try again!")
            raise
