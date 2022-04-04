from tkinter import *
from tkinter.ttk import Notebook
from main import Tabs
from tkinter import ttk



root=Tk()
root.geometry('1300x750')
root.title('LEARN2DRIVE')

main_frame = Frame(root,padx=5,pady=5)

title_frame=Frame(main_frame,padx=5,pady=5)
Label(title_frame,text='DRIVING SCHOOL MANAGEMENT SYSTEM',font=('ms sans serif',20)).pack()
title_frame.grid(row=0,column=0,padx=10,pady=15)


tabControl=Notebook(main_frame,width=1230)

ob1 = Tabs(tabControl,'CUSTOMER DETAILS','customer',['Customer ID','Name','Age','Gender','Phone','Aadhar number','Address'],
           ['cust_id','name','age','gender','phone','aadhar_number','address'],
           ['Customer ID','Customer Name','Customer Phone','Course ID'],
           ['cust_id','name','phone','course_id'])
tb1=ob1.funcc()

ob2 = Tabs(tabControl,'EMPLOYEE DETAILS','employee',['Employee ID','Name','Age','Gender','Designation','Salary','Date of Join','Aadhar number','Phone'],
           ['emp_id','name','age','gender','designation','salary','date_of_join','aadhar_number','phone'],
           ['Employee ID','Employee Name'],
           ['emp_id','name'])
tb2=ob2.funcc()

ob3 = Tabs(tabControl,'CLASS DETAILS','class',['Class ID','Date','Towards Course ID','RC number of vehicle'],
           ['class_id','date','course_id','reg_no_of_vehicle'],
           ['Class ID','Date','Course ID'],
           ['class_id','date','towards_course'])
tb3=ob3.funcc()

ob4 = Tabs(tabControl,'COURSE DETAILS','course',['Course ID','Classes Enrolled','Classes Done','Classes remaining','Start Date','Time of the Day','Total Amount for Enrolled Classes','Amount Received','Amount Remaining','Type of Vehicle','Trainer ID','Towards Customer ID'],
           ['course_id','total_classes_enrolled','total_class_done','total_class_remaining','start_date_of_the_course','time_of_the_course','total_amt','amt_received','amount_remaining','vehicle_type','trainer_id','cust_id'],
           ['Course ID','Customer ID','Customer Name','Trainer ID'],
           ['course_id','cust_id','name','trainer_id'])
tb4=ob4.funcc()

ob5 = Tabs(tabControl,'VEHICLE DETAILS','vehicle',['RC Number','Name','Insurance Expiry Date','Emission Expiry Date','Last Service Date','Type of Vehicle'],
           ['registration_no','name_of_vehicle','insurance_expiry_date','emission_expiry_date','last_service_date','type'],
           ['RC number','Type'],
           ['registration_no','type'])
tb5=ob5.funcc()

ob6 = Tabs(tabControl,'PAYMENT DETAILS','payment',['Payment ID','Amount','Date','Mode','Towards Course','Collected By'],
           ['payment_id','amount','date','mode','towards_course_id','collected_by_emp_id'],
           ['Payment ID','Date','Course ID'],
           ['payment_id','date','towards_course_id'])
tb6=ob6.funcc()


tabControl.add(tb1,text='CUSTOMER DETAILS')
tabControl.add(tb2,text='EMPLOYEE DETAILS')
tabControl.add(tb5,text='VEHICLE DETAILS')
tabControl.add(tb4,text='COURSE DETAILS')
tabControl.add(tb3,text='CLASS DETAILS')
tabControl.add(tb6,text='PAYMENT DETAILS')
tabControl.grid(row=1,column=0)
main_frame.pack()
root.mainloop()