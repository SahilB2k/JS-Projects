import tkinter as tk
import mysql.connector

window = tk.Tk()
window.geometry("600x500")
window.title("Registration Form")

# Establishing connection to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@sahil@anaanti",
    database="new"
)

# Creating a cursor object
mycursor = mydb.cursor()

# Creating table if it doesn't exist
mycursor.execute("CREATE TABLE IF NOT EXISTS driving_license ("
                 "id INT AUTO_INCREMENT PRIMARY KEY,"
                 "first_name VARCHAR(255),"
                 "last_name VARCHAR(255),"
                 "email VARCHAR(255),"
                 "phone_number VARCHAR(20),"
                 "gender VARCHAR(10),"
                 "city VARCHAR(100)"
                 ")")

def selection():
    selection_text = "You selected the option " + str(radio.get())
    lbl.config(text=selection_text)

def submit():
    first_name = first_name_value.get()
    last_name = last_name_value.get()
    email_address = email_address_value.get()
    phone_number = phone_number_value.get()
    gender = "Male" if radio.get() == 1 else "Female"
    city = cv.get()

    # Inserting data into MySQL table
    sql = "INSERT INTO registration_form(first_name, last_name, email, phone_number, gender, city) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (first_name, last_name, email_address, phone_number, gender, city)
    mycursor.execute(sql, val)
    mydb.commit()

    response_label.config(text='Your response has been submitted')

def clear_data():
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    email_address_entry.delete(0, tk.END)
    phone_number_entry.delete(0, tk.END)

def update_data():
    id_to_update = id_to_update_entry.get()
    first_name = first_name_value.get()
    last_name = last_name_value.get()
    email_address = email_address_value.get()
    phone_number = phone_number_value.get()
    gender = "Male" if radio.get() == 1 else "Female"
    city = cv.get()

    # Updating data in MySQL table
    sql = "UPDATE registration_form SET first_name = %s, last_name = %s, email = %s, phone_number = %s, gender = %s, city = %s WHERE id = %s"
    val = (first_name, last_name, email_address, phone_number, gender, city, id_to_update)
    mycursor.execute(sql, val)
    mydb.commit()

    response_label.config(text='Data updated successfully')

def read_data():
    mycursor.execute("SELECT * FROM registration_form")
    records = mycursor.fetchall()
    for record in records:
        print(record)

def delete_data():
    id_to_delete = id_to_delete_entry.get()

    # Deleting data from MySQL table
    sql = "DELETE FROM registration_form WHERE id = %s"
    val = (id_to_delete,)
    mycursor.execute(sql, val)
    mydb.commit()

    response_label.config(text='Data deleted successfully')

tk.Label(text='First Name', font=(10)).grid(row=1, column=0, padx=80, pady=20)
tk.Label(text='Last Name', font=(10)).grid(row=2, column=0, padx=80, pady=20)
tk.Label(text='Email Address', font=(10)).grid(row=3, column=0, padx=80, pady=20)
tk.Label(text='Phone Number', font=(10)).grid(row=4, column=0, padx=80, pady=20)

first_name_value = tk.StringVar()
last_name_value = tk.StringVar()
email_address_value = tk.StringVar()
phone_number_value = tk.StringVar()

first_name_entry = tk.Entry(window, textvariable=first_name_value, font=(10))
last_name_entry = tk.Entry(window, textvariable=last_name_value, font=(10))
email_address_entry = tk.Entry(window, textvariable=email_address_value, font=(10))
phone_number_entry = tk.Entry(window, textvariable=phone_number_value, font=(10))

first_name_entry.grid(row=1, column=1, pady=20)
last_name_entry.grid(row=2, column=1, pady=20)
email_address_entry.grid(row=3, column=1, pady=20)
phone_number_entry.grid(row=4, column=1, pady=20)

radio = tk.IntVar()
lbl = tk.Label(text="Select Your Gender:", font=(17))
lbl.grid(row=5, column=0, padx=80, pady=20)

tk.Radiobutton(window, text="Male", font=(12), variable=radio, value=1, command=selection).grid(row=5, column=1)
tk.Radiobutton(window, text="Female", font=(12), variable=radio, value=2, command=selection).grid(row=5, column=2)

list_of_cities = ("MUMBAI", "NAVI MUMBAI", "PUNE", "SOLAPUR", "KOLHAPUR", "TULJAPUR")
cv = tk.StringVar()
drplist = tk.OptionMenu(window, cv, *list_of_cities)
drplist.grid(row=6, column=1)
cv.set("SELECT CITY")

city_label = tk.Label(window, text="Select city", font=("bold", 17))
city_label.grid(row=6, column=0)

response_label = tk.Label(window, text='', font=(17))
response_label.grid(row=7, column=1, pady=20)

id_to_update_entry = tk.Entry(window, font=(10))
id_to_update_entry.grid(row=8, column=1, pady=10)
tk.Label(window, text="Enter ID to Update:", font=(10)).grid(row=8, column=0)

id_to_delete_entry = tk.Entry(window, font=(10))
id_to_delete_entry.grid(row=9, column=1, pady=10)
tk.Label(window, text="Enter ID to Delete:", font=(10)).grid(row=9, column=0)

tk.Button(text='Submit', command=submit, font=(17)).grid(row=10, column=0, pady=20)
tk.Button(text='Clear', command=clear_data, font=(17)).grid(row=10, column=1, pady=20)
tk.Button(text='Update', command=update_data, font=(17)).grid(row=11, column=0, pady=20)
tk.Button(text='Read', command=read_data, font=(17)).grid(row=11, column=1, pady=20)
tk.Button(text='Delete', command=delete_data, font=(17)).grid(row=12, column=0, pady=20)

window.mainloop()