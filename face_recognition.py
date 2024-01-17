from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime
from PIL import Image, ImageTk

class Face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x780+0+0")
        self.root.title("Face recognition System")
        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="blue",fg="white")
        title_lbl.place(x=0,y=0,width=1280,height=45)
        img5=Image.open("E:\\Facial Recognition\\college_images\\facial.png")
        img5=img5.resize((610,550),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        bg_img=Label(self.root,image=self.photoimg5)
        bg_img.place(x=10,y=70,width=610,height=550)
        b2=Button(self.root,text="CLICK HERE TO SCAN",cursor="hand2",command=self.face_recog,font=("times new roman",25,"bold"),bg="darkblue",fg="red")
        b2.place(x=700,y=400,width=500,height=50)
    #=====================attendence================================================================
    def mark_attendance(self,i,r,n,d):
        with open("aman.csv","r+",newline="\n")as f:
            mydataList=f.readlines()
            name_list=[]
            for line in mydataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (n not in name_list) and (d not in name_list) and (r not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtSrting=now.strftime("%H:%M:%S")   
                f.writelines(f"\n{i},{r},{n},{d},{dtSrting},{d1},Present")


    # ================face recognition=====================
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]
            for(x,y,w,h)  in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                conn = mysql.connector.connect(host="localhost", username="root", password="Aman7607",database="face_recognition")
                my_cursor = conn.cursor()

                my_cursor.execute("Select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
               # n=str(n)
                n="".join(n)

                my_cursor.execute("Select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                #r=str(r)
                r="".join(r)

                my_cursor.execute("Select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
               # d=str(d)
                d="".join(d)

                my_cursor.execute("Select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
              #  i=str(i)
                i="".join(i)

                if confidence>77:
                    cv2.putText(img,f"Student id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3) 
                coord=[x,y,w,h]
            return coord        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

if __name__=="__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()
