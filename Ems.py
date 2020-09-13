from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from cx_Oracle import *
import socket

root = Tk()
root.title("Employee Management System")
root.geometry("760x500+150+150")
root.configure(background="chartreuse2")

def f1():
	root.withdraw()
	adst.deiconify()
	entAddId.focus()

def f2():
	entAddId.delete(0 ,END)
	entAddName.delete(0, END)
	entAddSalary.delete(0, END)
	adst.withdraw()
	root.deiconify()

def f3():
	stdata.delete(1.0, END)
	root.withdraw()
	vist.deiconify()
	con = None
	try:
		con = connect('system/abc123')
		cursor = con.cursor()
		sql = "select id, name, salary from employee_info"
		cursor.execute(sql)
		data = cursor.fetchall()
		if len(data):
			msg = " "
			for d in data:
				msg = msg + "Id : " + str(d[0]) + "\t\t" + "   Name : "+ str(d[1])  + "\t\t\t" + " Salary : "+ str(d[2])  +"\n"
			stdata.insert(INSERT, msg)
		else:
			stdata.insert(INSERT,"No records found")
	except DatabaseError as e:
		messagebox.showerror("issue",str(e))
	finally:
		if con is not None:
			con.close()

def f4():
	vist.withdraw()
	root.deiconify()

def f5():
	root.withdraw()
	upst.deiconify()
	entUpdId.focus()

def f6():
	entUpdId.delete(0 ,END)
	entUpdName.delete(0, END)
	entUpdSalary.delete(0, END)
	upst.withdraw()
	root.deiconify()

def f7():
	root.withdraw()
	dlst.deiconify()
	entDltId.focus()

def f8():
	entDltId.delete(0 ,END)
	dlst.withdraw()
	root.deiconify()

def f9():
	con = None
	try:
		con = connect('system/abc123')
		if len(entAddId.get())==0:
			messagebox.showwarning("Issue","Please enter id")
			return
		if len(entAddName.get())==0:
			messagebox.showwarning("Issue","Please enter Name")
			return
		if len(entAddSalary.get())==0:
			messagebox.showwarning("Issue","Please Enter Salary")
			return
		if entAddId.get().lstrip('-').isdigit()==True:
			id = int(entAddId.get())
		else:

			messagebox.showerror("Error","Id cannot contain alphabets")
			entAddId.delete(0,END)
			entAddId.focus()
			return
			id = int(entAddId.get())
			
		if int(id) <= 0:

			messagebox.showerror("Error","Id should be positive")
			entAddId.delete(0,END)
			entAddId.focus()
			return
		cursor = con.cursor()
		sql = "select id from employee_info where id='%d'"	
		cursor.execute(sql % id)
		data = cursor.fetchall()
		if len(data):				

			messagebox.showerror("Error","Record Already Exists")
			entAddId.delete(0,END)
			entAddId.focus()
			return
		if entAddName.get().isalpha()==True:
			name = entAddName.get()
		else:

			messagebox.showerror("Error","Invalid Name")
			entAddName.delete(0,END)
			entAddName.focus()
			return
		if len(name)<2:

			messagebox.showerror("Error","Invalid name")
			entAddName.delete(0,END)
			entAddName.focus()
			return
		if entAddSalary.get().lstrip('-').isdigit()==True:
			salary = int(entAddSalary.get())
		else:

			messagebox.showerror("Error","Salary should be in integer")
			entAddSalary.delete(0,END)
			entAddSalary.focus()
			return
		if salary < 10000:

			messagebox.showerror("Error","Salary can't be less than 10,000")
			entAddSalary.delete(0,END)
			entAddSalary.focus()
			return
			
		sql = "insert into employee_info values('%d','%s','%d')"
		args = (id,name,salary)
		cursor.execute(sql % args)
		con.commit()
		messagebox.showinfo("Success","record inserted")
		entAddId.delete(0,END)
		entAddName.delete(0,END)
		entAddSalary.delete(0,END)
		entAddId.focus()
	except DatabaseError as e:
		con.rollback()
		messagebox.showerror("issue",str(e))
	finally:
		if con is not None:
			con.close()

