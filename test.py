from Tkinter import *
import time
import MySQLdb
from datetime import datetime

db = MySQLdb.connect("119.46.143.134", "noetwo12", "749656", "EngSiam1")

i = 0
root = Tk()
root.option_add("*Font", "consolas 16")
# root.option_add
# root.geometry('400x400')
root.title("MES")

# window = Tk()
# window.title('Clock')
# window.geometry('200x60')

lb_clock = Label(font='times 16')
lb_clock.grid(row=0, column=6, sticky=E, padx=10, pady=10)


def tick():
    global curtime
    curtime = datetime.now()
    ftime = curtime.strftime('%d:%m:%Y-%H:%M:%S')
    lb_clock.config(text=ftime)
    lb_clock.after(1000, tick)


tick()
test_label0 = Label(root, text="Machine 01").grid(row=1, column=3)
test_label1 = Label(root, text="Plan").grid(row=2, column=1)
test_label2 = Label(root, text="10000", bg="white").grid(row=2, column=2)
test_label3 = Label(root, text="Actual").grid(row=2, column=4)


class DashBoard:
    i = 0

    def __init__(self):
        # self.i=0
        # self.text1 = ""
        self.text2 = "Hello here  is uptodate"
        self.mFrame = Frame()
        self.mFrame.grid(row=2, column=5)

        # self.watch = Label(self.mFrame, text=self.text2, font=('times',12,'bold'))
        self.watch = Label(self.mFrame, text=self.text2, font=('times 16'), bg="white")
        self.watch.grid()

        self.refresh_Label()  # first call it manually

    def refresh_Label(self):
        db = MySQLdb.connect("119.46.143.134", "noetwo12", "749656", "EngSiam1")
        mycursor = db.cursor()
        mycursor.execute(
            "((SELECT COUNT(TYPE) AS icnt FROM Mes2 ot WHERE TYPE=1  AND Date >  CURDATE() GROUP BY TYPE)) ")
        myresult = mycursor.fetchall()
        db.close()
        self.text2 = myresult
        self.watch.configure(text=self.text2)
        self.mFrame.after(5000, self.refresh_Label)  # repeat every 5s


obj1 = DashBoard()
test_label6 = Label(root, text="Number").grid(row=3, column=1)
test_label6 = Label(root, text="Hypothetical number", bg="white").grid(row=3, column=2)

test_label0 = Label(root, text="Machine 02").grid(row=1, column=9)
test_label1 = Label(root, text="Plan").grid(row=2, column=7)
test_label2 = Label(root, text="10000", bg="white").grid(row=2, column=8)
test_label3 = Label(root, text="Actual").grid(row=2, column=10)


class DashBoard1:
    i = 0

    def __init__(self):
        # self.i=0
        # self.text1 = ""
        self.text2 = "Hello here  is uptodate"
        self.mFrame = Frame()
        self.mFrame.grid(row=2, column=11)

        # self.watch = Label(self.mFrame, text=self.text2, font=('times',12,'bold'))
        self.watch = Label(self.mFrame, text=self.text2, font=('times 16'), bg="white")
        self.watch.grid()

        self.refresh_Label()  # first call it manually

    def refresh_Label(self):
        db = MySQLdb.connect("119.46.143.134", "noetwo12", "749656", "EngSiam1")
        mycursor = db.cursor()
        mycursor.execute(
            "((SELECT COUNT(TYPE) AS icnt FROM Mes ot WHERE TYPE=1  AND Date > CURDATE()  GROUP BY TYPE)) ")
        myresult = mycursor.fetchall()
        db.close()
        self.text2 = myresult
        self.watch.configure(text=self.text2)
        self.mFrame.after(5000, self.refresh_Label)  # repeat every 5s


obj1 = DashBoard1()
test_label6 = Label(root, text="Number").grid(row=3, column=7)
test_label6 = Label(root, text="Hypothetical number", bg="white").grid(row=3, column=8)

test_label0 = Label(root, text="Machine 03").grid(row=4, column=3)
test_label1 = Label(root, text="Plan").grid(row=5, column=1)
test_label2 = Label(root, text="10000", bg="white").grid(row=5, column=2)
test_label3 = Label(root, text="Actual").grid(row=5, column=4)


