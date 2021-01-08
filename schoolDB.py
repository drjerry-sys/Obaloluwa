from tkinter import *
import tkinter.ttk as ttk
import random
from tkinter.messagebox import *
from tkinter.filedialog import *
import shutil, datetime, time
from tkcalendar import DateEntry
from PIL import Image, ImageTk
import mysql.connector
class SDBM:
    class_id = ''
    student_id = ''
    def __init__(self):
        self.root = Tk()
        self.root.geometry('500x600')
        self.root.iconbitmap(r'images/pgs.ico')
        self.root.title('Practising Grammar School')
        self.root.config(bg='#C8C5E2')
        self.root.maxsize(500, 600)
        self.startupPage()
        self.resultNinfo = ''
        self.mycon = ""
        self.teacherScoreIndex = 1
        self.keepCourseId = []
        self.root.mainloop()

    def dbconnection(self):
        try:
            self.mycon = mysql.connector.connect(host='localhost', user='root', password='', database='school_DB')
            self.mycursor = self.mycon.cursor()
        except:
            showwarning("Connection Error", "Server is not running. Please run your server")

    def startupPage(self):
        self.initialframe = Frame(self.root, width=500, height=600, bg='#C8C5E2')
        self.initialframe.grid(row=0, column=0)
        Label(self.initialframe, text='P R A C T I S I N G  G R A M M A R  S C H O O L', font=('AvantGarde Bk BT', 10, 'bold'), bg='#C8C5E2').place(x=93, y=0)
        Label(self.initialframe, text='WELCOME!', font=('AvantGarde Bk BT', 15), bg='#3E4095', fg='#ffffff').place(x=196, y=180)
        Label(self.initialframe, text='Login as:', font=('AvantGarde Bk BT', 12), bg='#C8C5E2').place(x=217, y=210)
        self.student = Button(self.initialframe, text='STUDENT', font=('AvantGarde Bk BT', 12, 'bold', 'underline'),bg='#C8C5E2', cursor='hand2', bd=0, command=lambda: self.loginpage('std'))
        self.student.place(x=206, y=240)
        self.staff = Button(self.initialframe, text='STAFF', font=('AvantGarde Bk BT', 12, 'bold', 'underline'),bg='#C8C5E2', cursor='hand2', bd=0, command=lambda: self.loginpage('stf'))
        self.staff.place(x=218, y=270)

    def loginpage(self, who):
        self.initialframe.destroy()
        self.person = who
        self.initialframe = Frame(self.root, width=500, height=600, bg='#C8C5E2')
        self.initialframe.grid(row=0, column=0)
        Label(self.initialframe, text='PRACTISING GRAMMAR SCHOOL', font=('AvantGarde Bk BT', 15), bg='#C8C5E2').place(x=85, y=0)
        self.studentframe = Frame(self.initialframe, bg='#3E4095', height=150, width=264)
        self.studentframe.place(x=120, y=110)
        Frame(self.studentframe, height=14, width=264, bg='#3E4095').pack()
        self.loginframe = Frame(self.initialframe, bg='ivory', height=74, width=264)
        self.loginframe.place(x=120, y=258)
        self.entryframe = Frame(self.initialframe, bg='#3E4095', height=142, width=264)
        self.entryframe.place(x=120, y=328)
        Label(self.initialframe, text='© P R A C T I S I N G  G R A M M A R  S C H O O L', font=('AvantGarde Bk BT', 8),bg='#C8C5E2').place(y=580, x=125)
        self.image = Image.open('images/pgs1.png')
        self.logo = ImageTk.PhotoImage(self.image)
        self.logoframe = Frame(self.studentframe, height=95, width=105, bg='#3E4095')
        self.logoframe.pack(side='top', anchor='c')
        Label(self.logoframe, image=self.logo, height=95, width=105, bg='#3E4095').pack()
        if who == 'std':
            Label(self.studentframe, text='STUDENT', font=('AvantGarde Bk BT', 19, 'bold'), bg='#3E4095',fg='#ffffff').pack(side='left')
            Label(self.entryframe, text='Student ID:', fg='#ffffff', bg='#3E4095').place(x=10, y=10)
        else:
            Label(self.studentframe, text='STAFF', font=('AvantGarde Bk BT', 19, 'bold'), bg='#3E4095',fg='#ffffff').pack(side='left')
            Label(self.entryframe, text='Staff ID:', fg='#ffffff', bg='#3E4095').place(x=10, y=10)
        Label(self.loginframe, text=' Login', font=('AvantGarde Bk BT', 15), bg='#ffffff', fg='#000000').pack(side='top',anchor='w')
        Label(self.loginframe, text=' Practise Grammar School', font=('AvantGarde Bk BT', 10, 'bold'), bg='#ffffff',fg='#000000').pack(side='top', anchor='w')
        Label(self.loginframe, text=' ...practise makes perfection', font=('AvantGarde Bk BT', 8), bg='#ffffff',fg='#000000').pack(side='top', anchor='w')
        Frame(self.loginframe, width=264).pack(side='bottom')
        self.invarid = StringVar()
        self.invarpas = StringVar()
        Entry(self.entryframe, textvariable=self.invarid, width=25, font=('AvantGarde Bk BT', 8, 'bold'), justify='right').place(x=80, y=11)
        Label(self.entryframe, text='Password:', fg='#ffffff', bg='#3E4095').place(x=10, y=40)
        Entry(self.entryframe, textvariable=self.invarpas, width=25, show='•', font=('AvantGarde Bk BT', 8, 'bold'), justify='right').place(x=80, y=41)
        self.next = Frame(self.entryframe, width=264, height=22, bg='ivory')
        self.next.place(x=0, y=120)
        Button(self.entryframe, text='Submit', font=('AvantGarde Bk BT', 8, 'bold'), fg='#000000', bd=0, cursor='hand2', bg='ivory', command=self.userlogin).place(x=110, y=80)
        Button(self.next, text=' BACK', font=('AvantGarde Bk BT', 8, 'bold'), fg='#000000', bd=0, cursor='hand2', bg='ivory',command=self.startupPage).place(x=0, y=0)
        Button(self.next, text='EXIT', font=('AvantGarde Bk BT', 8, 'bold'), fg='#000000', bd=0, cursor='hand2', bg='#ffffff',command=self.root.quit).place(x=223, y=0)

    def userlogin(self):
        self.dbconnection()
        if self.mycon:
            if self.person == 'stf':
                self.mycursor.execute('SELECT Staff_aid, password FROM staffs_tb WHERE Staff_aid = %s and password = %s', (self.invarid.get(), self.invarpas.get()))
                self.myfetch = self.mycursor.fetchone()
                self.mycursor.execute('SELECT First_name FROM staffs_tb WHERE Staff_aid=%s', (self.invarid.get(),))
                self.myfetch_name = self.mycursor.fetchone()[0]
                if self.myfetch:
                    if self.myfetch[0][:5] == 'PGADM':
                        self.admin()
                    elif self.myfetch[0][:5] == 'PGSTF':
                        self.submit()
                    else:
                        showerror("Error", "Invalid login details supplied")
                else:
                    showerror("Error", "Invalid login details supplied")
            elif self.person == 'std':
                self.mycursor.execute('SELECT Student_aid, class_id FROM student_tb WHERE Student_aid = %s and password = %s', (self.invarid.get(), self.invarpas.get()))
                self.myfetch = self.mycursor.fetchone()
                SDBM.student_id = self.invarid.get()
                if self.myfetch:
                    SDBM.class_id = self.myfetch[1]
                    self.submit()
                else:
                    showerror("Error", "Invalid login details")
        # elif val == 2:
        #     self.in_path = askopenfilename(defaultextension='.jpg', filetypes=[('jpeg file','.jpeg'), ('png file','.png'),('jpg file','.jpg')])
        #     self.picentry.set(self.in_path)

    def admin(self):
        self.dbconnection()
        self.mycursor.execute("SELECT concat(First_name,' ',middle_name,' ',Last_name), job_title, title, First_name, Passport, Status_Value, Staff_aid FROM staffs_tb WHERE Staff_aid = %s",(self.invarid.get(),))
        self.myfetch = self.mycursor.fetchone()
        self.initialframe.destroy()
        self.initialframe = Frame(self.root, width=500, height=600)
        self.initialframe.place(x=0, y=0)
        self.labelframe = Frame(self.initialframe, width=231, height=600, bg='#3E4095')
        self.labelframe.place(x=0, y=0)
        self.imageframe = Frame(self.initialframe, width=269, height=600)
        self.imageframe.place(x=231, y=0)
        Label(self.labelframe, text='ADMIN', width=16, height=2, font=('AvantGarde Bk BT', 17, 'bold'), bg='#ffffff').place(x=12, y=10)
        Label(self.imageframe, width=45, height=4, text=f'PSG || {self.myfetch[2]} {self.myfetch[3]}', font=('AvantGarde Bk BT', 8), fg='#ffffff', bg='#3E4095').place(x=0, y=10)
        self.picframe = Frame(self.imageframe, width=182, height=202, bg='#C8C5E2')
        self.picframe.place(x=38, y=178)
        try:
            self.pic = Image.open(self.myfetch[4])
            self.picprocess = ImageTk.PhotoImage(self.pic)
            Label(self.picframe, image=self.picprocess).pack(anchor='c')
        except:
            pass
        Label(self.imageframe, text= self.myfetch[2] + ' ' + self.myfetch[3], width=18, bg='#3E4095', fg='#ffffff', font=('AvantGarde Bk BT', 13, 'bold')).place(x=40, y=153)
        Button(self.labelframe, text='BACK', width=10, font=('AvantGarde Bk BT', 8, 'bold'), bd=1, command=lambda: self.loginpage(self.person)).place(x=80, y=500)
        Button(self.labelframe, text='EXIT', width=10, font=('AvantGarde Bk BT', 8, 'bold'), bd=1, command=self.root.quit).place(x=80, y=525)
        Label(self.labelframe, text='PRACTISING GRAMMAR SCHOOL', bg='#3E4095', fg='#ffffff', font=('AvantGarde Bk BT', 8)).place(x=30, y=575)
        Label(self.labelframe, text='STAFF NAME:', bg='#3E4095', fg='#ffffff').place(x=141, y=390)
        self.jobtitle = Label(self.labelframe, text='JOB TITLE:', bg='#3E4095', fg='#ffffff')
        self.jobtitle.place(x=154, y=430)
        Label(self.labelframe, text='STAFF ID:', bg='#3E4095', fg='#ffffff').place(x=160, y=410)
        Label(self.imageframe, text=self.myfetch[0], fg='#000000').place(x=38, y=390)
        Label(self.imageframe, text=self.invarid.get(), fg='#000000').place(x=38, y=410)
        Label(self.imageframe, text=self.myfetch[1], fg='#000000').place(x=38, y=430)
        if self.myfetch[1].lower() == 'principal' and self.myfetch[5] == 'ACTIVE':
            Button(self.labelframe, text='Student', width=20, font=('AvantGarde Bk BT', 12, 'bold'), bg='#ffffff', bd=0,
                   cursor='hand2',command=lambda:self.admnstudent('1')).place(x=13, y=158)
            Button(self.labelframe, text='Mark Presence', width=20, font=('AvantGarde Bk BT', 12, 'bold'), cursor='hand2', bg='#ffffff', bd=0, command=self.markPresence).place(x=13, y=191)
            Button(self.labelframe, text='Staff', width=20, font=('AvantGarde Bk BT', 12, 'bold'), bg='#ffffff', cursor='hand2', bd=0, command=lambda:self.stafftop(1,1)).place(x=13, y=224)
            Button(self.labelframe, text='Write Report', width=20, font=('AvantGarde Bk BT', 12, 'bold'), bg='#ffffff', bd=0, command=lambda:self.writereport('r')).place(x=13, y=257)
            Button(self.labelframe, text='Chck/Upd Notice Board', width=20, font=('AvantGarde Bk BT', 12, 'bold'), bg='#ffffff', bd=0, command=lambda:self.noticeboard(1,0)).place(x=13, y=290)
            Button(self.labelframe, text='Exam/School Control', width=20, font=('AvantGarde Bk BT', 12, 'bold'), bg='#ffffff', bd=0, command=lambda:self.control(2)).place(x=13, y=323)
        elif self.myfetch[1].lower() == 'academic officer' and self.myfetch[5] == 'ACTIVE':
            Button(self.labelframe, text='Student', width=20, font=('AvantGarde Bk BT', 12, 'bold'), bg='#ffffff', bd=0, command=lambda:self.admnstudent('3')).place(x=13, y=160)
            Button(self.labelframe, text='Mark Presence', width=20, font=('AvantGarde Bk BT', 12, 'bold'), bg='#ffffff', bd=0, command=self.markPresence).place(x=13, y=193)
            Button(self.labelframe, text='Staff', width=20, font=('AvantGarde Bk BT', 12, 'bold'), bg='#ffffff', bd=0, command=lambda:self.stafftop(2)).place(x=13, y=226)
            Button(self.labelframe, text='Write Report', width=20, font=('AvantGarde Bk BT', 12, 'bold'), bg='#ffffff', bd=0, command=lambda:self.writereport('r')).place(x=13, y=259)
            Button(self.labelframe, text='Chck/Upd Notice Board', width=20, font=('AvantGarde Bk BT', 12, 'bold'), bg='#ffffff', bd=0, command=lambda:self.noticeboard(1,0)).place(x=13, y=292)
        elif self.myfetch[1].lower() == 'bursar' and self.myfetch[5] == 'ACTIVE':
                Button(self.labelframe, text='Student', width=20, font=('AvantGarde Bk BT', 12, 'bold'), bg='#ffffff',bd=0, command=lambda:self.admnstudent('2')).place(x=13, y=120)
                Button(self.labelframe, text='Mark Presence', width=20, font=('AvantGarde Bk BT', 12, 'bold'), bg='#ffffff', bd=0, command=self.markPresence).place(x=13, y=153)
                Button(self.labelframe, text='Staff', width=20, font=('AvantGarde Bk BT', 12, 'bold'), bg='#ffffff', bd=0).place(x=13, y=186)
                Button(self.labelframe, text='Write Report', width=20, font=('AvantGarde Bk BT', 12, 'bold'), bg='#ffffff', bd=0, command=lambda:self.writereport('r')).place(x=13, y=219)
                Button(self.labelframe, text='Chck/Upd Notice Board', width=20, font=('AvantGarde Bk BT', 12, 'bold'), bg='#ffffff', bd=0, command=lambda:self.noticeboard(1,0)).place(x=13, y=252)
        elif self.myfetch[1].lower() == 'proprietor':
                Button(self.labelframe, text='Staff', width=20, font=('AvantGarde Bk BT', 12, 'bold'), bg='#ffffff', bd=0, command=lambda:self.stafftop(1, 0)).place(x=13, y=176)
                Button(self.labelframe, text='Student', width=20, font=('AvantGarde Bk BT', 12, 'bold'), bg='#ffffff', bd=0, command=lambda:self.admnstudent('1')).place(x=13, y=209)
                Button(self.labelframe, text='Chck/Upd Notice Board', width=20, font=('AvantGarde Bk BT', 12, 'bold'), bg='#ffffff', bd=0, command=lambda:self.noticeboard(1,0)).place(x=13, y=242)
                Button(self.labelframe, text='View Report', width=20, font=('AvantGarde Bk BT', 12, 'bold'), bg='#ffffff', bd=0, command=lambda:self.writereport(4)).place(x=13, y=275)
                Button(self.labelframe, text='Exam/School Control', width=20, font=('AvantGarde Bk BT', 12, 'bold'), bg='#ffffff', bd=0, command=lambda:self.control(1)).place(x=13, y=308)
        else:
            showerror('PGS', 'Access Denied,\n See the Admin')

    def control(self, value):
        # value = 1 for proprietor and 2 for principal
        self.imageframe.destroy()
        self.imageframe = Frame(self.initialframe, width=269, height=600)
        self.imageframe.place(x=231, y=0)
        Label(self.imageframe, width=45, height=4, text='PSG || ' + self.myfetch_name, font=('AvantGarde Bk BT', 8), fg='#ffffff', bg='#3E4095').place(x=0, y=10)
        self.temporal = Frame(self.imageframe, height=249, width=264, bg='#DFDAEC')
        self.temporal.place(x=2, y=120)
        self.staffinvar = StringVar()
        self.staffinvar.set('Exam Control')
        Label(self.temporal, text='STUDENTS', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=1, y=0)
        options = ['Exam Control', 'Sessional/Term']
        self.staffoptionmenu = OptionMenu(self.temporal, self.staffinvar, *options)
        self.staffoptionmenu.config(bg='#BDBFC1', width=20, bd=1, relief=RIDGE)
        self.staffoptionmenu.place(x=38, y=80)
        Button(self.temporal, text='GO', bg='#00AFEF', width=10, fg='#ffffff', bd=0, cursor='hand2', command=lambda: self.ok('2')).place(x=94, y=115)
        Button(self.temporal, text='BACK', bg='#00AFEF', width=10, fg='#ffffff', bd=0, cursor='hand2', command=self.admin).place(x=94,y=140)

    def markPresence(self):
        self.dbconnection()
        self.time = datetime.datetime.now()
        if self.person == 'std':
            self.mycursor.execute('SELECT Day_Marked FROM presence_tb WHERE Student_aid = %s and Day_Marked = %s', (self.invarid.get(), str(self.time)[:10]))
        elif self.person == 'stf':
            self.mycursor.execute('SELECT Day_Marked FROM presence_tb WHERE Staff_aid = %s and Day_Marked = %s', (self.invarid.get(), str(self.time)[:10]))
        self.myfetch = self.mycursor.fetchone()
        if self.myfetch:
            showwarning('PGS', 'You can only Mark Presence\nonce in a day!')
        else:
            weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
            if (self.time.strftime('%A') in weekdays):
                if self.person == 'stf':
                    self.mycursor.execute("INSERT INTO presence_tb(Day_Marked, Time_Marked, Staff_aid, Weekday)\
                     VALUES(%s,%s,%s,%s)",(str(self.time)[:10], str(self.time)[11:16], self.invarid.get(), self.time.strftime('%A')))
                elif self.person == 'std':
                    self.mycursor.execute("INSERT INTO presence_tb(Day_Marked, Time_Marked, Student_aid, Weekday)\
                    VALUES(%s,%s,%s,%s)",(str(self.time)[:10], str(self.time)[11:16], self.invarid.get(), self.time.strftime('%A')))
                self.mycon.commit()
                showinfo('PGS', 'Present Today.')
            else: showerror('PGS', 'Today is not a working day')

    def submit(self):
        self.initialframe.destroy()
        self.initialframe = Frame(self.root, width=500, height=600)
        self.initialframe.grid(row=0, column=0)
        self.imageframe = Frame(self.initialframe, width=269, height=600)
        self.imageframe.place(x=231, y=0)
        self.labelframe = Frame(self.initialframe, width=231, height=463, bg='#3E4095')
        self.labelframe.pack(side='top', anchor='w')
        Frame(self.initialframe, height=9, width=231).pack(side='top', anchor='w')
        self.discriptionframe = Frame(self.initialframe, width=500, height=128, bg='#3E4095')
        self.discriptionframe.pack(side='top')
        self.studentpageframe = Frame(self.labelframe, width=204, height=67, bg='#ffffff')
        self.studentpageframe.place(x=13, y=13)
        self.picframe = Frame(self.imageframe, width=182, height=202, bg='#C8C5E2')
        self.picframe.place(x=37, y=158)
        Label(self.labelframe, text='© P R A C T I S I N G  G R A M M A R  S C H O O L', font=('AvantGarde Bk BT', 6, 'bold'), bg='#3E4095', fg='#ffffff').place(x=19, y=445)
        Button(self.discriptionframe, text='LOG OUT', font=('AvantGarde Bk BT', 8), width=20, command=lambda: self.loginpage(self.person)).place(x=192, y=97)
        if self.person == 'std':
            self.dbconnection()
            self.mycursor.execute('SELECT First_name, Middle_name, Passport, class_tb.Qualifier, class_tb.Class_name, \
            Student_aid, Status_Value FROM student_tb JOIN class_tb USING(class_id) WHERE Student_aid = %s and Password = %s',(self.invarid.get(), self.invarpas.get()))
            self.myfetchstd = self.mycursor.fetchone()
            if self.myfetchstd[6] == 'ACTIVE':
                self.pic = Image.open(self.myfetchstd[2])
                self.picprocess = ImageTk.PhotoImage(self.pic)
                Label(self.picframe, image=self.picprocess).pack(anchor='c')
                Label(self.studentpageframe, text='STUDENT\nPAGE', font=('AvantGarde Bk BT', 17, 'bold'),bg='#ffffff').place(x=42, y=3)
                Label(self.discriptionframe, text='STUDENT NAME:', font=('AvantGarde Bk BT', 8), bg='#3E4095', fg='#ffffff').place(x=110, y=15)
                Label(self.discriptionframe, text=f'{self.myfetchstd[0]} {self.myfetchstd[1]}', font=('AvantGarde Bk BT', 8), bg='#3E4095', fg='#ffffff').place(x=200, y=15)
                Label(self.discriptionframe, text='STUDENT ID:', font=('AvantGarde Bk BT', 8), bg='#3E4095', fg='#ffffff').place(x=130, y=35)
                Label(self.discriptionframe, text=self.myfetchstd[5], font=('AvantGarde Bk BT', 8), bg='#3E4095', fg='#ffffff').place(x=200, y=35)
                Label(self.discriptionframe, text='CLASS:', font=('AvantGarde Bk BT', 8), bg='#3E4095', fg='#ffffff').place(x=152, y=55)
                Label(self.discriptionframe, text=self.myfetchstd[4], font=('AvantGarde Bk BT', 8), bg='#3E4095', fg='#ffffff').place(x=200, y=55)
                Label(self.imageframe, text=f'PGS || {self.myfetchstd[1]}\'s Page').place(x=60, y=1)
                Label(self.discriptionframe, text='DEPARTMENT:', font=('AvantGarde Bk BT', 8), bg='#3E4095', fg='#ffffff').place(x=120, y=75)
                Label(self.discriptionframe, text=self.myfetchstd[3], font=('AvantGarde Bk BT', 8), bg='#3E4095', fg='#ffffff').place(x=200, y=75)
                Label(self.imageframe, text=self.myfetchstd[1], width=18, bg='#3E4095', fg='#ffffff',font=('AvantGarde Bk BT', 13, 'bold')).place(x=272, y=130)
                Button(self.labelframe, text='Discussion Room', width=20, font=('AvantGarde Bk BT', 12, 'bold'), cursor='hand2',
                       bg='#ffffff', bd=0).place(x=13, y=120)
                Button(self.labelframe, text='Mark Attendance', width=20, font=('AvantGarde Bk BT', 12, 'bold'), cursor='hand2',
                       bg='#ffffff', bd=0, command=self.markPresence).place(x=13, y=153)
                Button(self.labelframe, text='Check Payment', width=20, font=('AvantGarde Bk BT', 12, 'bold'), cursor='hand2',
                       bg='#ffffff',bd=0, command=lambda:self.noticeboard(2,5)).place(x=13, y=186)
                self.mycursor.execute('SELECT Control_Value FROM control_tb WHERE Control_id=%s', (2,))
                self.myfetch = self.mycursor.fetchone()
                if self.myfetch[0] == '0':
                    Button(self.labelframe, text='Start Exam', width=20, state=DISABLED, font=('AvantGarde Bk BT', 12, 'bold'),
                           bg='#ffffff',bd=0, command=self.startexam).place(x=13, y=219)
                else:
                    Button(self.labelframe, text='Start Exam', width=20, font=('AvantGarde Bk BT', 12, 'bold'), cursor='hand2',
                           bg='#ffffff',bd=0, command=self.startexam).place(x=13, y=219)
                Button(self.labelframe, text='Check Result', width=20, font=('AvantGarde Bk BT', 12, 'bold'),
                       cursor='hand2', bg='#ffffff',bd=0, command=self.stdResultCheck).place(x=13, y=252)
                Button(self.labelframe, text='List of Courses', width=20, font=('AvantGarde Bk BT', 12, 'bold'), cursor='hand2',
                       bg='#ffffff', bd=0, command=lambda:self.noticeboard(2,3)).place(x=13, y=285)
                Button(self.labelframe, text='List of Books', width=20, font=('AvantGarde Bk BT', 12, 'bold'), cursor='hand2', bg='#ffffff',bd=0, command=lambda:self.noticeboard(2,4)).place(x=13, y=318)
                Button(self.labelframe, text='Check Notice Board', width=20, font=('AvantGarde Bk BT', 12, 'bold'), cursor='hand2',bg='#ffffff', bd=0, command=lambda: self.noticeboard(2, 2)).place(x=13, y=351)
            else: showinfo('PGS', 'Go and See the Admin')
        else:
            self.dbconnection()
            self.mycursor.execute("SELECT concat(title,' ', First_name,' ', middle_name), job_title, passport,\
             department, Status_Value, First_name FROM staffs_tb WHERE staff_aid = %s", (self.invarid.get(),))
            self.myfetch = self.mycursor.fetchone()
            if self.myfetch[4] == 'ACTIVE':
                self.pic = Image.open(self.myfetch[2])
                self.picprocess = ImageTk.PhotoImage(self.pic)
                Label(self.picframe, image=self.picprocess).pack(anchor='c')
                Label(self.studentpageframe, text='STAFF\nPAGE', font=('AvantGarde Bk BT', 17, 'bold'), bg='#ffffff').place(x=58, y=3)
                Label(self.imageframe, text=f'PGS || {self.myfetch[5]}\'s Page').place(x=60, y=1)
                Label(self.discriptionframe, text='STAFF NAME:', font=('AvantGarde Bk BT', 8), bg='#3E4095', fg='#ffffff').place(x=110, y=15)
                Label(self.discriptionframe, text=self.myfetch[5], font=('AvantGarde Bk BT', 8), bg='#3E4095', fg='#ffffff').place(x=200, y=15)
                Label(self.discriptionframe, text='STAFF ID:', font=('AvantGarde Bk BT', 8), bg='#3E4095', fg='#ffffff').place(x=130, y=35)
                Label(self.discriptionframe, text=f'{self.invarid.get().upper()}', font=('AvantGarde Bk BT', 8), bg='#3E4095', fg='#ffffff').place(x=200, y=35)
                Label(self.discriptionframe, text='JOB TITLE:', font=('AvantGarde Bk BT', 8), bg='#3E4095', fg='#ffffff').place(x=125, y=55)
                Label(self.discriptionframe, text=f'{self.myfetch[1]}', font=('AvantGarde Bk BT', 8), bg='#3E4095', fg='#ffffff').place(x=200, y=55)
                Label(self.discriptionframe, text='DEPARTMENT:', font=('AvantGarde Bk BT', 8), bg='#3E4095', fg='#ffffff').place(x=107, y=75)
                Label(self.discriptionframe, text=self.myfetch[3], font=('AvantGarde Bk BT', 8), bg='#3E4095', fg='#ffffff').place(x=200, y=75)
                Label(self.imageframe, text=self.myfetch[0], width=18, bg='#3E4095', fg='#ffffff',font=('AvantGarde Bk BT', 13, 'bold')).place(x=39, y=130)
                Button(self.labelframe, text='Discussion Room', width=20, cursor='hand2', font=('AvantGarde Bk BT', 12, 'bold'),bg='#ffffff', bd=0).place(x=13, y=120)
                Button(self.labelframe, text='Mark Presence', width=20, cursor='hand2', font=('AvantGarde Bk BT', 12, 'bold'),bg='#ffffff', bd=0, command=self.markPresence).place(x=13, y=153)
                Button(self.labelframe, text='Check Std Performance', width=20, font=('AvantGarde Bk BT', 12, 'bold'), bg='#ffffff', cursor='hand2',\
                       bd=0, command=lambda:self.stdCrsNperf('b')).place(x=13, y=186)
                self.mycursor.execute('SELECT Control_Value FROM control_tb WHERE Control_id = %s', (1,))
                self.myfetch = self.mycursor.fetchone()[0]
                if self.myfetch == '0':
                    Button(self.labelframe, text='Set Exam Ques', width=20, font=('AvantGarde Bk BT', 12, 'bold'),bd=0, state=DISABLED).place(x=13, y=219)
                else:
                    Button(self.labelframe, text='Set Exam Ques', width=20, font=('AvantGarde Bk BT', 12, 'bold'), cursor='hand2', bg='#ffffff',bd=0, command=lambda:self.staffSetExam(1)).place(x=13, y=219)
                Button(self.labelframe, text='My Course Students', width=20, font=('AvantGarde Bk BT', 12, 'bold'), cursor='hand2', bg='#ffffff',bd=0, command=lambda:self.stdCrsNperf('a')).place(x=13, y=252)
                Button(self.labelframe, text='My Course List', width=20, font=('AvantGarde Bk BT', 12, 'bold'), cursor='hand2', bg='#ffffff', bd=0, command=lambda:self.staffbuttonoptions('a')).place(x=13, y=285)
                Button(self.labelframe, text='My Course Books', width=20, font=('AvantGarde Bk BT', 12, 'bold'), cursor='hand2', bg='#ffffff',bd=0, command=lambda:self.staffbuttonoptions('b')).place(x=13, y=318)
                Button(self.labelframe, text='Check Notice Board', width=20, font=('AvantGarde Bk BT', 12, 'bold'),bg='#ffffff', bd=0, command=lambda: self.noticeboard(2, 2)).place(x=13, y=351)
            else:
                showinfo('PGS', 'Go and See the Admin')

    def writereport(self, who=None):
        self.report_or_Nboard = who
        self.imageframe.destroy()
        self.imageframe = Frame(self.initialframe, width=269, height=600)
        self.imageframe.place(x=231, y=0)
        self.temporal = Frame(self.initialframe, width=269, height=600)
        self.temporal.place(x=231, y=0)
        if who == 'r':
            Label(self.temporal, text='Report', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=2, y=0)
        elif who == 'n':
            Label(self.temporal, text='Notice Board', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=2, y=0)
            Label(self.temporal, text='Date to be Pasted:', fg='#000000').place(x=15, y=467)
            self.postingDate = DateEntry(self.temporal, background='darkblue', height=35, locale='en_US', date_pattern='y/mm/dd')
            self.postingDate.place(x=135, y=467)
        Label(self.temporal, text='Heading:', fg='#000000').place(x=15, y=50)
        self.reportheading = Entry(self.temporal, width=25, font=('courier', 13, 'bold'), bd=0)
        self.reportheading.place(x=5, y=70)
        Label(self.temporal, text='Body:', fg='#000000').place(x=15, y=95)
        self.reportbody = Text(self.temporal, width=32, height=12)
        self.reportbody.place(x=5, y=115)
        Label(self.temporal, text='Summary:', fg='#000000').place(x=15, y=310)
        self.reportsum = Text(self.temporal, width=32, height=8)
        self.reportsum.place(x=5, y=330)
        Button(self.temporal, text='SEND', bd=0, bg='#3E4095', fg='#ffffff', width=30, command=self.noticeboard_or_reportSend).place(x=25, y=510)
        Button(self.temporal, text='BACK', bd=0, bg='#3E4095', fg='#ffffff', width=30, command=self.admin).place(x=25, y=533)

    def noticeboard(self, val, course=None):
        if val==1:
            self.dbconnection()
            self.imageframe.destroy()
            self.imageframe = Frame(self.initialframe, width=526, height=600)
            self.imageframe.place(x=231, y=0)
            self.temporal = Frame(self.imageframe, height=526, width=264, bg='#DFDAEC')
            self.temporal.place(x=2, y=73)
            Label(self.imageframe, width=45, height=4, text='PSG || MR OBALOLUWA', font=('AvantGarde Bk BT', 8),fg='#ffffff', bg='#3E4095').place(x=0, y=10)
            if course == 0:
                self.dbconnection()
                self.present = str(datetime.datetime.now())[:10]
                Label(self.temporal, text='NOTICE BOARD', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=1, y=0)
                self.mycursor.execute('SELECT Heading, Body, Summary FROM noticeboard WHERE Post_Date = %s',
                                      (self.present,))
                self.myfetch = self.mycursor.fetchall()
                w, x, y, z = 42, 60, 123, 140
                for i in range(len(self.myfetch)):
                    Label(self.temporal, text=f'---{self.myfetch[i][0]}---', font=('Arial', 10, 'bold'),bg='#DFDAEC', width=33, height=1).place(x=0, y=w)
                    Message(self.temporal, text=self.myfetch[i][1], font=('Arial', 10), bg='#DFDAEC', width=263).place(x=0, y=x)
                    Label(self.temporal, text='Summarily:', font=('Arial', 8, 'bold'), bg='#DFDAEC').place(x=0, y=y)
                    Message(self.temporal, text=self.myfetch[i][2], font=('Arial', 10), bg='#DFDAEC', width=263).place(x=0, y=z)
                    w += 150
                    x += 168
                    y += 185
                    z += 202
                Button(self.temporal, text='UPDATE', bg='#3E4095', width=22, fg='#ffffff', bd=0, command=lambda:self.noticeboardupdate(0)).place(x=0, y=506)
            elif course == 1:
                Label(self.temporal, text='Students\' Courses', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=1,y=0)
                Button(self.temporal, text='UPDATE', bg='#3E4095', width=22, fg='#ffffff', bd=0, cursor='hand2', command=lambda:self.noticeboardupdate(1)).place(x=0, y=506)
            Button(self.temporal, text='BACK ', bg='red', width=15, fg='#ffffff', bd=0, cursor='hand2', command=self.admin).place(x=160, y=506)
        elif val == 2:
            self.dbconnection()
            v, h, j, w = 40, 60, 80, 40
            self.imageframe.destroy()
            self.imageframe = Frame(self.initialframe, width=269, height=462)
            self.imageframe.place(x=231, y=0)
            self.temporal = Frame(self.imageframe, height=462, width=264, bg='#DFDAEC')
            self.temporal.place(x=2, y=0)
            if course == 2:
                Label(self.temporal, text='NOTICE BOARD', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=1, y=0)
                self.present = str(datetime.datetime.now())[:10]
                self.mycursor.execute('SELECT Heading, Body, Summary FROM noticeboard WHERE Post_Date = %s', (self.present,))
                self.myfetch = self.mycursor.fetchall()
                w, x, y, z = 42, 60, 123, 140
                for i in range(len(self.myfetch)):
                    Label(self.temporal, text=f'---{self.myfetch[i][0]}---', font=('Arial', 10, 'bold', 'underline'), bg='#DFDAEC', width=33, height=1).place(x=0, y=w)
                    Message(self.temporal, text=self.myfetch[i][1], font=('Arial', 10), bg='#DFDAEC', width=263).place(x=0, y=x)
                    Label(self.temporal, text='Summarily:', font=('Arial', 8, 'bold'), bg='#DFDAEC').place(x=0, y=y)
                    Message(self.temporal, text=self.myfetch[i][2], font=('Arial', 10), bg='#DFDAEC', width=263).place(x=0, y=z)
                    w+=150
                    x+=168
                    y+=185
                    z+=202
            elif course == 3:
                Label(self.temporal, text='Courses', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=1,y=0)
                Label(self.temporal, text='Courses\n ', width=25, bg='#3E4095', fg='#ffffff').place(x=1, y=37)
                Label(self.temporal, text='Exam/Test\nDate&Time', width=10, bg='#3E4095', fg='#ffffff').place(x=183, y=37)
                self.mycursor.execute('SELECT Course_name, staffs_tb.title, staffs_tb.First_name,TestExam_TimeStart, TestExam_Date FROM course_tb JOIN \
                staffs_tb USING(staff_aid) JOIN class_tb USING(class_id) JOIN student_tb USING(class_id) WHERE Student_aid = %s',(self.invarid.get(),))
                self.myfetch = self.mycursor.fetchall()
                if self.myfetch:
                    v, h = 75, 95
                    for i in range(len(self.myfetch)):
                        Label(self.temporal, text=f'{str(i+1)}.)', bg='#DFDAEC', font=('Arial', 10, 'bold')).place(x=0, y=v)
                        Label(self.temporal, text=f'Subject: {self.myfetch[i][0]}', bg='#DFDAEC', font=('Arial', 10, 'bold')).place(x=17, y=v)
                        Label(self.temporal, text=f'Teacher: {self.myfetch[i][1]} {self.myfetch[i][2]}', bg='#DFDAEC', font=('Arial', 10, 'bold')).place(x=17, y=h)
                        Label(self.temporal, text=f'{self.myfetch[i][3]}\n{self.myfetch[i][4]}', bg='#DFDAEC', font=('Arial', 10, 'bold')).place(x=187, y=v)
                        v+=41
                        h+=41
            elif course == 4:
                Label(self.temporal, text='Lists Of Books', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=1,
                                                                                                                  y=0)
                self.mycursor.execute('SELECT Class_id FROM class_tb JOIN student_tb USING(class_id) WHERE Student_aid = %s',
                                      (self.invarid.get(),))
                self.myfetch = self.mycursor.fetchone()
                self.mycursor.execute('SELECT Book_Name, Author, Course_Name FROM books_tb JOIN course_tb\
                USING(Course_id) WHERE class_id = %s', (self.myfetch[0],))
                self.myfetch = self.mycursor.fetchall()
                for i in range(len(self.myfetch)):
                    Label(self.temporal, text=f'{str(i+1)}.)', bg='#DFDAEC', font=('Arial', 10, 'bold')).place(x=0, y=v)
                    Label(self.temporal, text=f'Subject: {self.myfetch[i][2]}', bg='#DFDAEC', font=('Arial', 10, 'bold')).place(x=17, y=v)
                    Label(self.temporal, text=f'Book: {self.myfetch[i][0]}', bg='#DFDAEC', font=('Arial', 10, 'bold')).place(x=17, y=h)
                    Label(self.temporal, text=f'Author: {self.myfetch[i][1]}', bg='#DFDAEC', font=('Arial', 10, 'bold')).place(x=17, y=j)
                    v += 61
                    h += 61
                    j += 61
            elif course == 5:
                self.dbconnection()
                self.mycursor.execute('SELECT Value_For, Session, Term, Date_Paid FROM payment_tb WHERE Student_aid = %s',(self.invarid.get(),))
                self.myfetch = self.mycursor.fetchall()
                Label(self.temporal, text='Payment History', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=1,y=0)
                for i in range(len(self.myfetch) + 1):
                    Label(self.temporal, text=f'{str(i + 1)}.)', bg='#DFDAEC').place(x=0, y=w)
                    w+=61
                    for k in self.myfetch:
                        Label(self.temporal, text=f'Payment For: {k[0]}', bg='#DFDAEC').place(x=17, y=v)
                        Label(self.temporal, text=f'Session/Term: {k[1]} || {k[2]}', bg='#DFDAEC').place(x=17, y=h)
                        Label(self.temporal, text=f'Date of Payment: {k[3]}', bg='#DFDAEC').place(x=17, y=j)
                        v += 61
                        h += 61
                        j += 61
                self.mycon.close()
            Button(self.temporal, text='CANCEL', bg='#00AFEF', fg='#ffffff', bd=0, width=34, font=('AvantGarde Bk BT', 10, 'bold'), command=self.submit).place(x=0, y=438)

    def askclasses(self):
        self.mycursor.execute(f'SELECT First_name, Middle_name, title FROM staffs_tb WHERE Staff_aid = %s',(self.invarid.get(),))
        self.myfetch = self.mycursor.fetchmany()
        self.temporal.destroy()
        self.imageframe.destroy()
        self.imageframe = Frame(self.initialframe, width=269, height=600)
        self.imageframe.place(x=231, y=0)
        self.temporal = Frame(self.imageframe, height=270, width=264, bg='#DFDAEC')
        self.temporal.place(x=2, y=120)
        Label(self.temporal, text='STUDENTS', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=1, y=0)
        Label(self.imageframe, width=45, height=4, text='PSG || MR OBALOLUWA', font=('AvantGarde Bk BT', 8),fg='#ffffff', bg='#3E4095').place(x=0, y=10)
        self.stu = Label(self.temporal, text='Student Info', bg='#3E4095', fg='#ffffff', width=37, height=1)
        self.stu.place(x=1, y=37)
        Label(self.temporal, text='JUNIOR CLASS', bg='#3E4095', fg='#ffffff', font=('AvantGarde Bk BT', 7)).place(x=20,y=90)
        Label(self.temporal, text='SENIOR CLASS', bg='#3E4095', fg='#ffffff', font=('AvantGarde Bk BT', 7)).place(x=170,y=90)
        self.invarclass = StringVar()
        Radiobutton(self.temporal, text='JSS 1', value='jss1', variable=self.invarclass, bg='#DFDAEC', tristatevalue=1).place(x=20, y=120)
        Radiobutton(self.temporal, text='JSS 2', value='jss2', variable=self.invarclass, bg='#DFDAEC', tristatevalue=1).place(x=20, y=140)
        Radiobutton(self.temporal, text='JSS 3', value='jss3', variable=self.invarclass, bg='#DFDAEC', tristatevalue=1).place(x=20, y=160)
        Radiobutton(self.temporal, text='SSS 1', value='sss1', variable=self.invarclass, bg='#DFDAEC', tristatevalue=1).place(x=170,y=120)
        Radiobutton(self.temporal, text='SSS 2', value='sss2', variable=self.invarclass, bg='#DFDAEC', tristatevalue=1).place(x=170,y=140)
        Radiobutton(self.temporal, text='SSS 3', value='sss3', variable=self.invarclass, bg='#DFDAEC', tristatevalue=1).place(x=170,y=160)
        self.classesgo = Button(self.temporal, text='GO', bg='#3E4095', fg='#ffffff', bd=0, width=10,command=lambda: self.ok('6'))
        self.classesgo.place(x=55, y=215)

    def controlOk(self, value):
        self.dbconnection()
        self.present = datetime.datetime.now()
        if value == 1:
            self.mycursor.execute('UPDATE control_tb SET Control_Value = %s, Last_Altered = %s WHERE Control_id=%s',
                                  (str(self.invarQuesControl.get()), str(self.present)[:10], 1))
            showinfo('PGS', 'Change Altered')
        elif value == 2:
            self.mycursor.execute('UPDATE control_tb SET Control_Value = %s, Last_Altered = %s WHERE Control_id=%s',
                                  (str(self.invarexamMode.get()), str(self.present)[:10], 2))
            showinfo('PGS', 'Change Altered')
        elif value == 3:
            self.mycursor.execute('SELECT Last_Altered FROM control_tb WHERE Control_id = %s', (4,))
            self.myfetch = self.mycursor.fetchone()[0]
            self.myfetch = self.myfetch.split('-')
            self.present1 = str(self.present)[:10].split('-')
            self.myfetch = [int(i[1]) if i[0] == '0' else int(i) for i in self.myfetch]
            self.present1 = [int(i[1]) if i[0] == '0' else int(i) for i in self.present1]
            self.date1 = datetime.date(self.myfetch[0], self.myfetch[1], self.myfetch[2])
            self.date2 = datetime.date(self.present1[0], self.present1[1], self.present1[2])
            self.diff = self.date2 - self.date1
            if self.diff.days > 70:
                self.mycursor.execute('SELECT lower(Control_Value) FROM control_tb WHERE Control_id = %s', (4,))
                self.myfetch = self.mycursor.fetchone()
                if self.myfetch[0] == 'first term':
                    self.mycursor.execute('UPDATE control_tb SET Control_Value = %s, Last_Altered = %s WHERE Control_id = %s', ('self.second Term', str(self.present)[:10], 4))
                elif self.myfetch[0] == 'self.second term':
                    self.mycursor.execute('UPDATE control_tb SET Control_Value = %s, Last_Altered = %s WHERE Control_id = %s', ('Third Term', str(self.present)[:10],4))
                elif self.myfetch[0] == 'third term':
                    self.mycursor.execute('UPDATE control_tb SET Control_Value = %s, Last_Altered = %s WHERE Control_id = %s', ('First Term', str(self.present)[:10],4))
                self.mycon.commit()
                self.ok('2')
            else:
                showerror('PGS', 'Changes can only be made after more \nthan 2-months after the begining of the term')
        elif value == 4:
            self.mycursor.execute('SELECT Last_Altered FROM control_tb WHERE Control_id = %s', (3,))
            self.myfetch = self.mycursor.fetchone()
            self.myfetch = self.myfetch[0]
            self.myfetch = self.myfetch.split('-')
            self.present1 = str(self.present)[:10].split('-')
            self.myfetch = [int(i[1]) if i[0] == '0' else int(i) for i in self.myfetch]
            self.present1 = [int(i[1]) if i[0] == '0' else int(i) for i in self.present1]
            self.date1 = datetime.date(self.myfetch[0], self.myfetch[1], self.myfetch[2])
            self.date2 = datetime.date(self.present1[0], self.present1[1], self.present1[2])
            self.diff = self.date2 - self.date1
            if self.diff.days > 180:
                self.mycursor.execute('SELECT Control_Value FROM control_tb WHERE Control_id = %s', (3,))
                self.myfetchl = self.mycursor.fetchone()[0]
                self.myfetchl = self.myfetchl.split('/')
                use1 = str(int(self.myfetchl[0]) + 1)
                use2 = str(int(self.myfetchl[1]) + 1)
                self.mycursor.execute('UPDATE control_tb SET Control_Value = %s, Last_Altered = %s WHERE Control_id = %s', (use1+'/'+use2, str(self.present)[:10], 3))
                self.mycursor.execute('UPDATE control_tb SET Control_Value = %s, Last_Altered = %s WHERE Control_id = %s', ('First Term', str(self.present)[:10], 4))
                self.mycon.commit()
                self.ok('2')
            else:
                showerror('PGS', 'Changes can only be made after more \nthan 6-months after the begining of the Session')
        elif value == '5':
            self.imageframe.destroy()
            self.imageframe = Frame(self.initialframe, width=269, height=600)
            self.imageframe.place(x=231, y=0)
            self.dbconnection()
            Label(self.imageframe, width=45, height=4, text='PSG || ' + self.myfetch_name, font=('AvantGarde Bk BT', 8),
                  fg='#ffffff', bg='#3E4095').place(x=0, y=10)
            self.temporal = Frame(self.imageframe, height=526, width=264, bg='#DFDAEC')
            self.temporal.place(x=2, y=73)
            Button(self.temporal, text='Ok', width=37, bg='#3E4095', fg='#ffffff', bd=0, command=self.examTimeSet, cursor='hand2').place(x=0, y=340)
            Label(self.temporal, text='Subject Time & Date', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=1, y=0)
            self.mycursor.execute('SELECT Course_id, Course_name FROM course_tb')
            self.myfetchSubDate = self.mycursor.fetchall()
            self.courseidNname = {i[1]:i[0] for i in self.myfetchSubDate}
            Label(self.temporal, text='Subject', bg='#DFDAEC').place(x=60,y=65)
            Label(self.temporal, text='Date and Time', bg='#DFDAEC').place(x=60,y=130)
            self.cobMySubject = ttk.Combobox(self.temporal, width=10, values=[i for i in self.courseidNname.keys()])
            self.cobMySubject.place(x=55, y=90)
            self.cobMySubject.set('Subject')
            self.cobDate = DateEntry(self.temporal, locale='en_US', date_pattern='y/mm/dd')
            self.cobDate.place(x=55, y=150)
            value = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24']
            self.cobTimeHour = ttk.Combobox(self.temporal, state='readonly', width=3)
            self.cobTimeHour.set('H')
            self.cobTimeHour.place(x=55, y=180)
            self.cobTimeHour.config(values=value)
            self.cobTimeMin = ttk.Combobox(self.temporal, state='readonly', width=3)
            self.cobTimeMin.set('M')
            self.cobTimeMin.place(x=55, y=210)
            self.cobTimeMin.config(values=['00','10','20','30','40','50'])
        self.mycon.commit()

    def examTimeSet(self):
        self.dbconnection()
        self.exam_time = self.cobTimeHour.get() + ':' + self.cobTimeMin.get()
        self.date = str(self.cobDate.get()).replace('/','-')
        self.mycursor.execute('UPDATE course_tb SET TestExam_TimeStart=%s, TestExam_Date=%s WHERE Course_id=%s',
                              (self.exam_time, self.date, self.courseidNname[self.cobMySubject.get()]))
        self.mycon.commit()
        showinfo('PGS', 'Changes Confirmed')
        self.cobTimeHour.set('H')
        self.cobTimeMin.set('M')

    def stdResultCheck(self):
        self.dbconnection()
        self.imageframe.destroy()
        self.imageframe = Frame(self.initialframe, width=269, height=462)
        self.imageframe.place(x=231, y=0)
        self.temporal = Frame(self.imageframe, height=462, width=264, bg='#DFDAEC')
        self.temporal.place(x=2, y=0)
        Label(self.temporal, text='My Result', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=1, y=0)
        Label(self.temporal, text='S/N', width=3, bg='#3E4095', fg='#ffffff').place(x=1, y=37)
        Label(self.temporal, text='Type', width=7, bg='#3E4095', fg='#ffffff').place(x=30, y=37)
        Label(self.temporal, text='Subject', width=17, bg='#3E4095', fg='#ffffff').place(x=87, y=37)
        Label(self.temporal, text='Score', width=7, bg='#3E4095', fg='#ffffff').place(x=214, y=37)
        Button(self.temporal, text='CANCEL', bg='#00AFEF', fg='#ffffff', bd=0, width=34,
               font=('AvantGarde Bk BT', 10, 'bold'), command=self.submit).place(x=0, y=438)
        self.mycursor.execute('SELECT Score, Course_name, Type FROM result_tb JOIN course_tb USING(Course_id) WHERE\
         Student_aid = %s and Session_=(SELECT Control_Value FROM control_tb WHERE Control_id=%s) and \
         Term = (SELECT Control_Value FROM control_tb WHERE Control_id=%s) ORDER BY Type', (self.invarid.get(), 3, 4))
        self.myfetchres = self.mycursor.fetchall()
        # self.myfetchres.clear()
        if self.myfetchres:
            y =60
            self.res_count = 1
            for i in self.myfetchres:
                if i[2] == 'Test':
                    Label(self.temporal, text=f'{self.res_count}.)      {i[2]}      {i[1]}\t{i[0]}', font=('Arial', 10, 'bold'), bg='#DFDAEC').place(x=1, y=y)
                else:
                    Label(self.temporal, text=f'{self.res_count}.)      {i[2]}    {i[1]}\t{i[0]}',
                          font=('Arial', 10, 'bold'), bg='#DFDAEC').place(x=1, y=y)
                y+=20
                self.res_count+=1
        else:
            Label(self.temporal, text='No Result\nYet', font=('Arial', 25, 'bold'), bg='#DFDAEC').place(x=55, y=105)

    def ok(self, val, val2=None):
        self.mycursor.execute('SELECT concat(title, \' \', First_name) FROM staffs_tb WHERE Staff_aid = %s', (self.invarid.get(),))
        self.myfetch = self.mycursor.fetchone()
        if val == '1':
            if val2 == 0:
                getting = self.writepad.get(1.0, END)
                showinfo('PGS', 'Notice Board Updated')
                self.noticeboard(1, 0)
            elif val2 == 1:
                getting = self.writepad.get(1.0, END)
                showinfo('PGS', 'Course Updated')
                self.noticeboard(1, 1)
        elif val == '2':
            if self.staffinvar.get() == 'Students Access':
                self.temporal.destroy()
                self.temporal = Frame(self.imageframe, height=249, width=264, bg='#DFDAEC')
                self.temporal.place(x=2, y=120)
                Label(self.temporal, text='STUDENTS', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=1, y=0)
                Label(self.imageframe, width=45, height=4, text=f'PSG || {self.myfetch_name}', font=('AvantGarde Bk BT', 8), fg='#ffffff', bg='#3E4095').place(x=0, y=10)
                Label(self.temporal, text='Students Access', bg='#3E4095', fg='#ffffff', width=37, height=1).place(x=1, y=37)
                Label(self.temporal, text='Student Id:', bg='#DFDAEC').place(x=32, y=100)
                self.stfinvar = StringVar()
                self.stfentry = Entry(self.temporal, textvariable=self.stfinvar, width=15, font=('AvantGarde Bk BT', 10, 'bold'))
                self.stfentry.place(x=95, y=100)
                Button(self.temporal, text='REVOKE', bg='#00AFEF', width=12, fg='#ffffff', bd=0, command=lambda: self.ok('4', 'r')).place(x=129, y=160)
                Button(self.temporal, text='INACTIVE', bg='#00AFEF', width=12, fg='#ffffff', bd=0, command=lambda: self.ok('4', 'i')).place(x=35, y=185)
                Button(self.temporal, text='ENABLE', bg='#00AFEF', width=12, fg='#ffffff', bd=0, command=lambda: self.ok('4', 'a')).place(x=35, y=160)
                if self.dvalue == '1':
                    Button(self.temporal, text='BACK', bg='#00AFEF', fg='#ffffff', bd=0, width=12,command=lambda: self.admnstudent('1')).place(x=129, y=185)
                elif self.dvalue == '2':
                    Button(self.temporal, text='BACK', bg='#00AFEF', fg='#ffffff', bd=0, width=12,command=lambda: self.admnstudent('2')).place(x=129, y=185)
                elif self.dvalue == '3':
                    Button(self.temporal, text='BACK', bg='#00AFEF', fg='#ffffff', bd=0, width=12,command=lambda: self.admnstudent('3')).place(x=129, y=185)
            elif self.staffinvar.get() == 'Total Number of Students':
                self.dbconnection()
                self.mycursor.execute("SELECT count(Student_aid) FROM student_tb")
                self.myfetch = self.mycursor.fetchone()
                showinfo('PGS', f'You have {self.myfetch[0]} Students in total.')
            elif self.staffinvar.get() == 'Print Receipt':
                self.imageframe.destroy()
                self.imageframe = Frame(self.initialframe, width=269, height=600)
                self.imageframe.place(x=231, y=0)
                Label(self.imageframe, width=45, height=4, text='PSG || MR OBALOLUWA', font=('AvantGarde Bk BT', 8),fg='#ffffff', bg='#3E4095').place(x=0, y=10)
                self.temporal = Frame(self.imageframe, height=43, width=264, bg='#DFDAEC')
                self.temporal.place(x=2, y=74)
                Label(self.temporal, text='Reg No:', bg='#3E4095', fg='#ffffff').place(x=10, y=8)
                Entry(self.temporal, width=10, font=('Courier', 15,'bold'), bd=0).place(x=62, y=6)
                Button(self.temporal, text='OK', fg='#ffffff', bg='darkred', bd=0).place(x=185, y=9)
                Button(self.temporal, text='BACK', fg='#ffffff', bg='red', bd=0, command=self.admin).place(x=210, y=9)
                self.temporal = Frame(self.imageframe, height=252, width=264, bg='#DFDAEC')
                self.temporal.place(x=2, y=120)
                Label(self.temporal, text='Receipt', width=38, height=1, bg='#3E4095', fg='#ffffff').place(x=0, y=0)
                lst = ['Name:','Reg No:','Class:','Department:','Amount Paid:','Date Issued:','Signature:','Value:','Session:','Term:']
                v=26
                for nid in lst:
                    Label(self.temporal, text=nid, bg='#DFDAEC').place(x=0, y=v)
                    v += 20
                Button(self.temporal, text='Print', width=33, bg='#3E4095', fg='#ffffff', bd=0).place(x=15, y=228)
            elif self.staffinvar.get() == 'Payment History':
                self.imageframe.destroy()
                self.imageframe = Frame(self.initialframe, width=269, height=600)
                self.imageframe.place(x=231, y=0)
                Label(self.imageframe, width=45, height=4, text='PSG || MR OBALOLUWA', font=('AvantGarde Bk BT', 8),fg='#ffffff', bg='#3E4095').place(x=0, y=10)
                self.temporal = Frame(self.imageframe, height=43, width=264, bg='#DFDAEC')
                self.temporal.place(x=2, y=74)
                Label(self.temporal, text='Reg No:', bg='#3E4095', fg='#ffffff').place(x=10, y=8)
                Entry(self.temporal, width=10, font=('Courier', 15,'bold'), bd=0).place(x=62, y=6)
                Button(self.temporal, text='OK', fg='#ffffff', bg='darkred', bd=0).place(x=185, y=9)
                Button(self.temporal, text='BACK', fg='#ffffff', bg='red', bd=0, command=self.admin).place(x=210, y=9)
                self.temporal = Frame(self.imageframe, height=450, width=264, bg='#DFDAEC')
                self.temporal.place(x=2, y=120)
                Label(self.temporal, text='Receipt', width=38, height=1, bg='#3E4095', fg='#ffffff').place(x=0, y=0)
                Button(self.temporal, text='Print', width=33, bg='#3E4095', fg='#ffffff', bd=0).place(x=15, y=500)
            elif (self.staffinvar.get() == 'School Fee') or (self.staffinvar.get() == 'Special Funds'):
                self.imageframe.destroy()
                self.imageframe = Frame(self.initialframe, width=269, height=600)
                self.imageframe.place(x=231, y=0)
                Label(self.imageframe, width=45, height=4, text=f'PSG || MR {self.myfetch_name}', font=('AvantGarde Bk BT', 8),fg='#ffffff', bg='#3E4095').place(x=0, y=10)
                self.temporal = Frame(self.imageframe, height=252, width=264, bg='#DFDAEC')
                self.temporal.place(x=2, y=120)
                Label(self.temporal, text='School Fee', width=38, height=2, bg='#3E4095', fg='#ffffff').place(x=0, y=0)
                Label(self.temporal, text='Reg No:', bg='#DFDAEC', fg='#000000').place(x=10, y=88)
                Label(self.temporal, text='Amount:', bg='#DFDAEC', fg='#000000').place(x=10, y=116)
                Entry(self.temporal, width=12, font=('Courier', 15,'bold'), bd=0).place(x=62, y=88)
                Entry(self.temporal, width=12, font=('Courier', 15,'bold'), bd=0).place(x=62, y=116)
                Button(self.temporal, text='OK', width=37, bg='#3E4095', fg='#ffffff', bd=0).place(x=0, y=205)
                if self.staffinvar.get() == 'Special Funds':
                    Label(self.temporal, text='Fund\nName:', bg='#DFDAEC', fg='#000000').place(x=10, y=140)
                    Entry(self.temporal, width=12, font=('Courier', 15, 'bold'), bd=0).place(x=62, y=146)
                Button(self.temporal, text='BACK', width=37, bg='darkred', fg='#ffffff', bd=0, command=self.admin).place(x=0, y=228)
            elif self.staffinvar.get() == 'Lists of Books':
                self.resultNinfo = 2
                self.askclasses()
                self.stu.config(text='Lists of Books')
                self.classesgo.config(command=lambda:self.ok('6'))
                if self.dvalue == '1':
                    Button(self.temporal, text='BACK', bg='#3E4095', fg='#ffffff', bd=0, width=10, command=lambda:self.admnstudent('1')).place(x=132, y=215)
                elif self.dvalue == '2':
                    Button(self.temporal, text='BACK', bg='#3E4095', fg='#ffffff', bd=0, width=10, command=lambda: self.admnstudent('2')).place(x=132, y=215)
                elif self.dvalue == '3':
                    Button(self.temporal, text='BACK', bg='#3E4095', fg='#ffffff', bd=0, width=10, command=lambda: self.admnstudent('3')).place(x=132, y=215)
            elif (self.staffinvar.get() == 'Register Student'):
                self.temporal.destroy()
                self.temporal = Frame(self.imageframe, height=526, width=264, bg='#DFDAEC')
                self.temporal.place(x=2, y=73)
                Label(self.temporal, text='STUDENTS', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=1, y=0)
                Label(self.temporal, text='Student Registration', bg='#3E4095', fg='#ffffff', width=37, height=1).place(x=1, y=37)
                self.invarfname, self.invarsname, self.invarlname, self.invaradres, self.invardob = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
                self.invarphone, self.invaremail, self.invarfather, self.invarmother, self.invarkin, self.invarreligion = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
                self.invarlanguage, self.invarsess, self.invarstate, self.invartown, self.invarnation = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
                self.invarentryclass = StringVar()
                parameters = {'First Name:': self.invarsname, 'Middle Name:': self.invarfname,'Last Name:': self.invarlname,
                              'Address:': self.invaradres, 'Nationality:': self.invarnation, 'State:': self.invarstate,'Town:': self.invartown, 'D-O-B:': self.invardob,
                              'Entry Class:': self.invarentryclass, 'Phone No:': self.invarphone,'E-mail:': self.invaremail,
                              'Father Name:': self.invarfather, 'Mother Name:': self.invarmother,'Next of Kin:': self.invarkin,
                              'Religion': self.invarreligion, 'Languages:': self.invarlanguage,'Session:': self.invarsess}
                j = 45
                c = 48
                for key, value in parameters.items():
                    j += 20
                    c += 20
                    Label(self.temporal, text=key, bg='#DFDAEC').place(x=2, y=j)
                    if key == 'D-O-B:':
                        self.dname = DateEntry(self.temporal, width=23, background='darkblue', font=('Courier', 7, 'bold'))
                        self.dname.place(x=85, y=c)
                    else:
                        self.fname = Entry(self.temporal, width=23, bd=0, textvariable=value)
                        self.fname.place(x=85, y=c)
                Label(self.temporal, text='Passport:', bg='#DFDAEC').place(x=2, y=405)
                self.picentry = StringVar()
                self.picname = Entry(self.temporal, width=15, bd=0, textvariable=self.picentry)
                self.picname.place(x=85, y=408)
                Button(self.temporal, text='Import', bg='#ffffff', bd=1, width=5, font=('Times', 7), command=lambda: self.usercheck(2)).place(x=200, y=408)
                Button(self.temporal, text='OK ', bg='#3E4095', width=22, fg='#ffffff', bd=0, command=self.staff_reg).place(x=0, y=506)
                Button(self.temporal, text='BACK ', bg='red', width=15, fg='#ffffff', bd=0, command=lambda: self.admnstudent('3')).place(x=160, y=506)
            elif self.staffinvar.get() == 'Student Info':
                self.resultNinfo = 0
                self.askclasses()
                if self.dvalue == '1':
                    Button(self.temporal, text='BACK', bg='#3E4095', fg='#ffffff', bd=0, width=10, command=lambda:self.admnstudent('1')).place(x=132, y=215)
                elif self.dvalue == '2':
                    Button(self.temporal, text='BACK', bg='#3E4095', fg='#ffffff', bd=0, width=10, command=lambda: self.admnstudent('2')).place(x=132, y=215)
                elif self.dvalue == '3':
                    Button(self.temporal, text='BACK', bg='#3E4095', fg='#ffffff', bd=0, width=10, command=lambda: self.admnstudent('3')).place(x=132, y=215)
            elif self.staffinvar.get() == 'Student Courses':
                self.noticeboard(1,1)
            elif self.staffinvar.get() == 'Student Result':
                self.resultNinfo = 1
                self.imageframe.destroy()
                self.imageframe = Frame(self.initialframe, width=269, height=600)
                self.imageframe.place(x=231, y=0)
                self.temporal = Frame(self.imageframe, height=249, width=264, bg='#DFDAEC')
                self.temporal.place(x=2, y=120)
                Label(self.temporal, text='STUDENTS', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=1, y=0)
                Label(self.imageframe, width=45, height=4, text='PSG || MR OBALOLUWA', font=('AvantGarde Bk BT', 8),fg='#ffffff', bg='#3E4095').place(x=0, y=10)
                Label(self.temporal, text='Student Result', bg='#3E4095', fg='#ffffff', width=37, height=1).place(x=1,y=37)
                Label(self.temporal, text='JUNIOR CLASS', bg='#3E4095', fg='#ffffff',font=('AvantGarde Bk BT', 7)).place(x=20, y=90)
                Label(self.temporal, text='SENIOR CLASS', bg='#3E4095', fg='#ffffff',font=('AvantGarde Bk BT', 7)).place(x=170, y=90)
                self.invarclass = StringVar()
                Radiobutton(self.temporal, text='JSS 1', value='j1', variable=self.invarclass, bg='#DFDAEC').place(x=20,y=120)
                Radiobutton(self.temporal, text='JSS 2', value='j2', variable=self.invarclass, bg='#DFDAEC').place(x=20,y=140)
                Radiobutton(self.temporal, text='JSS 3', value='j3', variable=self.invarclass, bg='#DFDAEC').place(x=20,y=160)
                Radiobutton(self.temporal, text='SSS 1', value='ss1', variable=self.invarclass, bg='#DFDAEC').place(x=170, y=120)
                Radiobutton(self.temporal, text='SSS 2', value='ss2', variable=self.invarclass, bg='#DFDAEC').place(x=170, y=140)
                Radiobutton(self.temporal, text='SSS 3', value='ss3', variable=self.invarclass, bg='#DFDAEC').place(x=170, y=160)
                Button(self.temporal, text='GO', bg='#3E4095', fg='#ffffff', bd=0, width=10, command=lambda: self.ok('6')).place(x=55, y=215)
                if self.dvalue == '1':
                    Button(self.temporal, text='BACK', bg='#3E4095', fg='#ffffff', bd=0, width=10, command=lambda: self.admnstudent('1')).place(x=132, y=215)
                elif self.dvalue == '2':
                    Button(self.temporal, text='BACK', bg='#3E4095', fg='#ffffff', bd=0, width=10, command=lambda: self.admnstudent('2')).place(x=132, y=215)
                elif self.dvalue == '3':
                    Button(self.temporal, text='BACK', bg='#3E4095', fg='#ffffff', bd=0, width=10, command=lambda: self.admnstudent('3')).place(x=132, y=215)
            elif self.staffinvar.get() == 'Exam Control':
                self.temporal.destroy()
                self.temporal = Frame(self.imageframe, height=249, width=264, bg='#DFDAEC')
                self.temporal.place(x=2, y=120)
                self.dbconnection()
                Label(self.temporal, text='Exam Control', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=1, y=0)
                Label(self.temporal, text='Staff Question:', width=12, bg='#3E4095', fg='#ffffff').place(x=2, y=50)
                Label(self.temporal, text='Mode:', width=5, bg='#3E4095', fg='#ffffff').place(x=2, y=100)
                Button(self.temporal, text='Set Exam/Test Date and Time', bg='#3E4095', fg='#ffffff', bd=0, width=25,
                       command=lambda:self.controlOk('5')).place(x=0, y=130)
                Label(self.temporal, text='Notifications from Staffs', width=37, bg='darkred', height=1, fg='#ffffff').place(x=0, y=150)
                self.invarQuesControl = IntVar()
                self.invarexamMode = IntVar()
                Radiobutton(self.temporal, text='Enable', variable=self.invarQuesControl, value=1, bg='#DFDAEC').place(x=90, y=50)
                Radiobutton(self.temporal, text='Disable', variable=self.invarQuesControl, value=0, bg='#DFDAEC').place(x=160, y=50)
                Button(self.temporal, text='OK', bg='#3E4095', fg='#ffffff', bd=0, command=lambda:self.controlOk(1)).place(x=235, y=50)
                Radiobutton(self.temporal, text='Off', value=0, variable=self.invarexamMode, bg='#DFDAEC').place(x=50, y=100)
                Radiobutton(self.temporal, text='Test', value=1, variable=self.invarexamMode, bg='#DFDAEC').place(x=90, y=100)
                Radiobutton(self.temporal, text='Examination', value=2, variable=self.invarexamMode, bg='#DFDAEC').place(x=137, y=100)
                Button(self.temporal, text='OK', bg='#3E4095', fg='#ffffff', bd=0,command=lambda: self.controlOk(2)).place(x=238, y=100)
                notify = f'You have {str(5)} new notifications\n from Staffs'
                Label(self.temporal, text=notify, bg='#DFDAEC', fg='#000000', font=('Arial', 10, 'bold')).place(x=27, y=177)
                self.mycursor.execute('SELECT Control_Value FROM control_tb')
                self.myfetchl = self.mycursor.fetchall()
                self.invarQuesControl.set(int(self.myfetchl[0][0]))
                self.invarexamMode.set(int(self.myfetchl[1][0]))
                Button(self.temporal, text='CHECK', bg='#3E4095', fg='#ffffff', bd=0, width=7).place(x=70, y=220)
                Button(self.temporal, text='BACK', bg='darkred', fg='#ffffff', bd=0, width=7, command=lambda:self.control(2)).place(x=130, y=220)
            elif self.staffinvar.get() == 'Sessional/Term':
                self.temporal.destroy()
                self.temporal = Frame(self.imageframe, height=249, width=264, bg='#DFDAEC')
                self.temporal.place(x=2, y=120)
                Label(self.temporal, text='Sessional/Term Control', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=1,y=0)
                Label(self.temporal, text='Current Session:', width=13, bg='#3E4095', fg='#ffffff').place(x=1,y=50)
                self.mycursor.execute('SELECT Control_Value FROM control_tb')
                self.myfetchl = self.mycursor.fetchall()
                keep = self.myfetchl[3][0]
                Label(self.temporal, text=self.myfetchl[2][0], bg='#DFDAEC', fg='#000000', font=('Courier', 11, 'bold')).place(x=105,y=50)
                Button(self.temporal, text='Proceed to Next Session', bg='darkred', fg='#ffffff', bd=0, command=lambda:self.controlOk(4)).place(x=65,y=72)
                Label(self.temporal, text='Current Term:', width=12, bg='#3E4095', fg='#ffffff').place(x=1,y=120)
                Label(self.temporal, text=keep, width=12, fg='#000000', bg='#DFDAEC', font=('Courier', 11, 'bold')).place(x=105,y=120)
                Button(self.temporal, text='Proceed to Next Term', bg='darkred', fg='#ffffff', bd=0, command=lambda:self.controlOk(3)).place(x=65,y=142)
                Button(self.temporal, text='BACK', bg='#3E4095', fg='#ffffff', bd=0, width=10, command=lambda:self.control(2)).place(x=100,y=200)
        elif val == '3':
            if self.staffinvar.get() == 'Staff Access':
                self.temporal.destroy()
                self.temporal = Frame(self.imageframe, height=249, width=264, bg='#DFDAEC')
                self.temporal.place(x=2, y=120)
                Label(self.temporal, text='STAFF', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=1, y=0)
                Label(self.imageframe, width=45, height=4, text='PSG || '+self.myfetch[0], font=('AvantGarde Bk BT', 8), fg='#ffffff', bg='#3E4095').place(x=0, y=10)
                Label(self.temporal, text='Staff Access', bg='#3E4095', fg='#ffffff', width=37, height=1).place(x=1, y=37)
                Label(self.temporal, text='Staff Id:', bg='#DFDAEC').place(x=43, y=100)
                self.stfinvar = StringVar()
                self.stfentry = Entry(self.temporal, textvariable=self.stfinvar, width=15, font=('AvantGarde Bk BT', 10, 'bold'))
                self.stfentry.place(x=95, y=100)
                Button(self.temporal, text='REVOKE', bg='#00AFEF', width=12, fg='#ffffff', bd=0, command=lambda:self.ok('4', 'r')).place(x=129, y=160)
                Button(self.temporal, text='INACTIVE', bg='#00AFEF', width=12, fg='#ffffff', bd=0, command=lambda:self.ok('4', 'i')).place(x=35, y=185)
                Button(self.temporal, text='ACTIVE', bg='#00AFEF', width=12, fg='#ffffff', bd=0, command=lambda:self.ok('4', 'a')).place(x=35, y=160)
                Button(self.temporal, text='BACK', bg='#00AFEF', width=12, fg='#ffffff', bd=0, command=lambda:self.stafftop(1,0)).place(x=129, y=185)
            elif self.staffinvar.get() == 'Total Number of Staff':
                self.mycursor.execute('SELECT count(Staff_aid) FROM staffs_tb')
                self.myfetchcount = self.mycursor.fetchone()
                showinfo('Count Completed!', f'You have {self.myfetchcount[0]} members of staff')
            elif self.staffinvar.get() == 'Staff Info':
                self.temporal.destroy()
                self.temporal = Frame(self.imageframe, height=526, width=264, bg='#DFDAEC')
                self.temporal.place(x=2, y=73)
                Label(self.temporal, text='STAFF', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=1, y=0)
                Label(self.temporal, text='Staff Info', bg='#3E4095', fg='#ffffff', width=37, height=1).place(x=1, y=37)
                self.mycursor.execute('SELECT concat(Staff_aid,\' \',First_name,\' \', middle_name,\' \', Last_name) \
                FROM staffs_tb WHERE Staff_aid LIKE %s', ('PGSTF%',))
                self.myfetch = self.mycursor.fetchall()
                listofteachers = [i[0] for i in self.myfetch]
                self.vscrol = Scrollbar(self.initialframe, orient='vertical')
                self.listboxofTeachers = Listbox(self.temporal, font=('AvantGarde Bk BT', 11), bg='#BDBFC1', width=35, height=25, bd=0, yscrollcommand=self.vscrol.set)
                for teach in listofteachers:
                    self.listboxofTeachers.insert(END, teach)
                self.vscrol.config(command=self.listboxofTeachers.yview)
                self.listboxofTeachers.place(x=0, y=58)
                self.vscrol.place(x=480, y=132, height=446)
                Button(self.temporal, text='OK ', bg='#3E4095', width=25, fg='#ffffff', bd=0, command=lambda:self.ok('5')).place(x=0, y=506)
                Button(self.temporal, text='BACK ', bg='red', width=12, fg='#ffffff', bd=0, command=lambda:self.stafftop(1,1)).place(x=180, y=506)
            elif self.staffinvar.get() == 'Check Staff Presence':
                self.temporal.destroy()
                self.temporal = Frame(self.imageframe, height=249, width=264, bg='#DFDAEC')
                self.temporal.place(x=2, y=120)
                Label(self.temporal, text='STAFF', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=1, y=0)
                Label(self.temporal, text='Staff Presence', bg='#3E4095', fg='#ffffff', width=37, height=1).place(x=1, y=37)
                self.invardays = StringVar()
                Radiobutton(self.temporal, variable=self.invardays, value=1, text='MONDAY ', bg='#5262AB',
                            font=('AvantGarde Bk BT', 8), justify='left', width=12, fg='#ffffff').place(x=155, y=80)
                Radiobutton(self.temporal, variable=self.invardays, value=2, text='TUESDAY ', bg='#5262AB',
                            font=('AvantGarde Bk BT', 8), justify='left', width=12, fg='#ffffff').place(x=155, y=106)
                Radiobutton(self.temporal, variable=self.invardays, value=3, text='WEDSDAY', bg='#5262AB',
                            font=('AvantGarde Bk BT', 8), justify='left', width=12, fg='#ffffff').place(x=155, y=132)
                Radiobutton(self.temporal, variable=self.invardays, value=4, text='THURSDAY', bg='#5262AB',
                            font=('AvantGarde Bk BT', 8), justify='left', width=12, fg='#ffffff').place(x=155, y=158)
                Radiobutton(self.temporal, variable=self.invardays, value=5, text='FRIDAY  ', bg='#5262AB',
                            font=('AvantGarde Bk BT', 8), justify='left', width=12, fg='#ffffff').place(x=155, y=184)
                self.invarsession = StringVar()
                self.mycursor.execute('SELECT session FROM presence_tb')
                self.myfetchSession = self.mycursor.fetchall()
                self.sessions = []
                for i in self.myfetchSession:
                    if i[0] in self.sessions:
                        continue
                    else:
                        self.sessions.append(i[0])
                # self.mycursor.execute('SELECT session, term, Day_marked, Time_marked, concat(First_name, \' \', Last_name)\
                #  FROM presence_tb JOIN staffs_tb USING(Staff_aid)')
                self.session = ttk.Combobox(self.temporal, values=self.sessions, width=15)
                self.session.set('Session')
                self.session.place(x=10, y=80)
                self.invarterm = IntVar()
                Label(self.temporal, text='Term', bg='#DFDAEC', font=('AvantGarde Bk BT', 8, 'italic')).place(x=10, y=130)
                Radiobutton(self.temporal, variable=self.invarterm, value=1, text='1st Term', font=('AvantGarde Bk BT', 8),
                            justify='left', width=12, fg='#000000', bg='#DFDAEC').place(x=0, y=150)
                Radiobutton(self.temporal, variable=self.invarterm, value=2, text='2nd Term', font=('AvantGarde Bk BT', 8),
                            justify='left', width=12, fg='#000000', bg='#DFDAEC').place(x=0, y=170)
                Radiobutton(self.temporal, variable=self.invarterm, value=3, text='3rd Term', font=('AvantGarde Bk BT', 8),
                            justify='left', width=12, fg='#000000', bg='#DFDAEC').place(x=0, y=190)
                Button(self.temporal, text='GO', bg='#5262AB', font=('AvantGarde Bk BT', 8), width=24, fg='#ffffff', bd=0, command=lambda:self.ok('8')).place(x=1, y=220)
                Button(self.temporal, text='BACK', bg='#5262AB', font=('AvantGarde Bk BT', 8), width=18, fg='#ffffff', bd=0, command=lambda:self.stafftop(1, 0)).place(x=153, y=220)
                self.invarweek = StringVar()
                self.week = ttk.Combobox(self.temporal, values=(1,2,3,4,5,6,7), width=15)
                self.week.set('Date')
                self.week.place(x=10, y=105)
            elif (self.staffinvar.get() == 'Register Staff'):
                self.imageframe.destroy()
                self.imageframe = Frame(self.initialframe, width=269, height=600)
                self.imageframe.place(x=231, y=0)
                Label(self.imageframe, width=45, height=4, text='PSG || MR OBALOLUWA', font=('AvantGarde Bk BT', 8),fg='#ffffff', bg='#3E4095').place(x=0, y=10)
                self.temporal = Frame(self.imageframe, height=526, width=264, bg='#DFDAEC')
                self.temporal.place(x=2, y=73)
                Label(self.temporal, text='STAFF', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=1, y=0)
                Label(self.temporal, text='Staff Registration', bg='#3E4095', fg='#ffffff', width=37, height=1).place(x=1, y=37)
                self.canvasframe = Frame(self.temporal, height=446, width=264, bg='#DFDAEC')
                self.canvasframe.place(x=0, y=58)
                self.canvas = Canvas(self.canvasframe, height=800, width=264, bg='#DFDAEC',scrollregion=(0,0,500,500))
                self.canvas.place(x=0, y=0)
                self.on_canvas = Frame(self.canvas, height=800, width=264, bg='#DFDAEC')
                self.on_canvas.place(x=0, y=0)
                self.vscrol = Scrollbar(self.temporal, orient='vertical', command=self.canvas.yview)
                self.canvas.config(yscrollcommand=self.vscrol.set)
                self.canvas.bind("<Configure>", self.scrollbar)
                self.vscrol.place(x=254, y=58, height=446, width=11)
                # self.canvas.create_window((0,0), window=self.temporal)
                self.invarfname, self.invarsname, self.invarlname, self.invaradres, self.invartitle = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
                self.invarphone, self.invaremail, self.invarfather, self.invarmother, self.invarkin, self.invarreligion = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
                self.invarlanguage, self.invarsess, self.invarstate, self.invartown,self.picentry, self.invarnation = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
                self.invarentryclass, self.invarAttach, self.invarCV, self.invarMarital, self.yearExp, self.invarlevel = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
                parameters = {'First Name:': self.invarsname, 'Middle Name:': self.invarfname, 'Last Name:': self.invarlname,
                              'Address:': self.invaradres, 'Nationality:': self.invarnation, 'State:': self.invarstate,'Town:': self.invartown, 'D-O-B:': '',
                              'Subject:': self.invarentryclass, 'Phone No:': self.invarphone,'E-mail:': self.invaremail,
                              'Father Name:': self.invarfather, 'Mother Name:': self.invarmother, 'Aca Level:': self.invarlevel,
                              'Next of Kin:': self.invarkin, 'Marital Status:': self.invarMarital, 'Job Title': self.invartitle,
                              'Religion': self.invarreligion, 'Languages:': self.invarlanguage, 'Year Of Exp:':self.yearExp, 'Session:': self.invarsess}
                j = 0
                c = 3
                for key, value in parameters.items():
                    j += 20
                    c += 20
                    Label(self.on_canvas, text=key, bg='#DFDAEC').place(x=2, y=j)
                    if key == 'D-O-B:':
                        self.dname = DateEntry(self.on_canvas, width=23, background='darkblue',font=('Courier', 7, 'bold'))
                        self.dname.place(x=85, y=c)
                    else:
                        self.fname = Entry(self.on_canvas, width=23, bd=0, textvariable=value)
                        self.fname.place(x=85, y=c)
                j = 465
                c = 468
                parameters = {'Scanned CV:': self.invarCV, 'Attachment:': self.invarAttach, 'Passport:':self.picentry}
                for key, value in parameters.items():
                    Label(self.on_canvas, text=key, bg='#DFDAEC').place(x=2, y=j)
                    self.picname = Entry(self.on_canvas, width=15, bd=0, textvariable=value)
                    self.picname.place(x=85, y=c)
                    Button(self.on_canvas, text='Import', bg='#ffffff', bd=1, width=5, font=('Times', 7), command=lambda: self.usercheck(2)).place(x=200, y=c)
                    j += 20
                    c += 20
                Button(self.temporal, text='OK ', bg='#3E4095', width=22, fg='#ffffff', bd=0, command=self.staff_reg).place(x=0, y=506)
                Button(self.temporal, text='BACK ', bg='red', width=15, fg='#ffffff', bd=0, command=lambda: self.admnstudent('3')).place(x=160, y=506)
        elif val == '4':
            self.release = 0
            self.check = self.stfentry.get()[2:5].lower()
            if self.check == 'std':
                self.mycursor.execute("SELECT Student_aid FROM student_tb")
            else: self.mycursor.execute("SELECT Staff_aid FROM staffs_tb")
            self.myfetch = self.mycursor.fetchall()
            for i in self.myfetch:
                if i[0] == self.stfentry.get():
                    self.release = 1
                    break
            if self.release == 1 and self.stfentry.get() != 'PGADM1':
                if val2 == 'r' and self.check != 'std':
                    self.mycursor.execute('UPDATE staffs_tb SET Status_Value = %s WHERE Staff_aid = %s', ('REVOKE', self.stfentry.get()))
                elif val2 == 'r' and self.check == 'std':
                    self.mycursor.execute('UPDATE student_tb SET Status_Value = %s WHERE Student_aid = %s', ('REVOKE', self.stfentry.get()))
                elif val2 == 'i' and self.check != 'std':
                    self.mycursor.execute('UPDATE staffs_tb SET Status_Value = %s WHERE Staff_aid = %s', ('INACTIVE', self.stfentry.get()))
                elif val2 == 'i' and self.check == 'std':
                    self.mycursor.execute('UPDATE student_tb SET Status_Value = %s WHERE Student_aid = %s', ('INACTIVE', self.stfentry.get()))
                elif val2 == 'a' and self.check != 'std':
                    self.mycursor.execute('UPDATE staffs_tb SET Status_Value = %s WHERE Staff_aid = %s', ('ACTIVE', self.stfentry.get()))
                elif val2 == 'a' and self.check == 'std':
                    self.mycursor.execute('UPDATE student_tb SET Status_Value = %s WHERE Student_aid = %s', ('ACTIVE', self.stfentry.get()))
                self.mycon.commit()
                showinfo('Completed!', 'Access Altered!')
            else:
                if self.check == 'std':
                    showerror('Error!', 'Student ID do not exist.')
                else: showerror('Error!', 'Staff ID do not exist.')
        elif val == '5':
            collected = self.listboxofTeachers.get(self.listboxofTeachers.curselection())
            if collected:
                collected = collected.split(' ')
                self.dbconnection()
                self.vscrol.destroy()
                self.temporal.destroy()
                self.temporal = Frame(self.imageframe, height=526, width=264, bg='#DFDAEC')
                self.temporal.place(x=2, y=73)
                Label(self.temporal, text='STAFF', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=1, y=0)
                Label(self.imageframe, width=45, height=4, text=f'PSG || {self.myfetch_name}', font=('AvantGarde Bk BT', 8), fg='#ffffff', bg='#3E4095').place(x=0, y=10)
                Label(self.temporal, text='Staff Info', bg='#3E4095', fg='#ffffff', width=37, height=1).place(x=1, y=37)
                self.picframe = Frame(self.temporal, width=182, height=202, bg='#C8C5E2')
                self.picframe.place(x=38, y=100)
                self.mycursor.execute('SELECT passport, job_title, Email, Phone_number, Address, title, \
                concat(First_name,\' \', middle_name), department FROM staffs_tb WHERE Staff_aid = %s', (collected[0],))
                self.myfetchinfo = self.mycursor.fetchone()
                try:
                    self.pic = Image.open(self.myfetchinfo[0])
                    self.picprocess = ImageTk.PhotoImage(self.pic)
                except: pass
                Label(self.picframe, image=self.picprocess).pack(anchor='c')
                Label(self.temporal, text=self.myfetchinfo[6], fg='#000000').place(x=38, y=320)
                Label(self.temporal, text=collected[0], fg='#000000').place(x=38, y=340)
                Label(self.temporal, text=self.myfetchinfo[1], fg='#000000').place(x=38, y=360)
                Label(self.temporal, text=self.myfetchinfo[2], fg='#000000').place(x=38, y=380)
                Label(self.temporal, text=self.myfetchinfo[6], fg='#000000').place(x=38, y=380)
                Button(self.temporal, text='BACK', bg='#3E4095', width=38, fg='#ffffff', bd=0, command=lambda:self.ok('3')).place(x=0, y=480)
                Button(self.temporal, text='HOME', bg='#3E4095', width=38, fg='#ffffff', bd=0, command=self.admin).place(x=0, y=503)
        elif val == '6':
            self.dbconnection()
            self.temporal.destroy()
            self.temporal = Frame(self.imageframe, height=526, width=264, bg='#DFDAEC')
            self.temporal.place(x=2, y=73)
            count = 1
            Label(self.temporal, text='STUDENTS', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=1, y=0)
            self.vscrol = Scrollbar(self.initialframe, orient='vertical')
            self.listboxofStudents = Listbox(self.temporal, font=('AvantGarde Bk BT', 11), bg='#BDBFC1', width=35,height=25, bd=0, yscrollcommand=self.vscrol.set)
            if self.resultNinfo == 0: # for student information(admin)s
                self.answer = 'students'
                Label(self.temporal, text='Student Info', bg='#3E4095', fg='#ffffff', width=37, height=1).place(x=1,y=37)
                self.listofStudents = dict()
                self.mycursor.execute('SELECT Class_id FROM class_tb WHERE lower(Class_name) LIKE %s', (self.invarclass.get()+'%',))
                self.myfetchid = self.mycursor.fetchall()
                for ids in self.myfetchid:
                    self.mycursor.execute("SELECT concat(First_name, ' ', Middle_name), Student_aid FROM student_tb\
                     WHERE class_id = %s", (ids[0],))
                    self.myfetchstd = self.mycursor.fetchall()
                    for students in self.myfetchstd:
                        self.listofStudents[students[1]] = students[0]
                for key, value in self.listofStudents.items():
                    self.listboxofStudents.insert(END, str(count) + ')    ' + value + '  ' + key)
                    count += 1
            elif self.resultNinfo == 1: # for student results (admin)
                self.answer = 'courses'
                Label(self.temporal, text='Student Results', bg='#3E4095', fg='#ffffff', width=37, height=1).place(x=1,y=37)
                listofStudentscourses = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11', 'c12', 'c13', 'c14', 'c15', 'c16', 'c17', 'c18', 'c19', 'c20', 'c21', 'c22', 'c23', 'c24', 'c25', 'c26', 'c27', 'c28']
                for teach in listofStudentscourses:
                    self.listboxofStudents.insert(END, teach)
            elif self.resultNinfo == 2: # for student lists of books (admin)
                self.answer = 'books'
                Label(self.temporal, text='Lists of Books', bg='#3E4095', fg='#ffffff', width=37, height=1).place(x=1,y=37)
                listofStudentscourses = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'B24', 'B25', 'B26', 'B27', 'B28']
                for teach in listofStudentscourses:
                    self.listboxofStudents.insert(END, teach)
            self.vscrol.config(command=self.listboxofStudents.yview)
            self.listboxofStudents.place(x=0, y=58)
            self.vscrol.place(x=480, y=132, height=446)
            Button(self.temporal, text='OK ', bg='#3E4095', width=25, fg='#ffffff', bd=0, command=lambda: self.ok('7')).place(x=0, y=506)
            Button(self.temporal, text='BACK ', bg='red', width=12, fg='#ffffff', bd=0, command=lambda: self.ok('2')).place(x=180, y=506)
        elif val == '7':
            self.dbconnection()
            collected = self.listboxofStudents.get(self.listboxofStudents.curselection())
            collected = collected.split(' ')
            collected = [i.strip() for i in collected if i != '']
            self.vscrol.destroy()
            self.temporal.destroy()
            self.temporal = Frame(self.imageframe, height=526, width=264, bg='#DFDAEC')
            self.temporal.place(x=2, y=73)
            if self.answer == 'students':
                self.mycursor.execute("SELECT Last_name, passport, class_id, Date_of_birth, Phone_number, Email, Address FROM student_tb WHERE Student_aid = %s", (collected[3],))
                self.myfetchl = self.mycursor.fetchone()
                self.mycursor.execute("SELECT Class_name FROM class_tb WHERE Class_id = %s", (self.myfetchl[2],))
                self.myfetchstd = self.mycursor.fetchone()
                Label(self.temporal, text='STUDENTS', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=1, y=0)
                Label(self.imageframe, width=45, height=4, text='PSG || MR OBALOLUWA', font=('AvantGarde Bk BT', 8), fg='#ffffff', bg='#3E4095').place(x=0, y=10)
                Label(self.temporal, text='Student Info', bg='#3E4095', fg='#ffffff', width=37, height=1).place(x=1, y=37)
                self.picframe = Frame(self.temporal, width=182, height=202, bg='#C8C5E2')
                self.picframe.place(x=38, y=100)
                self.pic = Image.open(self.myfetchl[1])
                self.picprocess = ImageTk.PhotoImage(self.pic)
                self.jobtitle.config(text='CLASS:')
                Label(self.picframe, image=self.picprocess).pack(anchor='c')
                Label(self.temporal, text=collected[1] + ' ' + collected[2] + ' ' + self.myfetchl[0], fg='#000000').place(x=38, y=320)
                Label(self.temporal, text=collected[3], fg='#000000').place(x=38, y=340)
                Label(self.temporal, text=self.myfetchstd[0], fg='#000000').place(x=38, y=360)
                Label(self.temporal, text=f'D-O-B: \t{self.myfetchl[3]}', fg='#000000', font=('Arial', 10, 'bold')).place(x=38, y=380)
                Label(self.temporal, text=f'Phone Number: \t{self.myfetchl[4]}', fg='#000000', font=('Arial', 10, 'bold')).place(x=38, y=400)
                Label(self.temporal, text=f'E-mail: \t{self.myfetchl[5]}', fg='#000000', font=('Arial', 10, 'bold')).place(x=38, y=400)
                Label(self.temporal, text=f'Address: \t{self.myfetchl[6]}', fg='#000000', font=('Arial', 10, 'bold')).place(x=38, y=420)
                Button(self.temporal, text='BACK', bg='#3E4095', width=38, fg='#ffffff', bd=0, command=lambda: self.ok('6')).place(x=0, y=480)
                Button(self.temporal, text='HOME', bg='#3E4095', width=38, fg='#ffffff', bd=0, command=self.admin).place(x=0, y=503)
            elif self.answer == 'courses':
                Label(self.temporal, text='STUDENTS', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=1, y=0)
                Label(self.temporal, text='Student Results', bg='#3E4095', fg='#ffffff', width=37, height=1).place(x=1,y=37)
                Label(self.temporal, text='Student Name', bg='#3E4095', fg='#ffffff', width=11, height=1).place(x=1,y=60)
                Label(self.temporal, text='Student ID', bg='#3E4095', fg='#ffffff', width=11, height=1).place(x=88,y=60)
                Label(self.temporal, text='Student Score', bg='#3E4095', fg='#ffffff', width=12, height=1).place(x=175,y=60)
                Button(self.temporal, text='BACK', bg='#3E4095', width=38, fg='#ffffff', bd=0,command=lambda:self.ok('6')).place(x=0, y=480)
                Button(self.temporal, text='HOME', bg='#3E4095', width=38, fg='#ffffff', bd=0,command=self.admin).place(x=0, y=503)
            elif self.answer == 'books':
                self.editbook = StringVar()
                Label(self.temporal, text='Edit Book Name', bg='#3E4095', fg='#ffffff').place(x=0, y=50)
                Entry(self.temporal, textvariable=self.editbook, bd=0).place(x=0, y=80)
        elif val == '8':
            self.term, self.session, self = self.invarterm.get()

    def admnstudent(self, dvalue):
        self.mycursor.execute('SELECT concat(title, \' \', middle_name) FROM staffs_tb WHERE Staff_aid = %s', (self.invarid.get(),))
        self.myfetch = self.mycursor.fetchone()
        self.dvalue = dvalue
        self.imageframe.destroy()
        self.imageframe = Frame(self.initialframe, width=269, height=600)
        self.imageframe.place(x=231, y=0)
        Label(self.imageframe, width=45, height=4, text='PSG || ' + self.myfetch_name, font=('AvantGarde Bk BT', 8), fg='#ffffff', bg='#3E4095').place(x=0, y=10)
        self.temporal = Frame(self.imageframe, height=249, width=264, bg='#DFDAEC')
        self.temporal.place(x=2, y=120)
        self.staffinvar = StringVar()
        Button(self.temporal, text='GO', bg='#00AFEF', width=10, fg='#ffffff', bd=0,command=lambda: self.ok('2')).place(x=94, y=115)
        Button(self.temporal, text='BACK', bg='#00AFEF', width=10, fg='#ffffff', bd=0, command=self.admin).place(x=94,y=140)
        if dvalue == '1': # Proprietor and Prinipal
            self.staffinvar.set('Student Info')
            Label(self.temporal, text='STUDENTS', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=1, y=0)
            options = ['Students Access', 'Total Number of Students', 'Student Info', 'Student Result', 'Student Courses']
            self.staffoptionmenu = OptionMenu(self.temporal, self.staffinvar, *options)
            self.staffoptionmenu.config(bg='#BDBFC1', width=20, bd=1, relief=RIDGE)
            self.staffoptionmenu.place(x=38, y=80)
        elif dvalue == '2': #Bursar
            self.staffinvar.set('Payment History')
            Label(self.temporal, text='STUDENTS', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=1, y=0)
            options = ['Payment History', 'Print Receipt', 'School Fee', 'Special Funds']
            self.staffoptionmenu = OptionMenu(self.temporal, self.staffinvar, *options)
            self.staffoptionmenu.config(bg='#BDBFC1', width=20, bd=1, relief=RIDGE)
            self.staffoptionmenu.place(x=38, y=80)
        elif dvalue == '3': # Academic Officer
            self.staffinvar.set('Student Info')
            Label(self.temporal, text='STUDENTS', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=1, y=0)
            options = ['Students Access', 'Register Student', 'Student Info', 'Student Result', 'Student Courses', 'Lists of Books', 'Students Attendance']
            self.staffoptionmenu = OptionMenu(self.temporal, self.staffinvar, *options)
            self.staffoptionmenu.config(bg='#BDBFC1', width=20, bd=1, relief=RIDGE)
            self.staffoptionmenu.place(x=38, y=80)

    def stafftop(self, u, n=None):
        self.imageframe.destroy()
        self.imageframe = Frame(self.initialframe, width=269, height=600)
        self.imageframe.place(x=231, y=0)
        Label(self.imageframe, width=45, height=4, text='PSG || MR OBALOLUWA', font=('AvantGarde Bk BT', 8), fg='#ffffff', bg='#3E4095').place(x=0, y=10)
        self.temporal = Frame(self.imageframe, height=249, width=264, bg='#DFDAEC')
        Label(self.temporal, text='STAFF', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=1, y=0)
        self.temporal.place(x=2, y=120)
        self.staffinvar = StringVar()
        if u==1: # from admin panel
            self.staffinvar.set('Staff Info')
            if n == 0:
                options = ['Staff Access', 'Total Number of Staff', 'Staff Info', 'Check Staff Presence']
                self.staffoptionmenu = OptionMenu(self.temporal, self.staffinvar, *options)
            elif n == 1:
                options = ['Staff Access', 'Total Number of Staff', 'Staff Info', 'Register Staff']
                self.staffoptionmenu = OptionMenu(self.temporal, self.staffinvar, *options)
            Button(self.temporal, text='BACK', bg='#00AFEF', width=10, fg='#ffffff', bd=0, command=self.admin).place(x=94, y=140)
        elif u==2: # academic officer
            self.staffinvar.set('Assign Course')
            options = ['Assign Course', 'Check Disscussion Rooms', 'Teacher & Courses']
            self.staffoptionmenu = OptionMenu(self.temporal, self.staffinvar, *options)
            Button(self.temporal, text='BACK', bg='#00AFEF', width=10, fg='#ffffff', bd=0, command=self.admin).place(x=94, y=140)
        self.staffoptionmenu.config(bg='#BDBFC1', width=20, bd=1, relief=RIDGE)
        self.staffoptionmenu.place(x=38, y=80)
        Button(self.temporal, text='GO', bg='#00AFEF', width=10, fg='#ffffff', bd=0,command=lambda: self.ok('3')).place(x=94, y=115)

    def staffbuttonoptions(self, cvalue):
        self.dbconnection()
        self.imageframe.destroy()
        self.imageframe = Frame(self.initialframe, width=269, height=400)
        self.imageframe.place(x=231, y=0)
        self.temporal = Frame(self.imageframe, height=290, width=264, bg='#DFDAEC')
        self.temporal.place(x=2, y=79)
        Label(self.imageframe, text=f'PGS || {self.myfetch_name[0]}\'s Page').place(x=60, y=1)
        Label(self.temporal, text='S/N', width=4, height=1, bg='#3E4095', fg='#ffffff').place(x=1, y=37)
        self.mycursor.execute('SELECT Course_name, Book_name, Author FROM course_tb JOIN books_tb USING(Course_id) WHERE Staff_aid = %s',
            (self.invarid.get(),))
        self.myfetchl = self.mycursor.fetchall()
        v = 70
        z = 90
        if cvalue == 'a':
            Label(self.temporal, text='My Courses', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=1, y=0)
            Label(self.temporal, text='Courses', width=32, height=1, bg='#3E4095', fg='#ffffff').place(x=36, y=37)
            for ind,val in enumerate(self.myfetchl):
                Label(self.temporal, text=str(ind+1)+') \t'+val[0], fg='#000000', bg='#DFDAEC', font=('Arial', 10, 'bold')).place(x=5, y=v)
                v+=20
        elif cvalue == 'b':
            Label(self.temporal, text='Course Books', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=1, y=0)
            Label(self.temporal, text='Books', width=32, height=1, bg='#3E4095', fg='#ffffff').place(x=36, y=37)
            for ind,val in enumerate(self.myfetchl):
                Label(self.temporal, text=str(ind+1)+') '+val[0], fg='#000000', bg='#DFDAEC').place(x=5, y=v)
                Label(self.temporal, text=val[1]+' by '+val[2], fg='#000000', bg='#DFDAEC').place(x=15, y=z)
                v+=40
                z+=40
        Button(self.temporal, text='Back', width=37, bg='#3E4095', fg='#ffffff', height=1, bd=0, command=self.submit).place(x=0, y=270)

    def staffSetExam(self, val):
        if val == 1:
            self.imageframe.destroy()
            self.imageframe = Frame(self.initialframe, width=269, height=462)
            self.imageframe.place(x=231, y=0)
            self.temporal = Frame(self.imageframe, height=290, width=264, bg='#DFDAEC')
            self.temporal.place(x=2, y=79)
            Label(self.imageframe, text=f'PGS || {self.myfetch_name[0]}\'s Page').place(x=60, y=1)
            Label(self.temporal, text='Set Courses Exam/Test Span', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=1, y=0)
            Button(self.temporal, text='Proceed To Set Question', width=37, bg='#3E4095', fg='#ffffff', height=1, bd=0, command=lambda:self.staffSetExam(2)).place(x=0, y=247)
            Button(self.temporal, text='Back', width=37, bg='#3E4095', fg='#ffffff', height=1, bd=0, command=self.submit).place(x=0, y=270)
            self.mycursor.execute('SELECT course_name, course_id FROM course_tb WHERE Staff_aid=%s', (self.invarid.get(),))
            self.myfetchSubject = self.mycursor.fetchall()
            self.mySubject = {i[0]:i[1]for i in self.myfetchSubject}
            self.subject = [i for i in self.mySubject.keys()]
            Label(self.temporal, text='Select Subject', bg='#DFDAEC').place(x=85,  y=65)
            self.cobMySubject = ttk.Combobox(self.temporal, width=20, state='readonly', values=self.subject)
            self.cobMySubject.place(x=45, y=90)
            self.cobMySubject.set('Subject')
            self.inminute, self.inhour = [i for i in range(60)], [i for i in range(6)]
            Label(self.temporal, text='Span', bg='#DFDAEC').place(x=100, y=125)
            Label(self.temporal, text='Minute', bg='#DFDAEC').place(x=25, y=200)
            Label(self.temporal, text='Hour', bg='#DFDAEC').place(x=25, y=150)
            self.cobMyHour = ttk.Combobox(self.temporal, width=10, state='readonly', values=self.inhour)
            self.cobMyHour.place(x=75, y=150)
            self.cobMyHour.set(0)
            self.cobMyMin = ttk.Combobox(self.temporal, width=10, state='readonly', values=self.inminute)
            self.cobMyMin.place(x=75, y=200)
            self.cobMyMin.set(1)
        elif val == 2:
            if self.cobMySubject.get() in self.subject:
                self.dbconnection()
                subject, hour, minute = self.cobMySubject.get(), self.cobMyHour.get(), self.cobMyMin.get()
                self.dbsubjectid = self.mySubject[subject]
                self.mycursor.execute('UPDATE course_tb SET TestExam_TimeHour=%s, TestExam_TimeMinutes=%s WHERE\
                 Course_id = %s', (hour, minute, self.dbsubjectid))
                self.mycon.commit()
                self.imageframe.destroy()
                self.imageframe = Frame(self.initialframe, width=269, height=462)
                self.imageframe.place(x=231, y=0)
                self.temporal = Frame(self.imageframe, height=500, width=264, bg='#DFDAEC')
                self.temporal.place(x=2, y=2)
                Label(self.temporal, text='Set Exam', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=1, y=0)
                Label(self.temporal, text='Question:', bg='#DFDAEC').place(x=98, y=40)
                self.invarquestion, self.invaroptionA, self.invaroptionB = StringVar(), StringVar(), StringVar()
                self.invaroptionC, self.invaroptionD, self.invaranswer = StringVar(), StringVar(), StringVar()
                self.question = Entry(self.temporal, textvariable=self.invarquestion, width=16, font=('Arial', 20), justify='right')
                self.question.place(x=9, y=60)
                Label(self.temporal, text='Right Optn:', bg='#DFDAEC').place(x=98, y=100)
                self.answer = Entry(self.temporal, textvariable=self.invaranswer, width=16, font=('Arial', 20))
                self.answer.place(x=9, y=120)
                Label(self.temporal, text='Option A:', bg='#DFDAEC').place(x=98, y=160)
                self.optionA = Entry(self.temporal, textvariable=self.invaroptionA, width=16, font=('Arial', 20), justify='right')
                self.optionA.place(x=9, y=180)
                Label(self.temporal, text='Option B:', bg='#DFDAEC').place(x=98, y=230)
                self.optionB = Entry(self.temporal, textvariable=self.invaroptionB, width=16, font=('Arial', 20), justify='right')
                self.optionB.place(x=9, y=250)
                Label(self.temporal, text='Option C:', bg='#DFDAEC').place(x=98, y=300)
                self.optionC = Entry(self.temporal, textvariable=self.invaroptionC, width=16, font=('Arial', 20),justify='right')
                self.optionC.place(x=9, y=320)
                Label(self.temporal, text='Option D:', bg='#DFDAEC').place(x=98, y=370)
                self.optionD = Entry(self.temporal, textvariable=self.invaroptionD, width=16, font=('Arial', 20),justify='right')
                self.optionD.place(x=9, y=390)
                Button(self.temporal, text='Submit', width=24, bd=0, bg='#3E4095', fg='#ffffff', command=lambda:self.staffSetExam(3)).place(x=5, y=436)
                Button(self.temporal, text='Back', width=10, bd=0, bg='red', fg='#ffffff', command=self.submit).place(x=178, y=436)
            else: showerror('PSG', 'You must select a subject')
        elif val == 3:
            self.dbconnection()
            self.mycursor.execute('SELECT Control_Value FROM control_tb')
            self.myfetchControl = self.mycursor.fetchall()
            if self.myfetchControl[1][0] == '1':
                self.type = 'Test'
            elif self.myfetchControl[1][0] == '2':
                self.type = 'Exam'
            self.mycursor.execute('INSERT INTO question_tb(Question, Option_a, Option_b, Option_c, Option_d, Correct_answer\
            , Course_id, Term, Session, Type) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (self.invarquestion.get(), self.invaroptionA.get()
            ,self.invaroptionB.get(), self.invaroptionC.get(), self.invaroptionD.get(), self.invaranswer.get(), self.dbsubjectid
                             , self.myfetchControl[3][0], self.myfetchControl[2][0], self.type))
            self.mycon.commit()
            self.invarquestion.set('')
            self.invaroptionA.set('')
            self.invaroptionB.set('')
            self.invaroptionC.set('')
            self.invaroptionD.set('')
            self.invaranswer.set('')

    def stdCrsNperf(self, opt):
        self.imageframe.destroy()
        self.imageframe = Frame(self.initialframe, width=269, height=462)
        self.imageframe.place(x=231, y=0)
        self.temporal = Frame(self.imageframe, height=462, width=264, bg='#DFDAEC')
        self.temporal.place(x=0, y=0)
        Label(self.temporal, text='S/N', width=4, height=1, bg='#3E4095', fg='#ffffff').place(x=1, y=37)
        self.dbconnection()
        if opt == 'a':
            self.dbconnection()
            self.mycursor.execute('SELECT course_name, course_id FROM course_tb WHERE Staff_aid = %s', (self.invarid.get(),))
            self.myfetchCourse = self.mycursor.fetchall()
            print(self.myfetchCourse)
            self.mycursor.execute('SELECT concat(First_name,\' \', Middle_name) FROM student_tb JOIN class_tb \
            USING(class_id) JOIN course_tb USING(class_id) WHERE course_id = %s', (self.myfetchCourse[0][1],))
            self.myfetchstd = self.mycursor.fetchall()
            Label(self.temporal, text='My Courses Students', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=1, y=0)
            Label(self.temporal, text=f'{self.myfetchCourse[0][0]} (Names)', width=32, height=1, bg='#3E4095', fg='#ffffff').place(x=36, y=37)
            for ind, val in enumerate(self.myfetchstd):
                Label(self.temporal, text=f' {ind+1})\t{val[0]}', bg='#DFDAEC', fg='#000000').place(x=0, y=63)
            Button(self.temporal, text='→', width=11, bg='green', fg='#ffffff', height=1, bd=0,command=lambda:self.nextCourse('a')).place(x=183, y=439)
        elif opt == 'b':
            Label(self.temporal, text='Student Performance', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=1, y=0)
            Button(self.temporal, text='→', width=11, bg='green', cursor='hand2', fg='#ffffff', height=1, bd=0,command=lambda:self.nextCourse('b')).place(x=183, y=439)
            self.mycursor.execute('SELECT Course_name, Course_id FROM course_tb WHERE Staff_aid=%s ORDER BY Course_name DESC', (self.invarid.get(),))
            self.myfetchCourse = self.mycursor.fetchall()
            Label(self.temporal, text=f'{self.myfetchCourse[0][0]} (Scores)', width=32, height=1, bg='#3E4095',
                  fg='#ffffff').place(x=36, y=37)
            self.mycursor.execute('SELECT concat(First_name,\'  \', Last_name), Score, Type FROM student_tb JOIN result_tb USING\
             (Student_aid) WHERE Course_id = %s and Session_=(SELECT Control_Value FROM control_tb \
             WHERE Control_id=%s) and Term=(SELECT Control_Value FROM control_tb WHERE Control_id \
             = %s) ORDER BY Type', (self.myfetchCourse[0][1], 3, 4))
            self.myfetchScore_teacher = self.mycursor.fetchall()
            if self.myfetchScore_teacher:
                v = 65
                self.res_count = 1
                for i in self.myfetchScore_teacher:
                    Label(self.temporal, text=f'{self.res_count}.)', bg='#DFDAEC').place(x=0, y=v)
                    Label(self.temporal, text=f'{i[0]}', bg='#DFDAEC').place(x=32, y=v)
                    if i[2] == 'Test':
                        Label(self.temporal, text=f'{i[2]}        {i[1]}', bg='#DFDAEC').place(x=180, y=v)
                    else:
                        Label(self.temporal, text=f'{i[2]}     {i[1]}', bg='#DFDAEC').place(x=180, y=v)
                    v+=21
                    self.res_count+=1
        Button(self.temporal, text='Back', width=25, bg='#3E4095', fg='#ffffff', height=1, cursor='hand2', bd=0,command=self.submit).place(x=1, y=439)

    def startexam(self):
        self.root.destroy()
        self.dbconnection()
        self.mycursor.execute('SELECT Student_aid, class_id FROM student_tb WHERE Student_aid = %s and password = %s',(self.invarid.get(), self.invarpas.get()))
        self.myfetch = self.mycursor.fetchone()
        cbt = CbtExam()
        self.student_id = self.myfetch[0]

    def nextCourse(self, val):
        self.res_count = 1
        if val == 'a':
            self.keepCourseId.append(self.myfetchCourse[0][0])
            for i in range(len(self.myfetchCourse)):
                try:
                    Label(self.temporal, text=f'{self.myfetchCourse[i][0]} (Names)', width=32, height=1, bg='#3E4095',
                      fg='#ffffff').place(x=36, y=37)
                    self.mycursor.execute('SELECT concat(First_name,\' \', Middle_name) FROM student_tb JOIN class_tb \
                    USING(class_id) JOIN course_tb USING(class_id) WHERE course_id = %s',(self.myfetchCourse[i][1],))
                    self.keepCourseId.append(self.myfetchCourse[i][1])
                    if self.myfetchCourse[i][1] in self.keepCourseId:
                        continue
                    else: break
                except: pass
        elif val == 'b' and len(self.myfetchCourse) > 1:
            if self.teacherScoreIndex > len(self.myfetchCourse)-1:
                self.teacherScoreIndex = 1
                self.stdCrsNperf('b')
            else:
                self.temporal.destroy()
                self.temporal = Frame(self.imageframe, height=462, width=264, bg='#DFDAEC')
                self.temporal.place(x=0, y=0)
                Label(self.temporal, text='S/N', width=4, height=1, bg='#3E4095', fg='#ffffff').place(x=1, y=37)
                Label(self.temporal, text='Student Performance', width=37, height=2, bg='#3E4095', fg='#ffffff').place(x=1,y=0)
                Button(self.temporal, text='→', width=11, bg='green', fg='#ffffff', height=1, bd=0,
                       command=lambda: self.nextCourse('b'), cursor='hand2').place(x=183, y=439)
                Button(self.temporal, text='Back', width=25, bg='#3E4095', fg='#ffffff', height=1, bd=0,
                       command=self.submit, cursor='hand2').place(x=1, y=439)
                self.dbconnection()
                Label(self.temporal, text=f'{self.myfetchCourse[self.teacherScoreIndex][0]} (Scores)', width=32, height=1, bg='#3E4095',
                      fg='#ffffff').place(x=36, y=37)
                self.mycursor.execute('SELECT concat(First_name,\'  \', Last_name), Score, Type FROM student_tb JOIN result_tb USING\
                             (Student_aid) WHERE Course_id = %s and Session_=(SELECT Control_Value FROM control_tb \
                             WHERE Control_id=%s) and Term=(SELECT Control_Value FROM control_tb WHERE Control_id \
                             = %s) ORDER BY Type', (self.myfetchCourse[self.teacherScoreIndex][1], 3, 4))
                self.myfetchScore_teacher = self.mycursor.fetchall()
                if self.myfetchScore_teacher:
                    v = 65
                    self.res_count = 1
                    for i in self.myfetchScore_teacher:
                        Label(self.temporal, text=f'{self.res_count}.)', bg='#DFDAEC').place(x=0, y=v)
                        Label(self.temporal, text=f'{i[0]}', bg='#DFDAEC').place(x=32, y=v)
                        if i[2] == 'Test':
                            Label(self.temporal, text=f'{i[2]}        {i[1]}', bg='#DFDAEC').place(x=180, y=v)
                        else:
                            Label(self.temporal, text=f'{i[2]}     {i[1]}', bg='#DFDAEC').place(x=180, y=v)
                        v += 21
                        self.res_count += 1
                self.teacherScoreIndex+=1

    def student(self):
        pass

