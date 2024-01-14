import tkinter 
from tkinter import ttk
from tkinter import messagebox
import random
import pandas as pd

def submit():
    firstname = first_name_entry.get()
    lastname = last_name_entry.get()

    if firstname and lastname:
        age = age_spinbox.get()
        department = department_combobox.get()

        # Student's info
        email_id = email_id_entry.get()
        ph_no = ph_no_entry.get()
        class_ten_no = class_ten_no_entry.get()
        class_twelve_no = class_twelve_no_entry.get()
        address = address_entry.get()  # Include address

        # Generate unique registration ID
        registration_id = random.randint(1000000000, 9999999999)

        # Create a DataFrame for Excel export
        data = {
            "Registration ID": registration_id,
            "First Name": firstname,
            "Last Name": lastname,
            "Age": age,
            "Department": department,
            "Email ID": email_id,
            "Phone No.": ph_no,
            "Class 10 (%)": class_ten_no,
            "Class 12 (%)": class_twelve_no,
            "Address": address  # Include address
        }
        df = pd.DataFrame(data, index=[0])

        # Export DataFrame to Excel
        df.to_excel("student_data.xlsx", index=False)

        print("Registration ID:", registration_id)
        print("----------------------------------------")
        print("Data saved to Excel successfully.")

    else:
        tkinter.messagebox.showwarning(title="Error", message="First name and last name are required.")

def clear_all():
    for widget in student_info.winfo_children():
        if(isinstance(widget,tkinter.Entry)):
            widget.delete(0,'end')
        if(isinstance(widget,tkinter.Text)):
            widget.delete(0,'end')
        if(isinstance(widget,tkinter.Spinbox)):
            widget.delete(0,'end')
        if(isinstance(widget,ttk.Combobox)):
            widget.delete(0,'end')

        
    
window= tkinter.Tk()
window.title(" Student's Data Entry form")

frame= tkinter.Frame(window)
frame.pack()

student_info=tkinter.LabelFrame(frame,text="Student Information")
student_info.grid(row=0,column=0,padx=20, pady=10)

first_name_label=tkinter.Label(student_info, text="First Name")
first_name_label.grid(row=0,column=0)
last_name_label = tkinter.Label(student_info, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(student_info)
last_name_entry = tkinter.Entry(student_info)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

age_label = tkinter.Label(student_info, text="Age")
age_spinbox = tkinter.Spinbox(student_info, from_=18, to=110)
age_label.grid(row=4, column=0)
age_spinbox.grid(row=5, column=0)

department_label = tkinter.Label(student_info, text="Department")
department_combobox = ttk.Combobox(student_info, values=["CSE-A", "CSE-B", "IT", "ECE", "AIML", "EE"])
department_label.grid(row=4, column=1)
department_combobox.grid(row=5, column=1)

address_label=tkinter.Label(student_info, text="Address")
address_label.grid(row=6,column=0)
address_entry = tkinter.Entry(student_info)
address_entry.grid(row=6, column=1)

email_id_label=tkinter.Label(student_info, text="Email ID")
email_id_label.grid(row=8,column=0)
email_id_entry = tkinter.Entry(student_info)
email_id_entry.grid(row=8, column=1)

ph_no_label=tkinter.Label(student_info, text="Phone NO.")
ph_no_label.grid(row=10,column=0)
ph_no_entry = tkinter.Entry(student_info)
ph_no_entry.grid(row=10, column=1)

class_ten_no_label=tkinter.Label(student_info, text="Class 10 (in %) :")
class_ten_no_label.grid(row=12,column=0)
class_ten_no_entry = tkinter.Entry(student_info)
class_ten_no_entry.grid(row=12, column=1)

class_twelve_no_label=tkinter.Label(student_info, text="Class 12 (in %) :")
class_twelve_no_label.grid(row=14,column=0)
class_twelve_no_entry = tkinter.Entry(student_info)
class_twelve_no_entry.grid(row=14, column=1)


button1 = tkinter.Button(student_info, 
                   text="SUBMIT", 
                   fg="green",
                   command=lambda : submit())
button1.grid(row=20,column=0,padx=20, pady=10)


button2 = tkinter.Button(student_info, 
                   text="RESET", 
                   fg="black",
                   command=lambda : clear_all())
button2.grid(row=20,column=1,padx=20, pady=10)


button3 = tkinter.Button(student_info, 
                   text="BACK", 
                   fg="red",
                   command=quit)
button3.grid(row=20,column=2,padx=20, pady=10)

window.mainloop()
