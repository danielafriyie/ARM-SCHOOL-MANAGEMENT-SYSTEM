from tkinter import *
from tkinter import ttk
from datetime import datetime as dt
from tkinter import messagebox as mbx
from Main_Window import database

A_S_M_S_D = database.ArmDatabase('armdata.db')


class ClassModuleWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.frame = Frame(self.master, bg='light green')
        self.frame.pack(expand=True, fill=BOTH)
        self.font = ('Times New Roman', 15)

        # Display tree frame
        self.display_tree_frame = LabelFrame(self.frame, text='Class List', font=self.font, bg='green', fg='white')
        self.display_tree_frame.pack(side=LEFT, fill=Y, anchor=N)

        # Class credentials frame
        self.credentials_frame = LabelFrame(self.frame, text='Class Credentials', font=self.font, bg='green',
                                            fg='white')
        self.credentials_frame.pack(anchor=N, fill=BOTH)

        # Class details display tree
        self.detail_frame = LabelFrame(self.frame, text='Class Details', font=self.font, bg='green', fg='white')
        self.detail_frame.pack(fill=BOTH, expand=True)

        # Display box and search box
        # self.search = ttk.Entry(self.display_tree_frame, width=30, font=('courier', 12, 'bold'))
        # self.search.pack(ipady=5)
        #
        # self.display_box = Listbox(self.display_tree_frame, relief=FLAT)
        # self.display_box.pack(expand=True, fill=BOTH, side=LEFT)
        #
        # self.scroll = ttk.Scrollbar(self.display_tree_frame)
        # self.scroll.pack(side=LEFT, fill=Y)
        # self.display_box.config(yscrollcommand=self.scroll.set)
        # self.scroll.config(command=self.display_box.yview)

        # Class credentials entries
        self.TNF = ('Times New Roman', 14)
        self.ENF = ('courier', 12, 'bold')

        self.class_image = PhotoImage(
            file='images\\class_icon.png')
        self.class_image_label = Label(self.credentials_frame, image=self.class_image, bg='green')
        self.class_image_label.grid(row=0, column=0, rowspan=7)

        self.date = Label(self.credentials_frame, text='Date', font=self.TNF, bg='green', fg='white')
        self.date.grid(row=1, column=1, sticky=NW, padx=20)
        self.date_entry = ttk.Entry(self.credentials_frame, font=self.ENF)
        self.date_entry.delete(0, END)
        self.date_entry.insert(END, dt.today().date())
        self.date_entry.grid(row=1, column=2, sticky=NW)

        self.name = Label(self.credentials_frame, text='Class Name', font=self.TNF, bg='green', fg='white')
        self.name.grid(row=2, column=1, sticky=NW, padx=20)
        self.name_entry = ttk.Entry(self.credentials_frame, width=35, font=self.ENF)
        self.name_entry.grid(row=2, column=2, sticky=NW)

        self.class_code = Label(self.credentials_frame, text='Class Code', font=self.TNF, bg='green', fg='white')
        self.class_code.grid(row=3, column=1, sticky=NW, padx=20)
        self.class_code_entry = ttk.Entry(self.credentials_frame, width=35, font=self.ENF)
        self.class_code_entry.grid(row=3, column=2, sticky=NW)

        self.teacher = Label(self.credentials_frame, text='Assign Teacher', font=self.TNF, bg='green', fg='white')
        self.teacher.grid(row=4, column=1, sticky=NW, padx=20)
        self.teacher_entry = ttk.Combobox(self.credentials_frame, state='readonly', font=self.ENF, width=33)
        tea = A_S_M_S_D.tea_t_no()
        tea.insert(0, '')
        self.teacher_entry.config(values=tea)
        self.teacher_entry.current(0)
        self.teacher_entry.grid(row=4, column=2, sticky=NW)

        self.a_teacher = Label(self.credentials_frame, text='Assistant Teacher(s)', font=self.TNF, bg='green',
                               fg='white')
        self.a_teacher.grid(row=5, column=1, sticky=NW, padx=20)
        self.a_teacher_entry = ttk.Combobox(self.credentials_frame, state='readonly', font=self.ENF, width=33)
        self.a_teacher_entry.config(values=tea)
        self.a_teacher_entry.current(0)
        self.a_teacher_entry.grid(row=5, column=2, sticky=NW)

        self.a_teacher_box = Listbox(self.credentials_frame, width=35, height=4, relief=FLAT, font=self.ENF)
        self.a_teacher_box.grid(row=6, column=2, sticky=NW)
        self.a_teacher_box_btn = ttk.Button(self.credentials_frame, text="Add", width=9,
                                            command=self.teacher_box_btn_command)
        self.a_teacher_box_btn.grid(row=6, column=4, sticky=N)
        self.a_teacher_box_btn = ttk.Button(self.credentials_frame, text="Remove", width=9
                                            , command=self.teacher_box_rev_command)
        self.a_teacher_box_btn.grid(row=6, column=4)

        # Class details display
        self.details = ttk.Treeview(self.detail_frame)
        self.details.pack(side=LEFT, expand=True, fill=BOTH)
        self.details.bind("<<TreeviewSelect>>", self.get_selected_row)

        # ================= Treeview Column names and headings ===============
        self.columns = ('date', 'c_name', 'c_code', 'c_size', 't_no', 'tea')
        self.headings = ('Date', 'Class Name', 'Class Code', 'Class Size', 'Teacher No', 'Class Teacher')
        self.details.config(columns=self.columns)
        for col in self.columns:
            if col == 'date':
                self.col_width = 50
            elif col == "c_name":
                self.col_width = 70
            elif col == "c_code":
                self.col_width = 70
            elif col == "c_size":
                self.col_width = 70
            elif col == 't_no':
                self.col_width = 70
            elif col == 'tea':
                self.col_width = 150
            self.details.column(col, width=self.col_width, anchor=CENTER)
        counter = 0
        for col in self.columns:
            self.details.heading(col, text=self.headings[counter])
            counter += 1
        self.details.column('#0', width=30, anchor=CENTER)
        self.details.heading("#0", text="Class ID")

        self.details_scroll = ttk.Scrollbar(self.detail_frame)
        self.details_scroll.pack(side=LEFT, fill=Y)
        self.details.config(yscrollcommand=self.details_scroll.set)
        self.details_scroll.config(command=self.details.yview)

        self.btn_font = ("Times New Roman", 12, 'bold')
        self.btn_frame = LabelFrame(self.detail_frame, text='Buttons')
        self.btn_frame.pack()

        self.add_btn = Button(self.detail_frame, text='Add New', relief=FLAT, bg='#000000', fg='#b7f731', width=10,
                              height=1, font=self.btn_font, pady=5, activebackground='black',
                              activeforeground='white', command=self.add_new_btn_command)
        self.add_btn.pack(padx=5)

        self.update_btn = Button(self.detail_frame, text='Update', relief=FLAT, bg='#000000', fg='#b7f731', width=10,
                                 height=1, font=self.btn_font, pady=5, activebackground='black',
                                 activeforeground='white', command=self.update_btn_command)
        self.update_btn.pack()

        # self.edit_btn = Button(self.detail_frame, text='Edit', relief=FLAT, bg='#000000', fg='#b7f731', width=10,
        #                        height=1, font=self.btn_font, pady=5, activebackground='black',
        #                        activeforeground='white')
        # self.edit_btn.pack()

        self.refresh_btn = Button(self.detail_frame, text='Refresh', relief=FLAT, bg='#000000', fg='#b7f731', width=10,
                                  height=1, font=self.btn_font, pady=5, activebackground='black',
                                  activeforeground='white', command=self.refresh_btn_command)
        self.refresh_btn.pack()

        self.clear_btn = Button(self.detail_frame, text='Clear', relief=FLAT, bg='#000000', fg='#b7f731', width=10,
                                height=1, font=self.btn_font, pady=5, activebackground='black',
                                activeforeground='white', command=self.clear_btn_command)
        self.clear_btn.pack()

        self.delete_btn = Button(self.detail_frame, text='Delete', relief=FLAT, bg='#000000', fg='#b7f731', width=10,
                                 height=1, font=self.btn_font, pady=5, activebackground='black',
                                 activeforeground='white', command=self.delete_btn_command)
        self.delete_btn.pack()

    def add_new_btn_command(self):
        try:
            if self.date_entry.get() == '' or self.name_entry.get() == '' or self.class_code_entry.get() == '' or \
                    self.teacher_entry.get() == '':
                mbx.showinfo('Incomplete details', 'Please fill all the necessary entries!')
            else:
                query = mbx.askyesno('Confirm class', 'Do you want to add this class?')
                if query is True:
                    A_S_M_S_D.cls_add_new(
                        self.date_entry.get(),
                        self.name_entry.get(),
                        self.class_code_entry.get(),
                        self.teacher_entry.get(),
                        str(self.a_teacher_box.get(0, END)),
                        size=0
                    )
                    mbx.showinfo('', 'Added successfully')
                    self.name_entry.delete(0, END)
                    self.class_code_entry.delete(0, END)
                    self.teacher_entry.current(0)
                    self.a_teacher_entry.current(0)
                    self.a_teacher_box.delete(0, END)
                else:
                    pass
        except Exception:
            mbx.showinfo('Error', "Unexpected error, couldn't add subject")
            raise

    def teacher_box_btn_command(self):
        if self.a_teacher_entry.get() == '':
            mbx.showinfo('', 'You have not selected any teacher!')
            pass
        elif self.a_teacher_entry.get() in self.a_teacher_box.get(0, END):
            mbx.showinfo('', 'Teacher Already exist!')
            pass
        else:
            self.a_teacher_box.insert(END, self.a_teacher_entry.get())

    def teacher_box_rev_command(self):
        try:
            index = self.a_teacher_box.curselection()[0]
            self.a_teacher_box.delete(index)
        except IndexError:
            pass

    def clear_btn_command(self):
        self.name_entry.delete(0, END)
        self.class_code_entry.delete(0, END)
        self.teacher_entry.current(0)
        self.a_teacher_entry.current(0)
        self.a_teacher_box.delete(0, END)

    def refresh_btn_command(self):
        try:
            for children in self.details.get_children():
                self.details.delete(children)
            for cls in A_S_M_S_D.cls_view_all():
                self.details.insert('', END, cls[0], text=cls[0])
                self.details.set(cls[0], self.columns[0], cls[1])
                self.details.set(cls[0], self.columns[1], cls[2])
                self.details.set(cls[0], self.columns[2], cls[3])
                self.details.set(cls[0], self.columns[3], cls[6])
                self.details.set(cls[0], self.columns[4], cls[4])
                for tea in A_S_M_S_D.cls_teacher(cls[4]):
                    self.details.set(cls[0], self.columns[5], tea[0])
        except Exception:
            mbx.showinfo('Error', "Couldn't refresh, please try again!")
            raise

    def get_selected_row(self, event):
        try:
            self.date_entry.delete(0, END)
            self.name_entry.delete(0, END)
            self.class_code_entry.delete(0, END)
            self.teacher_entry.current(0)
            self.a_teacher_box.delete(0, END)
            index = self.details.selection()[0]
            for data in A_S_M_S_D.cls_get_selected_row(index):
                self.date_entry.insert(END, data[1])
                self.name_entry.insert(END, data[2])
                self.class_code_entry.insert(END, data[3])
                self.teacher_entry.set(data[4])
                for t_code in data[5].strip("()").replace("'", '').split(','):
                    self.a_teacher_box.insert(END, t_code.strip("' '"))
        except Exception:
            raise

    def update_btn_command(self):
        try:
            index = self.details.selection()[0]
            query = mbx.askyesno('Confirm update', 'Do you want to update this class?')
            if query is True:
                A_S_M_S_D.cls_update(
                    self.name_entry.get(),
                    self.class_code_entry.get(),
                    self.teacher_entry.get(),
                    str(self.a_teacher_box.get(0, END)),
                    index
                )
                mbx.showinfo('', 'Updated successfully')
                self.name_entry.delete(0, END)
                self.class_code_entry.delete(0, END)
                self.teacher_entry.current(0)
                self.a_teacher_entry.current(0)
                self.a_teacher_box.delete(0, END)
            else:
                pass
        except Exception:
            mbx.showinfo('Error', "Unexpected error, couldn't update this subject\nPlease try again!")
            raise

    def delete_btn_command(self):
        try:
            index = self.details.selection()[0]
            query = mbx.askyesno('Confirm delete', "Do you want to delete this class?")
            if query is True:
                A_S_M_S_D.cls_delete(index)
                mbx.showinfo('', 'Deleted successfully')
                self.name_entry.delete(0, END)
                self.class_code_entry.delete(0, END)
                self.teacher_entry.current(0)
                self.a_teacher_entry.current(0)
                self.a_teacher_box.delete(0, END)
        except Exception:
            mbx.showinfo('Error', "Unexpected error, couldn't delete class!!")
            raise

