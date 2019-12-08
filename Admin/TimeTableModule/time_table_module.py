from tkinter import *
from tkinter import ttk
from datetime import datetime as dt
from Main_Window import database
from tkinter import messagebox as mbx

A_S_M_S_D = database.ArmDatabase('armdata.db')


class TimeTableModuleWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.frame = Frame(self.master)
        self.frame.pack(expand=True, fill=BOTH)
        self.font = ('Times New Roman', 15)

        # Credentials frame
        self.credentials_frame = LabelFrame(self.frame, text='Time Table', bg='green', fg='white', font=self.font)
        self.credentials_frame.pack(fill=X)

        # Time table details frame
        self.details_frame = LabelFrame(self.frame, text='Time Table Details', bg='green', fg='white', font=self.font)
        self.details_frame.pack(fill=BOTH, expand=True)

        # Time table credentials
        self.TNF = ('Times New Roman', 14)
        self.ENF = ('courier', 12, 'bold')

        self.time_image = PhotoImage(
            file='Admin\\TimeTableModule\\timetable.png')
        self.time_image_label = Label(self.credentials_frame, image=self.time_image, bg='green')
        self.time_image_label.grid(row=0, column=0, rowspan=7)

        self.date = Label(self.credentials_frame, text='Date', font=self.TNF, bg='green', fg='white')
        self.date.grid(row=1, column=1, sticky=NW, padx=20)
        self.date_entry = ttk.Entry(self.credentials_frame, font=self.ENF)
        self.date_entry.delete(0, END)
        self.date_entry.insert(END, dt.today().date())
        self.date_entry.grid(row=1, column=2, sticky=NW)

        self.teacher = Label(self.credentials_frame, text='Assign Teacher', font=self.TNF, bg='green', fg='white')
        self.teacher.grid(row=2, column=1, sticky=NW, padx=20)
        self.teacher_entry = ttk.Combobox(self.credentials_frame, state='readonly', font=self.ENF, width=33)
        self.a_tea = A_S_M_S_D.tim_teacher()
        self.a_tea.insert(0, '')
        self.teacher_entry.config(values=self.a_tea)
        self.teacher_entry.current(0)
        self.teacher_entry.grid(row=2, column=2, sticky=NW)

        self.time = Label(self.credentials_frame, text='Time', font=self.TNF, bg='green', fg='white')
        self.time.grid(row=3, column=1, sticky=NW, padx=20)
        self.time_entry = ttk.Entry(self.credentials_frame, width=35, font=self.ENF)
        self.time_entry.grid(row=3, column=2, sticky=NW)

        self.day = Label(self.credentials_frame, text='Day', font=self.TNF, bg='green', fg='white')
        self.day.grid(row=4, column=1, sticky=NW, padx=20)
        self.day_entry = ttk.Combobox(self.credentials_frame, state='readonly', font=self.ENF, width=33)
        self.day_entry.config(values=['', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
        self.day_entry.current(0)
        self.day_entry.grid(row=4, column=2, sticky=NW)

        self.subject = Label(self.credentials_frame, text='Assign Subject', font=self.TNF, bg='green', fg='white')
        self.subject.grid(row=5, column=1, sticky=NW, padx=20)
        self.subject_entry = ttk.Combobox(self.credentials_frame, state='readonly', font=self.ENF, width=33)
        self.a_sub = A_S_M_S_D.tim_subject()
        self.a_sub.insert(0, '')
        self.subject_entry.config(values=self.a_sub)
        self.subject_entry.current(0)
        self.subject_entry.grid(row=5, column=2, sticky=NW)

        self.clss = Label(self.credentials_frame, text='Assign Class', font=self.TNF, bg='green', fg='white')
        self.clss.grid(row=6, column=1, sticky=NW, padx=20)
        self.clss_entry = ttk.Combobox(self.credentials_frame, state='readonly', font=self.ENF, width=33)
        self.a_class = A_S_M_S_D.tim_class()
        self.a_class.insert(0, '')
        self.clss_entry.config(values=self.a_class)
        self.clss_entry.current(0)
        self.clss_entry.grid(row=6, column=2, sticky=NW)

        # Class details display
        self.details = ttk.Treeview(self.details_frame)
        self.details.pack(side=LEFT, expand=True, fill=BOTH)
        self.details.bind("<<TreeviewSelect>>", self.get_selected_row)

        # ================= Treeview Column names and headings ===============
        self.columns = ('date', 't_name', 'time', 'day', 'subj', 'class')
        self.headings = ('Date', 'Teacher Name', 'Time', 'Day', 'Subject', 'Class')
        self.details.config(columns=self.columns)
        for col in self.columns:
            if col == 'date':
                col_width = 100
            elif col == "t_name":
                col_width = 300
            elif col == "time":
                col_width = 100
            elif col == "day":
                col_width = 200
            elif col == 'subj':
                col_width =300
            elif col == "class":
                col_width = 200
            self.details.column(col, width=col_width, anchor=CENTER)
        counter = 0
        for col in self.columns:
            self.details.heading(col, text=self.headings[counter])
            counter += 1
        self.details.column('#0', width=100, anchor=CENTER)
        self.details.heading("#0", text="ID")

        self.details_scroll = ttk.Scrollbar(self.details_frame)
        self.details_scroll.pack(side=LEFT, fill=Y)
        self.details.config(yscrollcommand=self.details_scroll.set)
        self.details_scroll.config(command=self.details.yview)

        self.btn_font = ("Times New Roman", 12, 'bold')
        self.btn_frame = LabelFrame(self.details_frame, text='Buttons')
        self.btn_frame.pack()

        self.add_btn = Button(self.details_frame, text='Add New', relief=FLAT, bg='#000000', fg='#b7f731', width=10,
                              height=1, font=self.btn_font, pady=5, activebackground='black',
                              activeforeground='white', command=self.add_new_btn_command)
        self.add_btn.pack(padx=5)

        self.update_btn = Button(self.details_frame, text='Update', relief=FLAT, bg='#000000', fg='#b7f731', width=10,
                                 height=1, font=self.btn_font, pady=5, activebackground='black',
                                 activeforeground='white', command=self.update_btn_command)
        self.update_btn.pack()

        # self.edit_btn = Button(self.details_frame, text='Edit', relief=FLAT, bg='#000000', fg='#b7f731', width=10,
        #                        height=1, font=self.btn_font, pady=5, activebackground='black',
        #                        activeforeground='white')
        # self.edit_btn.pack()

        self.refresh_btn = Button(self.details_frame, text='Refresh', relief=FLAT, bg='#000000', fg='#b7f731', width=10,
                                  height=1, font=self.btn_font, pady=5, activebackground='black',
                                  activeforeground='white', command=self.refresh_btn_command)
        self.refresh_btn.pack()

        self.clear_btn = Button(self.details_frame, text='Clear', relief=FLAT, bg='#000000', fg='#b7f731', width=10,
                                height=1, font=self.btn_font, pady=5, activebackground='black',
                                activeforeground='white', command=self.clear_btn_command)
        self.clear_btn.pack()

        self.delete_btn = Button(self.details_frame, text='Delete', relief=FLAT, bg='#000000', fg='#b7f731', width=10,
                                 height=1, font=self.btn_font, pady=5, activebackground='black',
                                 activeforeground='white', command=self.delete_btn_command)
        self.delete_btn.pack()

    def add_new_btn_command(self):
        try:
            if self.date_entry.get() == '' or self.teacher_entry.get() == '' or self.time_entry.get() == '' or \
                    self.clss_entry.get() == '' or self.subject_entry.get() == '' or self.day_entry.get() == '':
                mbx.showinfo('Incomplete data', 'Please fill all the necessary entries!')
            else:
                query = mbx.askyesno('Confirm schedule', 'Do you want to add this schedule?')
                if query is True:
                    A_S_M_S_D.tim_add_new(
                        self.date_entry.get(),
                        self.teacher_entry.get(),
                        self.time_entry.get(),
                        self.day_entry.get(),
                        self.subject_entry.get(),
                        self.clss_entry.get()
                    )
                    mbx.showinfo('', 'Added successfully')
                    self.date_entry.delete(0, END)
                    self.teacher_entry.current(0)
                    self.time_entry.delete(0, END)
                    self.day_entry.current(0)
                    self.subject_entry.current(0)
                    self.clss_entry.current(0)
                    self.date_entry.insert(END, dt.today().date())
                else:
                    pass
        except Exception:
            mbx.showinfo('Error', "Unexpected error, couldn't add time table")
            raise

    def update_btn_command(self):
        try:
            index = self.details.selection()[0]
            query = mbx.askyesno('Confirm update', 'Do you want to update this schedule?')
            if query is True:
                A_S_M_S_D.tim_update(
                    self.teacher_entry.get(),
                    self.time_entry.get(),
                    self.day_entry.get(),
                    self.subject_entry.get(),
                    self.clss_entry.get(),
                    index
                )
                mbx.showinfo('', 'Updated successfully')
                self.date_entry.delete(0, END)
                self.teacher_entry.set('')
                self.time_entry.delete(0, END)
                self.day_entry.set('')
                self.subject_entry.set('')
                self.clss_entry.set('')
                self.date_entry.insert(END, dt.today().date())
            else:
                pass
        except IndexError:
            pass
        except Exception:
            mbx.showinfo('Error', "Unexpected error, couldn't update this schedule\nPlease try again!")
            raise

    def delete_btn_command(self):
        try:
            index = self.details.selection()[0]
            query = mbx.askyesno('Confirm delete', "Do you want to delete this schedule?")
            if query is True:
                A_S_M_S_D.tim_delete(index)
                mbx.showinfo('', 'Deleted successfully')
                self.date_entry.delete(0, END)
                self.teacher_entry.set('')
                self.time_entry.delete(0, END)
                self.day_entry.set('')
                self.subject_entry.set('')
                self.clss_entry.set('')
                self.date_entry.insert(END, dt.today().date())
        except Exception:
            mbx.showinfo('Error', "Unexpected error, couldn't delete schedule!!")
            raise

    def clear_btn_command(self):
        self.date_entry.delete(0, END)
        self.teacher_entry.set('')
        self.time_entry.delete(0, END)
        self.day_entry.set('')
        self.subject_entry.set('')
        self.clss_entry.set('')
        self.date_entry.insert(END, dt.today().date())

    def refresh_btn_command(self):
        try:
            for children in self.details.get_children():
                self.details.delete(children)
            for data in A_S_M_S_D.tim_view_all():
                self.details.insert('', END, data[0], text=data[0])
                self.details.set(data[0], self.columns[0], data[1])
                # self.details.set(data[0], self.columns[1], data[2])
                self.details.set(data[0], self.columns[2], data[3])
                self.details.set(data[0], self.columns[3], data[4])
                # self.details.set(data[0], self.columns[4], data[5])
                self.details.set(data[0], self.columns[5], data[6])
                for tea in A_S_M_S_D.cls_teacher(data[2]):
                    self.details.set(data[0], self.columns[1], tea[0])
                for sub in A_S_M_S_D.tim_sub_name(data[5]):
                    self.details.set(data[0], self.columns[4], sub[0])
        except IndexError:
            pass
        except Exception:
            mbx.showinfo('Error', "Unexpected error, couldn't access the database\nPlease try again")
            raise

    def get_selected_row(self, event):
        try:
            index = self.details.selection()[0]
            self.date_entry.delete(0, END)
            self.teacher_entry.current(0)
            self.time_entry.delete(0, END)
            self.day_entry.current(0)
            self.subject_entry.current(0)
            self.clss_entry.current(0)
            for data in A_S_M_S_D.tim_get_selected_row(index):
                self.date_entry.insert(END, data[1])
                self.teacher_entry.set(data[2])
                self.time_entry.insert(END, data[3])
                self.day_entry.set(data[4])
                self.subject_entry.set(data[5])
                self.clss_entry.set(data[6])
        except Exception:
            raise
