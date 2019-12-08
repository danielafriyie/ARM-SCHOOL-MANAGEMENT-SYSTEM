from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mbx
from Main_Window import database

A_S_M_S_D = database.ArmDatabase('armdata.db')


class SubjectModuleWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.frame = Frame(self.master)
        self.frame.pack(expand=True, fill=BOTH)

        # Search
        self.search_frame = Frame(self.frame, bg='green')
        self.search_frame.pack(fill=X)

        self.ENF = ('courier', 12, 'bold')

        self.image = PhotoImage(file='Teacher\\Subject\\img.png')
        self.img_label = Label(self.search_frame, image=self.image, bg='green')
        self.img_label.grid(row=0, column=0, rowspan=6)

        self.search = Label(self.search_frame, bg='green', fg='white', font=('Arial', 13, 'bold'),
                            text='Enter Teacher Number')
        self.search.grid(row=1, column=1, sticky=W)
        self.search_entry = ttk.Entry(self.search_frame, width=35, font=self.ENF)
        self.search_entry.grid(row=1, column=2, ipady=5, padx=20, sticky=W)
        self.search_entry.bind('<Return>', self.search_command)

        self.date = Label(self.search_frame, bg='green', fg='white', font=('Arial', 13, 'bold'),
                          text='Date')
        self.date.grid(row=2, column=1, sticky=W)
        self.date_entry = ttk.Entry(self.search_frame, width=35, font=self.ENF)
        self.date_entry.grid(row=2, column=2, ipady=5, padx=20, sticky=W)

        self.name = Label(self.search_frame, bg='green', fg='white', font=('Arial', 13, 'bold'),
                          text='Name')
        self.name.grid(row=3, column=1, sticky=W)
        self.name_entry = ttk.Entry(self.search_frame, width=35, font=self.ENF)
        self.name_entry.grid(row=3, column=2, ipady=5, padx=20, sticky=W)

        self.phone = Label(self.search_frame, bg='green', fg='white', font=('Arial', 13, 'bold'),
                           text='Phone')
        self.phone.grid(row=4, column=1, sticky=W)
        self.phone_entry = ttk.Entry(self.search_frame, width=35, font=self.ENF)
        self.phone_entry.grid(row=4, column=2, ipady=5, padx=20, sticky=W)

        self.email = Label(self.search_frame, bg='green', fg='white', font=('Arial', 13, 'bold'),
                           text='Email')
        self.email.grid(row=5, column=1, sticky=W)
        self.email_entry = ttk.Entry(self.search_frame, width=35, font=self.ENF)
        self.email_entry.grid(row=5, column=2, ipady=5, padx=20, sticky=W)

        # Display tree
        self.display_frame = Frame(self.frame, bg='green')
        self.display_frame.pack(expand=True, fill=BOTH)

        self.display_tree = ttk.Treeview(self.display_frame)
        self.display_tree.pack(expand=True, fill=BOTH, side=LEFT)

        self.scroll = ttk.Scrollbar(self.display_frame, command=self.display_tree.yview)
        self.display_tree.config(yscrollcommand=self.scroll.set)
        self.scroll.pack(side=LEFT, fill=Y)

        # display tree column and heading names
        self.columns = ('date', 'name', 'code')
        self.headings = ('Date', 'Subject Name', 'Subject Code')
        self.display_tree.config(columns=self.columns)

        for col in self.columns:
            if col == 'date':
                col_width = 100
            elif col == "name":
                col_width = 350
            elif col == "code":
                col_width = 100
            self.display_tree.column(col, width=col_width, anchor=CENTER)
        counter = 0
        for col in self.columns:
            self.display_tree.heading(col, text=self.headings[counter])
            counter += 1
        self.display_tree.column('#0', width=100, anchor=CENTER)
        self.display_tree.heading("#0", text="ID")

    def search_command(self, event):
        try:
            self.date_entry.delete(0, END)
            self.name_entry.delete(0, END)
            self.phone_entry.delete(0, END)
            self.email_entry.delete(0, END)
            for children in self.display_tree.get_children():
                self.display_tree.delete(children)
            for data in A_S_M_S_D.tea_t_data(self.search_entry.get().title()):
                self.date_entry.insert(END, data[1])
                self.name_entry.insert(END, data[2])
                self.phone_entry.insert(END, data[3])
                self.email_entry.insert(END, data[4])
                for subj in data[5].strip("()").replace("'", "").split(','):
                    print(subj.strip(' '))
                    for s in A_S_M_S_D.tea_c_sub(subj.strip(' ')):
                        self.display_tree.insert('', END, s[0], text=s[0])
                        self.display_tree.set(s[0], self.columns[0], s[1])
                        self.display_tree.set(s[0], self.columns[1], s[2])
                        self.display_tree.set(s[0], self.columns[2], s[3])
        except Exception:
            mbx.showinfo('Error', 'Unexpected error, please try again!')
            raise
