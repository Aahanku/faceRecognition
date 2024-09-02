from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import ttk, messagebox
import mysql.connector


class Student:
    def __init__(self, root):
        self.root = root 
        self.root.geometry("2030x1800+0+0")
        self.root.title("Face Recognition System")


        # ==============variables===============
        self.var_id=StringVar()
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_regestrationno=StringVar()
        self.var_name=StringVar()
        self.var_hall=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_roll=StringVar()
        self.var_phone=StringVar()
        self.var_photo=StringVar()

        # First image
        img = Image.open(r"C:\Users\Nitish Kumar\OneDrive\Desktop\face reconization\images\STUDENT DETAILS 1.jpg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimag = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimag)
        f_lbl.place(x=0, y=0, width=500, height=130)
    
        # Second image
        img1 = Image.open(r"C:\Users\Nitish Kumar\OneDrive\Desktop\face reconization\images\STUDENT IMAGES 2.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimag1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoimag1)
        f_lbl1.place(x=1500, y=0, width=420, height=130)

        # Third image 
        img2 = Image.open(r"C:\Users\Nitish Kumar\OneDrive\Desktop\face reconization\images\student deatails.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimag2 = ImageTk.PhotoImage(img2)
        f_lbl2 = Label(self.root, image=self.photoimag2)
        f_lbl2.place(x=500, y=0, width=500, height=130)

        # Fourth image
        img3 = Image.open(r"C:\Users\Nitish Kumar\OneDrive\Desktop\face reconization\images\robo face.jpg")
        img3 = img3.resize((500, 130), Image.LANCZOS)
        self.photoimag3 = ImageTk.PhotoImage(img3)
        f_lbl3 = Label(self.root, image=self.photoimag3)
        f_lbl3.place(x=1000, y=0, width=500, height=130)

        # Fifth background image
        img4 = Image.open(r"C:\Users\Nitish Kumar\OneDrive\Desktop\face reconization\images\STUDENT IMAGES 5.jpg")
        img4 = img4.resize((1530, 1000), Image.LANCZOS)
        self.photoimag4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimag4)
        bg_img.place(x=0, y=130, width=2000, height=1000)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=2030, height=45)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=200, y=100, width=1700, height=1050)

        # Left label frame 
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=900, height=700)

        left_img3 = Image.open(r"C:\Users\Nitish Kumar\OneDrive\Desktop\face reconization\images\students 124.jpg")
        left_img3 = left_img3.resize((890, 130), Image.LANCZOS)
        self.photoimag3_left = ImageTk.PhotoImage(left_img3)
        f_lbl3 = Label(left_frame, image=self.photoimag3_left)
        f_lbl3.place(x=5, y=0, width=890, height=130)

        # current course 
        current_course_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Current Course information ", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=20, y=170, width=880, height=150)

        # department level
        dep_label=Label(current_course_frame,text="Department",font=("times now roman",12,"bold"))
        dep_label.grid(row=0,column=0)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep ,font=("times new roman", 12, "bold"), state="readonly")
        dep_combo["values"]=("Select Department","Computer Science (AI & ML)","Computer Science (Data Science)","Civil","Mechnical","Electronics and Communication","Electrical Engineering")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=10, sticky=W)

        # course
        course_label=Label(current_course_frame,text="Course",font=("times now roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course, font=("times new roman", 13, "bold"), state="readonly",width=20)
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # year
        year_label=Label(current_course_frame,text="Year",font=("times now roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year, font=("times new roman", 13, "bold"), state="readonly",width=20)
        year_combo["values"]=("Select Year","2023-2024","2022-2023","2021-2022","2020-2021")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # semester
        semester_label=Label(current_course_frame,text="Semester",font=("times now roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_sem, font=("times new roman", 13, "bold"), state="readonly",width=20)
        semester_combo["values"]=("Select Semester","First","Second")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # Class student information
        class_student_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information ", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=20, y=270, width=880, height=400)
 
        # student id
        student_Id_label = Label(class_student_frame, text="Reg:", font=("times new roman", 13, "bold"), bg="white")
        student_Id_label.grid(row=0,column=0,padx=10,sticky=W)

        student_Id_entry=ttk.Entry(class_student_frame,textvariable=self.var_regestrationno,width=20,font=("times new roman",13,"bold"))
        student_Id_entry.grid(row=0,column=1,padx=10,sticky=W)

        # Student name
        student_name_label = Label(class_student_frame,text="Student Name:", font=("times new roman", 13, "bold"), bg="white")
        student_name_label.grid(row=0,column=2,padx=10,sticky=W)

        student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_name ,width=20,font=("times new roman",13,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,sticky=W)

        # Class hall no
        class_hall_number = Label(class_student_frame, text="Hall no :", font=("times new roman", 13, "bold"), bg="white")
        class_hall_number.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        class_hall_entry=ttk.Entry(class_student_frame,textvariable=self.var_hall,width=20,font=("times new roman",13,"bold"))
        class_hall_entry.grid(row=1,column=1,padx=10,sticky=W)

        # Class roll no
        class_roll_number = Label(class_student_frame,text="Roll no :", font=("times new roman", 13, "bold"), bg="white")
        class_roll_number.grid(row=1,column=2,padx=10,pady=10,sticky=W)

        class_roll_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll ,width=20,font=("times new roman",13,"bold"))
        class_roll_entry.grid(row=1,column=3,padx=10,sticky=W)

        # Gender
        gender= Label(class_student_frame,text="Gender :", font=("times new roman", 13, "bold"), bg="white")
        gender.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        gender_entry=ttk.Entry(class_student_frame, textvariable=self.var_gender,width=20,font=("times new roman",13,"bold"))
        gender_entry.grid(row=2,column=1,padx=10,sticky=W)

        # Date of birth
        dob= Label(class_student_frame,text="Date Of Birth :", font=("times new roman", 13, "bold"), bg="white")
        dob.grid(row=2,column=2,padx=10,pady=10,sticky=W)

        dob_entry=ttk.Entry(class_student_frame, textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=10,sticky=W)
        
        # Class email id
        class_email_number = Label(class_student_frame ,text="Email Id :", font=("times new roman", 13, "bold"), bg="white")
        class_email_number.grid(row=3,column=0,padx=10,pady=10,sticky=W)

        class_email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        class_email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # Mobile number label
        class_mobile_number = Label(class_student_frame, text="Mobile No:", font=("times new roman", 13, "bold"), bg="white")
        class_mobile_number.grid(row=3, column=2, padx=10, pady=10, sticky=W)

        # Mobile number entry
        class_mobile_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone, width=20, font=("times new roman", 13, "bold"))
        class_mobile_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)
  
        # Address
        address= Label(class_student_frame, text="Address:", font=("times new roman", 13, "bold"), bg="white")
        address.grid(row=4,column=0,padx=10,pady=10,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        # Radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value=TRUE)
        radiobtn1.grid(row=6,column=0)

        # self.var_radio1=StringVar()

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1, text="No Photo Sample",value=FALSE)
        radiobtn2.grid(row=6,column=1)

        # Button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="yellow")
        btn_frame.place(x=0,y=250,width=900,height=130)

        save_btn = Button(btn_frame, text="save",command=self.add_data,font=("times new roman", 13, "bold"), bg="red", fg="white")
        save_btn.grid(row=0, column=0, padx=10, pady=10)

        UPDATE_btn = Button(btn_frame, text="Update", font=("times new roman", 13, "bold"), bg="red", fg="white")
        UPDATE_btn.grid(row=0, column=1, padx=10, pady=10)

        delete_btn = Button(btn_frame, text="Delete", font=("times new roman", 13, "bold"), bg="red", fg="white")
        delete_btn.grid(row=0, column=2, padx=10, pady=10)

        reset_btn = Button(btn_frame, text="Reset", font=("times new roman", 13, "bold"), bg="red", fg="white")
        reset_btn.grid(row=0, column=3, padx=10, pady=10)

        take_photo_btn = Button(btn_frame, text="Take Photo Sample", font=("times new roman", 13, "bold"), bg="red", fg="white")
        take_photo_btn.grid(row=1, column=0, padx=10, pady=20)

        update_photo_btn = Button(btn_frame, text="Update Photo Sample", font=("times new roman", 13, "bold"), bg="red", fg="white")
        update_photo_btn.grid(row=1, column=1, padx=10, pady=20)

        btn_detect = Button(btn_frame, text="Check Details", font=("times new roman", 13, "bold"), bg="red", fg="white")
        btn_detect.grid(row=1, column=2, padx=10, pady=20)

        # Right label frame 
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=960, y=10, width=700, height=700)


          # Search frame
        search_frame = LabelFrame(right_frame, bd=2, bg="yellow", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=100, width=680, height=490)

        search_label = Label(search_frame, text="Search By:", font=("times new roman", 13, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=20, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 13, "bold"), state="readonly", width=20)
        search_combo["values"]=("Select","Roll No","Phone no")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry=ttk.Entry(search_frame,width=20,font=("times new roman",10,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",font=("times new roman",10,"bold"),bg="red",fg="white")
        search_btn.grid(row=0,column=3,padx=10)

        showAll_btn=Button(search_frame,text="Show All",font=("times new roman",10,"bold"),bg="red",fg="white")
        showAll_btn.grid(row=0,column=4,padx=10)




        # table frame 

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="crimson")
        table_frame.place(x=5,y=180,width=680,height=490)

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)

        self.Student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","hall","roll","gender","dob","email","phone","address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("id", text="Student Id")
        self.Student_table.heading("dep",text="Department")
        self.Student_table.heading("course",text="Course")
        self.Student_table.heading("year",text="Year")
        self.Student_table.heading("sem",text="Semester")
        self.Student_table.heading("regestrationno",text="regestrationno")
        self.Student_table.heading("name",text="neme")
        self.Student_table.heading("hall",text="Hall")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("dob",text="DOB")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("address",text="Address")
        self.Student_table.heading("roll",text="roll")
        self.Student_table.heading("phone",text="Phone")
        self.Student_table.heading("photo",text="PhotoSampleStatus")
        self.Student_table["show"]="headings"
        self.Student_table.pack(fill=BOTH,expand=1)

    # create a function for add data

    def add_data(self):
        # try
        if self.var_dep.get()=="Select Department" or self.var_std_regestrationno.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        # else:
        try:
             conn=mysql.connector.connect(host="localhost",username="root",password="7250859718@",database="nitish")
             my_cursor=conn.cursor()
             my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                 self.var_phone.get(),
                                                                                                 self.var_dep.get(),
                                                                                                 self.var_course.get(),
                                                                                                 self.var_year.get(),
                                                                                                 self.var_sem.get(),
                                                                                                 self.var_name.get(),
                                                                                                 self.var_hall.get(),
                                                                                                 self.var_roll.get(),
                                                                                                 self.var_gender.get(),
                                                                                                 self.var_dob.get(),
                                                                                                 self.var_email.get(),
                                                                                                 self.var_reg.get(),
                                                                                                 self.var_address.get(),
                                                                                                 self.var_photo.get(),

                                                                                             ))
             conn.commit()
             conn.close()
             messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}",parent=self.root)


           # =======fetch data=============
            # def fetch_data(self):
            #     conn=mysql.connector.connect(host="localhost",username=root,password="7250859718@",database="finalstudent")
            


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()

 