def f10():
	con = None
	try:
		con = connect('system/abc123')
		if len(entUpdId.get())==0:
			messagebox.showwarning("Issue","Please enter Id")
			return
		if len(entUpdName.get())==0:
			messagebox.showwarning("Issue","Please Enter Name")
			return
		if len(entUpdSalary.get())==0:
			messagebox.showwarning("Issue","Please Enter Salary ")
			return
		if entUpdId.get().lstrip('-').isdigit() == True:
			id = int(entUpdId.get())
		else:

			messagebox.showerror("Error","Invalid id")
			entUpdId.delete(0 ,END)
			entUpdId.focus()
			return
			id = int(entUpdId.get())
		if int(id) <= 0:

			messagebox.showerror("Error","Id cannot be Negative")
			entUpdId.delete(0 ,END)
			entUpdId.focus()
			return
		cursor = con.cursor()
		sql = "select id from employee_info where id='%d'"	
		cursor.execute(sql % id)
		data = cursor.fetchall()
		if len(data):
			pass
		else:

			messagebox.showerror("Error","Record does not exists")
			entUpdId.delete(0,END)
			entUpdId.focus()
			return		
		if entUpdName.get().isalpha()==True:
			name =entUpdName.get()
		else:

			messagebox.showerror("Error","Invalid Name")
			entUpdName.delete(0,END)
			entUpdName.focus()
			return
		if len(name) < 2:

			messagebox.showerror("Error","Name must be of atleast 2 characters")
			entUpdName.delete(0,END)
			entUpdName.focus()
			return
		if entUpdSalary.get().lstrip('-').isdigit()==True:
			salary=int(entUpdSalary.get())
		else:

			messagebox.showerror("Error","Salary cannot contain alphabets")
			entUpdSalary.delete(0,END)
			entUpdSalary.focus()
			return
		if Salary < 10000:

			messagebox.showerror("Error","Salary can't be less than 10,000")
			entUpdSalary.delete(0,END)
			entUpdSalary.focus()
			return
		sql = "update employee_info set id = '%d',name = '%s',salary = '%d' where id = '%d'"
		args = (id,name,salary,id)
		cursor.execute(sql % args)
		con.commit()
		messagebox.showinfo("Success","record Updated")
		entUpdId.delete(0 ,END)
		entUpdName.delete(0, END)
		entUpdSalary.delete(0, END)
		entUpdId.focus()
	except DatabaseError as e:
		con.rollback()
		messagebox.showerror("issue",str(e))
	finally:
		if con is not None:
			con.close()

def f11():
	con = None
	try:
		con = connect('system/abc123')
		if entDltId.get().lstrip('-').isdigit() == True:
			id = int(entDltId.get())
		else:
			messagebox.showerror("Error","id cannot contain alphabets")
			return
		if len(entDltId.get())==0:
			messagebox.showwarning("Issue","Please enter id")
			return
		if int(id) <= 0:
			messagebox.showerror("Error","id cannot be Negative")
			return
		cursor = con.cursor()
		sql = "select id from employee_info where id='%d'"	
		cursor.execute(sql % id)
		data = cursor.fetchall()
		if len(data):
			sql = "delete from employee_info where id = '%d'"
			cursor.execute(sql % id)
			con.commit()	
			messagebox.showinfo("Success","record Deleted")
		else:
			messagebox.showwarning("Warning","Record does not exists")
			return
	except DatabaseError as e:
		con.rollback()
		messagebox.showerror("issue",str(e))
	finally:
		entDltId.delete(0 ,END)
		entDltId.focus()
		if con is not None:
			con.close()

 
def f12():
	import requests
	import socket
	try:
		socket.create_connection(("www.google.com",80))
		res = requests.get("https://ipinfo.io")
		data = res.json()
		city = data['city']
		return str(city)
	except OSError:
		return ("Not-Available")
 
def f13():
	import requests
	import socket
	try:
		socket.create_connection(("www.google.com",80))
		res = requests.get("https://ipinfo.io")
		data = res.json()    
		city = data['city']
		a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
		a2 = "&q=" + city
		a3 = "&appid=c6e315d09197cec231495138183954bd"
		api_address = a1 + a2 + a3
		res = requests.get(api_address)
		data = res.json()
		temp = data['main']['temp']
		return(temp)
	except OSError :
		return("Not-Available")
	except KeyError:
		return("Not-Available")

def f14():
	import bs4
	import requests
	res  = requests.get("https://www.brainyquote.com/quotes_of_the_day.html")
	soup = bs4.BeautifulSoup(res.text , 'lxml')
	quote = soup.find('img', {"class":"p-qotd"})
	msg = quote['alt']
	return(msg)

def f15():
	con = None
	try:
		con = connect('system/abc123')
		cursor = con.cursor()
		sql = "select name,salary from employee_info"	
		cursor.execute(sql)
		data = cursor.fetchall()
		if len(data):
			import pandas as pd
			import matplotlib.pyplot as plt
			import numpy as np
			names=[]
			salary=[]
			for d in data:
				names.append(d[0])
				salary.append(d[1])
			x = np.arange(len(names))
			bars = plt.bar(x , salary,label='Salary',width=0.2)
			plt.xticks(x,names)
			plt.legend()
			plt.grid()
			for bar in bars:
			    yval = bar.get_height()
			    plt.text(bar.get_x(), yval + .005, yval)
			plt.xlabel("Names")
			plt.ylabel("Salary")
			plt.title("Marks Graph")
			plt.show()
		else:
			messagebox.showwarning("Warning","No record available")
	except DatabaseError as e:
		con.rollback()
		messagebox.showerror("issue",str(e))
	finally:
		if con is not None:
			con.close()

CityRslt=f12()
TempRslt=f13()
QotdRslt=f14()

