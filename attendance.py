import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
from PIL import Image, ImageTk

mydata=[]

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x780+0+0")
        self.root.title("ATTENDENCE")
        img=Image.open("E:\\Facial Recognition\\college_images\\AdobeStock.jpeg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=400,y=0,width=500,height=130)
        #backgrpung
        img1=Image.open("E:\\Facial Recognition\\college_images\\blue.jpg")
        img1=img1.resize((1280,710),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        bg_img=Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=130,width=1280,height=710)
        
        title_lbl=Label(bg_img,text="Attendance Management System",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1280,height=45)
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=5,y=50,width=1260,height=570)
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=610,height=550)
        currentcourse_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE)
        currentcourse_frame.place(x=5, y=12, width=710, height=300)
        #labels and entry
        AttendanceID_label = Label(currentcourse_frame, text="AttendanceID:", font=("times new roman", 11, "bold"),
                                bg="white")
        AttendanceID_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        AttendanceID_entry = ttk.Entry(currentcourse_frame, width=20,
                                    font=('times new roman', 11, 'bold'))
        AttendanceID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        rollLabel_label = Label(currentcourse_frame, text="Roll:", font=("times new roman", 11, "bold"),
                                  bg="white")
        rollLabel_label.grid(row=0, column=2, padx=4, pady=8)

        rollLabel_entry = ttk.Entry(currentcourse_frame, width=20,
                                      font=('times new roman', 11, 'bold'))
        rollLabel_entry.grid(row=0, column=3,pady=8,)

        nameLabel_label = Label(currentcourse_frame, text="Name:", font=("times new roman", 11, "bold"),
                                  bg="white")
        nameLabel_label.grid(row=1, column=0)

        nameLabel_entry = ttk.Entry(currentcourse_frame, width=20,
                                      font=('times new roman', 11, 'bold'))
        nameLabel_entry.grid(row=1, column=1,pady=8)

        depLabel_label = Label(currentcourse_frame, text="Department:", font=("times new roman", 11, "bold"),
                                  bg="white")
        depLabel_label.grid(row=1, column=2)

        depLabel_entry = ttk.Entry(currentcourse_frame, width=20,
                                      font=('times new roman', 11, 'bold'))
        depLabel_entry.grid(row=1, column=3,pady=8)

        timeLabel_label = Label(currentcourse_frame, text="Time:", font=("times new roman", 11, "bold"),
                                  bg="white")
        timeLabel_label.grid(row=2, column=0)

        timeLabel_entry = ttk.Entry(currentcourse_frame, width=20,
                                      font=('times new roman', 11, 'bold'))
        timeLabel_entry.grid(row=2, column=1,pady=8)
        dateLabel_label = Label(currentcourse_frame, text="Date:", font=("times new roman", 11, "bold"),
                                  bg="white")
        dateLabel_label.grid(row=2, column=2)

        dateLabel_entry = ttk.Entry(currentcourse_frame, width=20,
                                      font=('times new roman', 11, 'bold'))
        dateLabel_entry.grid(row=2, column=3,pady=8)
        attendanceLabel=Label(currentcourse_frame, text="Attendance Status",bg="white",font=("times new roman", 11, "bold"))
        attendanceLabel.grid(row=3, column=0)
        self.atten_status=ttk.Combobox(currentcourse_frame,width=20,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0) 
        Import_btn= Button(currentcourse_frame,text="Import",command=self.importCsv, width=14, font=('times new roman', 13, 'bold'),
                          bg="blue", fg="white")
        Import_btn.grid(row=4, column=3)





        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("times new roman",11,"bold"))
        Right_frame.place(x=630,y=10,width=620,height=550)
        table_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE,
                                  font=("times new roman", 15, "bold"))
        table_frame.place(x=5, y=12, width=690, height=400)
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
    #fetch data
    def fetchData(self,rows):
       self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
       for i in rows:
        self.AttendanceReportTable.insert("",END,values=i)
        
    def importCsv(self):
        global mydata
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)    


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
