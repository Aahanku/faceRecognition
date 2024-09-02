from tkinter import *
from PIL import Image, ImageTk
from student import Student

class Face_Reconition_Systeam:
    def __init__(self, root):
        self.root = root 
        self.root.geometry("2030x1800+0+0")  # Corrected geometry value (x instead of *)
        self.root.title("face recognition systeam")
         
        # First image
        img=Image.open(r"C:\Users\Nitish Kumar\OneDrive\Desktop\face reconization\images\student deatails.jpg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimag=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimag)
        f_lbl.place(x=0,y=0,width=500,height=130)
    
        # Second image
        img1=Image.open(r"C:\Users\Nitish Kumar\OneDrive\Desktop\face reconization\images\robo face.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimag1=ImageTk.PhotoImage(img1)

        f_lbl1=Label(self.root,image=self.photoimag1)
        f_lbl1.place(x=1500,y=0,width=420,height=130)


        # Third image 
        img2=Image.open(r"C:\Users\Nitish Kumar\OneDrive\Desktop\face reconization\images\biometric.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimag2=ImageTk.PhotoImage(img2)

        f_lbl2=Label(self.root,image=self.photoimag2)
        f_lbl2.place(x=500,y=0,width=500,height=130)

        # Fourth image
        img3=Image.open(r"C:\Users\Nitish Kumar\OneDrive\Desktop\face reconization\images\face back.jpg")
        img3 = img3.resize((500, 130), Image.LANCZOS)
        self.photoimag3=ImageTk.PhotoImage(img3)

        f_lbl3=Label(self.root,image=self.photoimag3)
        f_lbl3.place(x=1000,y=0,width=500,height=130)

        # Fifth background image
        img4=Image.open(r"C:\Users\Nitish Kumar\OneDrive\Desktop\face reconization\images\bg final.jpg")
        img4 = img4.resize((1530, 1000), Image.LANCZOS)
        self.photoimag4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimag4)
        bg_img.place(x=0,y=130,width=2000,height=1000)

        title_lbl=Label(bg_img,text="ADVANNCE FACE RECOGNDANCE ATTENDANCE SYSTEAM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=2030,height=45)

        # STUDENT BUTTON 1
        img5=Image.open(r"C:\Users\Nitish Kumar\OneDrive\Desktop\face reconization\images\bg final.jpg")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimag5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimag5,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        # DETECT FACE BUTTON 2
        img6=Image.open(r"C:\Users\Nitish Kumar\OneDrive\Desktop\face reconization\images\bg final.jpg")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimag6=ImageTk.PhotoImage(img6)

        b2=Button(bg_img,image=self.photoimag6,cursor="hand2")
        b2.place(x=500,y=100,width=220,height=220)

        b2_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b2_1.place(x=500,y=300,width=220,height=40)

        # ATTENDANCE BUTTON 3
        img7=Image.open(r"C:\Users\Nitish Kumar\OneDrive\Desktop\face reconization\images\atten.jpg")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoimag7=ImageTk.PhotoImage(img7)

        b3=Button(bg_img,image=self.photoimag7,cursor="hand2")
        b3.place(x=800,y=100,width=220,height=220)

        b3_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b3_1.place(x=800,y=300,width=220,height=40)

        #  # help BUTTON 4
        # img8=Image.open(r"C:\Users\Nitish Kumar\OneDrive\Desktop\face reconization\images\")
        # img8 = img8.resize((220, 220), Image.LANCZOS)
        # self.photoimag8=ImageTk.PhotoImage(img8)

        # b4=Button(bg_img,image=self.photoimag8,cursor="hand2")
        # b4.place(x=800,y=100,width=220,height=220)

        # b4_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        # b4_1.place(x=1100,y=300,width=220,height=40)

        # attendence 4 
        img8=Image.open(r"C:\Users\Nitish Kumar\OneDrive\Desktop\face reconization\images\help center.jpg")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimag8=ImageTk.PhotoImage(img8)

        b4=Button(bg_img,image=self.photoimag8,cursor="hand2")
        b4.place(x=1100,y=100,width=220,height=220)

        b4_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b4_1.place(x=1100,y=300,width=220,height=40)
 
        # developer BUTTON 5
        img9=Image.open(r"C:\Users\Nitish Kumar\OneDrive\Desktop\face reconization\images\developer.jpg")
        img9 = img9.resize((220, 220), Image.LANCZOS)
        self.photoimag9=ImageTk.PhotoImage(img9)

        b5=Button(bg_img,image=self.photoimag9,cursor="hand2")
        b5.place(x=200,y=400,width=220,height=220)

        b5_1=Button(bg_img,text="developer",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b5_1.place(x=200,y=620,width=220,height=40)
        # ==============funstion button=========================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = Face_Reconition_Systeam(root)
    root.mainloop()
