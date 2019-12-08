from tkinter import *
from tkinter import ttk
from datetime import datetime as dt
from Main_Window import database
from tkinter import messagebox as mbx
from sqlite3 import IntegrityError, Error

A_S_M_S_D = database.ArmDatabase('armdata.db')


class SubjectModuleWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.frame = Frame(self.master)
        self.frame.pack(expand=True, fill=BOTH)
        self.font = ('Times New Roman', 15)

        # Credentials frame
        self.credentials_frame = LabelFrame(self.frame, text='Add/Edit Subject', bg='green', fg='white', font=self.font)
        self.credentials_frame.pack(fill=X)

        # Subjects details frame
        self.details_frame = LabelFrame(self.frame, text='Subject Details', bg='green', fg='white', font=self.font)
        self.details_frame.pack(fill=BOTH, expand=True)

        # Subject credentials
        self.TNF = ('Times New Roman', 14)
        self.ENF = ('courier', 12, 'bold')

        self.time_image = PhotoImage(
            file='Admin\\SubjectModule\\subject.png')
        self.time_image_label = Label(self.credentials_frame, image=self.time_image, bg='green')
        self.time_image_label.grid(row=0, column=0, rowspan=4)

        self.date = Label(self.credentials_frame, text='Date', font=self.TNF, bg='green', fg='white')
        self.date.grid(row=1, column=1, sticky=NW, padx=20)
        self.date_entry = ttk.Entry(self.credentials_frame, font=self.ENF)
        self.date_entry.delete(0, END)
        self.date_entry.insert(END, dt.today().date())
        self.date_entry.grid(row=1, column=2, sticky=NW)

        self.name = Label(self.credentials_frame, text='Subject Name', font=self.TNF, bg='green', fg='white')
        self.name.grid(row=2, column=1, sticky=NW, padx=20)
        self.name_entry = ttk.Entry(self.credentials_frame, width=35, font=self.ENF)
        self.name_entry.grid(row=2, column=2, sticky=NW)

        self.code = Label(self.credentials_frame, text='Subject Code', font=self.TNF, bg='green', fg='white')
        self.code.grid(row=3, column=1, sticky=NW, padx=20)
        self.code_entry = ttk.Entry(self.credentials_frame, width=35, font=self.ENF)
        self.code_entry.grid(row=3, column=2, sticky=NW)

        # Class details display
        self.details = ttk.Treeview(self.details_frame)
        self.details.pack(side=LEFT, expand=True, fill=BOTH)
        self.details.bind("<<TreeviewSelect>>", self.highlight_select)

        # ================= Treeview Column names and headings ===============
        self.columns = ('date', 's_name', 's_code')
        self.headings = ('Date', 'Subject Name', 'Subject Code')
        self.details.config(columns=self.columns)
        for col in self.columns:
            if col == 'date':
                col_width = 100
            elif col == "s_name":
                col_width = 350
            elif col == "s_code":
                col_width = 100
            self.details.column(col, width=col_width, anchor=CENTER)
        counter = 0
        for col in self.columns:
            self.details.heading(col, text=self.headings[counter])
            counter += 1
        self.details.column('#0', width=100, anchor=CENTER)
        self.details.heading("#0", text="Subject ID")

        self.details_scroll = ttk.Scrollbar(self.details_frame)
        self.details_scroll.pack(side=LEFT, fill=Y)
        self.details.config(yscrollcommand=self.details_scroll.set)
        self.details_scroll.config(command=self.details.yview)

        self.btn_font = ("Times New Roman", 12, 'bold')
        self.btn_frame = LabelFrame(self.details_frame, text='Buttons')
        self.btn_frame.pack()

        self.add_btn = Button(self.details_frame, text='Add New', relief=FLAT, bg='#000000', fg='#b7f731', width=10,
                              height=1, font=self.btn_font, pady=5, activebackground='black',
                              activeforeground='white', command=self.add_btn_command)
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

    #############################################
    #       BUTTONS COMMANDS
    #############################################
    def add_btn_command(self):
        try:
            if self.date_entry.get() == '' or self.name_entry.get() == '' or self.code_entry.get() == '':
                mbx.showinfo('Incomplete details', 'Please fill the necessary entries')
            else:
                query = mbx.askyesno('Confirm Subject', 'Do you want to add this subject?')
                if query is True:
                    A_S_M_S_D.sub_add_new(
                        self.date_entry.get(),
                        self.name_entry.get(),
                        self.code_entry.get()
                    )
                    mbx.showinfo('', 'Subject Added Successfully')
                    self.name_entry.delete(0, END)
                    self.code_entry.delete(0, END)
                else:
                    pass
        except Exception:
            mbx.showinfo('Error', "Unexpected error, couldn't add subject")
            raise

    def clear_btn_command(self):
        self.name_entry.delete(0, END)
        self.code_entry.delete(0, END)

    def refresh_btn_command(self):
        for children in self.details.get_children():
            self.details.delete(children)
        for sub in A_S_M_S_D.sub_view_all():
            self.details.insert('', END, sub[0], text=sub[0])
            self.details.set(sub[0], self.columns[0], sub[1])
            self.details.set(sub[0], self.columns[1], sub[2])
            self.details.set(sub[0], self.columns[2], sub[3])

    def delete_btn_command(self):
        index = self.details.selection()
        try:
            query = mbx.askyesno('Confirm Delete', 'Do you want to delete this subject?')
            if query is True:
                A_S_M_S_D.sub_delete(index[0])
                mbx.showinfo('', 'Subject Deleted Successfully')
                self.name_entry.delete(0, END)
                self.code_entry.delete(0, END)
        except Exception:
            print('Unexpected Error << check delete_btn_command >>')
            mbx.showinfo('Error', "Unexpected error, couldn't delete this subject.")
            raise

    def highlight_select(self, event):
        index = self.details.selection()
        self.name_entry.delete(0, END)
        self.code_entry.delete(0, END)
        for data in A_S_M_S_D.sub_highlight_select(index[0]):
            self.name_entry.insert(END, data[2])
            self.code_entry.insert(END, data[3])

    def update_btn_command(self):
        index = self.details.selection()
        try:
            query = mbx.askyesno('Confirm Update', 'Do you want to update this subject?')
            if query is True:
                A_S_M_S_D.sub_update(
                    index[0],
                    self.name_entry.get(),
                    self.code_entry.get()
                )
                mbx.showinfo('', 'Subject updated successfully')
                self.name_entry.delete(0, END)
                self.code_entry.delete(0, END)
            else:
                pass
        except Exception:
            print('Unexpected Error << check update_btn_command >>')
            mbx.showinfo('Error', "Unexpected error, couldn't update this subject.")
            raise