class CbtExam(SDBM):
    def __init__(self):
        self.root = Tk()
        self.width = round(self.root.winfo_screenwidth()/1.3)
        self.height = round(self.root.winfo_screenheight()/1.1)
        self.root.geometry(f'{self.width}x{self.height}')
        self.root.maxsize(self.width, self.height)
        self.root.minsize(self.width, self.height)
        self.root.config(bg='#E6E7E8')
        self.root.title('PGS||CBT EXAMINATION APP')
        self.root.iconbitmap('images/pgs.ico')
        self.destroyFrame = Frame(self.root, width=self.width, height=self.height, bg='#606062')
        self.destroyFrame.place(x=0, y=0)
        self.firstSeen()
        self.root.mainloop()
    def timer(self,  val, toStopAfter=True):
        if val == 1:
            self.time-=1
            if self.time == 0:
                self.buttonaction()
            else:
                self.countdown.configure(text= self.myfetchinfo[2] +' Starts in '+ str(self.time))
                self.countdown.place_configure(x=360, y=220)
                self.root.after(1000, lambda:self.timer(1))
        elif val == 2:
            # this ensures the time is collected just once from the database
            if self.levels == 0:
                self.hour, self.minute, self.second = int(self.myfetchtime[0]), int(self.myfetchtime[1]), 0
                self.levels = 1
            if toStopAfter:
                if self.second != 0:
                    self.second -= 1
                    self.timedisp.config(text=f'{self.hour}:{self.minute}:{self.second}')
                if self.second <= 0 and self.minute != 0 and self.hour != 0:
                    self.minute -= 1
                    self.second = 59
                    self.timedisp.config(text=f'{self.hour}:{self.minute}:{self.second}')
                elif self.second <= 0 and self.minute == 0 and self.hour != 0:
                    self.second = 59
                    self.minute = 59
                    self.hour -= 1
                elif self.second <= 0 and self.minute == 0 and self.hour == 0:
                    super().dbconnection()
                    self.timedisp.config(text='00:00:00')
                    if self.levels == 1:
                        showwarning('PSG', 'Your time is up!')
                    self.destroyFrame.destroy()
                    self.getrightans = [r[-1] for r in self.quesOrder.values()]
                    self.answerconpare = tuple(zip([v.get() for v in self.stdAns.values()], self.getrightans))
                    for mark in self.answerconpare:
                        if mark[0] == mark[1]:
                            self.totalscore += 1
                    print(self.answerconpare, self.totalscore)
                    self.destroyFrame = Frame(self.root, width=self.width, height=self.height, bg='#606062')
                    self.destroyFrame.place(x=0, y=0)
                    self.firstSeen()
                    self.mycursor.execute('SELECT Control_Value FROM control_tb')
                    self.mycollect = self.mycursor.fetchall()
                    self.mycursor.execute('INSERT INTO result_tb(score, Student_aid, Course_id, Type,\
                     Session_, Term) VALUES(%s,%s,%s,%s,%s,%s)',
                        (self.totalscore, self.student_id, self.myfetchinfo[1], self.type, self.mycollect[2][0], self.mycollect[3][0]))
                    self.mycon.commit()
                elif self.second <= 0 and self.minute != 0 and self.hour == 0:
                    self.minute -= 1
                    self.second = 59
                    self.timedisp.config(text=f'{self.hour}:{self.minute}:{self.second}')
                if self.second == 0 and self.minute <= 0 and self.hour != 0:
                    self.hour -= 1
                    self.minute = 59
                    self.second = 59
                elif self.second == 0 and self.minute <= 0 and self.hour == 0:
                    self.timedisp.config(text='00:00:00')
                    self.timer(2, False)
                if self.second == 0 and self.minute == 0 and self.hour == 0:
                    self.timedisp.config(text='00:00:00')
                    self.timer(2, False)
                self.exalogoframe.update()
                self.root.after(1000, lambda:self.timer(2))

    def buttonaction(self):
        self.destroyFrame.destroy()
        self.destroyFrame = Frame(self.root, width=self.width, height=self.height, bg='#606062')
        self.destroyFrame.place(x=0, y=0)
        self.exalogoframe = Frame(self.destroyFrame, width=250, height=700, bg='#606062')
        self.exalogoframe.place(x=0, y=0)
        self.questionAction = Frame(self.exalogoframe, width=245, height=248, bg='#606062')
        self.questionAction.place(x=6, y=500)
        self.quesFrame = Frame(self.destroyFrame, width=801, height=670, bg='#E6E7E8')
        self.quesFrame.place(x=250, y=37)
        self.stdAns = dict()
        self.dbconnection()
        self.quesOrder = dict()
        self.type = ''
        self.mycursor.execute('SELECT Control_Value FROM control_tb')
        self.myfetchControl = self.mycursor.fetchall()
        if self.myfetchControl[1][0] == '1':
            self.type = 'Test'
        elif self.myfetchControl[1][0] == '2':
            self.type = 'Exam'
        self.present = str(datetime.datetime.now())
        #this section checks for the exam date, time and the student has exam/test
        self.mycursor.execute('SELECT class_id, course_id, ExamStatus FROM course_tb JOIN student_tb USING\
         (class_id) WHERE TestExam_Date = %s and Student_aid = %s and TestExam_TimeStart like %s',
                              (self.present[:10], self.student_id, self.present[11:15]+'%'))
        self.myfetchinfo = self.mycursor.fetchone()
        # if there exists a catch in self.myfetch, this block collects all the questions for the subjects at that time
        # the student can have only one course at a particular time and the same date
        self.examStatus = self.myfetchControl[2][0] + self.myfetchControl[3][0] + self.type
        self.enterExamPage()
        # and class_id = %s----, self.myfetchinfo[0]
        if self.myfetchinfo and (self.myfetchinfo[2] != self.examStatus):
            self.mycursor.execute('SELECT Question, Option_a, Option_b, Option_c, Option_d, Correct_answer FROM question_tb\
             WHERE Term = %s and Session = %s and Type = %s and course_id = %s',
                (self.myfetchControl[3][0], self.myfetchControl[2][0], self.type, self.myfetchinfo[1]))
            self.myfetch = self.mycursor.fetchall()
            self.mycursor.execute('UPDATE student_tb SET ExamStatus = %s WHERE Student_aid = %s', (self.examStatus, self.student_id))
            self.mycon.commit()
            # this secton arrange the buttons to easily navigate each questions
            self.ques = dict()
            for i in self.myfetch:
                self.ques[i[0]] = i[1:]
            self.quesView, l = [], 10
            self.sol = (len(self.ques)//10) + 1
            self.count = 1
            # since the number of questions for each course is user dependent, hence the question number button- this
            # block solves it
            for j in range(self.sol):
                # this produces the frame on which the buttons are to be placed
                self.quesf = Frame(self.questionAction, width=235, height=10, bg='#606062')
                self.quesf.pack()
                for i in self.ques.keys():
                    Button(self.quesf, text=self.count, width=2, command=lambda num=self.count:self.ques_show_select(num-1)).pack(side='left')
                    self.stdAns['answer'+str(self.count)] = StringVar()
                    self.count += 1
                    # this ensures that maximum of 10 buttons can be placed on the placed frame
                    if i == 10:
                        break
            for i in self.ques.keys():
                self.quesView.append(i)
            # questions shown on screen
            if self.test == 0:
                super().dbconnection()
                # this immediate line collect the question for the exam from the database and this is done only once
                random.shuffle(self.quesView)
                # right question answer and option order after shuffle
                for order in self.quesView:
                    self.quesOrder[order] = self.ques[order]
                # this immediate line collect the time for the exam from the database and this is done only once
                self.mycursor.execute(
                    'SELECT TestExam_Timehour, TestExam_Timeminutes FROM course_tb WHERE course_id = %s', (self.myfetchinfo[1],))
                self.myfetchtime = self.mycursor.fetchone()
                self.test = 1
            print(self.quesView)
            self.que_onscreen = Message(self.quesFrame, text='1)\t'+self.quesView[0], width=5000, bg='#E6E7E8', fg='#000000', font=('Arial', 20))
            self.que_onscreen.place(x=15, y=100)
            self.option_onscreenA = Radiobutton(self.quesFrame, text=f'   (a) {(self.ques[self.quesView[0]])[0]}', bg='#E6E7E8',
                value=(self.ques[self.quesView[0]])[0], variable=self.stdAns['answer1'], font=('Arial', 15), tristatevalue=0)
            self.option_onscreenA.place(x=15, y=180)
            self.option_onscreenB = Radiobutton(self.quesFrame, text=f'   (b) {(self.ques[self.quesView[0]])[1]}', bg='#E6E7E8',
                value=(self.ques[self.quesView[0]])[1], variable=self.stdAns['answer1'], font=('Arial', 15), tristatevalue=0)
            self.option_onscreenB.place(x=15, y=220)
            self.option_onscreenC = Radiobutton(self.quesFrame, text=f'   (c) {(self.ques[self.quesView[0]])[2]}', bg='#E6E7E8',
                value=(self.ques[self.quesView[0]])[2], variable=self.stdAns['answer1'], font=('Arial', 15), tristatevalue=0)
            self.option_onscreenC.place(x=15, y=260)
            self.option_onscreenD = Radiobutton(self.quesFrame, text=f'   (d) {(self.ques[self.quesView[0]])[2]}', bg='#E6E7E8',
                value=(self.ques[self.quesView[0]])[2], variable=self.stdAns['answer1'], font=('Arial', 15), tristatevalue=0)
            self.option_onscreenD.place(x=15, y=300)
            # this immediate line initiates the timer
            self.timer(2)
        else:
            if self.myfetchinfo[2] == self.examStatus:
                showinfo('PSG', 'you have done\n this exam')
            else:
                showinfo('PSG', 'you do not have any exam currently\n seek Teacher\'s Advice')

    def calculator(self):
        self.toplevel = Toplevel()
        self.toplevel.title('PGS[Cal]')
        self.toplevel.geometry('228x282')
        self.toplevel.maxsize(229, 282)
        self.firstFrame = Frame(self.toplevel, width=236, height=30, bg='#373435')
        self.firstFrame.pack(side='top', anchor='n')
        Label(self.firstFrame, text='PGS', font=('Courier', 12, 'bold'), bg='#373435', fg='#ffffff').place(x=2, y=3)
        self.invar_screen = StringVar()
        Entry(self.toplevel, textvariable=self.invar_screen, font=('courier', 32, 'bold'), disabledbackground='#A9ABAE', width=20,
              disabledforeground='#ffffff', bd=0, justify='right', state=DISABLED).pack(side='top')
        self.numFrame = Frame(self.toplevel, width=236, height=170, bg='#A9ABAE')
        self.numFrame.pack(side='bottom')
        Frame(self.toplevel, width=236, height=31, bg='#373435').pack(side='bottom')
        num = ['+', '1', '2', '3', '4', '←', '-', '5', '6', '7', '.', '±', '÷', '8', '9', '0', '√', '=']
        for i in range(3):
            self.buttonf = Frame(self.numFrame)
            self.buttonf.pack()
            for k in num:
                Button(self.buttonf, text=k, width=4, height=2, fg='#ffffff', bg='#000000', font=('courier', 9, 'bold')).pack(side='left')
                if k == '←' or k == '±':
                    num = num[(num.index(k))+1:]
                    break

    def exit(self):
        msg = askyesno('PGS', 'Do you really want to\n exit this page?')
        if msg == 1:
            self.examTestSubmit()
        elif msg == 0:
            pass
        self.root.quit()

    def examTestSubmit(self):
        msg = askyesno('PGS','Are you sure you want to submit?')
        if msg == 1:
            self.levels = 2
            self.hour, self.minute, self.second = 0, 0, 0
            self.timer(2, True)
        elif msg == 0:
            pass

    def ques_show_select(self, val):
        self.quesFrame.destroy()
        self.quesFrame = Frame(self.destroyFrame, width=801, height=670, bg='#E6E7E8')
        self.quesFrame.place(x=250, y=37)
        self.quesPick = self.quesView[val]
        self.ques_cont = self.ques[self.quesPick]
        self.que_onscreen = Message(self.quesFrame, text=str(val+1)+')\t'+self.quesPick, width=5000, bg='#E6E7E8',
                                    fg='#000000', font=('Arial', 20))
        self.que_onscreen.place(x=15, y=100)
        self.option_onscreenA = Radiobutton(self.quesFrame, text=f'   (a) {self.ques_cont[0]}',value=self.ques_cont[0],
                        variable=self.stdAns['answer'+str(val+1)], bg='#E6E7E8',font=('Arial', 15), tristatevalue=0)
        self.option_onscreenA.place(x=15, y=180)
        self.option_onscreenB = Radiobutton(self.quesFrame, text=f'   (b) {self.ques_cont[1]}', bg='#E6E7E8',
                        value=self.ques_cont[1], variable=self.stdAns['answer'+str(val+1)], font=('Arial', 15), tristatevalue=0)
        self.option_onscreenB.place(x=15, y=220)
        self.option_onscreenC = Radiobutton(self.quesFrame, text=f'   (c) {self.ques_cont[2]}', bg='#E6E7E8',
                    value=self.ques_cont[2], variable=self.stdAns['answer'+str(val+1)], font=('Arial', 15), tristatevalue=0)
        self.option_onscreenC.place(x=15, y=260)
        self.option_onscreenD = Radiobutton(self.quesFrame, text=f'   (d) {self.ques_cont[3]}', bg='#E6E7E8',
                            value=self.ques_cont[3], variable=self.stdAns['answer'+str(val+1)], font=('Arial', 15), tristatevalue=0)
        self.option_onscreenD.place(x=15, y=300)
        # for j in range(len(self.ques)):

school = SDBM()