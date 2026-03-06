# 💻 Tech Stack:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Anaconda](https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) ![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)

# 🚀 Python Student Projects

This repository contains two Python projects focused on **data analysis and GUI-based database applications**.

The goal of these projects is to demonstrate practical usage of:

* Python data analysis libraries
* GUI development with Tkinter
* Database integration using MySQL
* Basic exploratory data analysis and visualization

---

# 📂 Repository Structure

```
student-projects/
│
├── used_cars_analysis.py
├── student_registration_system.py
├── requirements.txt
└── README.md
```

---

# 📊 Project 1: Used Cars Data Analysis

This project performs **Exploratory Data Analysis (EDA)** on a used car dataset.

### Key Features

* Data cleaning and preprocessing
* Handling missing values
* Feature engineering (Car Age)
* Brand and model extraction
* Data visualization
* Log transformation for skewed variables

### Libraries Used

* Pandas
* NumPy
* Matplotlib
* Seaborn

### Run the Script

```
python used_cars_analysis.py
```

Make sure the dataset file is in the same directory.

---

# 🖥 Project 2: Student Registration System

A simple **GUI-based login and registration system** built with Tkinter and MySQL.

### Features

* Student registration
* Login authentication
* MySQL database storage
* Tkinter GUI interface

### Database Setup

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

### Run the Application

```
python student_registration_system.py
```

Make sure your MySQL server is running and credentials match the script.

---

# ⚙️ Installation

Install required dependencies:

```
pip install -r requirements.txt
```

---

# 🧰 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Tkinter
* MySQL

---

# 🎯 Purpose

These projects were created to practice:

* Data analysis workflows
* Python GUI development
* Database connectivity
* Visualization techniques

---

# 📌 Note

This repository is mainly for **learning and demonstration purposes**.

---

