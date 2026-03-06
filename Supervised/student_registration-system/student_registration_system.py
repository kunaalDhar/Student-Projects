import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Database connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="student_db"
    )

# Register function
def register():
    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()

    try:
        conn = connect_db()
        cursor = conn.cursor()

        query = "INSERT INTO students (name,email,password) VALUES (%s,%s,%s)"
        values = (name,email,password)

        cursor.execute(query,values)
        conn.commit()

        messagebox.showinfo("Success","Registration Successful")

    except Exception as e:
        messagebox.showerror("Error",str(e))

    finally:
        conn.close()

# Login function
def login():
    email = entry_email.get()
    password = entry_password.get()

    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT name FROM students WHERE email=%s AND password=%s"
    cursor.execute(query,(email,password))

    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Welcome",f"Welcome {result[0]}")
    else:
        messagebox.showerror("Error","Invalid Email or Password")

    conn.close()


# GUI
root = tk.Tk()
root.title("Student System")
root.geometry("400x300")

tk.Label(root,text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root,text="Email").pack()
entry_email = tk.Entry(root)
entry_email.pack()

tk.Label(root,text="Password").pack()
entry_password = tk.Entry(root,show="*")
entry_password.pack()

tk.Button(root,text="Register",command=register).pack(pady=5)
tk.Button(root,text="Login",command=login).pack(pady=5)

root.mainloop()