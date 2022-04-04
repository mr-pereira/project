from cgitb import small, text
from msilib.schema import ComboBox
from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
from turtle import bgcolor
import mysql.connector
import re

from mysqlx import Column



conn=mysql.connector.connect(host='localhost',
                             user='root',
                             password='admin',
                             database='dbms_pro')


c=conn.cursor()


class Tabs:
        
    """name='CUSTOMER DETAILS'
    table_name=''
    cols1=['cust_id','name','age','gender','phone','aadhar','address']
    cols2=['Customer_ID','Name','Age','Gender','Phone','Aadhar number','Address']
    table_name='customer"""

    def __init__(self,a,b,c,d,e,f,g) :
        self.tab=a
        self.tab_name=b
        self.table_name=c
        self.cols1=d
        self.cols2=e 
        self.entries=e.copy()
        self.is_delete=True
        self.search_cols1=f
        self.search_cols2=g

    def check_trainers(self):
        pass

    def addRecord(self):
        global c_name,c_age,c_gen,c_ph,c_add,c_adh,root2
        root2=Tk()
        root2.geometry('600x730')
        root2.title('LEARN2DRIVE')

        #--------------------------------------frame to disp details---------------------------------
        data_frame=LabelFrame(root2,text=f'ADD {self.tab_name}',pady=20,padx=20,bg='lightblue')
        
        if self.table_name=='vehicle':
            for i in range(0,len(self.cols1)):
                Label(data_frame,text=f'{self.cols1[i]}',padx=15,pady=20,bg='lightblue').grid(row=i,column=0)
                if self.cols2[i]=='type':
                    type=StringVar()
                    small_frame=Frame(data_frame,bg='lightblue')
                    Radiobutton(small_frame,text='2 Wheeler',value='2 Wheeler',variable=type).grid(row=0,column=0,padx=20)
                    Radiobutton(small_frame,text='4 Wheeler',value='4 Wheeler',variable=type).grid(row=0,column=1,padx=20)
                    small_frame.grid(row=i,column=1)
                    self.entries[i]=Entry(data_frame,text=type)
                else:
                    self.entries[i]=Entry(data_frame,width=40)
                    self.entries[i].grid(row=i,column=1)
        elif self.table_name=='course':
            for i in range(1,len(self.cols1)):
                if self.cols2[i] in ['total_class_done','total_class_remaining','total_amt','amt_received','amt_remaining']:
                        continue
                else:   
                    Label(data_frame,text=f'{self.cols1[i]}',padx=15,pady=20,bg='lightblue').grid(row=i-1,column=0)
                    if self.cols2[i] in ['total_class_done','total_class_remaining','total_amt','amt_received','amt_remaining']:
                        continue
                    else:
                        if self.cols2[i]=='vehicle_type':
                            type=StringVar()
                            small_frame=Frame(data_frame,bg='lightblue')
                            Radiobutton(small_frame,text='2 Wheeler',value='2 Wheeler',variable=type).grid(row=0,column=0,padx=20)
                            Radiobutton(small_frame,text='4 Wheeler',value='4 Wheeler',variable=type).grid(row=0,column=1,padx=20)
                            small_frame.grid(row=i-1,column=1)
                            self.entries[i]=Entry(data_frame,text=type)
                        elif self.cols2[i]=='trainer_id':
                            self.train_cmbx=ttk.Combobox(data_frame)
                            c.execute("select emp_id,e_name from employee where dsgn in ('trainer','Trainer')")
                            self.trains=[]
                            for r in c:
                                self.trains.append(str(r[0])+" "+str(r[1]))
                        
                            self.train_cmbx['values']=self.trains
                            self.train_cmbx.grid(row=i-1,column=1)
                        else:
                            self.entries[i]=Entry(data_frame,width=40)
                            self.entries[i].grid(row=i-1,column=1)
                     
        elif self.table_name=='customer':
            for i in range(1,len(self.cols1)):
                Label(data_frame,text=f'{self.cols1[i]}',padx=15,pady=20,bg='lightblue').grid(row=i-1,column=0)
                if self.cols2[i]=='c_gender':
                    gen=StringVar()
                    small_frame=Frame(data_frame,bg='lightblue')
                    Radiobutton(small_frame,text='Male',value='Male',variable=gen).grid(row=0,column=0,padx=20)
                    Radiobutton(small_frame,text='Female',value='Female',variable=gen).grid(row=0,column=1,padx=20)
                    small_frame.grid(row=i-1,column=1)
                    self.entries[i]=Entry(data_frame,text=gen)
                    
                else:       
                    self.entries[i]=Entry(data_frame,width=40)
                    self.entries[i].grid(row=i-1,column=1)
        elif self.table_name=='employee':
            for i in range(1,len(self.cols1)):
                Label(data_frame,text=f'{self.cols1[i]}',padx=15,pady=20,bg='lightblue').grid(row=i-1,column=0)
                if self.cols2[i]=='e_gender':
                    gen=StringVar()
                    small_frame=Frame(data_frame,bg='lightblue')
                    Radiobutton(small_frame,text='Male',value='Male',variable=gen).grid(row=0,column=0,padx=20)
                    Radiobutton(small_frame,text='Female',value='Female',variable=gen).grid(row=0,column=1,padx=20)
                    small_frame.grid(row=i-1,column=1)
                    self.entries[i]=Entry(data_frame,text=gen)
                    
                else:       
                    self.entries[i]=Entry(data_frame,width=40)
                    self.entries[i].grid(row=i-1,column=1)
        elif self.table_name=='class':
            for i in range(1,len(self.cols1)):
                Label(data_frame,text=f'{self.cols1[i]}',padx=15,pady=20,bg='lightblue').grid(row=i-1,column=0)
                if self.cols2[i]=='reg_no_vehicle':
                    self.reg_cmbx=ttk.Combobox(data_frame)
                    c.execute('select reg_no from vehicle')
                    self.regs=[]
                    for r in c:
                        self.regs.append(r[0])
                        
                    self.reg_cmbx['values']=self.regs
                    self.reg_cmbx.grid(row=i-1,column=1)
                    
                else:
                    self.entries[i]=Entry(data_frame,width=40)
                    self.entries[i].grid(row=i-1,column=1)
        else:
            for i in range(1,len(self.cols1)):
                Label(data_frame,text=f'{self.cols1[i]}',padx=15,pady=20,bg='lightblue').grid(row=i-1,column=0)
                self.entries[i]=Entry(data_frame,width=40)
                self.entries[i].grid(row=i-1,column=1)

        data_frame.grid(row=0,column=0,padx=30,pady=30)

        #----------------------------buttons------------------------------------
        sub_frame=Frame(root2,padx=10,pady=10)
        sub_frame.grid(row=1,column=0)

        ins_btn=Button(sub_frame,text='INSERT',pady=5,padx=5,command=self.finalAddRecord)
        ins_btn.grid(row=0,column=0,padx=10)

        clr=Button(sub_frame,text='CLEAR ALL',padx=5,pady=5,command=self.clear_fields)
        clr.grid(row=0,column=1,padx=10)
 
    
        root2.mainloop()
    
    def finalAddRecord(self):
        global c_name,c_age,c_gen,c_ph,c_add,c_adh,root2
        details=[]
        
        if self.table_name in ['customer','employee']:
            for i in range(1,len(self.entries)):
                if self.cols2[i] in ['c_phone','e_phone']:
                    pattern = re.compile(r"[6-9][0-9]{9}")
                    if(pattern.match(self.entries[i].get())):
                        details.append(self.entries[i].get())
                    else:
                        messagebox.showerror('Error','Enter valid 10 digit phone number')
                        return
                elif self.cols2[i] in ['c_aadhar','e_aadhar']:
                    pattern = re.compile(r"[0-9]{12}")
                    if(pattern.match(self.entries[i].get())):
                        details.append(self.entries[i].get())
                    else:
                        messagebox.showerror('Error','Enter valid 12 digit aadhar number')
                        return
                else:
                        details.append(self.entries[i].get())
                    
        elif self.table_name=='vehicle':
            for i in range(0,len(self.entries)):
                details.append(self.entries[i].get())
        elif self.table_name=='course':
            for i in range(1,len(self.entries)):
                if self.entries[i] in ['total_class_done','total_class_remaining','total_amt','amt_received','amt_remaining']:
                    continue
                print(self.entries[i])
                if self.entries[i]=='trainer_id':
                    details.append(self.trains[self.train_cmbx.current()][0])
                else:
                    details.append(self.entries[i].get())
            details.append(int(details[0])*200)        
            details.append(int(details[0])*200)        
            details.append(details[0])   
            details.append('0') 
        elif self.table_name=='class':
            for i in range(1,len(self.entries)):
                if self.entries[i]=='reg_no_vehicle':
                    details.append(self.regs[self.reg_cmbx.current()])
                else:
                    details.append(self.entries[i].get())
            
        else:
            for i in range(1,len(self.entries)):
                details.append(self.entries[i].get())
            
        #'course_id','total_class_enrolled','total_class_done','total_class_remaining','start_date','time',
        # 'total_amt','amt_received','amt_remaining','vehicle_type','trainer_id','towards_customer'],
        print(details)
        
        try:
            
            
            if self.table_name == 'customer':
                sql_command='insert into customer(c_name,c_age,c_gender,c_phone,c_aadhar,c_address) values (%s,%s,%s,%s,%s,%s)'
                values=tuple(details)
                c.execute(sql_command,values)
            elif self.table_name== 'employee':
                sql_command='insert into employee(e_name,e_age,e_gender,dsgn,salary,join_date,e_aadhar,e_phone) values (%s,%s,%s,%s,%s,%s,%s,%s)'
                values=tuple(details)
                c.execute(sql_command,values)
            elif self.table_name== 'class':
                sql_command='insert into class(date,towards_course,reg_no_vehicle) values (%s,%s,%s)'
                values=tuple(details)
                c.execute(sql_command,values)
            elif self.table_name== 'course':
                sql_command="""insert into course(total_class_enrolled,start_date,time,vehicle_type,trainer_id,towards_customer,total_amt,amt_remaining,
                total_class_remaining,total_class_done) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                values=tuple(details)
                c.execute(sql_command,values)
            elif self.table_name== 'vehicle':
                sql_command='insert into vehicle(reg_no,v_name,insurance_expiry,emission_expiry,last_service_date,type) values (%s,%s,%s,%s,%s,%s)'
                values=tuple(details)
                c.execute(sql_command,values)
            elif self.table_name== 'payment':
                sql_command='insert into payment(amount,payment_date,mode,amt_towards_course,collected_by) values (%s,%s,%s,%s,%s)'
                values=tuple(details)
                c.execute(sql_command,values)
            conn.commit() 
            
            
            self.tv.delete(*self.tv.get_children())
            c.execute(f'select * from {self.table_name}')
            for r in c:
                self.tv.insert('','end',text='',values=(r))
            messagebox.showinfo("Message","Record Added Successfully")
            root2.destroy()
            
        except:
            messagebox.showerror("Error","Enter valid information")
                   
        
    
    def deleteRecord(self):
        global c_name,c_age,c_gen,c_ph,c_add,c_adh,root2
        root2=Tk()
        root2.geometry('650x750')
        root2.title('LEARN2DRIVE')
        self.is_delete=True
        #--------------------frame to enter id --------------------------------
        delete_up_frame=LabelFrame(root2,text=f'ENTER THE {str.upper(self.cols1[0])} OF THE DELETING {str.upper(self.table_name)}',padx=10,pady=15,bg="#ebd48f")
        delete_up_frame.grid(row=0,column=0,pady=15,padx=15)

        global c_id
        self.entries[0]=Entry(delete_up_frame,width=20)
        self.entries[0].grid(row=0,column=0,pady=5,padx=10)

        fetchbtn=Button(delete_up_frame,text='FETCH',command=self.fetchBtn)
        fetchbtn.grid(row=0,column=1,padx=15,pady=5)

        #------------------------------frame to disp details---------------------------------------
        delete_frame=LabelFrame(root2,text=f'REVIEW {self.tab_name}',pady=20,padx=20,bg='lightblue')
        
        for i in range(1,len(self.cols1)):
            Label(delete_frame,text=f'{self.cols1[i]}',padx=14,pady=14,bg='lightblue').grid(row=i-1,column=0)
            self.entries[i]=Entry(delete_frame,width=40)
            self.entries[i].grid(row=i-1,column=1)

        delete_frame.grid(row=1,column=0,padx=30,pady=30)

        #--------------------------buttons----------------------------------------
        sub_frame=Frame(root2,padx=10,pady=10)
        sub_frame.grid(row=2,column=0,padx=15)

        ins_btn=Button(sub_frame,text='DELETE',pady=5,padx=5,command=self.finalDeleteRecord)
        ins_btn.grid(row=0,column=0,padx=10)

        root2.mainloop()
  
    def finalDeleteRecord(self):
        global root2
        id=int(self.entries[0].get())
        
        c.execute(f"delete from {self.table_name} where {self.cols2[0]}={id}")
        conn.commit()
        
        self.tv.delete(*self.tv.get_children())
        c.execute(f'select * from {self.table_name}')
        global count
        count=0
        tags=['evenrow','oddrow']
        for r in c:
            self.tv.insert('','end',text='',values=(r),tags=(f'{tags[count%2]}',))
            count=count+1                                                                                                               
        messagebox.showinfo("Message","Record Deleted Successfully")

        root2.destroy()    


    def fetchBtn(self):
        global c_name,c_age,c_gen,c_ph,c_add,c_adh,root2
        fetchedData=[]
        id=self.entries[0].get()
        print(f"select * from {self.table_name} where {self.cols2[0]}={id}")
        c.execute(f"select * from {self.table_name} where {self.cols2[0]}='{id}'")
        

        for i in c:
            for j in i:
                fetchedData.append(j)
                
                
        self.clear_fields()

        
        for i in range(1,len(self.entries)):
            self.entries[i].insert(0,fetchedData[i])
            
        if self.is_delete == True:
            for i in range(1,len(self.entries)):
                self.entries[i].configure(state='disabled')  


    def clear_fields(self):
        for i in range(1,len(self.entries)):
            self.entries[i].delete(0,END)


    def updateRecord(self):
        global root2
        root2=Tk()
        root2.geometry('650x750')
        root2.title('LEARN2DRIVE')
        
        self.is_delete=False

        #--------------------frame to enter id --------------------------------
        delete_up_frame=LabelFrame(root2,text=f'ENTER THE {str.upper(self.cols1[0])} OF THE UPDATING {str.upper(self.table_name)}',padx=10,pady=15,bg="#ebd48f")
        delete_up_frame.grid(row=0,column=0,pady=15,padx=15)

        global c_id
        self.entries[0]=Entry(delete_up_frame,width=20)
        self.entries[0].grid(row=0,column=0,pady=5,padx=10)

        fetchbtn=Button(delete_up_frame,text='FETCH',command=self.fetchBtn)
        fetchbtn.grid(row=0,column=1,padx=15,pady=5)

        #------------------------------frame to disp details---------------------------------------
        delete_frame=LabelFrame(root2,text=f'UPDATE {self.tab_name}',pady=20,padx=20,bg='lightblue')
        
        for i in range(1,len(self.cols1)):
            Label(delete_frame,text=f'{self.cols1[i]}',padx=14,pady=14,bg='lightblue').grid(row=i-1,column=0)
            self.entries[i]=Entry(delete_frame,width=40)
            self.entries[i].grid(row=i-1,column=1)
            
        delete_frame.grid(row=1,column=0,padx=30,pady=30)

        #--------------------------buttons----------------------------------------
        sub_frame=Frame(root2,padx=10,pady=10)
        sub_frame.grid(row=2,column=0,padx=15)

        ins_btn=Button(sub_frame,text='UPDATE',pady=5,padx=5,command=self.finalUpdateRecord)
        ins_btn.grid(row=0,column=0,padx=10)
        
        clr=Button(sub_frame,text='CLEAR ALL',padx=5,pady=5,command=self.clear_fields)
        clr.grid(row=0,column=1,padx=10)

        root2.mainloop()

    def finalUpdateRecord(self):
        global root2
        id=self.entries[0].get()
        details=[]
        for i in range(1,len(self.entries)):
            details.append(self.entries[i].get())
        
        try:   
            for i in range(1,len(self.cols2)):
                
                c.execute(f"update {self.table_name} set {self.cols2[i]}='{details[i-1]}' where {self.cols2[0]}={id}")
       
        except:
            messagebox.showerror('Error','Enter valid information')  
        conn.commit()
        self.tv.delete(*self.tv.get_children())
        c.execute(f'select * from {self.table_name}')
        global count
        count=0
        tags=['evenrow','oddrow']
        for r in c:
            self.tv.insert('','end',text='',values=(r),tags=(f'{tags[count%2]}',))
            count=count+1 
        messagebox.showinfo("Message","Record Updated Successfully")

        root2.destroy()
        
    
    def search(self):
        keys=[]
        search_attr=self.search_cols2[self.cmbobox.current()]
        if (search_attr in self.cols2):
            c.execute(f"select {self.cols2[0]} from {self.table_name} where {search_attr}='{self.search_entry.get()}'")
        elif (self.table_name=='customer' and search_attr=='course_id'):
            c.execute(f"select {self.cols2[0]} from customer,course where cust_id=towards_customer and course_id='{self.search_entry.get()}'")
        elif (self.table_name=='course' and search_attr=='cust_id'):
             c.execute(f"select {self.cols2[0]} from customer,course where cust_id=towards_customer and cust_id='{self.search_entry.get()}'")
        elif (self.table_name=='course' and search_attr=='c_name'):
             c.execute(f"select {self.cols2[0]} from customer,course where cust_id=towards_customer and c_name='{self.search_entry.get()}'")
        elif (self.table_name=='course' and search_attr=='trainer_id'):
             c.execute(f"select {self.cols2[0]} from course,employee where emp_id=trainer_id and trainer_id='{self.search_entry.get()}'")
        elif (self.table_name=='payment' and search_attr=='course_id'):
             c.execute(f"select {self.cols2[0]} from course,payment where course_id=amt_towards_course and course_id='{self.search_entry.get()}'")
        
            
                
        for r in c:
            keys.append(r[0])
        
        if(len(keys)==0):
            messagebox.showinfo("Message","No Records Found")
            self.search_entry.delete(0,END)
            return
        
        search_list="("    
        if len(keys)>1:
            for i in range(0,len(keys)-1):
                search_list=search_list+"'"+str(keys[i])+"',"
        search_list=search_list+"'"+str(keys[-1])+"'"
        search_list=search_list+")"
        
        print(search_list)
            
        
        c.execute(f'select * from {self.table_name} where {self.cols2[0]} in {search_list}')
        self.tv.delete(*self.tv.get_children())
        global count
        count=0
        tags=['evenrow','oddrow']
        for r in c:
            self.tv.insert('','end',text='',values=(r),tags=(f'{tags[count%2]}',))
            count=count+1

    def reset(self):
        
        global count
        count=0
        tags=['evenrow','oddrow']
        
        self.search_entry.delete(0,END)
        self.tv.delete(*self.tv.get_children())
        if self.table_name=='customer':
            c.callproc('new_procedure')                                                 #stored procedure
            for i in c.stored_results():
                for r in i.fetchall():
                    self.tv.insert('','end',text='',values=(r),tags=(f'{tags[count%2]}',))
                    count=count+1
            #c.execute(f'call dbms_pro.new_procedure();')
        else:
            c.execute(f'select * from {self.table_name}')
       
        for r in c:
            self.tv.insert('','end',text='',values=(r),tags=(f'{tags[count%2]}',))
            count=count+1

    def funcc(self):
        data_frame=Frame(self.tab,height=590,width=900,padx=5,bg='lightblue')
        table_frame=Frame(data_frame,highlightbackground="black", highlightthickness=2,padx=5,pady=5,height=580,width=620)
        table=Frame(table_frame,bd=4,relief=RIDGE)


        #-----------------------------data_frame-------------------------------
        #--------------------data frame--------------------------
        scrollx=Scrollbar(table,orient='horizontal')
        scrolly=Scrollbar(table,orient='vertical')
        self.tv=ttk.Treeview(table,selectmode='extended')
        scrollx.configure(command=self.tv.xview)
        scrolly.configure(command=self.tv.yview)
        self.tv.configure(xscrollcommand=scrollx.set)
        self.tv.configure(yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        self.tv['columns']=tuple(self.cols1)
        self.tv.column('#0', width=0, stretch=NO)
        self.tv.heading('#0', text='', anchor=CENTER)
        #tv['columns']=('cust_id','name','age','gender','phone','aadhar','address')

        for (i,j) in zip(self.cols1,self.cols2):
            self.tv.column(i,anchor=CENTER,width=80)
            self.tv.heading(i,text=i,anchor=CENTER)
        #-------fetching data from customer table--------------

        c.execute(f"select * from {self.table_name}")
        global count
        count=0
        tags=['evenrow','oddrow']
        for r in c:
            self.tv.insert('','end',text='',values=(r),tags=(f'{tags[count%2]}',))
            count=count+1

        self.tv.tag_configure('oddrow',background="white")
        self.tv.tag_configure('evenrow',background="#ffd8c5")
        
        self.tv.pack(fill="both",expand=1)

        table.pack(fill="both",expand=1)
        table_frame.place(x=20,y=20,height=500,width=930)

        #table_frame.pack()
        #-----------------side frame--------------------
        side_frame=Frame(data_frame,pady=5,padx=5,bg='lightblue')
        search_frame=LabelFrame(side_frame,text='SEARCH',padx=10,pady=10,height=500,bg="#ebd48f")
        Label(search_frame,text='Search by').grid(row=0,column=0)
        
        self.cmbobox = ttk.Combobox(search_frame,width=20,state='readonly')
        self.cmbobox['values']=self.search_cols1
        self.cmbobox.grid(row=1,column=0,padx=30,pady=10)
        self.search_entry=Entry(search_frame)
        self.search_entry.grid(row=2,column=0,padx=30,pady=10)
        search_frame.grid(row=0,column=0)
        search_opt_frame=Frame(search_frame,padx=5,pady=5,bg="#ebd48f")
        search_opt_frame.grid(row=3,column=0,padx=10,pady=10)
        search_btn=Button(search_opt_frame,text='Search',command=self.search).grid(row=0,column=0,padx=10,pady=10)
        reset_btn=Button(search_opt_frame,text='Reset',command=self.reset).grid(row=0,column=1,padx=10,pady=10)
        #----------dummy frame--------------------
        #dummy=Frame(side_frame,bg='lightblue')
        #Label(dummy,text='').pack()
        #Label(dummy,text='').pack()
        #Label(dummy,text='').pack()
        #dummy.pack()
        #-------------options frame--------------------
        options_frame=LabelFrame(side_frame,text='OPTIONS',pady=30,padx=80,height=500,bg="#ebd48f")
        addbtn=Button(options_frame,text='ADD',command=self.addRecord)
        addbtn.grid(row=0,column=0,pady=10)
        delbtn=Button(options_frame,text='DELETE',command=self.deleteRecord)
        delbtn.grid(row=1,column=0,pady=10)
        updbtn=Button(options_frame,text='UPDATE',command=self.updateRecord)
        updbtn.grid(row=2,column=0,pady=10)
        options_frame.grid(row=1,column=0,pady=50)

        side_frame.place(x=980,y=20)

        data_frame.pack()
        
        return data_frame