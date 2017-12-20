import smtplib
from Tkinter import *


root = Tk()
root.title("hello world")
root.geometry("400x400+250+200")
MyLable = Label(root, text="hello welcome to my software for send mails(^_^)", fg="blue")
MyLable.pack()


def SmtpGmail():
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(GmailUserEntry, GmailPasswordEntry)
        server.sendmail(GmailEmailTheSenderFrom, GmailEmailSenderTo2Entry, GmailEmailSenderMessage)
        server.close()
        print "the email send"
    except:
        print "error"
def SmtpHotMail():
    try:
        server = smtplib.SMTP_SSL('smtp.live.com', 25)
        server.login(HotMailUserEntry, HotmailLable1GetInfoPassword)
        server.sendmail(HotMailEmailTheSenderFrom, HotMailEmailSenderTo2Entry, HotMailEmailSenderMessage)
        server.close()
        print "the email send"
    except:
        print "error"
def SmtpWalla():
    try:
        server = smtplib.SMTP_SSL('in.walla.co.il', 993)
        server.login(WallaUserEntry, GmailLable1GetInfoPassword)
        server.sendmail(WallaEmailTheSenderFrom, WallaEmailSenderTo2Entry, WallaEmailSenderMessage)
        server.close()
        print "the email send"
    except:
        print "error"


def Gmail():
    GmailTK = Tk()
    GmailTK.title("Send Email by Gmail")
    GmailTK.geometry("400x400+250+250")
    GmailLable = Label(GmailTK, text="we to sender gmail_(^_')",fg="green", bg="blue")
    GmailLable.pack()
    GmailLable1 = Label(GmailTK, text="insert your user gmail and password(^_*)", fg="green", bg="blue")
    GmailLable1.pack()
    GmailLable1GetInfoUser = Label(GmailTK, text="insert your user Gmail!! here)", fg="white", bg="black")
    GmailLable1GetInfoUser.pack()
    GmailUserEntry = Entry(GmailTK,)
    GmailUserEntry.pack()
    GmailLable1GetInfoPassword = Label(GmailTK, text="insert your user Pssword Gmail!! here)",fg="white", bg="black")
    GmailLable1GetInfoPassword.pack()
    GmailPasswordEntry = Entry(GmailTK,show="*")
    GmailPasswordEntry.pack()
    GmailEmailTheSenderFromTitle= Label(GmailTK, text="plaese insert your mail sender ",fg="white", bg="black")
    GmailEmailTheSenderFromTitle.pack()
    GmailEmailTheSenderFrom = Entry(GmailTK)
    GmailEmailTheSenderFrom.pack()
    GmailEmailSenderTo = Label(GmailTK, text="insert the you wnat to send",fg="white", bg="black")
    GmailEmailSenderTo.pack
    GmailEmailSenderToEntry = Entry(GmailTK)
    GmailEmailSenderToEntry.pack
    GmailEmailSenderMessageLabel = Label(GmailTK, text="insert the you wnat to send the Message",fg="white", bg="black")
    GmailEmailSenderMessageLabel.pack()
    GmailEmailSenderMessage = Entry(GmailTK)
    GmailEmailSenderMessage.pack()
    GmailbuttnGetAll = Button(GmailTK, text="click me if you finish", command=SmtpGmail)
    GmailbuttnGetAll.pack()
    mainloop()

