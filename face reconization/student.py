import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("2030x1800+0+0")
        self.root.title("Face Recognition System")

        # Variables initialization
        self.var_phone = tk.StringVar()
        self.var_dep = tk.StringVar()
        self.var_course = tk.StringVar()
        self.var_year = tk.StringVar()
        self.var_sem = tk.StringVar()
        self.var_std_registration_no = tk.StringVar()
        self.var_name = tk.StringVar()
        self.var_hall = tk.StringVar()
        self.var_gender = tk.StringVar()
        self.var_dob = tk.StringVar()
        self.var_email = tk.StringVar()
        self.var_address = tk.StringVar()
        self.var_roll = tk.StringVar()
        self.var_photo = tk.StringVar()

        # Load images and place labels
        self.load_images()
        self.create_ui()

    def load_images(self):
        # Load images using relative paths or ensure images are in the right directory
        self.photoimag = self.load_image("images/STUDENT DETAILS 1.jpg", (500, 130))
        self.photoimag1 = self.load_image("images/STUDENT IMAGES 2.jpg", (500, 130))
        self.photoimag2 = self.load_image("images/student deatails.jpg", (500, 130))
        self.photoimag3 = self.load_image("images/robo face.jpg", (500, 130))
        self.photoimag4 = self.load_image("images/STUDENT IMAGES 5.jpg", (1530, 1000))
        self.photoimag3_left = self.load_image("images/students 124.jpg", (890, 130))

    def load_image(self, path, size):
        try:
            img = Image.open(path)
            img = img.resize(size, Image.LANCZOS)
            return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Error loading image {path}: {str(e)}")
            return None

    def create_ui(self):
        # Implement the user interface here, as shown in your initial code
        # Add the rest of the UI elements and frames

        # First image
        f_lbl = tk.Label(self.root, image=self.photoimag)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # Other images and labels are similarly placed...
        # Use similar approach to create frames, buttons, etc.

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_registration_no.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="yourpassword",
                                               database="radh")
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "INSERT INTO student (phone, dep, course, year, sem, std_registration_no, name, hall, gender, dob, email, address, roll, photo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (self.var_phone.get(), self.var_dep.get(), self.var_course.get(), self.var_year.get(),
                     self.var_sem.get(), self.var_std_registration_no.get(), self.var_name.get(), self.var_hall.get(),
                     self.var_gender.get(), self.var_dob.get(), self.var_email.get(), self.var_address.get(),
                     self.var_roll.get(), self.var_photo.get()))
                conn.commit()
                messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
            finally:
                conn.close()


# Main loop
if __name__ == "__main__":
    root = tk.Tk()
    app = Student(root)
    root.mainloop()
