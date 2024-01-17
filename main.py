from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
import os
class Face_recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x780+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")
        img=Image.open("E:\\Facial Recognition\\college_images\\Graphic.jpg")
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
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION & ATTENDENCE PROTAL",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1280,height=45)
        #student button
        img4=Image.open("E:\\Facial Recognition\\college_images\\gettyimages-1022573162.jpg")
        img4=img4.resize((200,200),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=80,width=200,height=200)
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2")
        b1_1.place(x=100,y=200,width=200,height=40)
       
        #detect face
        
        img5=Image.open("E:\\Facial Recognition\\college_images\\face_detector1.jpg")
        img5=img5.resize((200,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b2.place(x=350,y=80,width=200,height=200)
        b2_1=Button(bg_img,text="Scan Face",cursor="hand2",command=self.face_data)
        b2_1.place(x=350,y=200,width=200,height=40)

        #attendence 
        img6=Image.open("E:\Facial Recognition\college_images\\facialrecognition.png")
        img6=img6.resize((200,200),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b3=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b3.place(x=600,y=80,width=200,height=200)
        b3_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data)
        b3_1.place(x=600,y=200,width=200,height=40)
        
        #Train face
        img7=Image.open("E:\Facial Recognition\college_images\kisspng-website-wireframe-face-facial-recognition-system-w-recognition-5acafff32d2084.1500702215232532351849.jpg")
        img7=img7.resize((200,200),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        b4=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.train_data)
        b4.place(x=850,y=80,width=200,height=200)
        b4_1=Button(bg_img,text="Train Face",cursor="hand2",command=self.train_data)
        b4_1.place(x=850,y=200,width=200,height=40)

        #photos face
        img8=Image.open("E:\Facial Recognition\college_images\\teaser.png")
        img8=img8.resize((200,200),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        b5=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.open_img)
        b5.place(x=350,y=300,width=200,height=200)
        b5_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img)
        b5_1.place(x=350,y=420,width=200,height=40)

        #exit button
        img9=Image.open(r"E:\\Facial Recognition\\college_images\\exit.jpg")
        img9=img9.resize((200,200),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        b6=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b6.place(x=600,y=300,width=200,height=200)
        b6_1=Button(bg_img,text="EXIT",cursor="hand2")
        b6_1.place(x=600,y=420,width=200,height=40)

    def open_img(self):
        os.startfile("data")

    #FUNCTION BUTTONS
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)              
    







if __name__=="__main__":
    root=Tk()
    obj=Face_recognition_System(root)
    root.mainloop()
