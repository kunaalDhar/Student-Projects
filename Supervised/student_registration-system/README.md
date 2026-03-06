# 🧑‍🎓 Student Registration System

# 💻 Tech Stack

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge\&logo=python\&logoColor=ffdd54)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-blue?style=for-the-badge)
![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge\&logo=mysql\&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge\&logo=github\&logoColor=white)

---

# 🚀 Project Overview

This project is a **GUI-based Student Registration and Login System** built using **Python Tkinter and MySQL**.

The application allows users to:

* Register student accounts
* Store user data in a MySQL database
* Authenticate login credentials

It demonstrates **basic database connectivity and GUI development in Python.**

---

# ✨ Features

* Student registration form
* Login authentication
* GUI interface using Tkinter
* MySQL database integration
* Error handling and message alerts

---

# 📂 Project Structure

```
student-registration-system/
│
├── student_registration_system.py
└── README.md
```

---

# ⚙️ Database Setup

Run the following SQL commands:

```
CREATE DATABASE student_db;

USE student_db;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(100)
);
```

---

# ▶️ Run the Application

```
python student_registration_system.py
```

Make sure:

* MySQL server is running
* Database credentials in the script match your system

---

# 🎯 Learning Goals

This project demonstrates:

* GUI development with Tkinter
* MySQL database integration
* Basic authentication logic
* Form handling in Python

---

# 📜 License

This project is open-source and available under the MIT License.
