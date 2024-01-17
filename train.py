import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from PIL import Image, ImageTk

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x780+0+0")
        self.root.title("Train Data")
        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="blue",fg="white")
        title_lbl.place(x=0,y=0,width=1280,height=45)
        imgtop=Image.open("E:\\Facial Recognition\\college_images\\facialrecognition.png")
        imgtop=imgtop.resize((1280,650),Image.ANTIALIAS)
        self.photoimgtop=ImageTk.PhotoImage(imgtop)
        bg_img=Label(self.root,image=self.photoimgtop)
        bg_img.place(x=0,y=130,width=1280,height=650)
        b2=Button(self.root,text="CLICK HERE TO TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",25,"bold"),bg="darkblue",fg="red")
        b2.place(x=300,y=70,width=800,height=50)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L')  #grayscale
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        ##training the classifier
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")    
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training of dataset completed!!!!")


if __name__=="__main__":
    root=tkinter.Tk()
    obj=Train(root)
    root.mainloop()