class DashBoard2:
    i = 0

    def __init__(self):
        # self.i=0
        # self.text1 = ""
        self.text2 = "Hello here  is uptodate"
        self.mFrame = Frame()
        self.mFrame.grid(row=5, column=5)

        # self.watch = Label(self.mFrame, text=self.text2, font=('times',12,'bold'))
        self.watch = Label(self.mFrame, text=self.text2, font=('times 16'), bg="white")
        self.watch.grid()

        self.refresh_Label()  # first call it manually

    def refresh_Label(self):
        db = MySQLdb.connect("119.46.143.134", "noetwo12", "749656", "EngSiam1")
        mycursor = db.cursor()
        mycursor.execute(
            "((SELECT COUNT(TYPE) AS icnt FROM Mes2 ot WHERE TYPE=1  AND Date >  2019-08-16 GROUP BY TYPE)) ")
        myresult = mycursor.fetchall()
        db.close()
        self.text2 = myresult
        self.watch.configure(text=self.text2)
        self.mFrame.after(5000, self.refresh_Label)  # repeat every 5s


obj1 = DashBoard2()
test_label6 = Label(root, text="Number").grid(row=6, column=1)
test_label6 = Label(root, text="Hypothetical number", bg="white").grid(row=6, column=2)

test_label0 = Label(root, text="Machine 04").grid(row=4, column=9)
test_label1 = Label(root, text="Plan").grid(row=5, column=7)
test_label2 = Label(root, text="10000", bg="white").grid(row=5, column=8)
test_label3 = Label(root, text="Actual").grid(row=5, column=10)


class DashBoard3:
    i = 0

    def __init__(self):
        # self.i=0
        # self.text1 = ""
        self.text2 = "Hello here  is uptodate"
        self.mFrame = Frame()
        self.mFrame.grid(row=5, column=11)

        # self.watch = Label(self.mFrame, text=self.text2, font=('times',12,'bold'))
        self.watch = Label(self.mFrame, text=self.text2, font=('times 16'), bg="white")
        self.watch.grid()

        self.refresh_Label()  # first call it manually

    def refresh_Label(self):
        db = MySQLdb.connect("119.46.143.134", "noetwo12", "749656", "EngSiam1")
        mycursor = db.cursor()
        mycursor.execute(
            "((SELECT COUNT(TYPE) AS icnt FROM Mes ot WHERE TYPE=1  AND Date > 2019-08-16  GROUP BY TYPE)) ")
        myresult = mycursor.fetchall()
        db.close()
        self.text2 = myresult
        self.watch.configure(text=self.text2)
        self.mFrame.after(5000, self.refresh_Label)  # repeat every 5s


obj1 = DashBoard3()
test_label6 = Label(root, text="Number").grid(row=6, column=7)
test_label6 = Label(root, text="Hypothetical number", bg="white").grid(row=6, column=8)

test_label0 = Label(root, text="Machine 05").grid(row=7, column=3)
test_label1 = Label(root, text="Plan").grid(row=8, column=1)
test_label2 = Label(root, text="10000", bg="white").grid(row=8, column=2)
test_label3 = Label(root, text="Actual").grid(row=8, column=4)


class DashBoard4:
    i = 0

    def __init__(self):
        # self.i=0
        # self.text1 = ""
        self.text2 = "Hello here  is uptodate"
        self.mFrame = Frame()
        self.mFrame.grid(row=8, column=5)

        # self.watch = Label(self.mFrame, text=self.text2, font=('times',12,'bold'))
        self.watch = Label(self.mFrame, text=self.text2, font=('times 16'), bg="white")
        self.watch.grid()

        self.refresh_Label()  # first call it manually

    def refresh_Label(self):
        db = MySQLdb.connect("119.46.143.134", "noetwo12", "749656", "EngSiam1")
        mycursor = db.cursor()
        mycursor.execute(
            "((SELECT COUNT(TYPE) AS icnt FROM Mes2 ot WHERE TYPE=1  AND Date >  2019-08-16 GROUP BY TYPE)) ")
        myresult = mycursor.fetchall()
        db.close()
        self.text2 = myresult
        self.watch.configure(text=self.text2)
        self.mFrame.after(5000, self.refresh_Label)  # repeat every 5s


obj1 = DashBoard4()
test_label6 = Label(root, text="Number").grid(row=9, column=1)
test_label6 = Label(root, text="Hypothetical number", bg="white").grid(row=9, column=2)

test_label0 = Label(root, text="Machine 06").grid(row=7, column=9)
test_label1 = Label(root, text="Plan").grid(row=8, column=7)
test_label2 = Label(root, text="10000", bg="white").grid(row=8, column=8)
test_label3 = Label(root, text="Actual").grid(row=8, column=10)