btnAdd = Button(root, text="Add", font=('comic sans ms', 16, 'bold'), width=10, command=f1)
btnView = Button(root, text="View", font=('comic sans ms', 16, 'bold'), width=10, command=f3)
btnUpdate = Button(root, text="Update", font=('comic sans ms', 16, 'bold'), width=10, command=f5)
btnDelete = Button(root, text="Delete", font=('comic sans ms', 16, 'bold'), width=10, command=f7)
btnGraph = Button(root, text="Graph", font=('comic sans ms', 16, 'bold'), width=10, command=f15)
btnAdd.pack(pady=10)
btnView.pack(pady=10)
btnUpdate.pack(pady=10)
btnDelete.pack(pady=10)
btnGraph.pack(pady=10)

adst = Toplevel(root)
adst.title("Add Employee")
adst.geometry("760x500+150+150")
adst.configure(background="firebrick1")

lblAddId = Label(adst, text="enter id", font=('comic sans ms', 16, 'bold')) 
entAddId = Entry(adst, bd=5, font=('comic sans ms', 16, 'bold'))

lblAddName = Label(adst, text="enter name", font=('comic sans ms', 16, 'bold'))
entAddName = Entry(adst, bd=5, font=('comic sans ms', 16, 'bold'))

lblAddSalary = Label(adst, text="enter salary", font=('comic sans ms', 16, 'bold'))
entAddSalary = Entry(adst, bd=5, font=('comic sans ms', 16, 'bold'))

btnAddSave = Button(adst, text="Save", font=('comic sans ms', 16, 'bold'), command=f9)
btnAddBack = Button(adst, text="Back", font=('comic sans ms', 16, 'bold'), command=f2)

lblAddId.pack(pady=10)
entAddId.pack(pady=10)
lblAddName.pack(pady=10)
entAddName.pack(pady=10)
lblAddSalary.pack(pady=10)
entAddSalary.pack(pady=10)
btnAddSave.pack(pady=10)
btnAddBack.pack(pady=10)

adst.withdraw()

vist = Toplevel(root)
vist.title("View Employee")
vist.geometry("760x500+150+150")
vist.configure(background="DarkGoldenrod1")

stdata = scrolledtext.ScrolledText(vist, width=60, height=20)
btnViewBack = Button(vist, text="Back", font=('comic sans ms', 16, 'bold'),command=f4)

stdata.pack(pady=10)
btnViewBack.pack(pady=10)

vist.withdraw()

upst = Toplevel(root)
upst.title("Update Employee")
upst.geometry("760x500+150+150")
upst.configure(background="MediumOrchid1")

lblUpdId = Label(upst, text="enter id to update", font=('comic sans ms', 16, 'bold')) 
entUpdId = Entry(upst, bd=5, font=('comic sans ms', 16, 'bold'))

lblUpdName = Label(upst, text="enter name", font=('comic sans ms', 16, 'bold'))
entUpdName = Entry(upst, bd=5, font=('comic sans ms', 16, 'bold'))

lblUpdSalary = Label(upst, text="enter salary", font=('comic sans ms', 16, 'bold'))
entUpdSalary = Entry(upst, bd=5, font=('comic sans ms', 16, 'bold'))

btnUpdSave = Button(upst, text="Save", font=('comic sans ms', 16, 'bold'), command=f10)
btnUpdBack = Button(upst, text="Back", font=('comic sans ms', 16, 'bold'), command=f6)

lblUpdId.pack(pady=10)
entUpdId.pack(pady=10)
lblUpdName.pack(pady=10)
entUpdName.pack(pady=10)
lblUpdSalary.pack(pady=10)
entUpdSalary.pack(pady=10)
btnUpdSave.pack(pady=10)
btnUpdBack.pack(pady=10)

upst.withdraw()

dlst = Toplevel(root)
dlst.title("Delete Employee")
dlst.geometry("760x500+150+150")
dlst.configure(background="cyan")

lblDltId = Label(dlst, text="enter id to delete", font=('comic sans ms', 16, 'bold')) 
entDltId = Entry(dlst, bd=5, font=('comic sans ms', 16, 'bold'))

btnDltSave = Button(dlst, text="Save", font=('comic sans ms', 16, 'bold'), command=f11)
btnDltBack = Button(dlst, text="Back", font=('comic sans ms', 16, 'bold'), command=f8)

lblDltId.pack(pady=20)
entDltId.pack(pady=10)
btnDltSave.pack(pady=30)
btnDltBack.pack(pady=10)

dlst.withdraw()

lblCity=Label(root,text='City:',font=('comic sans ms', 16, 'bold'))
lblCityRslt=Label(root,text=CityRslt,font=('comic sans ms', 16, 'bold'))
lblTemp=Label(root,text='Temp:',font=('comic sans ms', 16, 'bold'))
lblTempRslt=Label(root,text=f13(),font=('comic sans ms', 16, 'bold'))
lblQotd=Label(root,text='QOTD:',font=('comic sans ms', 16, 'bold'))
lblQotdRslt=Label(root,text=QotdRslt,font=('comic sans ms', 16, 'bold'))

lblCity.place(x=110,y=380)
lblCityRslt.place(x=190,y=380)
lblTemp.place(x=510,y=380)
lblTempRslt.place(x=600,y=380)
lblQotd.place(x=60,y=440)
lblQotdRslt.place(x=150,y=440)



root.mainloop()