def Hotmail():
    HotmailTK = Tk()
    HotmailTK.title("Send Email by Hotmail")
    HotmailTK.geometry("400x400+250+250")
    HotmailLable = Label(HotmailTK, text="we to sender Hotmail_(^_')", fg="green", bg="blue")
    HotmailLable.pack()
    HotmailLable1 = Label(HotmailTK, text="insert your user Hotmail and password(^_*)", fg="green", bg="blue")
    HotmailLable1.pack()
    HotmailLable1GetInfoUser = Label(HotmailTK, text="insert your user Hotmail!! here)", fg="white", bg="black")
    HotmailLable1GetInfoUser.pack()
    HotmailUserEntry = Entry(HotmailTK, )
    HotmailUserEntry.pack()
    HotmailLable1GetInfoPassword = Label(HotmailTK, text="insert your user Pssword Hotmail!! here)", fg="white",bg="black")
    HotmailLable1GetInfoPassword.pack()
    HotmailPasswordEntry = Entry(HotmailTK, show="*")
    HotmailPasswordEntry.pack()
    HotmailEmailTheSenderFromTitle = Label(HotmailTK, text="plaese insert your mail sender ", fg="white", bg="black")
    HotmailEmailTheSenderFromTitle.pack()
    HotmailEmailTheSenderFrom = Entry(HotmailTK)
    HotmailEmailTheSenderFrom.pack()
    HotmailEmailSenderTo2 = Label(HotmailTK, text="insert the you wnat to send", fg="white", bg="black")
    HotmailEmailSenderTo2.pack
    HotmailEmailSenderTooEntry = Entry(HotmailTK)
    HotmailEmailSenderTooEntry.pack
    HotmailEmailSenderMessageLabel = Label(HotmailTK, text="insert the you wnat to send the Message", fg="white", bg="black")
    HotmailEmailSenderMessageLabel.pack()
    HotmailEmailSenderMessage = Entry(HotmailTK)
    HotmailEmailSenderMessage.pack()
    HotmailbuttnGetAll = Button(HotmailTK, text="click me if you finish", command=SmtpHotMail)
    HotmailbuttnGetAll.pack()
    mainloop()

def Walla():
    WallaTK = Tk()
    WallaTK.title("Send Email by Walla")
    WallaTK.geometry("400x400+250+250")
    WallaLable = Label(WallaTK, text="we to sender Walla_(^_')", fg="green", bg="blue")
    WallaLable.pack()
    WallaLable1 = Label(WallaTK, text="insert your user Walla and password(^_*)", fg="green", bg="blue")
    WallaLable1.pack()
    WallaLable1GetInfoUser = Label(WallaTK, text="insert your user Walla!! here)", fg="white", bg="black")
    WallaLable1GetInfoUser.pack()
    WallaUserEntry = Entry(WallaTK)
    WallaUserEntry.pack()
    WallaLable1GetInfoPassword = Label(WallaTK, text="insert your user Pssword Walla!! here)", fg="white",bg="black")
    WallaLable1GetInfoPassword.pack()
    WallaPasswordEntry = Entry(WallaTK, show="*")
    WallaPasswordEntry.pack()
    WallaEmailTheSenderFromTitle = Label(WallaTK, text="plaese insert your mail sender ", fg="white", bg="black")
    WallaEmailTheSenderFromTitle.pack()
    WallaEmailTheSenderFrom = Entry(WallaTK)
    WallaEmailTheSenderFrom.pack()
    WallaEmailSenderTo2 = Label(WallaTK, text="insert the you wnat to send", fg="white", bg="black")
    WallaEmailSenderTo2.pack
    WallaEmailSenderTooEntry = Entry(WallaTK)
    WallaEmailSenderTooEntry.pack
    WallaEmailSenderMessageLabel = Label(WallaTK, text="insert the you wnat to send the Message", fg="white", bg="black")
    WallaEmailSenderMessageLabel.pack()
    WallaEmailSenderMessage = Entry(WallaTK)
    WallaEmailSenderMessage.pack()
    WallabuttnGetAll = Button(WallaTK, text="click me if you finish", command=SmtpWalla)
    WallabuttnGetAll.pack()
    mainloop()
def EExit():
    exit()



MyButten1 = Button(root, text="Gmail",fg="green", bg="blue",command=Gmail)
MyButten2 = Button(root, text="HotMail",fg="green", bg="blue", command=Hotmail)
MyButten3 = Button(root, text="Walla",fg="green", bg="blue", command=Walla)
MyButten4 = Button(root, text="Exit",fg="green", bg="blue", command=EExit)
MyButten1.pack()
MyButten2.pack()
MyButten3.pack()
MyButten4.pack()
mainloop()