class DashBoard5:
    i = 0

    def __init__(self):
        # self.i=0
        # self.text1 = ""
        self.text2 = "Hello here  is uptodate"
        self.mFrame = Frame()
        self.mFrame.grid(row=8, column=11)

        # self.watch = Label(self.mFrame, text=self.text2, font=('times',12,'bold'))
        self.watch = Label(self.mFrame, text=self.text2, font=('times 16'), bg="white")
        self.watch.grid()

        self.refresh_Label()  # first call it manually

    def refresh_Label(self):
        db = MySQLdb.connect("119.46.143.134", "noetwo12", "749656", "EngSiam1")
        mycursor = db.cursor()
        mycursor.execute(
            "((SELECT COUNT(TYPE) AS icnt FROM Mes ot WHERE TYPE=1  AND Date > 2019-08-16  GROUP BY TYPE)) ")
        myresult = mycursor.fetchall()
        db.close()
        self.text2 = myresult
        self.watch.configure(text=self.text2)
        self.mFrame.after(5000, self.refresh_Label)  # repeat every 5s


obj1 = DashBoard5()
test_label6 = Label(root, text="Number").grid(row=9, column=7)
test_label6 = Label(root, text="Hypothetical number", bg="white").grid(row=9, column=8)

test_label0 = Label(root, text="Machine 07").grid(row=10, column=3)
test_label1 = Label(root, text="Plan").grid(row=11, column=1)
test_label2 = Label(root, text="10000", bg="white").grid(row=11, column=2)
test_label3 = Label(root, text="Actual").grid(row=11, column=4)


class DashBoard6:
    i = 0

    def __init__(self):
        # self.i=0
        # self.text1 = ""
        self.text2 = "Hello here  is uptodate"
        self.mFrame = Frame()
        self.mFrame.grid(row=11, column=5)

        # self.watch = Label(self.mFrame, text=self.text2, font=('times',12,'bold'))
        self.watch = Label(self.mFrame, text=self.text2, font=('times 16'), bg="white")
        self.watch.grid()

        self.refresh_Label()  # first call it manually

    def refresh_Label(self):
        db = MySQLdb.connect("119.46.143.134", "noetwo12", "749656", "EngSiam1")
        mycursor = db.cursor()
        mycursor.execute(
            "((SELECT COUNT(TYPE) AS icnt FROM Mes2 ot WHERE TYPE=1  AND Date >  2019-08-16 GROUP BY TYPE)) ")
        myresult = mycursor.fetchall()
        db.close()
        self.text2 = myresult
        self.watch.configure(text=self.text2)
        self.mFrame.after(5000, self.refresh_Label)  # repeat every 5s


obj1 = DashBoard6()
test_label6 = Label(root, text="Number").grid(row=12, column=1)
test_label6 = Label(root, text="Hypothetical number", bg="white").grid(row=12, column=2)

test_label0 = Label(root, text="Machine 08").grid(row=10, column=9)
test_label1 = Label(root, text="Plan").grid(row=11, column=7)
test_label2 = Label(root, text="10000", bg="white").grid(row=11, column=8)
test_label3 = Label(root, text="Actual").grid(row=11, column=10)


class DashBoard7:
    i = 0

    def __init__(self):
        # self.i=0
        # self.text1 = ""
        self.text2 = "Hello here  is uptodate"
        self.mFrame = Frame()
        self.mFrame.grid(row=11, column=11)

        # self.watch = Label(self.mFrame, text=self.text2, font=('times',12,'bold'))
        self.watch = Label(self.mFrame, text=self.text2, font=('times 16'), bg="white")
        self.watch.grid()

        self.refresh_Label()  # first call it manually

    def refresh_Label(self):
        db = MySQLdb.connect("119.46.143.134", "noetwo12", "749656", "EngSiam1")
        mycursor = db.cursor()
        mycursor.execute(
            "((SELECT COUNT(TYPE) AS icnt FROM Mes ot WHERE TYPE=1  AND Date > 2019-08-16  GROUP BY TYPE)) ")
        myresult = mycursor.fetchall()
        db.close()
        self.text2 = myresult
        self.watch.configure(text=self.text2)
        self.mFrame.after(5000, self.refresh_Label)  # repeat every 5s


obj1 = DashBoard7()
test_label6 = Label(root, text="Number").grid(row=12, column=7)
test_label6 = Label(root, text="Hypothetical number", bg="white").grid(row=12, column=8)



root.mainloop()
