#------------------------------------------- Hopsital Management System------------------------------------------------

#Module used
import shutil
from tkinter import *
import os.path
from tkinter import *
import datetime
import tkinter.messagebox as tmsg
import random
import string
#-------------------------------------------------Simmilar functions----------------------------------------------------
#exit function:
def exit_event(root):
    tmsg.showinfo("Info", "Closing...")
    root.destroy()

#logout function:
def logout(root):
    root.destroy()
    main_menu()

z = "\n"

z1 = datetime.datetime.now()
x1 = datetime.datetime.strftime(z1,'%d-%m-%Y')    #use this to print date


#---------------------------------------------------Logged as admin-----------------------------------------------------

def logged_as_admin(name, root):
    root.destroy()
    admin_root = Tk()
    admin_root.geometry("1366x768")
    admin_root.minsize(1365, 767)
    admin_root.maxsize(1368, 769)
    admin_root.configure(bg="#cececf")

    heading_frame = Frame(admin_root, bg="#1f7dad")
    heading_label = Label(heading_frame, text="Welcome " + name, bg="#1f7dad", fg="#ffffff",font=("Comic Sans Ms", 15, "bold"), pady=2).pack(pady=10)

    heading_frame.pack(side=TOP, anchor="n", fill=BOTH)

#--------------------------------------------------Output screens:------------------------------------------------------

    manage_admin_frame = Frame(admin_root, bg="#1c478b")
    def manage_form():
        manage_frm.pack(pady=90)
        View.forget()
        change_pass_frm.forget()
        manage_btn.configure(state=DISABLED)
        view_btn.configure(state=NORMAL)
        changepass_btn.configure(state=NORMAL)

    def view_f():
        View.pack()
        change_pass_frm.forget()
        manage_frm.forget()
        manage_btn.configure(state=NORMAL)
        view_btn.configure(state=DISABLED)
        changepass_btn.configure(state=NORMAL)

    def change_pass_admin():
        change_pass_frm.pack()
        View.forget()
        manage_frm.forget()

    def which_frame(val):
        if val == 1:
            manage_form()
        elif val == 2:
            view_f()
        elif val == 3:
            change_pass_admin()

    def add_admin_account():
        a1 = uservalue_admin.get()
        p1 = passvalue_admin.get()
        if os.path.exists("Logins/Admin/" + a1 + ".txt"):
            print("login already exists")
        else:
            f = open("Logins/Admin/" + a1 + ".txt", "x")
            f.write(p1)
            f.close()
            print("Admin logged", a1, p1)
            user_entry.delete(0, END)
            pass_entry.delete(0, END)

    def delete_admin_account():
        a2 = uservalue_admin.get()
        p2 = passvalue_admin.get()
        if os.path.exists("Logins/Admin/" + a2 + ".txt"):
            f = open("Logins/Admin/" + a2 + ".txt", "r")
            p2_check = f.readline()
            f.close()
            if p2 == p2_check:
                os.remove("Logins/Admin/" + a2 + ".txt")
                print("file has been deleted")
            else:
                print("Password does not match")
        else:
            print("file did not exists")
        user_entry.delete(0, END)
        pass_entry.delete(0, END)

    def check_admin_username():
        aa11 = change_uservalue_admin.get()
        if os.path.exists("Logins/Admin/" + aa11 + ".txt"):
            pass_entry.configure(state=NORMAL)
            chnge_pass_btn.configure(state=NORMAL)
        else:
            tmsg.showerror("Error", "Username didn't match")

    def new_pass_Set_admin():
        aa111 = change_uservalue_admin.get()
        n_p_a = new_pass_Admin.get()
        f = open("Logins/Admin/" + aa111 + ".txt", "w")
        f.write(n_p_a)
        f.close()
        tmsg.showinfo("Message", "Password has been set")



    uservalue_admin = StringVar()
    passvalue_admin = StringVar()

    manage_frm = Frame(manage_admin_frame, bg="#1c478b")

    user_entry_lbl = Label(manage_frm, text="Username: ", bg="#1c478b", fg="#ffffff",font=("Halvetica", 20, "bold")).pack()
    user_entry = Entry(manage_frm, textvariable=uservalue_admin, fg="#1c478b", relief=RIDGE, font=("Halvetica", 20, "bold"))
    user_entry.pack()

    pass_entry_lbl = Label(manage_frm, text="Password: ", bg="#1c478b", fg="#ffffff",font=("Halvetica", 20, "bold")).pack()
    pass_entry = Entry(manage_frm, textvariable=passvalue_admin, show="*", relief=RIDGE, fg="#1c478b",font=("Halvetica", 20, "bold"))
    pass_entry.pack()

    add_btn = Button(manage_frm, text="Add",  bg="#1f7dad",command=add_admin_account , width=10,fg="#ffffff", font=("Halvetica", 20, "bold"))
    add_btn.pack(pady=20)
    delete_btn = Button(manage_frm, text="Delete", bg="#1f7dad",command=delete_admin_account , width=10,fg="#ffffff", font=("Halvetica", 20, "bold"))
    delete_btn.pack(pady=20)



    change_pass_frm = Frame(manage_admin_frame, bg="#1c478b")

    change_uservalue_admin = StringVar()
    new_pass_Admin = StringVar()

    empty_lbl = Label(change_pass_frm, text="  ", bg="#1c478b").pack(pady=50)
    user_entry_lbl = Label(change_pass_frm, text="Username: ", bg="#1c478b", fg="#ffffff", font=("Halvetica", 20, "bold")).pack( pady=5)
    user_entry = Entry(change_pass_frm, textvariable=change_uservalue_admin, fg="#1c478b", relief=RIDGE, font=("Halvetica", 20, "bold"))
    user_entry.pack()

    pass_entry_lbl = Label(change_pass_frm, text="Password: ", bg="#1c478b", fg="#ffffff", font=("Halvetica", 20, "bold")).pack(pady=5)
    pass_entry = Entry(change_pass_frm, state=DISABLED ,textvariable=new_pass_Admin, show="*", relief=RIDGE, fg="#1c478b", font=("Halvetica", 20, "bold"))
    pass_entry.pack()

    chck_userna = Button(change_pass_frm, text="Check username", bg="#1f7dad", command=check_admin_username, width=15, fg="#ffffff", font=("Halvetica", 15, "bold"))
    chck_userna.pack(pady=20)
    chnge_pass_btn = Button(change_pass_frm, text="Set password", state=DISABLED , bg="#1f7dad", command=new_pass_Set_admin, width=15, fg="#ffffff", font=("Halvetica", 15, "bold"))
    chnge_pass_btn.pack(pady=20)




    View = Frame(manage_admin_frame, bg="#1c478b")
    empty_lbl = Label(View, text="  ", bg="#1c478b").pack(pady=25)
    admin_list_lbl = Label(View, text="Admins", bg="#1f7dad", fg="#ffffff", font=("Comic Sans Ms", 20, "bold"), pady=5)
    admin_list_lbl.pack(pady=5)

    list_frame = Frame(View, bg="#1c478b")
    #List scroll bar
    list_scrollbar = Scrollbar(list_frame)
    list_scrollbar.pack(side=RIGHT, fill=Y)
    #padmin list
    admin_listbox = Listbox(list_frame, yscrollcommand= list_scrollbar.set, fg="#ffffff", bg="#4db3b3" ,width=150, height=30, font=("Comic Sans Ms", 15, "bold"))
    admins_list = os.listdir("Logins/Admin/")
    numb = len(admins_list)
    total_admins = "Total Admins: " + str(numb)
    admin_listbox.insert(END, total_admins)
    for i in range(numb):
        adm = admins_list[i]
        admin_listbox.insert(END, adm)

    admin_listbox.pack()

    list_scrollbar.configure(command=admin_listbox.yview)

    list_frame.pack(pady=8, padx=10)

    head_lbl = Label(manage_admin_frame, text="Manage Admins", bg="#1f7dad", fg="#ffffff", font=("Comic Sans Ms", 30, "bold"), pady=2)
    head_lbl.pack(pady=20, padx=370)
    manage_btn = Button(manage_admin_frame, text="Manage",command=lambda :which_frame(1) , fg="#ffffff", width= 16, bg="#f62c47", font=("Halvetica", 15, "bold"))
    manage_btn.place(x=100, y=100)

    changepass_btn = Button(manage_admin_frame, text="Change Password", fg="#ffffff", command=lambda: which_frame(3), width=16, bg="#f62c47", font=("Halvetica", 15, "bold"))
    changepass_btn.place(x=400, y=100)

    view_btn = Button(manage_admin_frame, text="View", fg="#ffffff",command=lambda :which_frame(2) , width= 16, bg="#f62c47", font=("Halvetica", 15, "bold"))
    view_btn.place(x=700, y=100)








#-------------------------------------------------------view doc part---------------------------------------------------

    view_doc_frame = Frame(admin_root, bg="#1c478b")

    head_doc_lbl = Label(view_doc_frame, text="View Doctors", bg="#1f7dad", fg="#ffffff", font=("Comic Sans Ms", 34, "bold"), pady=2)
    head_doc_lbl.pack(pady=20, padx=370)

    doc_list_frame = Frame(view_doc_frame, bg="#1c478b")
    # List scroll bar
    doc_list_scrollbar = Scrollbar(doc_list_frame)
    doc_list_scrollbar.pack(side=RIGHT, fill=Y)
    # Doc list
    doc_listbox = Listbox(doc_list_frame, yscrollcommand=doc_list_scrollbar.set, fg="#ffffff", bg="grey", width=150, height=40, font=("Comic Sans Ms", 15, "bold"))
    doc_list = os.listdir("Logins/Doctor/")
    numb1 = len(doc_list)
    total_doc = "Total Doctors: " + str(numb1)
    lbl1 = Label(view_doc_frame,text="Name", font=("Comic Sans Ms", 10, "bold"), fg="#ffffff", bg="#1c478b").place(x=50, y=160)
    lbl2 = Label(view_doc_frame, text="Password", font=("Comic Sans Ms", 10, "bold"), fg="#ffffff", bg="#1c478b").place(x=225, y=160)
    lbl3 = Label(view_doc_frame, text="Date of joining", font=("Comic Sans Ms", 10, "bold"), fg="#ffffff", bg="#1c478b").place(x=330, y=160)
    lbl4 = Label(view_doc_frame, text="Gender", font=("Comic Sans Ms", 10, "bold"), fg="#ffffff", bg="#1c478b").place(x=465, y=160)
    lbl6 = Label(view_doc_frame, text="Phone no.", font=("Comic Sans Ms", 10, "bold"), fg="#ffffff", bg="#1c478b").place(x=570, y=160)
    lbl6a = Label(view_doc_frame, text="Timing", font=("Comic Sans Ms", 10, "bold"), fg="#ffffff", bg="#1c478b").place(x=700, y=160)
    lbl7 = Label(view_doc_frame, text="Week off", font=("Comic Sans Ms", 10, "bold"), fg="#ffffff", bg="#1c478b").place(x=800   , y=160)
    lbl8 = Label(view_doc_frame, text="Salary", font=("Comic Sans Ms", 10, "bold"), fg="#ffffff", bg="#1c478b").place(x=906, y=160)
    total_lalb = Label(view_doc_frame,text=total_doc, font=("Comic Sans Ms", 15, "bold"), fg="#ffffff", bg="#1c478b").pack()
    empty_lbl = Label(view_doc_frame, text="  ", bg="#1c478b").pack(pady=15)


    for i1 in range(numb1):

        adm1 = doc_list[i1]
        f = open("Logins/Doctor/" + adm1)
        uname = f.readline()
        psw = f.readline()
        Age = f.readline()
        Gender = f.readline()
        Phone = f.readline()
        time_j = f.readline()
        week_off = f.readline()
        Salary = f.readline()
        f.close()

        sp = "    "

        doc_listbox.insert(END, " Dr. " + uname + sp + psw + sp + Age + sp+ Gender+ sp  + Phone+ sp  + time_j+ sp  + week_off + sp  + Salary)

    doc_listbox.pack(side=LEFT)
    doc_list_scrollbar.configure(command=doc_listbox.yview)

    doc_list_frame.pack(pady=8, padx=10)

    manage_doc_frame = Frame(admin_root, bg="#1c478b")

    def del_doc_acc():
        ud = uservalue_doc.get()
        pd1 = passvalue_doc.get() + "\n"

        if os.path.exists("Logins/Doctor/" + ud + ".txt"):
            f = open("Logins/Doctor/" + ud + ".txt", "r")
            u_n = f.readline()
            p_d_check = f.readline()
            f.close()
            if pd1 == p_d_check:
                os.remove("Logins/Doctor/" + ud + ".txt")
                tmsg.showinfo("Message", "Login Deleted succesfully")
                user_entry1.delete(0, END)
                pass_entry1.delete(0, END)
            else:
                tmsg.showerror("Error", "Invalid Password")
        else:
            tmsg.showerror("Error", "Username not found")

    def add_doc():
        add_doc_frm.pack(fill=BOTH)
        del_doc_frm.forget()
        add_doc_btn.configure(state=DISABLED)
        delete_doc_btn.configure(state=NORMAL)

    def del_doc():
        del_doc_frm.pack()
        add_doc_frm.forget()
        delete_doc_btn.configure(state=DISABLED)
        add_doc_btn.configure(state=NORMAL)

    def check_doc_name():
        dname_check = doc_name.get()
        if os.path.exists("Logins/Doctor/" + dname_check + ".txt"):
            tmsg.showerror("Error", "Username already exist")
        else:
            u_entry.configure(fg="green")

            add_acc_btn.configure(state=NORMAL, bg="green")

    def create_doc_acc():
        dname = doc_name.get()
        dpass = doc_pass.get()
        dage= str(doc_age.get())
        dgend= doc_gend.get()
        dphone= str(doc_phone.get())
        dsalary= str(doc_salary.get())
        dweek= doc_week.get()
        dtime= doc_time.get()

        f = open("Logins/Doctor/" + dname + ".txt", "x")
        f.close()

        f = open("Logins/Doctor/" + dname + ".txt", "a")
        f.write(dname)
        f.write(z)
        f.write(dpass)
        f.write(z)
        f.write(dage)
        f.write(z)
        f.write(dgend)
        f.write(z)
        f.write(dphone)
        f.write(z)
        f.write(dtime)
        f.write(z)
        f.write(dweek)
        f.write(z)
        f.write(dsalary)
        f.close()
        tmsg.showinfo("Message", "Account succesfully Created")
        u_entry.delete(0, END)
        p_entry.delete(0, END)
        age_enty.delete(0, END)
        gender_entry.delete(0, END)
        phone_entry.delete(0, END)
        salary_entry.delete(0, END)
        wek_entry.delete(0, END)
        timing_entry.delete(0, END)

    add_doc_frm = Frame(manage_doc_frame, bg="#1c478b")

    #variables used to get the values:
    doc_name = StringVar()
    doc_pass = StringVar()
    doc_age = StringVar()
    doc_gend = StringVar()
    doc_phone = IntVar()
    doc_salary = IntVar()
    doc_week = StringVar()
    doc_time = StringVar()

    h_lbl = Label(add_doc_frm, text="Add Doctor", bg="#1c478b", fg="#ffffff",font=("Comic Sans Ms", 15, "bold")).pack()

    #Entry and labels for the entry wdget:

    u_lbl = Label(add_doc_frm, text= " Username" , bg="#1c478b", fg="#ffffff", font=("Halvetica", 20, "bold")).place(x=80, y=50)
    u_entry = Entry(add_doc_frm, textvariable=doc_name, fg="#1c478b", relief=RIDGE, font=("Halvetica", 12, "bold"))
    u_entry.place(x=250, y=55)

    p_lbl = Label(add_doc_frm, text="Password" ,bg="#1c478b", fg="#ffffff", font=("Halvetica", 20, "bold")).place(x= 490, y=50)
    p_entry = Entry(add_doc_frm, textvariable=doc_pass, fg="#1c478b", relief=RIDGE, font=("Halvetica", 12, "bold"))
    p_entry.place(x=650, y=55)

    age_lbl = Label(add_doc_frm, text="Date of join" , bg="#1c478b", fg="#ffffff", font=("Halvetica", 20, "bold")).place(x= 80, y=100)
    age_enty = Entry(add_doc_frm, textvariable=doc_age, fg="#1c478b", relief=RIDGE, font=("Halvetica", 12, "bold"))
    age_enty.place(x=250, y=105)

    gender_lbl = Label(add_doc_frm, text="Gender" , bg="#1c478b", fg="#ffffff", font=("Halvetica", 20, "bold")).place(x= 490, y=100)
    gender_entry = Entry(add_doc_frm, textvariable=doc_gend, fg="#1c478b", relief=RIDGE, font=("Halvetica", 12, "bold"))
    gender_entry.place(x=650, y=105)

    phone_lbl = Label(add_doc_frm, text="Phone no." , bg="#1c478b", fg="#ffffff", font=("Halvetica", 20, "bold")).place(x= 80, y=150)
    phone_entry = Entry(add_doc_frm, textvariable=doc_phone, fg="#1c478b", relief=RIDGE, font=("Halvetica", 12, "bold"))
    phone_entry.place(x=250, y=155)

    sal_lbl = Label(add_doc_frm, text="Salary" ,bg="#1c478b", fg="#ffffff", font=("Halvetica", 20, "bold")).place(x= 490, y=150)
    salary_entry = Entry(add_doc_frm, textvariable=doc_salary, fg="#1c478b", relief=RIDGE, font=("Halvetica", 12, "bold"))
    salary_entry.place(x=650, y=155)

    wek_lbl = Label(add_doc_frm, text="Week off" ,bg="#1c478b", fg="#ffffff", font=("Halvetica", 20, "bold")).place(x= 80, y=200)
    wek_entry = Entry(add_doc_frm, textvariable=doc_week, fg="#1c478b", relief=RIDGE, font=("Halvetica", 12, "bold"))
    wek_entry.place(x=250, y=205)

    timing_lbl = Label(add_doc_frm, text="Timing", bg="#1c478b", fg="#ffffff", font=("Halvetica", 20, "bold")).place(x= 490, y=200)
    timing_entry = Entry(add_doc_frm, textvariable=doc_time, fg="#1c478b", relief=RIDGE, font=("Halvetica", 12, "bold"))
    timing_entry.place(x=650, y=205)

    check_accname_btn = Button(add_doc_frm, text="Check username", command=check_doc_name, fg="#ffffff", width=14, bg="#f62c47", font=("Halvetica", 15, "bold"))
    check_accname_btn.place(x=270, y=300)

    add_acc_btn = Button(add_doc_frm, text="Create account", state=DISABLED , command=create_doc_acc , fg="#ffffff", width=14, bg="#f62c47",font=("Halvetica", 15, "bold"))
    add_acc_btn.place(x= 490, y=300)

    empty_lbl = Label(add_doc_frm, text="  ", bg="#1c478b").pack(pady=250)


    #Delete account of doctor frame:
    del_doc_frm = Frame(manage_doc_frame, bg="#1c478b")
    uservalue_doc = StringVar()
    passvalue_doc = StringVar()
    h1_lbl = Label(del_doc_frm, text="Delete Doctor", bg="#1c478b", fg="#ffffff",font=("Comic Sans Ms", 35, "bold")).pack()
    empty_lbl = Label(del_doc_frm, text="  ", bg="#1c478b").pack(pady=35)
    user_entry1_lbl = Label(del_doc_frm, text="Username: ", bg="#1c478b", fg="#ffffff", font=("Halvetica", 20, "bold")).pack()
    user_entry1 = Entry(del_doc_frm, textvariable=uservalue_doc, fg="#1c478b", relief=RIDGE, font=("Halvetica", 20, "bold"))
    user_entry1.pack()

    pass_entry1_lbl = Label(del_doc_frm, text="Password: ", bg="#1c478b", fg="#ffffff", font=("Halvetica", 20, "bold")).pack()
    pass_entry1 = Entry(del_doc_frm, textvariable=passvalue_doc, show="*", relief=RIDGE, fg="#1c478b", font=("Halvetica", 20, "bold"))
    pass_entry1.pack()
    delete_doc_btn = Button(del_doc_frm, text="Delete", fg="#ffffff", command= del_doc_acc, width=14, bg="#f62c47",font=("Halvetica", 15, "bold"))
    delete_doc_btn.pack(pady=10)
    empty_lbl = Label(del_doc_frm, text="  ", bg="#1c478b").pack(pady=105)

    head_mdoc_lbl = Label(manage_doc_frame, text="Manage Doctors", bg="#1f7dad", fg="#ffffff",font=("Comic Sans Ms", 30, "bold"), pady=2)
    head_mdoc_lbl.pack(pady=20, padx=370)

    empty_lbl = Label(manage_doc_frame, text="  ", bg="#1c478b").pack(pady=25)

    add_doc_btn = Button(manage_doc_frame, text="Add", fg="#ffffff", command=add_doc , width=16,bg="#f62c47", font=("Halvetica", 15, "bold"))
    add_doc_btn.place(x=100, y=100)

    delete_doc_btn = Button(manage_doc_frame, text="Delete", fg="#ffffff", command=del_doc , width=16,bg="#f62c47", font=("Halvetica", 15, "bold"))
    delete_doc_btn.place(x=700, y=100)



#--------------------------------------------------Manage Receptioninst-------------------------------------------------
    manage_rec_frame = Frame(admin_root, bg="#1c478b")

    def call_add_rec():
        add_rec_frm.pack(fill = BOTH)
        del_rec_frm.forget()
        add_rec_btn.configure(state=DISABLED)
        delete_rec_btn.configure(state=NORMAL)

    def call_del_rec():
        del_rec_frm.pack(fill = BOTH)
        add_rec_frm.forget()
        add_rec_btn.configure(state=NORMAL)
        delete_rec_btn.configure(state=DISABLED)


    head_rec_lbl = Label(manage_rec_frame, text="Manage Receptionist", bg="#1f7dad", fg="#ffffff", font=("Comic Sans Ms", 30, "bold"), pady=2)
    head_rec_lbl.pack(pady=40)
    empty_lbl = Label(manage_rec_frame, text="  ", bg="#1c478b").pack(pady=10)


    add_rec_btn = Button(manage_rec_frame, text="Add",command= call_add_rec , fg="#ffffff", width=16, bg="#f62c47", font=("Halvetica", 15, "bold"))
    add_rec_btn.place(x=100, y=110)

    delete_rec_btn = Button(manage_rec_frame, text="Delete",command= call_del_rec ,  fg="#ffffff", width=16, bg="#f62c47", font=("Halvetica", 15, "bold"))
    delete_rec_btn.place(x=700, y=110)


#delete frame
    del_rec_frm = Frame(manage_rec_frame, bg="#1c478b")

    def delete_rec_acc():
        user_check = recdel_name.get()
        pass_check_rec =  recdel_pass.get() + "\n"

        if os.path.exists("Logins/Recieptionist/" + user_check + ".txt"):
            f = open("Logins/Recieptionist/" + user_check + ".txt", "r")
            u111 = f.readline()
            ps_chk = f.readline()
            f.close()
            if pass_check_rec == ps_chk:
                os.remove("Logins/Recieptionist/" + user_check + ".txt")
                tmsg.showinfo("Message" ,"Login Deleted")
            else:
                tmsg.showerror("Error", "Incorrect Password")
        else:
            tmsg.showerror("Error", "Invalid Username")



    recdel_name = StringVar()
    recdel_pass = StringVar()

    rec_u_del_lbl = Label(del_rec_frm, text=" Username", bg="#1c478b", fg="#ffffff", font=("Halvetica", 25, "bold")).place(x=320, y=55)
    rec_u_del_entry = Entry(del_rec_frm, textvariable=recdel_name, fg="#1c478b", relief=RIDGE, font=("Halvetica", 16, "bold"))
    rec_u_del_entry.place(x=320, y=100)

    rec_p_del_lbl = Label(del_rec_frm, text="Password", bg="#1c478b", fg="#ffffff", font=("Halvetica", 25, "bold")).place(x=320, y=140)
    rec_p_del_entry = Entry(del_rec_frm, textvariable=recdel_pass, fg="#1c478b", relief=RIDGE,font=("Halvetica", 16, "bold"))
    rec_p_del_entry.place(x=320, y=200)

    rec_del_acc_btn = Button(del_rec_frm, text= "Delete account", command=delete_rec_acc, fg="#ffffff", width=14, bg="#f62c47", font=("Halvetica", 15, "bold"))
    rec_del_acc_btn.place(x=400, y=290)
    empty_lbl = Label(del_rec_frm, text="  ", bg="#1c478b").pack(pady=290)



#add Frame
    add_rec_frm = Frame(manage_rec_frame, bg="#1c478b")
    def check_rec_name():
        recusername = rec_name.get()
        if os.path.exists("Logins/Recieptionist/" + recusername + ".txt"):
            rec_u_entry.configure(fg="red")
            tmsg.showerror("Error", "Username already exist!")
        else:
            rec_u_entry.configure(fg="green")
            rec_p_entry.configure(state= NORMAL)
            rec_age_enty.configure(state= NORMAL)
            rec_gender_entry.configure(state= NORMAL)
            rec_phone_entry.configure(state= NORMAL)
            rec_salary_entry.configure(state= NORMAL)
            rec_wek_entry.configure(state= NORMAL)
            shift1_R.configure(state= NORMAL)
            shift12_R.configure(state= NORMAL)
            rec_add_acc_btn.configure(state= NORMAL, bg="green")



    def create_rec_acc():
        a1 = rec_name.get()
        p1 = rec_pass.get()
        d1 = rec_doj.get()
        g1 = rec_gend.get()
        ph1 = rec_phone.get()
        s1 = str(rec_salary.get())
        w1 = rec_week.get()
        sv1 = "Shift: " + str(shift_val.get())

        f = open("Logins/Recieptionist/" + a1 + ".txt", "x")
        f.close()
        f = open("Logins/Recieptionist/" + a1 + ".txt", "a")
        f.write(a1)
        f.write(z)
        f.write(p1)
        f.write(z)
        f.write(d1)
        f.write(z)
        f.write(g1)
        f.write(z)
        f.write(ph1)
        f.write(z)
        f.write(w1)
        f.write(z)
        f.write(sv1)
        f.write(z)
        f.write(s1)
        f.close()
        tmsg.showinfo("Message", "Login succesfully created")
        rec_u_entry.delete(0, END)
        rec_p_entry.delete(0, END)
        rec_age_enty.delete(0, END)
        rec_gender_entry.delete(0, END)
        rec_phone_entry.delete(0, END)
        rec_salary_entry.delete(0, END)
        rec_wek_entry.delete(0, END)
        rec_add_acc_btn.configure(state=DISABLED, bg="red")


#Variable used
    rec_name = StringVar()
    rec_pass = StringVar()
    rec_doj = StringVar()
    rec_gend = StringVar()
    rec_phone = StringVar()
    rec_salary = IntVar()
    rec_week = StringVar()
    shift_val = IntVar()


    rec_u_lbl = Label(add_rec_frm, text=" Username", bg="#1c478b", fg="#ffffff", font=("Halvetica", 20, "bold")).place(x=80, y=50)
    rec_u_entry = Entry(add_rec_frm, textvariable=rec_name, fg="#1c478b", relief=RIDGE, font=("Halvetica", 12, "bold"))
    rec_u_entry.place(x=250, y=55)

    rec_p_lbl = Label(add_rec_frm, text="Password", bg="#1c478b", fg="#ffffff", font=("Halvetica", 20, "bold")).place(x=490, y=50)
    rec_p_entry = Entry(add_rec_frm, state=DISABLED,  textvariable=rec_pass, fg="#1c478b", relief=RIDGE, font=("Halvetica", 12, "bold"))
    rec_p_entry.place(x=650, y=55)

    rec_age_lbl = Label(add_rec_frm, text="Date of join", bg="#1c478b", fg="#ffffff", font=("Halvetica", 20, "bold")).place(x=80, y=100)
    rec_age_enty = Entry(add_rec_frm, state=DISABLED,  textvariable=rec_doj, fg="#1c478b", relief=RIDGE, font=("Halvetica", 12, "bold"))
    rec_age_enty.place(x=250, y=105)

    rec_gender_lbl = Label(add_rec_frm, text="Gender", bg="#1c478b", fg="#ffffff", font=("Halvetica", 20, "bold")).place(x=490, y=100)
    rec_gender_entry = Entry(add_rec_frm, state=DISABLED,  textvariable=rec_gend, fg="#1c478b", relief=RIDGE, font=("Halvetica", 12, "bold"))
    rec_gender_entry.place(x=650, y=105)

    rec_phone_lbl = Label(add_rec_frm, text="Phone no.", bg="#1c478b", fg="#ffffff", font=("Halvetica", 20, "bold")).place(x=80, y=150)
    rec_phone_entry = Entry(add_rec_frm, state=DISABLED,  textvariable=rec_phone, fg="#1c478b", relief=RIDGE, font=("Halvetica", 12, "bold"))
    rec_phone_entry.place(x=250, y=155)

    rec_sal_lbl = Label(add_rec_frm, text="Salary", bg="#1c478b", fg="#ffffff", font=("Halvetica", 20, "bold")).place(x=490, y=150)
    rec_salary_entry = Entry(add_rec_frm, state=DISABLED,  textvariable=rec_salary, fg="#1c478b", relief=RIDGE, font=("Halvetica", 12, "bold"))
    rec_salary_entry.place(x=650, y=155)

    rec_wek_lbl = Label(add_rec_frm, text="Week off", bg="#1c478b", fg="#ffffff", font=("Halvetica", 20, "bold")).place(x=80, y=200)
    rec_wek_entry = Entry(add_rec_frm, state=DISABLED,  textvariable=rec_week, fg="#1c478b", relief=RIDGE, font=("Halvetica", 12, "bold"))
    rec_wek_entry.place(x=250, y=205)

    rec_timing_lbl = Label(add_rec_frm, text="Shift", bg="#1c478b", fg="#ffffff", font=("Halvetica", 20, "bold")).place(x=490, y=200)
    shift1_R = Radiobutton(add_rec_frm, state=DISABLED,  text="Shift 1",activebackground="#1c478b", selectcolor="#1c478b" ,activeforeground="#1c478b" , variable= shift_val, value= 1 , bg="#1c478b", fg="#ffffff", font=("Halvetica", 15, "bold"))
    shift1_R.place(x=650, y=205)
    shift12_R = Radiobutton(add_rec_frm, state=DISABLED,  text="Shift 2",activebackground="#1c478b", selectcolor="#1c478b" ,activeforeground="#1c478b" , variable= shift_val, value= 2 , bg="#1c478b", fg="#ffffff", font=("Halvetica", 15, "bold"))
    shift12_R.place(x=750, y=205)

    rec_check_accname_btn = Button(add_rec_frm, text="Check username", command=check_rec_name, fg="#ffffff", width=14, bg="#f62c47", font=("Halvetica", 15, "bold"))
    rec_check_accname_btn.place(x=270, y=300)

    rec_add_acc_btn = Button(add_rec_frm, text="Create account", state=DISABLED, command=create_rec_acc, fg="#ffffff", width=14, bg="#f62c47", font=("Halvetica", 15, "bold"))
    rec_add_acc_btn.place(x=490, y=300)

    empty_lbl = Label(add_rec_frm, text="  ", bg="#1c478b").pack(pady=290)


    # --------------------------------------------------View Receptioninst---------------------------------------------------

    view_recp_frame = Frame(admin_root, bg="#1c478b")

    head_rec_lbl = Label(view_recp_frame, text="View Recieptionist", bg="#1f7dad", fg="#ffffff", font=("Comic Sans Ms", 30, "bold"), pady=2)
    head_rec_lbl.pack(pady=20, padx=340)

    rec_list_frame = Frame(view_recp_frame, bg="#1c478b")
    # List scroll bar
    rec_list_scrollbar = Scrollbar(rec_list_frame)
    rec_list_scrollbar.pack(side=RIGHT, fill=Y)
    # Doc list
    rec_listbox = Listbox(rec_list_frame, yscrollcommand=rec_list_scrollbar.set, fg="#ffffff", bg="grey", width=150, height=40, font=("Comic Sans Ms", 15, "bold"))
    rec_list = os.listdir("Logins/Recieptionist/")
    rec_numb1 = len(rec_list)

    total_rec = "Total Recieptionist: " + str(rec_numb1)
    vr_lbl1 = Label(view_recp_frame, text="Name", font=("Comic Sans Ms", 10, "bold"), fg="#ffffff", bg="#1c478b").place(x=50, y=160)
    vr_lbl2 = Label(view_recp_frame, text="Password", font=("Comic Sans Ms", 10, "bold"), fg="#ffffff", bg="#1c478b").place(x=195, y=160)
    vr_lbl3 = Label(view_recp_frame, text="Date of joining", font=("Comic Sans Ms", 10, "bold"), fg="#ffffff",bg="#1c478b").place(x=295, y=160)
    vr_lbl4 = Label(view_recp_frame, text="Gender", font=("Comic Sans Ms", 10, "bold"), fg="#ffffff", bg="#1c478b").place(x=435, y=160)
    vr_lbl6 = Label(view_recp_frame, text="Phone no.", font=("Comic Sans Ms", 10, "bold"), fg="#ffffff",bg="#1c478b").place(x=544, y=160)
    vr_lbl6a = Label(view_recp_frame, text="Week off", font=("Comic Sans Ms", 10, "bold"), fg="#ffffff", bg="#1c478b").place(x=675, y=160)
    vr_lbl7 = Label(view_recp_frame, text="Shift", font=("Comic Sans Ms", 10, "bold"), fg="#ffffff", bg="#1c478b").place(x=790, y=160)
    vr_lbl8 = Label(view_recp_frame, text="Salary", font=("Comic Sans Ms", 10, "bold"), fg="#ffffff", bg="#1c478b").place(x=901, y=160)
    vr_total_lalb = Label(view_recp_frame, text=total_rec, font=("Comic Sans Ms", 15, "bold"), fg="#ffffff",bg="#1c478b").pack()
    empty_lbl = Label(view_recp_frame, text="  ", bg="#1c478b").pack(pady=15)

    for ii1 in range(rec_numb1):

        rec1 = rec_list[ii1]
        f = open("Logins/Recieptionist/" + rec1)
        rec_uname = f.readline()
        rec_psw = f.readline()
        rec_doj = f.readline()
        rec_Gender = f.readline()
        rec_Phone = f.readline()
        rec_week_off = f.readline()
        rec_shift = f.readline()
        rec_Salary = f.readline()
        f.close()

        sp = "    "

        rec_listbox.insert(END, "  " + rec_uname + sp + "  " + rec_psw + sp + rec_doj + sp + rec_Gender + sp + rec_Phone + sp + rec_week_off + sp + rec_shift + sp + rec_Salary )
    rec_listbox.pack(side=LEFT)
    rec_list_scrollbar.configure(command=rec_listbox.yview)

    rec_list_frame.pack(pady=8, padx=10)



    #---------------------------------------------------------View Income---------------------------------------------------
    view_income_frame = Frame(admin_root, bg="#1c478b")

    def find_year_file():
        which_year = year.get()
        if os.path.exists("Income/" + which_year + ".txt"):
            insert_in_list(which_year)
        else:
            tmsg.showerror("Error", "No record found of this year!")

    def insert_in_list(which_year1):
        f = open("Income/" + which_year1 + ".txt", "r")
        len_of_file = len(f.readlines())

        f.close()
        if len_of_file > 0:
            f = open("Income/" + which_year1 + ".txt", "r")
            for t in range(len_of_file):
                file_line = f.readline()
                income_of_year_list.insert(END, "   " + str(t+1) +".     "+ file_line)

            f.close()
        else:
            tmsg.showinfo("Message", "No record to show in this file")



    year = StringVar()

    view_income_lbl = Label(view_income_frame, text="Income", bg="#1f7dad", fg="#ffffff", font=("Comic Sans Ms", 30, "bold"), pady=2)
    view_income_lbl.pack(pady=20)
    which_year_lbl = Label(view_income_frame, text= "Select Year", font=("Comic Sans Ms", 15, "bold"), fg="#ffffff", bg="#1c478b").pack(pady=2)
    which_year_entry = Entry(view_income_frame, textvariable=year , fg="#1c478b", relief=RIDGE, font=("Halvetica", 12, "bold")).pack()
    find_year_file_btn = Button(view_income_frame, text="View income", command=find_year_file, fg="#ffffff", width=14, bg="#f62c47", font=("Halvetica", 15, "bold")).pack(pady=5)
    empty_lbl = Label(view_income_frame, text="  ", bg="#1c478b").pack(pady=15)
    head_in_v_lbl = Label(view_income_frame, text= " Sr.        Date                   Total income            Total spend           Today income" , font=("Comic Sans Ms", 15, "bold"), fg="#ffffff", bg="#1c478b").place(x = 10, y= 216)
    income_of_year_list = Listbox(view_income_frame, height=25, width=90, bg="#ccf2ff", fg="#00131a", font=("Halvetica", 18))
    income_of_year_list.pack()
    empty_lbl = Label(view_income_frame, text="  ", bg="#1c478b").pack(pady=100)





#--------------------------------------------------Manage salary--------------------------------------------------------
    salary_frame = Frame(admin_root, bg="#1c478b")

    def call_doc_salary_frame():
        doc_salary_manage_frm.pack(fill=BOTH)
        rec_salary_manage_frm.forget()
        doc_salary_btn.configure(state = DISABLED)
        recsalary_btn.configure(state = NORMAL)

    def call_rec_salary_frame():
        rec_salary_manage_frm.pack(fill=BOTH)
        doc_salary_manage_frm.forget()
        doc_salary_btn.configure(state = NORMAL)
        recsalary_btn.configure(state = DISABLED)

    def check_usr_for_salary():
        check_u = salary_usern.get()
        if os.path.exists("Logins/Doctor/" + check_u + ".txt"):

            f = open("Logins/Doctor/" + check_u + ".txt")
            u1= f.readline()
            p1= f.readline()
            doj1= f.readline()
            g= f.readline()
            pn= f.readline()
            tm= f.readline()
            wk= f.readline()
            sl= f.readline()
            f.close()
            salary_maage_listbox.insert(END, "  " + "Username: " + u1 + "      Gender: " + g + "      Phone no.: " + pn + "      Current Salary: " + sl)
            change_salary.pack()
            salary_change_entry.configure(state=NORMAL, fg="green")
            salary_change_btn.configure(state=NORMAL, bg="green")

        else:
            tmsg.showerror("Error", "Invalid Username")

    doc_salary_manage_frm = Frame(salary_frame, bg="#1c478b")
    salary_usern = StringVar()

    salary_usern_lbl = Label(doc_salary_manage_frm, text=" Username", bg="#1c478b", fg="#ffffff", font=("Halvetica", 25, "bold")).pack()
    salary_usern_entry = Entry(doc_salary_manage_frm, textvariable= salary_usern, fg="#1c478b", relief=RIDGE,font=("Halvetica", 16, "bold"))
    salary_usern_entry.pack(pady= 15)

    salary_usern_check_btn = Button(doc_salary_manage_frm, text="Search User", command=check_usr_for_salary , fg="#ffffff", width=14, bg="#f62c47", font=("Halvetica", 15, "bold"))
    salary_usern_check_btn.pack()
    salary_maage_listbox = Listbox(doc_salary_manage_frm, fg="#ffffff", bg="grey", width=90,height= 2, font=("Comic Sans Ms", 15, "bold"))
    salary_maage_listbox.pack(pady=15)

    change_salary = Frame(salary_frame, bg="#1c478b")

    def add_new_doc_salary():
        file_open = salary_usern.get()
        # list to store lines
        lines = []
        # read file
        f = open("Logins/Doctor/" + file_open + ".txt", "r")
        lines = f.readlines()
        f.close()

        # writting in the files
        f = open("Logins/Doctor/" + file_open + ".txt", "w")
        # iterate each line
        for number, line in enumerate(lines):
            if number not in [7]:
                f.write(line)
        f.close()
        sal = new_salary.get()
        f = open("Logins/Doctor/" + file_open + ".txt", "a")
        f.write(sal)
        tmsg.showinfo("Message", file_open + "'s Salary updated")
        f.close()
        salary_change_entry.delete(0, END)
        salary_usern_entry.delete(0, END)
        salary_maage_listbox.delete(0,END)
        salary_change_entry.configure(state=DISABLED)
        salary_change_btn.configure(state=DISABLED, bg="red")

    new_salary = StringVar()
    empty_lbl = Label(change_salary, text="  ", bg="#1c478b").pack(pady=10)
    salary_change_lbl = Label(change_salary, text="New salary", bg="#1c478b", fg="#ffffff", font=("Halvetica", 25, "bold")).pack()
    salary_change_entry = Entry(change_salary, state= DISABLED , textvariable=new_salary, fg="#1c478b", relief=RIDGE, font=("Halvetica", 16, "bold"))
    salary_change_entry.pack(pady=15)

    salary_change_btn = Button(change_salary, state= DISABLED ,  text="Add Salary", command= add_new_doc_salary, fg="#ffffff", width=14, bg="#f62c47", font=("Halvetica", 15, "bold"))
    salary_change_btn.pack()
    empty_lbl = Label(change_salary, text="  ", bg="#1c478b").pack(pady=50)

 #Recp Salary update frame:

    rec_salary_manage_frm = Frame(salary_frame, bg="#1c478b")

    def check_rec_usr_for_salary():
        check_u_rec = salary_usern_rec.get()
        if os.path.exists("Logins/Recieptionist/" + check_u_rec + ".txt"):

            f = open("Logins/Recieptionist/" + check_u_rec + ".txt")
            u11= f.readline()
            p11= f.readline()
            doj11= f.readline()
            g1= f.readline()
            pn1= f.readline()
            tm1= f.readline()
            wk1= f.readline()
            sl1= f.readline()
            f.close()
            salary_rec_maage_listbox.insert(END, "  " + "Username: " + u11 + "      Gender: " + g1 + "      Phone no.: " + pn1 + "      Current Salary: " + sl1)
            change_rec_salary.pack()
            salary_change_rec_entry.configure(state=NORMAL, fg="green")
            salary_change_rec_btn.configure(state=NORMAL, bg="green")

        else:
            tmsg.showerror("Error", "Invalid Username")

    salary_usern_rec = StringVar()

    salary_usern_rec_lbl = Label(rec_salary_manage_frm, text=" Username", bg="#1c478b", fg="#ffffff", font=("Halvetica", 25, "bold")).pack()
    salary_usern_rec_entry = Entry(rec_salary_manage_frm, textvariable= salary_usern_rec, fg="#1c478b", relief=RIDGE,font=("Halvetica", 16, "bold"))
    salary_usern_rec_entry.pack(pady= 15)

    salary_usern_rec_check_btn = Button(rec_salary_manage_frm, text="Search User", command=check_rec_usr_for_salary , fg="#ffffff", width=14, bg="#f62c47", font=("Halvetica", 15, "bold"))
    salary_usern_rec_check_btn.pack()
    salary_rec_maage_listbox = Listbox(rec_salary_manage_frm, fg="#ffffff", bg="grey", width=90,height= 2, font=("Comic Sans Ms", 15, "bold"))
    salary_rec_maage_listbox.pack(pady=15)

    change_rec_salary = Frame(salary_frame, bg="#1c478b")

    def add_new_rec_salary():
        file_open1 = salary_usern_rec.get()
        # list to store lines
        lines1 = []
        # read file
        f = open("Logins/Recieptionist/" + file_open1 + ".txt", "r")
        lines1 = f.readlines()
        f.close()

        # writting in the files
        f = open("Logins/Recieptionist/" + file_open1 + ".txt", "w")
        # iterate each line
        for number1, line1 in enumerate(lines1):
            if number1 not in [7]:
                f.write(line1)
        f.close()
        sal1 = new_salary1.get()
        f = open("Logins/Recieptionist/" + file_open1 + ".txt", "a")
        f.write(sal1)
        tmsg.showinfo("Message", file_open1 + "'s Salary updated")
        f.close()
        salary_change_rec_entry.delete(0, END)
        salary_usern_entry.delete(0, END)
        salary_rec_maage_listbox.delete(0,END)
        salary_change_rec_entry.configure(state=DISABLED)
        salary_change_rec_btn.configure(state=DISABLED, bg="red")

    new_salary1 = StringVar()
    empty_lbl = Label(change_rec_salary, text="  ", bg="#1c478b").pack(pady=10)
    salary_rec_change_lbl = Label(change_rec_salary, text="New salary", bg="#1c478b", fg="#ffffff", font=("Halvetica", 25, "bold")).pack()
    salary_change_rec_entry = Entry(change_rec_salary, state= DISABLED , textvariable=new_salary1, fg="#1c478b", relief=RIDGE, font=("Halvetica", 16, "bold"))
    salary_change_rec_entry.pack(pady=15)

    salary_change_rec_btn = Button(change_rec_salary, state= DISABLED ,  text="Add Salary", command= add_new_rec_salary, fg="#ffffff", width=14, bg="#f62c47", font=("Halvetica", 15, "bold"))
    salary_change_rec_btn.pack()
    empty_lbl = Label(change_rec_salary, text="  ", bg="#1c478b").pack(pady=50)


    manage_salary_lbl = Label(salary_frame, text="Manage Salary", bg="#1f7dad", fg="#ffffff", font=("Comic Sans Ms", 30, "bold"), pady=2)
    manage_salary_lbl.pack(pady=40)
    empty_lbl = Label(salary_frame, text="  ", bg="#1c478b").pack(pady=10)

    doc_salary_btn = Button(salary_frame, text="Doctor salary", command= call_doc_salary_frame, fg="#ffffff", width=16, bg="#f62c47", font=("Halvetica", 15, "bold"))
    doc_salary_btn.place(x=135, y=110)

    recsalary_btn = Button(salary_frame, text="Receptionist salary", command= call_rec_salary_frame,  fg="#ffffff", width=16, bg="#f62c47", font=("Halvetica", 15, "bold"))
    recsalary_btn.place(x=700, y=110)


    def manage_admin():

        manage_admin_frame.pack(side=RIGHT, anchor="e", fill=Y)
        view_doc_frame.forget()
        manage_doc_frame.forget()
        view_recp_frame.forget()
        manage_rec_frame.forget()
        view_income_frame.forget()
        salary_frame.forget()

        manege_admin_btn.configure(state=DISABLED)
        View_doctor_btn.configure(state=NORMAL)
        Manage_doctor_btn.configure(state=NORMAL)
        View_rec_btn.configure(state=NORMAL)
        Manage_rec_btn.configure(state=NORMAL)
        View_income.configure(state=NORMAL)
        Salary_btn.configure(state=NORMAL)

    def view_doc():
        manage_admin_frame.forget()
        view_doc_frame.pack()
        manage_doc_frame.forget()
        view_recp_frame.forget()
        manage_rec_frame.forget()
        view_income_frame.forget()
        salary_frame.forget()

        manege_admin_btn.configure(state=NORMAL)
        View_doctor_btn.configure(state=DISABLED)
        Manage_doctor_btn.configure(state=NORMAL)
        View_rec_btn.configure(state=NORMAL)
        Manage_rec_btn.configure(state=NORMAL)
        View_income.configure(state=NORMAL)
        Salary_btn.configure(state=NORMAL)

    def manage_doc():
        manage_admin_frame.forget()
        view_doc_frame.forget()
        manage_doc_frame.pack()
        view_recp_frame.forget()
        manage_rec_frame.forget()
        view_income_frame.forget()
        salary_frame.forget()

        manege_admin_btn.configure(state=NORMAL)
        View_doctor_btn.configure(state=NORMAL)
        Manage_doctor_btn.configure(state=DISABLED)
        View_rec_btn.configure(state=NORMAL)
        Manage_rec_btn.configure(state=NORMAL)
        View_income.configure(state=NORMAL)
        Salary_btn.configure(state=NORMAL)

    def view_recp():
        manage_admin_frame.forget()
        view_doc_frame.forget()
        manage_doc_frame.forget()
        view_recp_frame.pack()
        manage_rec_frame.forget()
        view_income_frame.forget()
        salary_frame.forget()

        manege_admin_btn.configure(state=NORMAL)
        View_doctor_btn.configure(state=NORMAL)
        Manage_doctor_btn.configure(state=NORMAL)
        View_rec_btn.configure(state=DISABLED)
        Manage_rec_btn.configure(state=NORMAL)
        View_income.configure(state=NORMAL)
        Salary_btn.configure(state=NORMAL)

    def manage_recp():
        manage_admin_frame.forget()
        view_doc_frame.forget()
        manage_doc_frame.forget()
        view_recp_frame.forget()
        manage_rec_frame.pack(fill = BOTH)
        view_income_frame.forget()
        salary_frame.forget()

        manege_admin_btn.configure(state=NORMAL)
        View_doctor_btn.configure(state=NORMAL)
        Manage_doctor_btn.configure(state=NORMAL)
        View_rec_btn.configure(state=NORMAL)
        Manage_rec_btn.configure(state=DISABLED)
        View_income.configure(state=NORMAL)
        Salary_btn.configure(state=NORMAL)

    def view_income():
        manage_admin_frame.forget()
        view_doc_frame.forget()
        manage_doc_frame.forget()
        view_recp_frame.forget()
        manage_rec_frame.forget()
        view_income_frame.pack(fill=BOTH)
        salary_frame.forget()

        manege_admin_btn.configure(state=NORMAL)
        View_doctor_btn.configure(state=NORMAL)
        Manage_doctor_btn.configure(state=NORMAL)
        View_rec_btn.configure(state=NORMAL)
        Manage_rec_btn.configure(state=NORMAL)
        View_income.configure(state=DISABLED)
        Salary_btn.configure(state=NORMAL)

    def salary():
        manage_admin_frame.forget()
        view_doc_frame.forget()
        manage_doc_frame.forget()
        view_recp_frame.forget()
        manage_rec_frame.forget()
        view_income_frame.forget()
        salary_frame.pack(fill=X)

        manege_admin_btn.configure(state=NORMAL)
        View_doctor_btn.configure(state=NORMAL)
        Manage_doctor_btn.configure(state=NORMAL)
        View_rec_btn.configure(state=NORMAL)
        Manage_rec_btn.configure(state=NORMAL)
        View_income.configure(state=NORMAL)
        Salary_btn.configure(state=DISABLED)



    # operations buttons

    operations_btn_frame = Frame(admin_root, bg="#1c478b")

    empty_lbl = Label(operations_btn_frame, text="  ", bg="#1c478b").pack(pady=20)
    manege_admin_btn = Button(operations_btn_frame, text="Manage admin", command= manage_admin , width=16, fg="#1c478b", bg="#ffffff",font=("Halvetica", 20, "bold"))
    manege_admin_btn.pack(padx=10, pady=10)
    View_doctor_btn = Button(operations_btn_frame, text="View Doctor", command=view_doc , width=16, fg="#1c478b", bg="#ffffff", font=("Halvetica", 20, "bold"))
    View_doctor_btn.pack(padx=10, pady=10)
    Manage_doctor_btn = Button(operations_btn_frame, text="Manage Doctor" , command=manage_doc ,width= 16, fg="#1c478b", bg="#ffffff",  font=("Halvetica", 20, "bold"))
    Manage_doctor_btn.pack(padx=10, pady=10)
    View_rec_btn = Button(operations_btn_frame, text="View Receptionist"        ,command= view_recp, width= 16, fg="#1c478b", bg="#ffffff",  font=("Halvetica", 20, "bold"))
    View_rec_btn.pack(padx=10, pady=10)
    Manage_rec_btn = Button(operations_btn_frame, text="Manage Receptionist"    ,command= manage_recp, fg="#1c478b", bg="#ffffff",  font=("Halvetica", 20, "bold"))
    Manage_rec_btn.pack(padx=10, pady=10)
    View_income = Button(operations_btn_frame, text="Income"       , command=view_income , width= 16, fg="#1c478b", bg="#ffffff",  font=("Halvetica", 20, "bold"))
    View_income.pack(padx=10, pady=10)
    Salary_btn = Button(operations_btn_frame, text="Salary", command=salary ,width=16, fg="#1c478b", bg="#ffffff", font=("Halvetica", 20, "bold"))
    Salary_btn.pack(padx=10, pady=10)
    logout_btn = Button(operations_btn_frame, text="Log Out",command=lambda :logout(admin_root) , fg="#ffffff", width= 16, bg="#f62c47", font=("Halvetica", 15, "bold"))
    logout_btn.pack(pady=5, padx=10)

    operations_btn_frame.pack(side=LEFT, anchor="w", fill=Y)

    admin_root.mainloop()


#---------------------------------------------------logged as doctor----------------------------------------------------
def logged_as_doctor(doc_name, root):
    root.destroy()
    doctor_root = Tk()
    doctor_root.geometry("1366x768")
    doctor_root.minsize(1365, 767)
    doctor_root.maxsize(1368, 769)
    doctor_root.configure(bg="#cececf")

    heading_frame = Frame(doctor_root, bg="#1f7dad")
    heading_label = Label(heading_frame, text="Welcome " + doc_name, bg="#1f7dad", fg="#ffffff", font=("Comic Sans Ms", 15, "bold"), pady=2).pack(pady=10)
    heading_frame.pack(side=TOP, anchor="n", fill=BOTH)


#working frames

#---------------------------------------------------------Doc profile page----------------------------------------------
    Myprofile_frame = Frame(doctor_root, bg="#1c478b")

    doc_profile_lbl = Label(Myprofile_frame, text="My profile", bg="#1f7dad", fg="#ffffff", font=("Comic Sans Ms", 30, "bold"), pady=2)
    doc_profile_lbl.pack(pady=20, fill= X)

    def open_edit_tabs():
        edit_btn.configure(state=DISABLED)
        name_entry.place(x = 350, y= 100)
        name_change_btn.place(x = 750, y= 98)
        password_entry.place(x = 350, y =158)
        pass_change_btn.place(x = 750, y =160)
        phone_entry.place(x = 350, y =340)
        phone_change_btn.place(x = 750, y =338)

        name_entry.configure(state= NORMAL)
        name_change_btn.configure(state= NORMAL)
        password_entry.configure(state= NORMAL)
        pass_change_btn.configure(state= NORMAL)
        phone_entry.configure(state= NORMAL)
        phone_change_btn.configure(state= NORMAL)

    def change_name():
        name_to_change = ne.get()
        # read file
        f = open("Logins/Doctor/" + doc_name + ".txt", "r")
        lines11 = f.readline()
        lines12 = f.readline()
        lines13 = f.readline()
        lines14 = f.readline()
        lines15 = f.readline()
        lines16 = f.readline()
        lines17 = f.readline()
        lines18 = f.readline()
        f.close()
        f = open("Logins/Doctor/" + name_to_change + ".txt", "x")
        f.close()
        line101 = name_to_change + "\n"
        f = open("Logins/Doctor/" + name_to_change + ".txt", "a")
        f.write(line101)
        f.write(lines12)
        f.write(lines13)
        f.write(lines14)
        f.write(lines15)
        f.write(lines16)
        f.write(lines17)
        f.write(lines18)
        f.close()

        os.remove("Logins/Doctor/" + doc_name + ".txt")
        edit_btn.configure(state=NORMAL)
        name_entry.configure(state = DISABLED)
        name_entry.delete(0, END)
        name_change_btn.configure(state = DISABLED)
        password_entry.configure(state = DISABLED)
        pass_change_btn.configure(state = DISABLED)
        phone_entry.configure(state = DISABLED)
        phone_change_btn.configure(state = DISABLED)


        tmsg.showinfo("Message", doc_name + " Username updates, Please re-Login to use")

    def change_pass():
        pass_to_change = pe.get()
        # read file
        f = open("Logins/Doctor/" + doc_name + ".txt", "r")
        lines11 = f.readline()
        lines12 = f.readline()
        lines13 = f.readline()
        lines14 = f.readline()
        lines15 = f.readline()
        lines16 = f.readline()
        lines17 = f.readline()
        lines18 = f.readline()
        f.close()
        os.remove("Logins/Doctor/" + doc_name + ".txt")
        f = open("Logins/Doctor/" + doc_name + ".txt", "x")
        f.close()
        line101 = pass_to_change + "\n"
        f = open("Logins/Doctor/" + doc_name + ".txt", "a")
        f.write(lines11)
        f.write(line101)
        f.write(lines13)
        f.write(lines14)
        f.write(lines15)
        f.write(lines16)
        f.write(lines17)
        f.write(lines18)
        f.close()

        edit_btn.configure(state=NORMAL)
        name_entry.configure(state=DISABLED)
        name_change_btn.configure(state=DISABLED)
        password_entry.configure(state=DISABLED)
        password_entry.delete(0, END)
        pass_change_btn.configure(state=DISABLED)
        phone_entry.configure(state=DISABLED)
        phone_change_btn.configure(state=DISABLED)

        tmsg.showinfo("Message", doc_name + " Password updated, Please re-Login to use")

    def change_phone():
        phone_to_change = phe.get()
        # read file
        f = open("Logins/Doctor/" + doc_name + ".txt", "r")
        lines11 = f.readline()
        lines12 = f.readline()
        lines13 = f.readline()
        lines14 = f.readline()
        lines15 = f.readline()
        lines16 = f.readline()
        lines17 = f.readline()
        lines18 = f.readline()
        f.close()
        os.remove("Logins/Doctor/" + doc_name + ".txt")
        f = open("Logins/Doctor/" + doc_name + ".txt", "x")
        f.close()
        line101 = phone_to_change + "\n"
        f = open("Logins/Doctor/" + doc_name + ".txt", "a")
        f.write(lines11)
        f.write(lines12)
        f.write(lines13)
        f.write(lines14)
        f.write(line101)
        f.write(lines16)
        f.write(lines17)
        f.write(lines18)
        f.close()

        edit_btn.configure(state=NORMAL)
        name_entry.configure(state=DISABLED)
        name_change_btn.configure(state=DISABLED)
        password_entry.configure(state=DISABLED)
        pass_change_btn.configure(state=DISABLED)
        phone_entry.configure(state=DISABLED)
        phone_entry.delete(0, END)
        phone_change_btn.configure(state=DISABLED)

        tmsg.showinfo("Message", doc_name + " Phone number updated, Please re-Login to use")


    f = open("Logins/Doctor/" + doc_name + ".txt", "r")
    a1 = f.readline()
    a2 = f.readline()
    a3 = f.readline()
    a4 = f.readline()
    a5 = f.readline()
    a6 = f.readline()
    a7 = f.readline()
    a8 = f.readline()

    name_lbl = Label(Myprofile_frame, text= "Username: " + a1,bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 17, "bold"))
    name_lbl.place(x= 40, y = 100)
    password_lbl = Label(Myprofile_frame, text="Password: " + a2, bg = "#1c478b", fg = "#ffffff", font = ("Comic Sans Ms", 17, "bold"))
    password_lbl.place(x= 40, y =160)
    doj_lbl = Label(Myprofile_frame, text="Date of joining: " + a3, bg = "#1c478b", fg = "#ffffff", font = ("Comic Sans Ms", 17, "bold"))
    doj_lbl.place(x= 40, y = 220)
    gender_lbl = Label(Myprofile_frame, text="Gender: " + a4, bg = "#1c478b", fg = "#ffffff", font = ("Comic Sans Ms", 17, "bold"))
    gender_lbl.place(x= 40, y =280)
    phone_lbl = Label(Myprofile_frame, text="Phone no.: " + a5, bg = "#1c478b", fg = "#ffffff", font = ("Comic Sans Ms", 17, "bold"))
    phone_lbl.place(x= 40, y =340)
    timing_lbl = Label(Myprofile_frame, text="Timing: " + a6, bg = "#1c478b", fg = "#ffffff", font = ("Comic Sans Ms", 17, "bold"))
    timing_lbl.place(x= 40, y =400)
    week_off_lbl = Label(Myprofile_frame, text="Week off: " + a7, bg = "#1c478b", fg = "#ffffff", font = ("Comic Sans Ms", 17, "bold"))
    week_off_lbl.place(x= 40, y = 460)
    salary_lbl = Label(Myprofile_frame, text="Salary: " + a8, bg = "#1c478b", fg = "#ffffff", font = ("Comic Sans Ms", 17, "bold"))
    salary_lbl.place(x= 40, y =520)
    f.close()
    edit_btn = Button(Myprofile_frame, command=open_edit_tabs , text="Edit", bg="red", fg="#ffffff", width=16, font=("Halvetica", 15, "bold"))
    edit_btn.place(x=440, y=590)

    ne = StringVar()
    pe = StringVar()
    phe = StringVar()

    name_entry = Entry(Myprofile_frame , textvariable= ne, bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 16, "bold"))
    password_entry = Entry(Myprofile_frame , textvariable= pe,  bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 16, "bold"))
    phone_entry = Entry(Myprofile_frame , textvariable= phe,  bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 16, "bold"))
    name_change_btn = Button(Myprofile_frame, command=change_name, text="Save", bg="green", fg="#ffffff", width = 16, font = ("Halvetica", 15, "bold"))
    pass_change_btn = Button(Myprofile_frame, command=change_pass, text="Save", bg="green", fg="#ffffff", width = 16, font = ("Halvetica", 15, "bold"))
    phone_change_btn = Button(Myprofile_frame, command=change_phone, text="Save", bg="green", fg="#ffffff", width = 16, font = ("Halvetica", 15, "bold"))

    empty_lbl = Label(Myprofile_frame, text="  ", bg="#1c478b").pack(pady=300)

#--------------------------------------------------patients frame-------------------------------------------------------

    patients_frame = Frame(doctor_root, bg="#1c478b")

    doc_patient_lbl = Label(patients_frame, text="Patients", bg="#1f7dad", fg="#ffffff", font=("Comic Sans Ms", 30, "bold"), pady=2)
    doc_patient_lbl.pack(pady=20, fill= X)

    #patient profile

    def Search_patient():
        patient_name = p_name.get()
        if os.path.exists("patients/" + patient_name + "/" + patient_name + ".txt"):
            search_btn.configure(state=DISABLED)
            f = open("patients/" + patient_name + "/" + patient_name + ".txt")
            age_p = f.readline()
            gen_p = f.readline()
            dotreatment_p = f.readline()
            pno_p = f.readline()
            f.close()

            f = open("patients/" + patient_name + "/" + "appointment letter.txt")
            l_app = f.readline()
            l_d_app = f.readline()
            f.close()

            no_of_rp = len(os.listdir("patients/" + patient_name +"/reports"))

            no_of_med_bils = len(os.listdir("patients/" + patient_name + "/medician"))

            f = open("patients/" + patient_name + "/" + "appointment letter.txt", "r")
            checjke = len(f.readlines())
            f.close()
            f = open("patients/" + patient_name + "/" + "appointment letter.txt", "r")
            for running in range(checjke):
                liiiiine = f.readline()
            f.close()

            patient_details_listbo.insert(END, "Name: " + patient_name)
            patient_details_listbo.insert(END, "Age: " + age_p)
            patient_details_listbo.insert(END, "Gender: " + gen_p)
            patient_details_listbo.insert(END, "Day of treatment start: " + dotreatment_p)
            patient_details_listbo.insert(END, "Name: " + pno_p)
            patient_details_listbo.insert(END, "Previous appointment: " + l_app)
            patient_details_listbo.insert(END, "Previous appointment details: " + l_d_app )
            patient_details_listbo.insert(END, "Total reports: " + str(no_of_rp))
            patient_details_listbo.insert(END, "Total Medicine bills: " + str(no_of_med_bils))
            if liiiiine == "Treatment ended":
                patient_details_listbo.insert(END, liiiiine)
            else:
                pass

        else:
            tmsg.showerror("Error", "Patient not found!")

    def new_p():
        search_btn.configure(state=NORMAL)
        patient_details_listbo.delete(0, END)

    p_name = StringVar()

    patients_profile_lbl= Label(patients_frame, text= "View patient profile" , bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 20, "bold"))
    patients_profile_lbl.pack()
    user_entry_lbl = Label(patients_frame, text="Patient name: ", bg="#1c478b", fg="#ffffff", font=("Halvetica", 14, "bold")).pack()
    user_entry = Entry(patients_frame, textvariable=p_name, fg="#1c478b", relief=RIDGE, font=("Halvetica", 16, "bold"))
    user_entry.pack()
    empty_lbl = Label(patients_frame, text="  ", bg="#1c478b").pack(pady=6)
    search_btn = Button(patients_frame, text="Search", command=Search_patient , bg="#1f7dad", width=10, fg="#ffffff", font=("Halvetica", 10, "bold"))
    search_btn.place(x = 420, y = 208)
    res_btn = Button(patients_frame, text="Reset", command=new_p, bg="#1f7dad", width=10, fg="#ffffff", font=("Halvetica", 10, "bold"))
    res_btn.place(x = 540, y = 208)

    list_scrollbar = Scrollbar(patients_frame)
    list_scrollbar.pack(side = RIGHT, fill = Y)

    list_scrollbar_x = Scrollbar(patients_frame, orient=HORIZONTAL)
    list_scrollbar_x.pack(side=BOTTOM, fill=X)

    patient_details_listbo = Listbox(patients_frame, xscrollcommand= list_scrollbar_x.set, yscrollcommand = list_scrollbar.set ,fg="#ffffff", bg="grey", width=100, height=40, font=("Comic Sans Ms", 15, "bold"))
    patient_details_listbo.pack(pady=1)
    list_scrollbar.configure(command=patient_details_listbo.yview)
    list_scrollbar_x.configure(command=patient_details_listbo.xview)

    # ----------------------------------------------------Patient report creation frame-----------------------------------------------

    create_report_frame = Frame(doctor_root, bg="#1c478b")

    create_report_lbl = Label(create_report_frame, text="Medical Report", bg="#1f7dad", fg="#ffffff", font=("Halvetica", 20, "bold"), pady=2)
    create_report_lbl.pack(pady=10, fill=X)
    empty_lbl = Label(create_report_frame, text="  ", bg="#1c478b").pack(pady=350)

    def enable_form():
        l = p_cr_name.get()
        if os.path.exists("patients/" + l):
            dop_entry_lbl.configure(state=NORMAL)
            dop_entry.configure(state=NORMAL)
            desc_problem_entry_lbl.configure(state=NORMAL)
            desc_problem_entry.configure(state=NORMAL)
            cs_ofcurrent_p_lbl.configure(state=NORMAL)
            car_ck.configure(state=NORMAL)
            work_ck.configure(state=NORMAL)
            gradual_ck.configure(state=NORMAL)
            other_ck.configure(state=NORMAL)
            req_surgery_lbl.configure(state=NORMAL)
            no_ck.configure(state=NORMAL)
            yes_ck.configure(state=NORMAL)
            d_surgery_lbl.configure(state=NORMAL)
            yes_entry.configure(state=NORMAL)
            past_medical_lbl.configure(state=NORMAL)
            past_medical_lbl2.configure(state=NORMAL)
            ck1.configure(state=NORMAL)
            ck2.configure(state=NORMAL)
            ck3.configure(state=NORMAL)
            ck4.configure(state=NORMAL)
            ck5.configure(state=NORMAL)
            ck6.configure(state=NORMAL)
            ck7.configure(state=NORMAL)
            ck8.configure(state=NORMAL)
            ck9.configure(state=NORMAL)
            ck10.configure(state=NORMAL)
            ck11.configure(state=NORMAL)
            ck12.configure(state=NORMAL)
            ck13.configure(state=NORMAL)
            ck14.configure(state=NORMAL)
            ck15.configure(state=NORMAL)
            ck16.configure(state=NORMAL)
            ck17.configure(state=NORMAL)
            ck18.configure(state=NORMAL)
            ck19.configure(state=NORMAL)
            ck20.configure(state=NORMAL)
            nosurgery_btn.configure(state=NORMAL)
            nosurgery_lbl1.configure(state=NORMAL)
            nosurgery_entry.configure(state=NORMAL)
            nosurgery_lbl2.configure(state=NORMAL)
            nosurgery_entry1.configure(state=NORMAL)
            nosurgery_lbl3.configure(state=NORMAL)
            nosurgery_entry2.configure(state=NORMAL)
            nomedication_btn.configure(state=NORMAL)
            nomedication_lbl.configure(state=NORMAL)
            nomedication_lbl0.configure(state=NORMAL)
            nomedication_lbl1.configure(state=NORMAL)
            nomedicatoin_entry.configure(state=NORMAL)
            nomedication_lbl2.configure(state=NORMAL)
            nomedicatoin_entry1.configure(state=NORMAL)
            nomedication_lbl3.configure(state=NORMAL)
            nomedicatoin_entry2.configure(state=NORMAL)
            allergy_lbl0.configure(state=NORMAL)
            allergy_entry.configure(state=NORMAL)
            q1yes_ck11.configure(state=NORMAL)
            q1no_ck11.configure(state=NORMAL)
            q1_lbl2.configure(state=NORMAL)
            notype_lbl30.configure(state=NORMAL)
            noac11_entry2.configure(state=NORMAL)
            notype_lbl31.configure(state=NORMAL)
            fever_entry2.configure(state=NORMAL)
            notype_lbl32.configure(state=NORMAL)
            bp_entry2.configure(state=NORMAL)
            create_repo_btn.configure(state=NORMAL)
        else:
            tmsg.showerror("Error", "Patient didn't found")


    def create_first():
        p_cr_n2 = p_cr_name.get()
        no_of_reports = len(os.listdir("patients/" + p_cr_n2 + "/reports/"))
        print(no_of_reports)

        if no_of_reports == 0:
            f = open("patients/" + p_cr_n2 + "/reports/" + "report" + str(0) + ".txt", "x")
            f.close()
            tmsg.showinfo("Message", "New report is created please save the data")

        else:
            name_of_new_report = "report" + str(no_of_reports)
            f = open("patients/" + p_cr_n2 + "/reports/" + name_of_new_report + ".txt", "x")
            f.close()
            tmsg.showinfo("Message", "New report is created please save the data")

        save_repo_btn.configure(state=NORMAL)
        create_repo_btn.configure(state=DISABLED)


    def file_c():
        val1 = var1.get()
        val2 = var2.get()
        val3 = var3.get()
        val4 = var4.get()
        val5 = var5.get()
        val7 = var7.get()
        val10 = var10.get()
        val11 = var11.get()
        val12 = var12.get()
        val13 = var13.get()
        val14 = var14.get()
        val15 = var15.get()
        val16 = var16.get()
        val17 = var17.get()
        val18 = var18.get()
        val19 = var19.get()
        val20 = var20.get()
        val21 = var21.get()
        val22 = var22.get()
        val23 = var23.get()
        val24 = var24.get()
        val25 = var25.get()
        val26 = var26.get()
        val27 = var27.get()
        val28 = var28.get()
        val29 = var29.get()
        val30 = var30.get()
        val31 = var31.get()
        val32 = var32.get()
        val33 = var33.get()
        val34 = var34.get()
        val35 = var35.get()
        val36 = var36.get()
        val37 = var37.get()
        val38 = var38.get()
        val46 = var46.get()
        val47 = var47.get()
        val48 = var48.get()
        p_cr_n = p_cr_name.get()

        no_of_reports = len(os.listdir("patients/" + p_cr_n +"/reports/"))
        print(no_of_reports)

#Adding data in file logic
        if no_of_reports == 1:
            f = open("patients/" + p_cr_n +"/reports/"+ "report" + str(0) + ".txt", "a")
            in0 = "Patient name: " + p_cr_n
            f.write(in0)
            f.write(z)
            if val1 == "":
                pass
            else:
                in1 = "When did the problem started: " + val1
                f.write(in1)
                f.write(z)

            if val2 == "":
                pass
            else:
                in2 = "Problem: " + val2
                f.write(in2)
                f.write(z)

            f.write("Cause of current problem:")
            if val3 == "":
                pass
            else:
                f.write(val3)
                f.write(z)

            if val4 == "":
                pass
            else:
                f.write(val4)
                f.write(z)

            if val5 == "":
                pass
            else:
                f.write(val5)
                f.write(z)

            if val7 == "":
                pass
            else:
                f.write(val7)
                f.write(z)

            f.write("Date of surgery")
            f.write(z)
            if val10 == "":
                f.write("Not req.")
                f.write(z)
            else:
                f.write(val10)
                f.write(z)

            f.write("Past medical history")
            f.write(z)
            if val11 == "":
                pass
            else:
                f.write(val11)
                f.write(z)

            if val12 == "":
                pass
            else:
                f.write(val12)
                f.write(z)

            if val13 == "":
                pass
            else:
                f.write(val13)
                f.write(z)

            if val14 == "":
                pass
            else:
                f.write(val14)
                f.write(z)

            if val15 == "":
                pass
            else:
                f.write(val15)
                f.write(z)

            if val16 == "":
                pass
            else:
                f.write(val16)
                f.write(z)

            if val17 == "":
                pass
            else:
                f.write(val17)
                f.write(z)

            if val18 == "":
                pass
            else:
                f.write(val18)
                f.write(z)

            if val19 == "":
                pass
            else:
                f.write(val19)
                f.write(z)

            if val20 == "":
                pass
            else:
                f.write(val20)
                f.write(z)

            if val21 == "":
                pass
            else:
                f.write(val21)
                f.write(z)

            if val22 == "":
                pass
            else:
                f.write(val22)
                f.write(z)

            if val23 == "":
                pass
            else:
                f.write(val23)
                f.write(z)

            if val24 == "":
                pass
            else:
                f.write(val24)
                f.write(z)

            if val25 == "":
                pass
            else:
                f.write(val25)
                f.write(z)

            if val26 == "":
                pass
            else:
                f.write(val26)
                f.write(z)

            if val27 == "":
                pass
            else:
                f.write(val27)
                f.write(z)

            if val28 == "":
                pass
            else:
                f.write(val28)
                f.write(z)

            if val29 == "":
                pass
            else:
                f.write(val29)
                f.write(z)

            if val30 == "":
                pass
            else:
                f.write(val30)
                f.write(z)

            f.write("Surgeries / Hospitalizations")
            f.write(z)
            if val31 == "":
                f.write("No")
                f.write(z)
            else:
                f.write(val31)
                f.write(z)

            if val32 == "":
                pass
            else:
                in6 = "Year: " + val32
                f.write(in6)
                f.write(z)

            if val33 == "":
                pass
            else:
                in7 = "Complications: " + val33
                f.write(in7)
                f.write(z)

            f.write("list medications that you are taking.")
            f.write(z)
            if val34 == "":
                f.write("No medication")
                f.write(z)
            else:
                in8 = "Medication(s): " + val34
                f.write(in8)
                f.write(z)

            if val35 == "":
                pass
            else:
                in9 = "Dose: " + val35
                f.write(in9)
                f.write(z)

            if val36 == "":
                pass
            else:
                in10 = "Reason of medication: " + val36
                f.write(in10)
                f.write(z)

            if val37 == "":
                pass
            else:
                in11 = "Allergy: " + val37
                f.write(in11)
                f.write(z)

            if val38 == 1:
                f.write("Do you have any religious/cultural views that will affect your treatment?: Yes")
                f.write(z)
            elif val38 == 2:
                f.write("Do you have any religious/cultural views that will affect your treatment?: No")
                f.write(z)
            else:
                pass

            if val46 == "":
                pass
            else:
                in12 = "Additional Comment: " + val46
                f.write(in12)
                f.write(z)

            if val47 == "":
                pass
            else:
                in13 = "Fever: " + val47
                f.write(in13)
                f.write(z)

            if val48 == "":
                pass
            else:
                in14 = "Blood pressure: " + val48
                f.write(in14)
                f.write(z)
            in15 = "Created by: " + doc_name
            f.write(in15)
            f.write(z)
            in16 = "Created at: " + x1
            f.write(in16)



            f.close()
            tmsg.showinfo("Message", "New file' data is saved.")
        elif no_of_reports > 1:
            name_of_new_report = "report" +str(no_of_reports - 1)
            f = open("patients/" + p_cr_n + "/reports/" + name_of_new_report + ".txt", "a")

            in0 = "Patient name: " + p_cr_n
            f.write(in0)
            f.write(z)
            if val1 == "":
                pass
            else:
                inn1 = "When did the problem started: " + val1
                f.write(inn1)
                f.write(z)

            if val2 == "":
                pass
            else:
                inn2 = "Problem: " + val2
                f.write(inn2)
                f.write(z)

            f.write("Cause of current problem:")
            if val3 == "":
                pass
            else:
                f.write(val3)
                f.write(z)

            if val4 == "":
                pass
            else:
                f.write(val4)
                f.write(z)

            if val5 == "":
                pass
            else:
                f.write(val5)
                f.write(z)

            if val7 == "":
                pass
            else:
                f.write(val7)
                f.write(z)

            f.write("Date of surgery")
            f.write(z)
            if val10 == "":
                f.write("Not req.")
                f.write(z)
            else:
                f.write(val10)
                f.write(z)

            f.write("Past medical history")
            f.write(z)
            if val11 == "":
                pass
            else:
                f.write(val11)
                f.write(z)

            if val12 == "":
                pass
            else:
                f.write(val12)
                f.write(z)

            if val13 == "":
                pass
            else:
                f.write(val13)
                f.write(z)

            if val14 == "":
                pass
            else:
                f.write(val14)
                f.write(z)

            if val15 == "":
                pass
            else:
                f.write(val15)
                f.write(z)

            if val16 == "":
                pass
            else:
                f.write(val16)
                f.write(z)

            if val17 == "":
                pass
            else:
                f.write(val17)
                f.write(z)

            if val18 == "":
                pass
            else:
                f.write(val18)
                f.write(z)

            if val19 == "":
                pass
            else:
                f.write(val19)
                f.write(z)

            if val20 == "":
                pass
            else:
                f.write(val20)
                f.write(z)

            if val21 == "":
                pass
            else:
                f.write(val21)
                f.write(z)

            if val22 == "":
                pass
            else:
                f.write(val22)
                f.write(z)

            if val23 == "":
                pass
            else:
                f.write(val23)
                f.write(z)

            if val24 == "":
                pass
            else:
                f.write(val24)
                f.write(z)

            if val25 == "":
                pass
            else:
                f.write(val25)
                f.write(z)

            if val26 == "":
                pass
            else:
                f.write(val26)
                f.write(z)

            if val27 == "":
                pass
            else:
                f.write(val27)
                f.write(z)

            if val28 == "":
                pass
            else:
                f.write(val28)
                f.write(z)

            if val29 == "":
                pass
            else:
                f.write(val29)
                f.write(z)

            if val30 == "":
                pass
            else:
                f.write(val30)
                f.write(z)

            f.write("Surgeries / Hospitalizations")
            f.write(z)
            if val31 == "":
                f.write("No")
                f.write(z)
            else:
                f.write(val31)
                f.write(z)

            if val32 == "":
                pass
            else:
                inn6 = "Year: " + val32
                f.write(inn6)
                f.write(z)

            if val33 == "":
                pass
            else:
                inn7 = "Complications: " + val33
                f.write(inn7)
                f.write(z)

            f.write("list medications that you are taking.")
            f.write(z)
            if val34 == "":
                f.write("No medication")
                f.write(z)
            else:
                inn8 = "Medication(s): " + val34
                f.write(inn8)
                f.write(z)

            if val35 == "":
                pass
            else:
                inn9 = "Dose: " + val35
                f.write(inn9)
                f.write(z)

            if val36 == "":
                pass
            else:
                inn10 = "Reason of medication: " + val36
                f.write(inn10)
                f.write(z)

            if val37 == "":
                pass
            else:
                inn11 = "Allergy: " + val37
                f.write(inn11)
                f.write(z)

            if val38 == 1:
                f.write("Do you have any religious/cultural views that will affect your treatment?: Yes")
                f.write(z)
            elif val38 == 2:
                f.write("Do you have any religious/cultural views that will affect your treatment?: No")
                f.write(z)
            else:
                pass

            if val46 == "":
                pass
            else:
                inn12 = "Additional Comment: " + val46
                f.write(inn12)
                f.write(z)

            if val47 == "":
                pass
            else:
                inn13 = "Fever: " + val47
                f.write(inn13)
                f.write(z)

            if val48 == "":
                pass
            else:
                inn14 = "Blood pressure: " + val48
                f.write(inn14)
                f.write(z)
            inn15 = "Created by: " + doc_name
            f.write(inn15)
            f.write(z)
            inn16 = "Created at: " + x1
            f.write(inn16)

            f.close()
            tmsg.showinfo("Message", "New Report with number: " + str(no_of_reports) + "'s data is saved.")
        else:
            tmsg.showinfo("Message", "Cant create file.")

        save_repo_btn.configure(state=DISABLED)
        create_repo_btn.configure(state=NORMAL)
        user_r_entry.delete(0, END)
        dop_entry.delete(0, END)
        desc_problem_entry.delete(0, END)
        car_ck.deselect()
        work_ck.deselect()
        gradual_ck.deselect()
        other_entry.delete(0, END)
        ck1.deselect()
        ck2.deselect()
        ck3.deselect()
        ck4.deselect()
        ck5.deselect()
        ck6.deselect()
        ck7.deselect()
        ck8.deselect()
        ck9.deselect()
        ck10.deselect()
        ck11.deselect()
        ck12.deselect()
        ck13.deselect()
        ck14.deselect()
        ck15.deselect()
        ck16.deselect()
        ck17.deselect()
        ck18.deselect()
        ck19.deselect()
        ck20.deselect()
        nosurgery_entry.delete(0, END)
        yes_entry.delete(0, END)
        nosurgery_entry1.delete(0, END)
        nosurgery_entry2.delete(0, END)
        nomedicatoin_entry.delete(0, END)
        nomedicatoin_entry1.delete(0, END)
        nomedicatoin_entry2.delete(0, END)
        q1yes_ck11.deselect()
        q1no_ck11.deselect()
        allergy_entry.delete(0, END)
        noac11_entry2.delete(0, END)
        fever_entry2.delete(0, END)
        bp_entry2.delete(0, END)

    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()
    var4 = StringVar()
    var5 = StringVar()
    var7 = StringVar()
    var10 = StringVar()
    var11 = StringVar()
    var12 = StringVar()
    var13 = StringVar()
    var14 = StringVar()
    var15 = StringVar()
    var16 = StringVar()
    var17 = StringVar()
    var18 = StringVar()
    var19 = StringVar()
    var20 = StringVar()
    var21 = StringVar()
    var22 = StringVar()
    var23 = StringVar()
    var24 = StringVar()
    var25 = StringVar()
    var26 = StringVar()
    var27 = StringVar()
    var28 = StringVar()
    var29 = StringVar()
    var30 = StringVar()
    var31 = StringVar()
    var32 = StringVar()
    var33 = StringVar()
    var34 = StringVar()
    var35 = StringVar()
    var36 = StringVar()
    var37 = StringVar()
    var38 = IntVar()
    var46 = StringVar()
    var47 = StringVar()
    var48 = StringVar()

    p_cr_name = StringVar()
    user_r_entry_lbl = Label(create_report_frame, text="Patient name: ", bg="#1c478b", fg="#ffffff", font=("Halvetica", 12, "bold")).place(x = 20, y = 55)
    user_r_entry = Entry(create_report_frame, textvariable=p_cr_name, fg="#1c478b", relief=RIDGE, font=("Halvetica", 10, "bold"))
    user_r_entry.place(x = 210, y = 55)
    search_r_btn = Button(create_report_frame, text="Search", command=enable_form, bg="#1f7dad", width=10, fg="#ffffff", font=("Halvetica", 10, "bold"))
    search_r_btn.place(x = 400, y = 55)

    dop_entry_lbl = Label(create_report_frame,state=DISABLED ,  text="When did your problem start:  ", bg="#1c478b", fg="#ffffff", font=("Halvetica", 12, "bold"))
    dop_entry_lbl.place(x=530, y=55)
    dop_entry = Entry(create_report_frame,state=DISABLED , textvariable= var1 , fg="#1c478b", relief=RIDGE, font=("Halvetica", 10, "bold"))
    dop_entry.place(x=810, y=55)
    desc_problem_entry_lbl = Label(create_report_frame,state=DISABLED ,  text="Describe problem:  ", bg="#1c478b", fg="#ffffff", font=("Halvetica", 12, "bold"))
    desc_problem_entry_lbl.place(x=20, y=90)
    desc_problem_entry = Entry(create_report_frame,state=DISABLED , textvariable= var2 , width = 105 ,fg="#1c478b", relief=RIDGE, font=("Halvetica", 10, "bold"))
    desc_problem_entry.place(x=210, y=90)
    cs_ofcurrent_p_lbl = Label(create_report_frame,state=DISABLED ,  text="Cause of current problem:  ", bg="#1c478b", fg="#ffffff", font=("Halvetica", 12, "bold"))
    cs_ofcurrent_p_lbl.place(x=20, y=130)


    car_ck = Checkbutton(create_report_frame,state=DISABLED , variable= var3 ,offvalue="", onvalue= "Car accident", text="Car accident", bg="#1c478b", fg="red", font=("Halvetica", 12, "bold"))
    car_ck.place(x=230, y=130)
    work_ck = Checkbutton(create_report_frame,state=DISABLED , variable= var4,offvalue="", onvalue= "Work incident",  text="Work incident", bg="#1c478b", fg="red", font=("Halvetica", 12, "bold"))
    work_ck.place(x=370, y=130)
    gradual_ck = Checkbutton(create_report_frame,state=DISABLED , variable= var5,offvalue="", onvalue= "Gradual onset",   text="Gradual onset" , bg="#1c478b", fg="red", font=("Halvetica", 12, "bold"))
    gradual_ck.place(x=510, y=130)
    def otherinci():
        car_ck.deselect()
        work_ck.deselect()
        gradual_ck.deselect()
        car_ck.configure(state=DISABLED)
        work_ck.configure(state=DISABLED)
        gradual_ck.configure(state=DISABLED)
        other_entry.configure(state=NORMAL)

    other_ck = Button(create_report_frame,state=DISABLED , command=otherinci ,text="Other", bg="#1c478b", fg="red", font=("Halvetica", 9, "bold"))
    other_ck.place(x=660, y=130)
    other_entry = Entry(create_report_frame,state=DISABLED , textvariable= var7, fg="#1c478b", relief=RIDGE, font=("Halvetica", 10, "bold"))
    other_entry.place(x=760, y=130)
    req_surgery_lbl = Label(create_report_frame,state=DISABLED ,  text="Did this problem required surgery:  ", bg="#1c478b", fg="#ffffff", font=("Halvetica", 12, "bold"))
    req_surgery_lbl.place(x=20, y=160)

    def enable_surgryreq():
        yes_entry.configure(state=NORMAL)
        no_ck.configure(state=DISABLED)
        yes_ck.configure(state=NORMAL)

    def disbale_surgryreq():
        yes_entry.configure(state=DISABLED)
        no_ck.configure(state=NORMAL)
        yes_ck.configure(state=DISABLED)


    no_ck = Button(create_report_frame,state=DISABLED , command=enable_surgryreq , text="Yes", bg="#1c478b", fg="red",font=("Halvetica", 9, "bold"))
    no_ck.place(x=310, y=160)
    yes_ck = Button(create_report_frame,state=DISABLED , command=disbale_surgryreq , text="No", bg="#1c478b", fg="red", font=("Halvetica", 9, "bold"))
    yes_ck.place(x=380, y=160)

    d_surgery_lbl = Label(create_report_frame,state=DISABLED ,  text="Date of surgery:  ", bg="#1c478b", fg="#ffffff", font=("Halvetica", 12, "bold"))
    d_surgery_lbl.place(x=510, y=160)
    yes_entry = Entry(create_report_frame,state=DISABLED , textvariable=var10 , fg="#1c478b", relief=RIDGE, font=("Halvetica", 10, "bold"))
    yes_entry.place(x=680, y=160)
    past_medical_lbl = Label(create_report_frame,state=DISABLED ,  text="Past Medical History", bg="#1c478b", fg="#ffffff", font=("Halvetica", 12, "bold"))
    past_medical_lbl.place(x=20, y=190)
    past_medical_lbl2 = Label(create_report_frame,state=DISABLED ,  text="Do you have a history of the following problems?", bg="#1c478b", fg="#ffffff", font=("Halvetica", 12, "bold"))
    past_medical_lbl2.place(x=200, y=190)
    ck1 = Checkbutton(create_report_frame,state=DISABLED ,variable= var11,offvalue="", onvalue= "Breathing problems", text="Breathing problems", bg="#1c478b", fg="red", font=("Halvetica", 12, "bold"))
    ck1.place(x=40, y=220)
    ck2 = Checkbutton(create_report_frame,state=DISABLED ,variable= var12,offvalue="", onvalue= "Pregnant", text="Pregnant", bg="#1c478b", fg="red", font=("Halvetica", 12, "bold"))
    ck2.place(x=40, y=250)
    ck3 = Checkbutton(create_report_frame,state=DISABLED ,variable= var13,offvalue="", onvalue= "Heart problem", text="Heart problem", bg="#1c478b", fg="red", font=("Halvetica", 12, "bold"))
    ck3.place(x=40, y=280)
    ck4 = Checkbutton(create_report_frame,state=DISABLED ,variable= var14,offvalue="", onvalue= "Current wound/Skin problem", text="Current wound/Skin problem", bg="#1c478b", fg="red", font=("Halvetica", 12, "bold"))
    ck4.place(x=40, y=310)
    ck5 = Checkbutton(create_report_frame,state=DISABLED ,variable= var15,offvalue="", onvalue= "Pace maker", text="Pace maker", bg="#1c478b", fg="red", font=("Halvetica", 12, "bold"))
    ck5.place(x=40, y=340)
    ck6 = Checkbutton(create_report_frame,state=DISABLED ,variable= var16,offvalue="", onvalue= "Stroke", text="Stroke", bg="#1c478b", fg="red", font=("Halvetica", 12, "bold"))
    ck6.place(x=300, y=220)
    ck7 = Checkbutton(create_report_frame,state=DISABLED ,variable= var17,offvalue="", onvalue= "Bone/Joint problem", text="Bone/Joint problem", bg="#1c478b", fg="red", font=("Halvetica", 12, "bold"))
    ck7.place(x=300, y=250)
    ck8 = Checkbutton(create_report_frame,state=DISABLED ,variable= var18,offvalue="", onvalue= "Kidney problem", text="Kidney problem", bg="#1c478b", fg="red", font=("Halvetica", 12, "bold"))
    ck8.place(x=300, y=280)
    ck9 = Checkbutton(create_report_frame,state=DISABLED ,variable= var19,offvalue="", onvalue= "Gallbaldder/Liver", text="Gallbaldder/Liver", bg="#1c478b", fg="red", font=("Halvetica", 12, "bold"))
    ck9.place(x=300, y=310)
    ck10 = Checkbutton(create_report_frame,state=DISABLED ,variable= var20,offvalue="", onvalue= "Electical Implants", text="Electical Implants", bg="#1c478b", fg="red", font=("Halvetica", 12, "bold"))
    ck10.place(x=300, y=340)
    ck11 = Checkbutton(create_report_frame,state=DISABLED ,variable= var21,offvalue="", onvalue= "Tumor/Cancer", text="Tumor/Cancer", bg="#1c478b", fg="red", font=("Halvetica", 12, "bold"))
    ck11.place(x=500, y=220)
    ck12 = Checkbutton(create_report_frame,state=DISABLED ,variable= var22,offvalue="", onvalue= "Depression", text="Depression", bg="#1c478b", fg="red", font=("Halvetica", 12, "bold"))
    ck12.place(x=500, y=250)
    ck13 = Checkbutton(create_report_frame,state=DISABLED ,variable= var23,offvalue="", onvalue= "Bowel/Bladder",   text="Bowel/Bladder", bg="#1c478b", fg="red", font=("Halvetica", 12, "bold"))
    ck13.place(x=500, y=280)
    ck14 = Checkbutton(create_report_frame,state=DISABLED ,variable= var24,offvalue="", onvalue= "History of heavy alcohol use",   text="History of heavy alcohol use", bg="#1c478b", fg="red", font=("Halvetica", 12, "bold"))
    ck14.place(x=500, y=310)
    ck15 = Checkbutton(create_report_frame,state=DISABLED ,variable= var25,offvalue="", onvalue= "Drug use",   text="Drug use", bg="#1c478b", fg="red", font=("Halvetica", 12, "bold"))
    ck15.place(x=500, y=340)
    ck16 = Checkbutton(create_report_frame,state=DISABLED ,variable= var26,offvalue="", onvalue= "Diabetes",   text="Diabetes", bg="#1c478b", fg="red", font=("Halvetica", 12, "bold"))
    ck16.place(x= 780, y=220)
    ck17 = Checkbutton(create_report_frame,state=DISABLED ,variable= var27,offvalue="", onvalue= "Smoking",   text="Smoking", bg="#1c478b", fg="red", font=("Halvetica", 12, "bold"))
    ck17.place(x= 780, y=250)
    ck18 = Checkbutton(create_report_frame,state=DISABLED ,variable= var28,offvalue="", onvalue= "Headaches",   text="Headaches", bg="#1c478b", fg="red", font=("Halvetica", 12, "bold"))
    ck18.place(x= 780, y=280)
    ck19 = Checkbutton(create_report_frame,state=DISABLED ,variable= var29,offvalue="", onvalue= "Anxiety attacks",   text="Anxiety attacks", bg="#1c478b", fg="red", font=("Halvetica", 12, "bold"))
    ck19.place(x= 780, y=310)
    ck20 = Checkbutton(create_report_frame,state=DISABLED ,variable= var30,offvalue="", onvalue= "Sleep Apnea",   text="Sleep Apnea", bg="#1c478b", fg="red", font=("Halvetica", 12, "bold"))
    ck20.place(x= 780, y=340)

    def nosurgery():
        nosurgery_entry.configure(state=DISABLED)
        nosurgery_entry1.configure(state=DISABLED)
        nosurgery_entry2.configure(state=DISABLED)

    nosurgery_btn = Button(create_report_frame,state=DISABLED ,command = nosurgery , text="No surgery", bg="#1f7dad", width=10, fg="#ffffff", font=("Halvetica", 10, "bold"))
    nosurgery_btn.place(x=875, y=370)
    nosurgery_lbl1 = Label(create_report_frame,state=DISABLED ,  text="Surgeries/Hospitalizations", bg="#1c478b", fg="#ffffff", font=("Halvetica", 12, "bold"))
    nosurgery_lbl1.place(x=20, y=380)
    nosurgery_entry = Entry(create_report_frame,state=DISABLED ,textvariable= var31,  fg="#1c478b", relief=RIDGE, font=("Halvetica", 10, "bold"))
    nosurgery_entry.place(x=230, y=380)
    nosurgery_lbl2 = Label(create_report_frame,state=DISABLED ,  text="Year", bg="#1c478b", fg="#ffffff", font=("Halvetica", 12, "bold"))
    nosurgery_lbl2.place(x=390, y=380)
    nosurgery_entry1 = Entry(create_report_frame,state=DISABLED ,textvariable= var32,  fg="#1c478b", relief=RIDGE, font=("Halvetica", 10, "bold"))
    nosurgery_entry1.place(x=435, y=380)
    nosurgery_lbl3 = Label(create_report_frame,state=DISABLED ,  text="Complications", bg="#1c478b", fg="#ffffff", font=("Halvetica", 12, "bold"))
    nosurgery_lbl3.place(x=600, y=380)
    nosurgery_entry2 = Entry(create_report_frame,state=DISABLED ,textvariable= var33,  fg="#1c478b", relief=RIDGE, font=("Halvetica", 10, "bold"))
    nosurgery_entry2.place(x=715, y=380)

    def nomedi():
        nomedicatoin_entry.configure(state=DISABLED)
        nomedicatoin_entry1.configure(state=DISABLED)
        nomedicatoin_entry2.configure(state=DISABLED)

    nomedication_btn = Button(create_report_frame,state=DISABLED ,command=nomedi , text="No Medication", padx=4 , bg="#1f7dad", width=10, fg="#ffffff", font=("Halvetica", 10, "bold"))
    nomedication_btn.place(x=875, y=410)
    nomedication_lbl = Label(create_report_frame,state=DISABLED ,  text="Medications", bg="#1c478b", fg="#ffffff", font=("Halvetica", 12, "bold"))
    nomedication_lbl.place(x=20, y=410)
    nomedication_lbl0 = Label(create_report_frame,state=DISABLED ,  text="Please list medications that you are taking.", bg="#1c478b", fg="#ffffff", font=("Halvetica", 12, "bold"))
    nomedication_lbl0.place(x=160, y=410)
    nomedication_lbl1 = Label(create_report_frame,state=DISABLED ,  text="Medication(s)", bg="#1c478b", fg="#ffffff", font=("Halvetica", 12, "bold"))
    nomedication_lbl1.place(x=20, y=435)
    nomedicatoin_entry = Entry(create_report_frame,state=DISABLED ,textvariable= var34,  fg="#1c478b", relief=RIDGE, font=("Halvetica", 10, "bold"))
    nomedicatoin_entry.place( x=150, y=435)
    nomedication_lbl2 = Label(create_report_frame,state=DISABLED ,  text="Dose", bg="#1c478b", fg="#ffffff", font=("Halvetica", 12, "bold"))
    nomedication_lbl2.place(x=310, y=435)
    nomedicatoin_entry1 = Entry(create_report_frame,state=DISABLED ,textvariable= var35,  fg="#1c478b", relief=RIDGE, font=("Halvetica", 10, "bold"))
    nomedicatoin_entry1.place( x=375, y=435)
    nomedication_lbl3 = Label(create_report_frame,state=DISABLED ,  text="Reason for medication", bg="#1c478b", fg="#ffffff", font=("Halvetica", 12, "bold"))
    nomedication_lbl3.place(x=535, y=435)
    nomedicatoin_entry2 = Entry(create_report_frame,state=DISABLED ,textvariable= var36,  fg="#1c478b", relief=RIDGE, font=("Halvetica", 10, "bold"))
    nomedicatoin_entry2.place( x=715, y=435)

    allergy_lbl0 = Label(create_report_frame,state=DISABLED ,  text="Allergies", bg="#1c478b", fg="#ffffff", font=("Halvetica", 12, "bold"))
    allergy_lbl0.place(x=20, y=470)
    allergy_entry = Entry(create_report_frame,state=DISABLED ,textvariable= var37, width=20 ,fg="#1c478b", relief=RIDGE, font=("Halvetica", 10, "bold"))
    allergy_entry.place(x=100, y=470)

    q1_lbl2 = Label(create_report_frame,state=DISABLED ,  text="Do you have any religious/cultural views that will affect your treatment?", bg="#1c478b", fg="#ffffff", font=("Halvetica", 12, "bold"))
    q1_lbl2.place(x=10, y=530)

    q1yes_ck11 = Radiobutton(create_report_frame,state=DISABLED,variable=var38 ,value= 1,text="Yes", bg="#1c478b", fg="red", font=("Halvetica", 9, "bold"))
    q1yes_ck11.place(x=590, y=530)
    q1no_ck11 = Radiobutton(create_report_frame,state=DISABLED,variable=var38 ,value= 2 ,text="No", bg="#1c478b", fg="red", font=("Halvetica", 9, "bold"))
    q1no_ck11.place(x=680, y=530)

    notype_lbl30 = Label(create_report_frame,state=DISABLED ,  text="Additional comment", bg="#1c478b", fg="#ffffff", font=("Halvetica", 12, "bold"))
    notype_lbl30.place(x=10, y=560)
    noac11_entry2 = Entry(create_report_frame,state=DISABLED , textvariable= var46 ,  fg="#1c478b", relief=RIDGE, font=("Halvetica", 10, "bold"))
    noac11_entry2.place(x=170, y=560)

    notype_lbl31 = Label(create_report_frame,state=DISABLED ,  text="Fever", bg="#1c478b", fg="#ffffff", font=("Halvetica", 12, "bold"))
    notype_lbl31.place(x=340, y=560)

    fever_entry2 = Entry(create_report_frame,state=DISABLED , textvariable= var47 ,  fg="#1c478b", relief=RIDGE, font=("Halvetica", 10, "bold"))
    fever_entry2.place(x=390, y=560)

    notype_lbl32 = Label(create_report_frame,state=DISABLED ,  text="Blood pressure", bg="#1c478b", fg="#ffffff", font=("Halvetica", 12, "bold"))
    notype_lbl32.place(x=580, y=560)
    bp_entry2 = Entry(create_report_frame,state=DISABLED , textvariable= var48 ,  fg="#1c478b", relief=RIDGE, font=("Halvetica", 10, "bold"))
    bp_entry2.place(x=715, y=560)

    create_repo_btn = Button(create_report_frame,state=DISABLED , command= create_first, text="Create", bg="green", width=10, fg="#ffffff", font=("Halvetica", 15, "bold"))
    create_repo_btn.place(x=250, y=600)

    save_repo_btn = Button(create_report_frame, state=DISABLED, command=file_c, text="Save data", bg="green",  width=10, fg="#ffffff", font=("Halvetica", 15, "bold"))
    save_repo_btn.place(x=500, y=600)


    #----------------------------------------------------Patient report frame-----------------------------------------------

    report_frame = Frame(doctor_root, bg="#1c478b")

    patient_report_lbl = Label(report_frame, text="Patient Report", bg="#1f7dad", fg="#ffffff", font=("Comic Sans Ms", 20, "bold"), pady=2)
    patient_report_lbl.pack(pady=20, fill=X)

    def search_report():
        patient_name = p_r_name.get()
        if os.path.exists("patients/" + patient_name):
            no_of_repors = len(os.listdir("patients/" + patient_name + "/reports/"))
            patient_report_details_listbo.insert(0, "Total reports: " + str(no_of_repors))
            rp = os.listdir("patients/" + patient_name + "/reports/")
            for mn in range(no_of_repors):
                num = mn + 1
                patient_report_details_listbo.insert(num, str(rp[mn]))

        else:
            tmsg.showerror("Error" , "Patient found")


    def rpo_func(event):
        cs = patient_report_details_listbo.curselection()
        file_name = patient_report_details_listbo.get(cs)
        print(file_name)
        rproot = Tk()
        rproot.geometry("1366x768")
        rproot.minsize(1365, 767)
        rproot.maxsize(1368, 769)
        rproot.configure(bg="#1c478b")
        rproot.title(file_name)




        head1 = Label(rproot, text="Krishna Hospital", bg="#1c478b", fg="#ffffff", pady=5 , font=("Halvetica", 20, "bold")).pack(fill = X)
        head2 = Label(rproot, text="Vrindavana, Uttar Pradesh 281121, India", bg="#1c478b", fg="#ffffff", font=("Halvetica", 15, "bold")).pack(fill=X)
        head2 = Label(rproot, text="Ph No.: 011101111, gmail: radhekrishna@gmail.com", bg="#1c478b", fg="#ffffff",font=("Halvetica", 11, "bold")).pack(fill=X)
        list_r_scrollbar44 = Scrollbar(report_frame)
        list_r_scrollbar44.pack(side=RIGHT, fill=Y)
        list_r_scrollbar22 = Scrollbar(report_frame, orient=HORIZONTAL)
        list_r_scrollbar22.pack(side=BOTTOM, fill=X)
        patient_report_details_listbo11 = Listbox(rproot, xscrollcommand=list_r_scrollbar22.set,yscrollcommand=list_r_scrollbar44.set, fg="#ffffff", bg="grey", width=100, height=40, font=("Comic Sans Ms", 15, "bold"))
        patient_report_details_listbo11.pack(pady=5)
        list_r_scrollbar44.configure(command=patient_report_details_listbo11.yview)
        list_r_scrollbar22.configure(command=patient_report_details_listbo11.xview)
        patient_name2 = p_r_name.get()
        f = open("patients/" + patient_name2 + "/reports/" + file_name, "r")
        no_of_line = len(f.readlines())
        f.close()
        f = open("patients/" + patient_name2 + "/reports/" + file_name, "r")
        for ii in range(no_of_line):
            ff = f.readline()
            patient_report_details_listbo11.insert(ii, "    " + ff)
        f.close()
        rproot.mainloop()


    p_r_name = StringVar()
    user_r_entry_lbl = Label(report_frame, text="Patient name: ", bg="#1c478b", fg="#ffffff", font=("Halvetica", 14, "bold")).pack()
    user_r_entry = Entry(report_frame, textvariable=p_r_name, fg="#1c478b", relief=RIDGE, font=("Halvetica", 16, "bold"))
    user_r_entry.pack()

    search_r_btn = Button(report_frame, text="Search", command= search_report, bg="#1f7dad", width=10, fg="#ffffff", font=("Halvetica", 10, "bold"))
    search_r_btn.pack(pady=5)

    list_r_scrollbar = Scrollbar(report_frame)
    list_r_scrollbar.pack(side=RIGHT, fill=Y)
    list_r_scrollbar2 = Scrollbar(report_frame, orient=HORIZONTAL)
    list_r_scrollbar2.pack(side=BOTTOM, fill=X)
    item = StringVar()
    patient_report_details_listbo = Listbox(report_frame, listvariable=item , xscrollcommand=list_r_scrollbar2.set ,yscrollcommand=list_r_scrollbar.set, fg="#ffffff", bg="grey", width=100, height=40, font=("Comic Sans Ms", 15, "bold"))
    patient_report_details_listbo.bind('<Double-1 >' , rpo_func)
    patient_report_details_listbo.pack(pady=5)
    list_r_scrollbar.configure(command=patient_details_listbo.yview)
    list_r_scrollbar2.configure(command=patient_details_listbo.xview)

#_--------------------------------------------------Appointment frame---------------------------------------------------
    appointment_frame = Frame(doctor_root, bg="#1c478b")

    def search_p():
        namem = pat_name.get()
        if namem == "":
            tmsg.showerror("Error", "Enter patient name first.")
        else:
            if os.path.exists("patients/" + namem):
                f = open("patients/" + namem + "/appointment letter.txt")
                no_line_A = len(f.readlines())
                f.close()
                more_appt.configure(state = NORMAL)
                end_treatment.configure(state = NORMAL)
                if no_line_A == 0:
                    tmsg.showinfo("Message", "No previous appointment")
                else:
                    f = open("patients/" + namem + "/appointment letter.txt")
                    for rpeat in range(no_line_A):
                        ln = f.readline()
                        lb.insert(rpeat, "  " +str(rpeat + 1)+ ". " + ln)
                    f.close
                    search_a_btn1.configure(state= DISABLED)
            else:
                tmsg.showerror("Error", "Patient didn't found")

    pat_name = StringVar()
    patient_appointment_lbl = Label(appointment_frame, text="Patient Appointments", bg="#1f7dad", fg="#ffffff", font=("Comic Sans Ms", 20, "bold"), pady=2).pack(pady=20, fill = X)
    user_a_entry_lbl1 = Label(appointment_frame, text="Patient name: ", bg="#1c478b", fg="#ffffff", font=("Halvetica", 14, "bold")).pack()
    user_a_entry1 = Entry(appointment_frame, textvariable=pat_name, fg="#1c478b", relief=RIDGE, font=("Halvetica", 16, "bold"))
    user_a_entry1.pack()
    search_a_btn1 = Button(appointment_frame, state= NORMAL ,text="Search", command= search_p, bg="#1f7dad", width=10, fg="#ffffff", font=("Halvetica", 10, "bold"))
    search_a_btn1.pack(pady=5)
    list_frame = Frame(appointment_frame, bg="#1c478b")
    lbsbx = Scrollbar(list_frame, orient=HORIZONTAL)
    lbsbx.pack(side = BOTTOM, fill=X)
    lbsby = Scrollbar(list_frame)
    lbsby.pack(side=RIGHT, fill=Y)
    lb = Listbox(list_frame, xscrollcommand=lbsbx.set ,yscrollcommand=lbsby.set, fg="#ffffff", bg="grey", width=85, height=10, font=("Comic Sans Ms", 15, "bold"))
    lb.pack()
    lbsbx.configure(command=lb.xview)
    lbsby.configure(command=lb.yview)
    list_frame.pack()

    other_frame = Frame(appointment_frame, bg="#1c478b")

    def next_app():
        date_lbl.place(x=20, y=10)
        date_entry.place(x=20, y=40)
        comment_lbl.place(x=150, y=10)
        comment_entry.place(x=150, y=40)
        sve_btn.place(x=390, y=37)
        more_appt.configure(state=DISABLED)

    def saving_date():
        dinak = date_app.get()
        vakya = comment_app.get()
        file_loc = pat_name.get()
        if vakya == "" and dinak =="":
            tmsg.showerror("Error",  "Please enter something")
        else:
            f = open("patients/" + file_loc + "/appointment letter.txt", "a")
            likho = dinak + ": " + vakya
            f.write(likho)
            f.write("\n")
            f.close()
            date_lbl.forget()
            date_entry.delete(0, END)
            comment_lbl.forget()
            comment_entry.delete(0, END)
            sve_btn.forget()
            more_appt.configure(state=NORMAL)
            lb.delete(0, END)
            search_a_btn1.configure(state=NORMAL)

    def end_treat():
        file_loc = pat_name.get()
        endq = tmsg.askyesno("Question", "Do you want to end the treatment")
        if endq == True:
            f = open("patients/" + file_loc + "/appointment letter.txt", "a")
            f.write(str(z1))
            f.write("\n")
            f.write("Treatment ended")
            f.close()
            more_appt.configure(state=NORMAL)
            lb.delete(0, END)
            search_a_btn1.configure(state=NORMAL)
            tmsg.showinfo("Message", "Treatment is ended")
        else:
            pass

    date_app = StringVar()
    comment_app = StringVar()
    date_lbl = Label(other_frame, text= "Date: ",bg="#1c478b", fg="#ffffff", font=("Halvetica", 17, "bold"))
    date_entry = Entry(other_frame, textvariable=date_app, width = 10 ,fg="#1c478b", relief=RIDGE, font=("Halvetica", 16, "bold"))
    comment_lbl = Label(other_frame, text="comment:", bg="#1c478b", fg="#ffffff", font=("Halvetica", 17, "bold"))
    comment_entry = Entry(other_frame, textvariable=comment_app, fg="#1c478b", relief=RIDGE, font=("Halvetica", 16, "bold"))
    sve_btn = Button(other_frame, command=saving_date , text="Save",bg="#1f7dad", width=10, fg="#ffffff", font=("Halvetica", 14, "bold"))
    lbl = Label(other_frame, text="", bg="#1c478b").pack(pady=15)
    more_appt = Button(other_frame, state=DISABLED ,text="Next appointment", command=next_app , bg="green", width=20, fg="#ffffff", font=("Halvetica", 15, "bold"))
    more_appt.pack(side=LEFT)
    end_treatment = Button(other_frame, state=DISABLED ,text="End Treatment", command = end_treat , bg="red", width=20, fg="#ffffff", font=("Halvetica", 15, "bold"))
    end_treatment.pack(side=LEFT)
    lbl= Label(other_frame, text = "",  bg="#1c478b").pack(pady=100)
    other_frame.pack()

#-----------------------------------------------Medicine frame----------------------------------------------------------
    medicine_frame = Frame(doctor_root, bg="#1c478b")

    def search_p_for_m():
        md_name = pat_name_for_md.get()
        if os.path.exists("patients/" + md_name):
            medicine_form_frame.pack(fill=BOTH, pady=10)
            med_sv_btn.pack()
            empty_lbl2.pack(pady=90)
            search_m_btn1.configure(state=DISABLED)

        else:
            tmsg.showerror("Error", "No patient found with that name.")

    def saving_medicine():
        md_name1 = pat_name_for_md.get()
        num_of_med_bill = len(os.listdir("patients/" + md_name1 + "/medician"))

        value1_m1 = md1.get()
        value1_m5 = md2.get()
        value1_m9 = md3.get()
        value1_m13   = md4.get()
        value1_m17  = md5.get()
        value1_m21  = md6.get()
        value1_m25  = md7.get()
        value1_m29  = md8.get()
        value1_m33   = md9.get()
        value1_m37 = md10.get()
        value1_m41   = md11.get()
        value1_m45 = md12.get()

        if value1_m1 == "" and value1_m5 == "" and value1_m9 =="" and value1_m13 =="" and    value1_m17 =="" and   value1_m21 =="" and   value1_m25 =="" and   value1_m29 =="" and   value1_m33 =="" and  value1_m37 =="" and  value1_m41 =="" and   value1_m45 =="":
            tmsg.showerror("Error", "Please enter some medicines")
        else:
            if num_of_med_bill == 0:
                f = open("patients/" + md_name1 + "/medician/" + "medicine" + str(0) + ".txt", "x")
                f.close()
                file_to_save1 = "patients/" + md_name1 + "/medician/" + "medicine" + str(0) + ".txt"
                saving_bill(file_to_save1)
            else:
                f = open("patients/" + md_name1 + "/medician/" + "medicine" + str(num_of_med_bill) + ".txt", "x")
                f.close()
                file_to_save2 = "patients/" + md_name1 + "/medician/" + "medicine" + str(num_of_med_bill) + ".txt"
                saving_bill(file_to_save2)

    def saving_bill(loca):
        value_m1 = md1.get()
        value_m2 = d1.get()
        value_m3 = wt1.get()
        value_m4 = ht1.get()

        value_m5 = md2.get()
        value_m6 = d2.get()
        value_m7 = wt2.get()
        value_m8 = ht2.get()

        value_m9 = md3.get()
        value_m10 = d3.get()
        value_m11 = wt3.get()
        value_m12 = ht3.get()

        value_m13 = md4.get()
        value_m14 = d4.get()
        value_m15 = wt4.get()
        value_m16 = ht4.get()

        value_m17 = md5.get()
        value_m18 = d5.get()
        value_m19 = wt5.get()
        value_m20 = ht5.get()

        value_m21 = md6.get()
        value_m22 = d6.get()
        value_m23 = wt6.get()
        value_m24 = ht6.get()

        value_m25 = md7.get()
        value_m26 = d7.get()
        value_m27 = wt7.get()
        value_m28 = ht7.get()

        value_m29 = md8.get()
        value_m30 = d8.get()
        value_m31 = wt8.get()
        value_m32 = ht8.get()

        value_m33 = md9.get()
        value_m34 = d9.get()
        value_m35 = wt9.get()
        value_m36 = ht9.get()

        value_m37 = md10.get()
        value_m38 = d10.get()
        value_m39 = wt10.get()
        value_m40 = ht10.get()

        value_m41 = md11.get()
        value_m42 = d11.get()
        value_m43 = wt11.get()
        value_m44 = ht11.get()

        value_m45 = md12.get()
        value_m46 = d12.get()
        value_m47 = wt12.get()
        value_m48 = ht12.get()

        if value_m1 == "" and value_m5 == "" and value_m9 =="" and value_m13 =="" and    value_m17 =="" and   value_m21 =="" and   value_m25 =="" and   value_m29 =="" and   value_m33 =="" and  value_m37 =="" and  value_m41 =="" and   value_m45 =="":
            tmsg.showerror("Error", "Please enter some medicines")
        else:
            f = open(loca, "a")
            f.write(str(z1))
            f.write("\n")
            if value_m1 == "":
                pass
            else:
                st1 = "     " + value_m1 + "            " + value_m2 + "            " + value_m3 + "            " + value_m4
                f.write(st1)
                f.write("\n")

            if value_m5 == "":
                pass
            else:
                st2 = "     " + value_m5 + "            " + value_m6 + "            " + value_m7 + "            " + value_m8
                f.write(st2)
                f.write("\n")

            if value_m9 == "":
                pass
            else:
                st3 = "     " + value_m9 + "            " + value_m10 +"            " + value_m11 + "            " + value_m12
                f.write(st3)
                f.write("\n")

            if value_m13 == "":
                pass
            else:
                st4 = "     " + value_m13 + "            " + value_m14 + "            " + value_m15 + "            " + value_m16
                f.write(st4)
                f.write("\n")

            if value_m17 == "":
                pass
            else:
                st5 = "     " + value_m17 + "            " + value_m18 +"            " + value_m19 + "            " + value_m20
                f.write(st5)
                f.write("\n")

            if value_m21 == "":
                pass
            else:
                st6 = "     " + value_m21 + "            " + value_m22 +"            " + value_m23 + "            " + value_m24
                f.write(st6)
                f.write("\n")

            if value_m25 == "":
                pass
            else:
                st7 = "     " + value_m25 + "            " + value_m26 +"            " + value_m27 + "            " + value_m28
                f.write(st7)
                f.write("\n")

            if value_m29 == "":
                pass
            else:
                st8 = "     " + value_m29 + "            " + value_m30 +"            " + value_m31 + "            " + value_m32
                f.write(st8)
                f.write("\n")

            if value_m33 == "":
                pass
            else:
                st9 = "     " + value_m33 + "            " + value_m34 +"            " + value_m35 + "            " + value_m36
                f.write(st9)
                f.write("\n")

            if value_m37 == "":
                pass
            else:
                st10 = "     " + value_m37 + "            " + value_m38 +"            " + value_m39 + "            " + value_m40
                f.write(st10)
                f.write("\n")

            if value_m41 == "":
                pass
            else:
                st11 = "     " + value_m41 + "            " + value_m42 +"            " + value_m43 + "            " + value_m44
                f.write(st11)
                f.write("\n")

            if value_m45 == "":
                pass
            else:
                st12 = "     " + value_m45 + "            " + value_m46 +"            " + value_m47 + "            " + value_m48
                f.write(st12)
                f.write("\n")

            f.close()
            tmsg.showinfo("message", "Medicine bill is saved")
            medicine_form_frame.forget()
            med_sv_btn.pack_forget()
            empty_lbl2.forget()
            search_m_btn1.configure(state= NORMAL)
            user_m_entry1.delete(0, END)

    pat_name_for_md = StringVar()
    patient_appointment_lbl = Label(medicine_frame, text="Medicine", bg="#1f7dad", fg="#ffffff", font=("Comic Sans Ms", 20, "bold"), pady=2).pack(pady=10)
    user_m_entry_lbl1 = Label(medicine_frame , text="Patient name: ", bg="#1c478b", fg="#ffffff", font=("Halvetica", 14, "bold")).pack()
    user_m_entry1 = Entry(medicine_frame , textvariable=pat_name_for_md, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold"))
    user_m_entry1.pack()
    search_m_btn1 = Button(medicine_frame , state=NORMAL, text="Search", command=search_p_for_m, bg="#1f7dad", width=10, fg="#ffffff", font=("Halvetica", 10, "bold"))
    search_m_btn1.pack(pady=5)

    medicine_form_frame = Frame(medicine_frame, bg="#99e6ff")
    med_name_lbl = Label(medicine_form_frame, text = "Medicine name", bg="#e6ffff", fg="#111111", font=("Halvetica", 14, "bold")).pack(side = LEFT, padx = 40, anchor="n")
    dose_med_lbl = Label(medicine_form_frame, text = "Dose", bg="#e6ffff", fg="#111111", font=("Halvetica", 14, "bold")).pack(side = LEFT, padx = 100, anchor="n")
    when_taken_lbl = Label(medicine_form_frame, text = "When taken", bg="#e6ffff", fg="#111111", font=("Halvetica", 14, "bold")).pack(side = LEFT, padx = 80, anchor="n")
    how_taken = Label(medicine_form_frame, text = "Comment", bg="#e6ffff", fg="#111111", font=("Halvetica", 14, "bold")).pack(side = LEFT, padx = 100, anchor="n")
    #variables
    md1 = StringVar()
    d1 = StringVar()
    wt1 = StringVar()
    ht1 = StringVar()
    md2 = StringVar()
    d2 = StringVar()
    wt2 = StringVar()
    ht2 = StringVar()
    md3 = StringVar()
    d3 = StringVar()
    wt3 = StringVar()
    ht3 = StringVar()
    md4 = StringVar()
    d4 = StringVar()
    wt4 = StringVar()
    ht4 = StringVar()
    md5 = StringVar()
    d5 = StringVar()
    wt5 = StringVar()
    ht5 = StringVar()
    md6 = StringVar()
    d6 = StringVar()
    wt6 = StringVar()
    ht6 = StringVar()
    md7 = StringVar()
    d7 = StringVar()
    wt7 = StringVar()
    ht7 = StringVar()
    md8 = StringVar()
    d8 = StringVar()
    wt8 = StringVar()
    ht8 = StringVar()
    md9 = StringVar()
    d9 = StringVar()
    wt9 = StringVar()
    ht9 = StringVar()
    md10 = StringVar()
    d10 = StringVar()
    wt10 = StringVar()
    ht10 = StringVar()
    md11 = StringVar()
    d11 = StringVar()
    wt11 = StringVar()
    ht11 = StringVar()
    md12 = StringVar()
    d12 = StringVar()
    wt12 = StringVar()
    ht12 = StringVar()

    line1e1 = Entry(medicine_form_frame, textvariable=md1, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x = 40, y = 30)
    line1e2 = Entry(medicine_form_frame, textvariable=d1 , fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x = 270, y = 30)
    line1e3 = Entry(medicine_form_frame, textvariable=wt1, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x = 530, y = 30)
    line1e4 = Entry(medicine_form_frame, textvariable=ht1, width = 30 ,fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x = 780, y = 30)

    line2e1 = Entry(medicine_form_frame, textvariable=md2, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=40, y=60)
    line2e2 = Entry(medicine_form_frame, textvariable=d2, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=270, y=60)
    line2e3 = Entry(medicine_form_frame, textvariable=wt2, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=530, y=60)
    line2e4 = Entry(medicine_form_frame, textvariable=ht2, width=30, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=780, y=60)

    line3e1 = Entry(medicine_form_frame, textvariable=md3, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=40, y=90)
    line3e2 = Entry(medicine_form_frame, textvariable=d3, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=270, y=90)
    line3e3 = Entry(medicine_form_frame, textvariable=wt3, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=530, y=90)
    line3e4 = Entry(medicine_form_frame, textvariable=ht3, width=30, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=780, y=90)

    line4e1 = Entry(medicine_form_frame, textvariable=md4, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=40, y=120)
    line4e2 = Entry(medicine_form_frame, textvariable=d4, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=270, y=120)
    line4e3 = Entry(medicine_form_frame, textvariable=wt4, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=530, y=120)
    line4e4 = Entry(medicine_form_frame, textvariable=ht4, width=30, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=780, y=120)

    line5e1 = Entry(medicine_form_frame, textvariable=md5, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=40, y=150)
    line5e2 = Entry(medicine_form_frame, textvariable=d5, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=270, y=150)
    line5e3 = Entry(medicine_form_frame, textvariable=wt5, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=530, y=150)
    line5e4 = Entry(medicine_form_frame, textvariable=ht5, width=30, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=780, y=150)

    line6e1 = Entry(medicine_form_frame, textvariable=md6, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=40, y=180)
    line6e2 = Entry(medicine_form_frame, textvariable=d6, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=270, y=180)
    line6e3 = Entry(medicine_form_frame, textvariable=wt6, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=530, y=180)
    line6e4 = Entry(medicine_form_frame, textvariable=ht6, width=30, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=780, y=180)

    line7e1 = Entry(medicine_form_frame, textvariable=md7, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=40, y=210)
    line7e2 = Entry(medicine_form_frame, textvariable=d7, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=270, y=210)
    line7e3 = Entry(medicine_form_frame, textvariable=wt7, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=530, y=210)
    line7e4 = Entry(medicine_form_frame, textvariable=ht7, width=30, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=780, y=210)

    line8e1 = Entry(medicine_form_frame, textvariable=md8, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=40, y=240)
    line8e2 = Entry(medicine_form_frame, textvariable=d8, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=270, y=240)
    line8e3 = Entry(medicine_form_frame, textvariable=wt8, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=530, y=240)
    line8e4 = Entry(medicine_form_frame, textvariable=ht8, width=30, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=780, y=240)

    line9e1 = Entry(medicine_form_frame, textvariable=md9, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=40, y=270)
    line9e2 = Entry(medicine_form_frame, textvariable=d9, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=270, y=270)
    line9e3 = Entry(medicine_form_frame, textvariable=wt9, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=530, y=270)
    line9e4 = Entry(medicine_form_frame, textvariable=ht9, width=30, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=780, y=270)

    line10e1 = Entry(medicine_form_frame, textvariable=md10, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=40, y=300)
    line10e2 = Entry(medicine_form_frame, textvariable=d10, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=270, y=300)
    line10e3 = Entry(medicine_form_frame, textvariable=wt10, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=530, y=300)
    line10e4 = Entry(medicine_form_frame, textvariable=ht10, width=30, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=780, y=300)

    line11e1 = Entry(medicine_form_frame, textvariable=md11, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=40, y=330)
    line11e2 = Entry(medicine_form_frame, textvariable=d11, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=270, y=330)
    line11e3 = Entry(medicine_form_frame, textvariable=wt11, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=530, y=330)
    line11e4 = Entry(medicine_form_frame, textvariable=ht11, width=30, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=780, y=330)

    line12e1 = Entry(medicine_form_frame, textvariable=md12, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=40, y=360)
    line12e2 = Entry(medicine_form_frame, textvariable=d12, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=270, y=360)
    line12e3 = Entry(medicine_form_frame, textvariable=wt12, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=530, y=360)
    line12e4 = Entry(medicine_form_frame, textvariable=ht12, width=30, fg="#1c478b", relief=RIDGE, font=("Halvetica", 11, "bold")).place(x=780, y=360)

    empty_lbl = Label(medicine_form_frame, text="  ", bg="#e6ffff")
    empty_lbl.pack(pady=190)
    med_sv_btn = Button(medicine_frame,command = saving_medicine , text="Save", bg="#1f7dad", width=10, fg="#ffffff", font=("Halvetica", 15, "bold"))
    empty_lbl2 = Label(medicine_frame, text="  ", bg="#e6ffff")

    #function to call buttons
    def doc_profile():
        Myprofile_frame.pack(fill= BOTH)
        patients_frame.forget()
        report_frame.forget()
        appointment_frame.forget()
        medicine_frame.forget()
        create_report_frame.forget()

        doc_profile_btn.configure(state=DISABLED)
        doc_patient_btn.configure(state=NORMAL)
        doc_report_btn.configure(state=NORMAL)
        doc_report_create_btn.configure(state=NORMAL)
        doc_appointment_btn.configure(state=NORMAL)
        Medicines_btn.configure(state=NORMAL)

    def doc_patient():
        Myprofile_frame.forget()
        patients_frame.pack(fill= BOTH)
        report_frame.forget()
        appointment_frame.forget()
        medicine_frame.forget()
        create_report_frame.forget()

        doc_profile_btn.configure(state=NORMAL)
        doc_patient_btn.configure(state=DISABLED)
        doc_report_btn.configure(state=NORMAL)
        doc_report_create_btn.configure(state=NORMAL)
        doc_appointment_btn.configure(state=NORMAL)
        Medicines_btn.configure(state=NORMAL)

    def doc_create_report():
        Myprofile_frame.forget()
        patients_frame.forget()
        report_frame.forget()
        create_report_frame.pack(fill= BOTH)
        appointment_frame.forget()
        medicine_frame.forget()

        doc_profile_btn.configure(state=NORMAL)
        doc_patient_btn.configure(state=NORMAL)
        doc_report_btn.configure(state=NORMAL)
        doc_report_create_btn.configure(state=DISABLED)
        doc_appointment_btn.configure(state=NORMAL)
        Medicines_btn.configure(state=NORMAL)

    def doc_report():
        Myprofile_frame.forget()
        patients_frame.forget()
        report_frame.pack()
        appointment_frame.forget()
        medicine_frame.forget()
        create_report_frame.forget()

        doc_profile_btn.configure(state=NORMAL)
        doc_patient_btn.configure(state=NORMAL)
        doc_report_btn.configure(state=DISABLED)
        doc_appointment_btn.configure(state=NORMAL)
        Medicines_btn.configure(state=NORMAL)
        doc_report_create_btn.configure(state=NORMAL)

    def doc_appointment():
        Myprofile_frame.forget()
        patients_frame.forget()
        report_frame.forget()
        appointment_frame.pack(fill = BOTH)
        medicine_frame.forget()
        create_report_frame.forget()

        doc_profile_btn.configure(state=NORMAL)
        doc_patient_btn.configure(state=NORMAL)
        doc_report_btn.configure(state=NORMAL)
        doc_report_create_btn.configure(state=NORMAL)
        doc_appointment_btn.configure(state=DISABLED)
        Medicines_btn.configure(state=NORMAL)

    def Medicines():
        Myprofile_frame.forget()
        patients_frame.forget()
        report_frame.forget()
        appointment_frame.forget()
        medicine_frame.pack(fill=BOTH)
        create_report_frame.forget()

        doc_profile_btn.configure(state=NORMAL)
        doc_patient_btn.configure(state=NORMAL)
        doc_report_btn.configure(state=NORMAL)
        doc_appointment_btn.configure(state=NORMAL)
        Medicines_btn.configure(state=DISABLED)
        doc_report_create_btn.configure(state=NORMAL)

    operations_btn_frame = Frame(doctor_root, bg="#1c478b")

    empty_lbl = Label(operations_btn_frame, text="  ", bg="#1c478b").pack(pady=20)
    doc_profile_btn = Button(operations_btn_frame, text="My profile" ,command= doc_profile, width=16, fg="#1c478b", bg="#ffffff", font=("Halvetica", 20, "bold"))
    doc_profile_btn.pack(padx=10, pady=10)
    doc_patient_btn = Button(operations_btn_frame, text="Patients",command= doc_patient,  width=16, fg="#1c478b", bg="#ffffff", font=("Halvetica", 20, "bold"))
    doc_patient_btn.pack(padx=10, pady=10)
    doc_report_create_btn = Button(operations_btn_frame, text="Create report", width=16, command=doc_create_report, fg="#1c478b", bg="#ffffff", font=("Halvetica", 20, "bold"))
    doc_report_create_btn.pack(padx=10, pady=10)
    doc_report_btn = Button(operations_btn_frame, text="View Report", width=16,command= doc_report,  fg="#1c478b", bg="#ffffff", font=("Halvetica", 20, "bold"))
    doc_report_btn.pack(padx=10, pady=10)
    doc_appointment_btn = Button(operations_btn_frame, text="Appointment",command= doc_appointment,  width=16, fg="#1c478b", bg="#ffffff", font=("Halvetica", 20, "bold"))
    doc_appointment_btn.pack(padx=10, pady=10)
    Medicines_btn = Button(operations_btn_frame, text="Medicines", width=16,command= Medicines,  fg="#1c478b", bg="#ffffff", font=("Halvetica", 20, "bold"))
    Medicines_btn.pack(padx=10, pady=10)
    logout_btn = Button(operations_btn_frame, text="Log Out", command=lambda: logout(doctor_root), fg="#ffffff", width=16, bg="#f62c47", font=("Halvetica", 15, "bold"))
    logout_btn.pack(pady=5, padx=10)

    operations_btn_frame.pack(side=LEFT, anchor="w", fill=Y)


#--------------------------------------------------Logged as receptionist-----------------------------------------------
def logged_as_recieptionist(recp_name, root):
    root.destroy()
    receptioninst_root = Tk()
    receptioninst_root.geometry("1366x768")
    receptioninst_root.minsize(1365, 767)
    receptioninst_root.maxsize(1368, 769)
    receptioninst_root.configure(bg="#cececf")

    heading_frame = Frame(receptioninst_root, bg="#1f7dad")
    heading_label = Label(heading_frame, text="Welcome " + recp_name, bg="#1f7dad", fg="#ffffff",font=("Comic Sans Ms", 15, "bold"), pady=2).pack(pady=10)
    heading_frame.pack(side=TOP, anchor="n", fill=BOTH)


    rec_My_Profile_frame = Frame(receptioninst_root, bg="#1c478b")
    rec_profile_lbl = Label(rec_My_Profile_frame, text="My profile", bg="#1f7dad", fg="#ffffff", font=("Comic Sans Ms", 30, "bold"), pady=2)
    rec_profile_lbl.pack(pady=20, fill=X)

    def open_edit_tabs():
        edit_btn.configure(state=DISABLED)
        name_entry.place(x=350, y=100)
        name_change_btn.place(x=750, y=98)
        password_entry.place(x=350, y=158)
        pass_change_btn.place(x=750, y=160)
        phone_entry.place(x=350, y=340)
        phone_change_btn.place(x=750, y=338)

        name_entry.configure(state=NORMAL)
        name_change_btn.configure(state=NORMAL)
        password_entry.configure(state=NORMAL)
        pass_change_btn.configure(state=NORMAL)
        phone_entry.configure(state=NORMAL)
        phone_change_btn.configure(state=NORMAL)

    def change_name():
        name_to_change = ne.get()
        # read file
        f = open("Logins/Recieptionist/" + recp_name + ".txt", "r")
        lines11 = f.readline()
        lines12 = f.readline()
        lines13 = f.readline()
        lines14 = f.readline()
        lines15 = f.readline()
        lines16 = f.readline()
        lines17 = f.readline()
        lines18 = f.readline()
        f.close()
        f = open("Logins/Recieptionist/" + name_to_change + ".txt", "x")
        f.close()
        line101 = name_to_change + "\n"
        f = open("Logins/Recieptionist/" + name_to_change + ".txt", "a")
        f.write(line101)
        f.write(lines12)
        f.write(lines13)
        f.write(lines14)
        f.write(lines15)
        f.write(lines16)
        f.write(lines17)
        f.write(lines18)
        f.close()
        os.remove("Logins/Recieptionist/" + recp_name + ".txt")
        edit_btn.configure(state=NORMAL)
        name_entry.configure(state=DISABLED)
        name_entry.delete(0, END)
        name_change_btn.configure(state=DISABLED)
        password_entry.configure(state=DISABLED)
        pass_change_btn.configure(state=DISABLED)
        phone_entry.configure(state=DISABLED)
        phone_change_btn.configure(state=DISABLED)
        tmsg.showinfo("Message", recp_name + " Username updates, Please re-Login to use")
        logout(receptioninst_root)

    def change_pass():
        pass_to_change = pe.get()
        # read file
        f = open("Logins/Recieptionist/" + recp_name + ".txt", "r")
        lines11 = f.readline()
        lines12 = f.readline()
        lines13 = f.readline()
        lines14 = f.readline()
        lines15 = f.readline()
        lines16 = f.readline()
        lines17 = f.readline()
        lines18 = f.readline()
        f.close()
        os.remove("Logins/Recieptionist/" + recp_name + ".txt")
        f = open("Logins/Recieptionist/" + recp_name + ".txt", "x")
        f.close()
        line101 = pass_to_change + "\n"
        f = open("Logins/Recieptionist/" + recp_name + ".txt", "a")
        f.write(lines11)
        f.write(line101)
        f.write(lines13)
        f.write(lines14)
        f.write(lines15)
        f.write(lines16)
        f.write(lines17)
        f.write(lines18)
        f.close()

        edit_btn.configure(state=NORMAL)
        name_entry.configure(state=DISABLED)
        name_change_btn.configure(state=DISABLED)
        password_entry.configure(state=DISABLED)
        password_entry.delete(0, END)
        pass_change_btn.configure(state=DISABLED)
        phone_entry.configure(state=DISABLED)
        phone_change_btn.configure(state=DISABLED)

        tmsg.showinfo("Message", recp_name + " Password updated, Please re-Login to use")
        logout(receptioninst_root)

    def change_phone():
        phone_to_change = phe.get()
        # read file
        f = open("Logins/Recieptionist/" + recp_name  + ".txt", "r")
        lines11 = f.readline()
        lines12 = f.readline()
        lines13 = f.readline()
        lines14 = f.readline()
        lines15 = f.readline()
        lines16 = f.readline()
        lines17 = f.readline()
        lines18 = f.readline()
        f.close()
        os.remove("Logins/Recieptionist/" + recp_name  + ".txt")
        f = open("Logins/Recieptionist/" + recp_name + ".txt", "x")
        f.close()
        line101 = phone_to_change + "\n"
        f = open("Logins/Recieptionist/" + recp_name  + ".txt", "a")
        f.write(lines11)
        f.write(lines12)
        f.write(lines13)
        f.write(lines14)
        f.write(line101)
        f.write(lines16)
        f.write(lines17)
        f.write(lines18)
        f.close()

        edit_btn.configure(state=NORMAL)
        name_entry.configure(state=DISABLED)
        name_change_btn.configure(state=DISABLED)
        password_entry.configure(state=DISABLED)
        pass_change_btn.configure(state=DISABLED)
        phone_entry.configure(state=DISABLED)
        phone_entry.delete(0, END)
        phone_change_btn.configure(state=DISABLED)

        tmsg.showinfo("Message", recp_name + " Phone number updated, Please re-Login to use")

    f = open("Logins/Recieptionist/" + recp_name + ".txt", "r")
    a1 = f.readline()
    a2 = f.readline()
    a3 = f.readline()
    a4 = f.readline()
    a5 = f.readline()
    a6 = f.readline()
    a7 = f.readline()
    a8 = f.readline()

    name_lbl = Label(rec_My_Profile_frame, text="Username: " + a1, bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 17, "bold"))
    name_lbl.place(x=40, y=100)
    password_lbl = Label(rec_My_Profile_frame, text="Password: " + a2, bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 17, "bold"))
    password_lbl.place(x=40, y=160)
    doj_lbl = Label(rec_My_Profile_frame, text="Date of joining: " + a3, bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 17, "bold"))
    doj_lbl.place(x=40, y=220)
    gender_lbl = Label(rec_My_Profile_frame, text="Gender: " + a4, bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 17, "bold"))
    gender_lbl.place(x=40, y=280)
    phone_lbl = Label(rec_My_Profile_frame, text="Phone no.: " + a5, bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 17, "bold"))
    phone_lbl.place(x=40, y=340)
    timing_lbl = Label(rec_My_Profile_frame, text="Timing: " + a6, bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 17, "bold"))
    timing_lbl.place(x=40, y=400)
    week_off_lbl = Label(rec_My_Profile_frame, text="Week off: " + a7, bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 17, "bold"))
    week_off_lbl.place(x=40, y=460)
    salary_lbl = Label(rec_My_Profile_frame, text="Salary: " + a8, bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 17, "bold"))
    salary_lbl.place(x=40, y=520)
    f.close()
    edit_btn = Button(rec_My_Profile_frame, command=open_edit_tabs, text="Edit", bg="red", fg="#ffffff", width=16, font=("Halvetica", 15, "bold"))
    edit_btn.place(x=440, y=590)

    ne = StringVar()
    pe = StringVar()
    phe = StringVar()

    name_entry = Entry(rec_My_Profile_frame, textvariable=ne, bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 16, "bold"))
    password_entry = Entry(rec_My_Profile_frame, textvariable=pe, bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 16, "bold"))
    phone_entry = Entry(rec_My_Profile_frame, textvariable=phe, bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 16, "bold"))
    name_change_btn = Button(rec_My_Profile_frame, command=change_name, text="Save", bg="green", fg="#ffffff", width=16, font=("Halvetica", 15, "bold"))
    pass_change_btn = Button(rec_My_Profile_frame, command=change_pass, text="Save", bg="green", fg="#ffffff", width=16, font=("Halvetica", 15, "bold"))
    phone_change_btn = Button(rec_My_Profile_frame, command=change_phone, text="Save", bg="green", fg="#ffffff", width=16, font=("Halvetica", 15, "bold"))
    empty_lbl = Label(rec_My_Profile_frame, text="  ", bg="#1c478b").pack(pady=300)

#-------------------------------------------------recieptionist patient frame-------------------------------------------
    rec_Patient_frame = Frame(receptioninst_root, bg="#1c478b")
    rec_profile_lbl = Label(rec_Patient_frame, text="Patient", bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 20, "bold"), pady=2)
    rec_profile_lbl.pack(pady=20)
    empty_lbl = Label(rec_Patient_frame, text="  ", bg="#1c478b").pack(pady=10)

    def apb():
        add_p_frame.pack(fill=BOTH)
        view_p_frame.forget()
        del_p_frame.forget()
        add_patient_btn.configure(state=DISABLED)
        view_patien_btn.configure(state=NORMAL)
        delete_patient_btn.configure(state=NORMAL)

    def vpb():
        add_p_frame.forget()
        view_p_frame.pack()
        del_p_frame.forget()
        add_patient_btn.configure(state=NORMAL)
        view_patien_btn.configure(state=DISABLED)
        delete_patient_btn.configure(state=NORMAL)

    def dpb():
        add_p_frame.forget()
        view_p_frame.forget()
        del_p_frame.pack()
        add_patient_btn.configure(state=NORMAL)
        view_patien_btn.configure(state=NORMAL)
        delete_patient_btn.configure(state=DISABLED)
    add_patient_btn = Button(rec_Patient_frame, text="Add Patient", bg="#1f7dad", command= apb , width=10, fg="#ffffff", font=("Halvetica", 12, "bold"))
    add_patient_btn.place(x= 80, y=80)
    view_patien_btn = Button(rec_Patient_frame, text="View Patient", bg="#1f7dad", command= vpb , width=10, fg="#ffffff", font=("Halvetica", 12, "bold"))
    view_patien_btn.place(x= 460, y=80)
    delete_patient_btn = Button(rec_Patient_frame, text="Delete Patient", bg="#1f7dad", command= dpb , width=14, fg="#ffffff", font=("Halvetica", 12, "bold"))
    delete_patient_btn.place(x= 878, y=80)

    add_p_frame = Frame(rec_Patient_frame, bg = "#1c478b")

    def saving_data_in_file(a, b, c, d):
        f = open("patients/"+ a +"/" + a + ".txt", "x")
        sttr = b + "\n"
        sttr1 = c + "\n"
        sttr2 = d
        f.write(sttr)
        f.write(sttr1)
        sttr3 = x1 + "\n"
        f.write(sttr3)
        f.write(sttr2)
        f.close()

        f = open("patients/" + a + "/" + "appointment letter.txt", "x")
        f.close

        directory1 = "bills"
        directory2 = "medician"
        directory3 = "reports"
        location = "C:/Users/GOPAL SINGH/PythonGui/Hospital Mang Sys/patients/" + a + "/"
        path1 = os.path.join(location, directory1)
        path2 = os.path.join(location, directory2)
        path3 = os.path.join(location, directory3)
        os.mkdir(path1)
        os.mkdir(path2)
        os.mkdir(path3)
        tmsg.showinfo("Message", "Patient Details saved succesfully")

        patient_name_entry.delete(0, END)
        patient_age_entry.delete(0, END)
        patient_gender_entry.delete(0, END)
        patient_phone_num_entry.delete(0, END)

    def saving_pateint():
        val1 = pne.get()
        val2 = pae.get()
        val3 = pge.get()
        val4 = ppne.get()

        if os.path.exists("patients/" + val1):
            tmsg.showerror("Error", "Patient with this name already exist. Please use different name.")
        else:
            directory = val1
            location = "C:/Users/GOPAL SINGH/PythonGui/Hospital Mang Sys/patients/"
            path = os.path.join(location, directory)
            os.mkdir(path)
            saving_data_in_file(val1, val2, val3, val4)

    empty_lbl = Label(add_p_frame, text="  ", bg="#1c478b").pack(pady=300)
    patient_name_lbl = Label(add_p_frame, text= "Patient Name:", bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 17, "bold")).place(x =60 , y = 20 )
    patient_age_lbl = Label(add_p_frame, text= "Patient Age:", bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 17, "bold")).place(x =60 , y = 70)
    patient_gender_lbl = Label(add_p_frame, text= "Patient Gender:", bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 17, "bold")).place(x =60 , y = 120)
    patient_phone_num_lbl = Label(add_p_frame, text= "Patient Phone No.:", bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 17, "bold")).place(x =60 , y = 170)

    pne = StringVar()
    pae = StringVar()
    pge = StringVar()
    ppne = StringVar()

    patient_name_entry = Entry(add_p_frame, textvariable=pne , bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 16, "bold"))
    patient_name_entry.place(x= 350 , y=20)
    patient_age_entry = Entry(add_p_frame, textvariable=pae , bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 16, "bold"))
    patient_age_entry.place(x= 350 , y=70)
    patient_gender_entry = Entry(add_p_frame, textvariable=pge , bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 16, "bold"))
    patient_gender_entry.place(x= 350 , y=120)
    patient_phone_num_entry = Entry(add_p_frame, textvariable=ppne , bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 16, "bold"))
    patient_phone_num_entry.place(x= 350 , y=170)
    save_ptnt_btn = Button(add_p_frame, text="Add", bg="#1f7dad", command=saving_pateint , width=20, fg="#ffffff", font=("Halvetica", 15, "bold"))
    save_ptnt_btn.place(x=280, y=230)

    view_p_frame = Frame(rec_Patient_frame, bg = "#1c478b")
    def Search_patient():
        patient_name = p_name.get()
        if os.path.exists("patients/" + patient_name + "/" + patient_name + ".txt"):
            search_btn.configure(state=DISABLED)
            f = open("patients/" + patient_name + "/" + patient_name + ".txt")
            age_p = f.readline()
            gen_p = f.readline()
            dotreatment_p = f.readline()
            pno_p = f.readline()
            f.close()

            f = open("patients/" + patient_name + "/" + "appointment letter.txt")
            l_app = f.readline()
            l_d_app = f.readline()
            f.close()

            no_of_rp = len(os.listdir("patients/" + patient_name +"/reports"))

            no_of_med_bils = len(os.listdir("patients/" + patient_name + "/medician"))

            f = open("patients/" + patient_name + "/" + "appointment letter.txt", "r")
            checjke = len(f.readlines())
            f.close()
            f = open("patients/" + patient_name + "/" + "appointment letter.txt", "r")
            for running in range(checjke):
                liiiiine = f.readline()

            patient_details_listbo.insert(END, "Name: " + patient_name)
            patient_details_listbo.insert(END, "Age: " + age_p)
            patient_details_listbo.insert(END, "Gender: " + gen_p)
            patient_details_listbo.insert(END, "Day of treatment start: " + dotreatment_p)
            patient_details_listbo.insert(END, "Name: " + pno_p)
            patient_details_listbo.insert(END, "Previous appointment: " + l_app)
            patient_details_listbo.insert(END, "Previous appointment details: " + l_d_app )
            patient_details_listbo.insert(END, "Total reports: " + str(no_of_rp))
            patient_details_listbo.insert(END, "Total Medicine bills: " + str(no_of_med_bils))
            if liiiiine == "Treatment ended":
                patient_details_listbo.insert(END, liiiiine)
            else:
                patient_details_listbo.insert(END, "Treatment is not ended")
            f.close()

        else:
            tmsg.showerror("Error", "Patient not found!")

    def new_p():
        search_btn.configure(state=NORMAL)
        patient_details_listbo.delete(0, END)

    p_name = StringVar()

    user_entry_lbl = Label(view_p_frame, text="Patient name: ", bg="#1c478b", fg="#ffffff", font=("Halvetica", 14, "bold")).pack()
    user_entry = Entry(view_p_frame, textvariable=p_name, fg="#1c478b", relief=RIDGE, font=("Halvetica", 16, "bold"))
    user_entry.pack()
    empty_lbl = Label(view_p_frame, text="  ", bg="#1c478b").pack(pady=6)
    search_btn = Button(view_p_frame, text="Search", command=Search_patient , bg="#1f7dad", width=10, fg="#ffffff", font=("Halvetica", 10, "bold"))
    search_btn.place(x = 420, y = 60)
    res_btn = Button(view_p_frame, text="Reset", command=new_p, bg="#1f7dad", width=10, fg="#ffffff", font=("Halvetica", 10, "bold"))
    res_btn.place(x = 540, y = 60)

    list_scrollbar = Scrollbar(view_p_frame)
    list_scrollbar.pack(side = RIGHT, fill = Y)

    list_scrollbar_x = Scrollbar(view_p_frame, orient=HORIZONTAL)
    list_scrollbar_x.pack(side=BOTTOM, fill=X)

    patient_details_listbo = Listbox(view_p_frame, xscrollcommand= list_scrollbar_x.set, yscrollcommand = list_scrollbar.set ,fg="#ffffff", bg="grey", width=100, height=37, font=("Comic Sans Ms", 15, "bold"))
    patient_details_listbo.pack(pady=1)
    list_scrollbar.configure(command=patient_details_listbo.yview)
    list_scrollbar_x.configure(command=patient_details_listbo.xview)


    del_p_frame = Frame(rec_Patient_frame, bg = "#1c478b")

    def deleting_patient():
        pfilename = ptodel.get()
        if os.path.exists("patients/" + pfilename):
            f = open("patients/" + pfilename + "/" + "appointment letter.txt", "r")
            checjke1 = len(f.readlines())
            f.close()
            f = open("patients/" + pfilename + "/" + "appointment letter.txt", "r")
            if checjke1 == 0:
                tmsg.showinfo("Message", "First end the treatment")
            else:
                for running in range(checjke1):
                    liiiiine2 = f.readline()
                f.close()
                if liiiiine2 == "Treatment ended":
                    recpq1 = tmsg.askyesno("Question", "Do you really want to delete the patient file?")
                    if recpq1 == YES:
                        shutil.rmtree("C:/Users/GOPAL SINGH/PythonGui/Hospital Mang Sys/patients/" + pfilename)
                        tmsg.showinfo("Message", "Patient file is deleted succesfully.")
                        patient_name_entry2.delete(0, END)
                    else:
                        pass
                else:
                    tmsg.showerror("Error", "Patient treatment is still not ended")
        else:
            tmsg.showerror("Error", "Patient didn't found")

    ptodel = StringVar()
    empty_lbl = Label(del_p_frame, text="  ", bg="#1c478b").pack(pady=50)
    pateint_name_lbl2  =Label(del_p_frame, text="Enter patient name:", bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 20, "bold")).pack(pady=20)
    patient_name_entry2 = Entry(del_p_frame, textvariable=ptodel, bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 18, "bold"))
    patient_name_entry2.pack()
    del_p_btn = Button(del_p_frame, text="Delete patient file", command=deleting_patient ,bg="#ff1a1a", fg="#ffffff", font=("Halvetica", 20, "bold")).pack(pady=60)
    empty_lbl = Label(del_p_frame, text="  ", bg="#1c478b").pack(pady=250)

#-----------------------------------------------------Bill Generate Frame-----------------------------------------------

    rec_Bill_Generate_frame = Frame(receptioninst_root, bg="#1c478b")
    rec_Bill_lbl = Label(rec_Bill_Generate_frame, text="Generate Bill", bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 20, "bold"), pady=10)
    rec_Bill_lbl.pack()
    def length(l):
        result = ''.join([random.choice(string.digits)
                          for n in range(l)])
        return result

    def saving_bill():
        a = int(e1.get())
        b = int(e2.get())
        d = int(e3.get())
        temp_total = a+b
        dis = (d / 100)*temp_total
        total = temp_total-dis
        print("total: ", total, "discount: ")

    def searchppppp():
        nmmm = nm.get()
        if os.path.exists("patients/" + nmmm):
            e1.configure(state = NORMAL)
            e2.configure(state = NORMAL)
            e3.configure(state = NORMAL)
            e4.configure(state = NORMAL)
            e5.configure(state = NORMAL)
            e6.configure(state = NORMAL)
            e7.configure(state = NORMAL)
            e8.configure(state = NORMAL)
            e9.configure(state = NORMAL)
            ee1.configure(state = NORMAL)
            ee2.configure(state = NORMAL)
            ee3.configure(state = NORMAL)
            ee4.configure(state = NORMAL)
            ee5.configure(state = NORMAL)
            ee6.configure(state = NORMAL)
            save_bill_btn.configure(state = NORMAL)
        else:
            tmsg.showerror("Error","Patient not found")


    nm = StringVar()
    bill_no = length(12)
    patient_name_lbl_33 = Label(rec_Bill_Generate_frame, text="Patient name",  bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 14, "bold")).pack()
    patient_name_entry_33 = Entry(rec_Bill_Generate_frame, textvariable=nm ,bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 14, "bold")).pack(pady=2)
    search_p_n_re_btn = Button(rec_Bill_Generate_frame, command=searchppppp ,text = "Search patient",bg="#ff1a1a", fg="#ffffff", font=("Halvetica", 12, "bold")).pack()
    empty_lbl = Label(rec_Bill_Generate_frame, text="  ", bg="#1c478b").pack(pady=200)
    appointment_charge_lbl = Label(rec_Bill_Generate_frame, text="Appointment Charge:",  bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 14, "bold")).place(x=60 , y=180)
    medicine_charge_lbl = Label(rec_Bill_Generate_frame, text="Medicine Charge:",  bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 14, "bold")).place(x=60 , y=220)
    discount_lbl = Label(rec_Bill_Generate_frame, text="discount: ", bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 14, "bold")).place(x=60, y=260)
    other_charges_lbl = Label(rec_Bill_Generate_frame, text="Other Charges:",  bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 14, "bold")).place(x=60 , y=300)
    other_charge_comment_lbl = Label(rec_Bill_Generate_frame, text="Other Charge comment:",  bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 14, "bold")).place(x=460 , y=300)
    other_charges_lbl11 = Label(rec_Bill_Generate_frame, text="Other Charges:", bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 14, "bold")).place(x=60, y=340)
    other_charge_comment_lbl11 = Label(rec_Bill_Generate_frame, text="Other Charge comment:", bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 14, "bold")).place(x=460, y=340)
    other_charges_lbl2 = Label(rec_Bill_Generate_frame, text="Other Charges:", bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 14, "bold")).place(x=60, y=380)
    other_charge_comment_lbl2 = Label(rec_Bill_Generate_frame, text="Other Charge comment:", bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 14, "bold")).place(x=460, y=380)
    other_charges_lbl3 = Label(rec_Bill_Generate_frame, text="Other Charges:", bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 14, "bold")).place(x=60, y=420)
    other_charge_comment_lbl3 = Label(rec_Bill_Generate_frame, text="Other Charge comment:", bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 14, "bold")).place(x=460, y=420)
    other_charges_lbl4 = Label(rec_Bill_Generate_frame, text="Other Charges:", bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 14, "bold")).place(x=60, y=460)
    other_charge_comment_lbl4 = Label(rec_Bill_Generate_frame, text="Other Charge comment:", bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 14, "bold")).place(x=460, y=460)
    other_charges_lbl5 = Label(rec_Bill_Generate_frame, text="Other Charges:", bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 14, "bold")).place(x=60, y=500)
    other_charge_comment_lbl5 = Label(rec_Bill_Generate_frame, text="Other Charge comment:", bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 14, "bold")).place(x=460, y=500)


    e1 = Entry(rec_Bill_Generate_frame, state=DISABLED , bg="#1c478b", width= 12 ,fg="#ffffff", font=("Comic Sans Ms", 14, "bold"))
    e1.place(x= 280, y= 180 )
    e2 = Entry(rec_Bill_Generate_frame, state=DISABLED , bg="#1c478b", width= 12 ,fg="#ffffff", font=("Comic Sans Ms", 14, "bold"))
    e2.place(x= 280, y= 220)
    e3 = Entry(rec_Bill_Generate_frame, state=DISABLED , bg="#1c478b", width= 12 ,fg="#ffffff", font=("Comic Sans Ms", 14, "bold"))
    e3.place(x= 280, y= 260)
    e4 = Entry(rec_Bill_Generate_frame, state=DISABLED , bg="#1c478b", width= 12 ,fg="#ffffff", font=("Comic Sans Ms", 14, "bold"))
    e4.place(x= 280, y= 300)
    e5 = Entry(rec_Bill_Generate_frame, state=DISABLED , bg="#1c478b", width= 12 ,fg="#ffffff", font=("Comic Sans Ms", 14, "bold"))
    e5.place(x= 280, y= 340)
    e6 = Entry(rec_Bill_Generate_frame, state=DISABLED , bg="#1c478b", width= 12 ,fg="#ffffff", font=("Comic Sans Ms", 14, "bold"))
    e6.place(x= 280, y= 380)
    e7 = Entry(rec_Bill_Generate_frame, state=DISABLED , bg="#1c478b", width= 12 ,fg="#ffffff", font=("Comic Sans Ms", 14, "bold"))
    e7.place(x= 280, y= 420)
    e8 = Entry(rec_Bill_Generate_frame, state=DISABLED , bg="#1c478b", width= 12 ,fg="#ffffff", font=("Comic Sans Ms", 14, "bold"))
    e8.place(x= 280, y= 460)
    e9 = Entry(rec_Bill_Generate_frame, state=DISABLED , bg="#1c478b", width= 12 ,fg="#ffffff", font=("Comic Sans Ms", 14, "bold"))
    e9.place(x= 280, y= 500)
    ee1 = Entry(rec_Bill_Generate_frame, state=DISABLED , bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 14, "bold"))
    ee1.place(x= 740, y= 300)
    ee2 = Entry(rec_Bill_Generate_frame, state=DISABLED , bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 14, "bold"))
    ee2.place(x= 740, y= 340)
    ee3 = Entry(rec_Bill_Generate_frame, state=DISABLED , bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 14, "bold"))
    ee3.place(x= 740, y= 380)
    ee4 = Entry(rec_Bill_Generate_frame, state=DISABLED , bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 14, "bold"))
    ee4.place(x= 740, y= 420)
    ee5 = Entry(rec_Bill_Generate_frame, state=DISABLED , bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 14, "bold"))
    ee5.place(x= 740, y= 460)
    ee6 = Entry(rec_Bill_Generate_frame, state=DISABLED , bg="#1c478b", fg="#ffffff", font=("Comic Sans Ms", 14, "bold"))
    ee6.place(x= 740, y= 500)

    save_bill_btn = Button(rec_Bill_Generate_frame, command=saving_bill ,state=DISABLED , text = "Save bill",bg="#1aff1a", fg="#ffffff", font=("Halvetica", 15, "bold"))
    save_bill_btn.pack()
    empty_lbl = Label(rec_Bill_Generate_frame, text="  ", bg="#1c478b").pack(pady=100)

#---------------------------------------------------Appointment Frame---------------------------------------------------

    rec_Appointment_frame = Frame(receptioninst_root, bg="#1c478b")

    def search_p():
        namem = pat_name.get()
        lb.delete(0, END)
        if namem == "":
            tmsg.showerror("Error", "Enter patient name first.")
        else:
            if os.path.exists("patients/" + namem):
                f = open("patients/" + namem + "/appointment letter.txt")
                no_line_A = len(f.readlines())
                f.close()
                more_appt.configure(state=NORMAL)
                if no_line_A == 0:
                    pass
                else:
                    f = open("patients/" + namem + "/appointment letter.txt")
                    for rpeat in range(no_line_A):
                        ln = f.readline()
                        lb.insert(rpeat, "  " + str(rpeat + 1) + ". " + ln)
                    f.close()
                    more_appt.configure(state=DISABLED)
                    tmsg.showinfo("Message", "Treatment is already in process.")
                    search_a_btn1.configure(state=NORMAL)
            else:
                tmsg.showerror("Error", "Patient didn't found")
                search_a_btn1.configure(state=NORMAL)

    pat_name = StringVar()
    patient_appointment_lbl = Label(rec_Appointment_frame, text="Patient Appointments", bg="#1f7dad", fg="#ffffff", font=("Comic Sans Ms", 20, "bold"), pady=2).pack(pady=20, fill=X)
    user_a_entry_lbl1 = Label(rec_Appointment_frame, text="Patient name: ", bg="#1c478b", fg="#ffffff", font=("Halvetica", 14, "bold")).pack()
    user_a_entry1 = Entry(rec_Appointment_frame, textvariable=pat_name, fg="#1c478b", relief=RIDGE, font=("Halvetica", 16, "bold"))
    user_a_entry1.pack()
    search_a_btn1 = Button(rec_Appointment_frame, state=NORMAL, text="Search", command=search_p, bg="#1f7dad", width=10, fg="#ffffff", font=("Halvetica", 10, "bold"))
    search_a_btn1.pack(pady=5)
    list_frame = Frame(rec_Appointment_frame, bg="#1c478b")
    lbsbx = Scrollbar(list_frame, orient=HORIZONTAL)
    lbsbx.pack(side=BOTTOM, fill=X)
    lbsby = Scrollbar(list_frame)
    lbsby.pack(side=RIGHT, fill=Y)
    lb = Listbox(list_frame, xscrollcommand=lbsbx.set, yscrollcommand=lbsby.set, fg="#ffffff", bg="grey", width=85,  height=10, font=("Comic Sans Ms", 15, "bold"))
    lb.pack()
    lbsbx.configure(command=lb.xview)
    lbsby.configure(command=lb.yview)
    list_frame.pack()

    other_frame = Frame(rec_Appointment_frame, bg="#1c478b")

    def next_app():
        date_lbl.place(x=20, y=10)
        date_entry.place(x=20, y=40)
        comment_lbl.place(x=150, y=10)
        comment_entry.place(x=150, y=40)
        sve_btn.place(x=80, y=87)
        more_appt.configure(state=DISABLED)
        search_a_btn1.configure(state=NORMAL)

    def saving_date():


         dinak = date_app.get()
         vakya = comment_app.get()
         file_loc = pat_name.get()
         if vakya == "" and dinak == "":
             tmsg.showerror("Error", "Please enter something")
         else:
             f = open("patients/" + file_loc + "/appointment letter.txt", "a")
             likho = dinak + ": " + vakya
             f.write(likho)
             f.write("\n")
             f.close()
             date_lbl.forget()
             date_entry.delete(0, END)
             date_entry.configure(state=DISABLED)
             comment_lbl.forget()
             comment_entry.delete(0, END)
             comment_entry.configure(state=DISABLED)
             sve_btn.forget()
             sve_btn.configure(state=DISABLED)
             more_appt.configure(state=NORMAL)
             lb.delete(0, END)
             search_a_btn1.configure(state=NORMAL)

    date_app = StringVar()
    comment_app = StringVar()
    date_lbl = Label(other_frame, text="Date: ", bg="#1c478b", fg="#ffffff", font=("Halvetica", 17, "bold"))
    date_entry = Entry(other_frame, textvariable=date_app, width=10, fg="#1c478b", relief=RIDGE, font=("Halvetica", 16, "bold"))
    comment_lbl = Label(other_frame, text="comment:", bg="#1c478b", fg="#ffffff", font=("Halvetica", 17, "bold"))
    comment_entry = Entry(other_frame, textvariable=comment_app, fg="#1c478b", relief=RIDGE, font=("Halvetica", 16, "bold"))
    sve_btn = Button(other_frame, command=saving_date, text="Save", bg="#1f7dad", width=10, fg="#ffffff", font=("Halvetica", 8, "bold"))
    lbl = Label(other_frame, text="", bg="#1c478b").pack(pady=15)
    more_appt = Button(other_frame, state=DISABLED, text="First appointment", command=next_app, bg="green", width=20, fg="#ffffff", font=("Halvetica", 15, "bold"))
    more_appt.pack(side=LEFT)
    lbl = Label(other_frame, text="", bg="#1c478b").pack(pady=100)
    other_frame.pack()

#----------------------------------------------------Income Frame-------------------------------------------------------

    rec_Income_frame = Frame(receptioninst_root, bg="#1f7dad")

    def search_year():
        searched_year = income_year.get()
        if os.path.exists("Income/" + searched_year + ".txt"):
            today_in_entry1.configure(state=NORMAL)
            today_in_entry2.configure(state=NORMAL)
            today_in_entry3.configure(state=NORMAL)
            rec_in_btn.configure(state=NORMAL)
            today_in_entry4.configure(state=NORMAL)
        else:
            tmsg.showerror("Error", "Year not found")

    def save_income():
        searched_year1 = income_year.get()
        totap_patient = rec_p.get()
        today_income = rec_ti.get()
        total_expense = rec_te.get()
        total_income = rec_total_in.get()
        f = open("Income/"+searched_year1+".txt", "a")
        f.write(x1)
        f.write(":          ")
        f.write(totap_patient)
        f.write("               ")
        f.write(today_income)
        f.write("               ")
        f.write(total_expense)
        f.write("               ")
        f.write(total_income)
        f.write(z)
        f.close()
        tmsg.showinfo("Message", "Income saved")
        today_in_entry1.delete(0, END)
        today_in_entry2.delete(0, END)
        today_in_entry3.delete(0, END)
        rec_in_btn.configure(state= DISABLED)
        today_in_entry4.delete(0, END)
        rec_in_entry.delete(0, END)
        today_in_entry1.configure(state= DISABLED)
        today_in_entry2.configure(state= DISABLED)
        today_in_entry3.configure(state= DISABLED)
        today_in_entry4.configure(state= DISABLED)

    income_year = StringVar()
    rec_in_frame = Frame(rec_Income_frame, bg = "#1c478b")
    rec_in_lbl = Label(rec_in_frame, text="Enter year ", bg="#1c478b", fg="#ffffff", font=("Halvetica", 14, "bold")).pack(pady = 15)
    rec_in_entry = Entry(rec_in_frame, textvariable=income_year, fg="#1c478b", relief=RIDGE, font=("Halvetica", 14, "bold"))
    rec_in_entry.pack()
    rec_in_search = Button(rec_in_frame, text="Search" ,command = search_year ,bg="#1f7dad", width=7, fg="#ffffff", font=("Halvetica", 12, "bold"))
    rec_in_search.pack(pady=20)
    today_in = Label(rec_in_frame, text="No. of patients", bg="#1c478b", fg="#ffffff", font=("Halvetica", 14, "bold")).place(x = 100, y = 170)
    today_in2 = Label(rec_in_frame, text="Today income", bg="#1c478b", fg="#ffffff", font=("Halvetica", 14, "bold")).place(x = 300, y = 170)
    today_in3 = Label(rec_in_frame, text="Today expense", bg="#1c478b", fg="#ffffff", font=("Halvetica", 14, "bold")).place(x = 500, y = 170)
    today_in3 = Label(rec_in_frame, text="Total Income", bg="#1c478b", fg="#ffffff", font=("Halvetica", 14, "bold")).place(x=700, y=170)
    rec_p = StringVar()
    rec_ti = StringVar()
    rec_te = StringVar()
    rec_total_in = StringVar()
    today_in_entry1 = Entry(rec_in_frame,textvariable= rec_p ,state = DISABLED ,fg="#1c478b", relief=RIDGE,width = 10 ,font=("Halvetica", 14, "bold"))
    today_in_entry1.place(x = 100, y = 200)
    today_in_entry2 = Entry(rec_in_frame,textvariable= rec_ti ,state = DISABLED ,fg="#1c478b", relief=RIDGE,width = 10 , font=("Halvetica", 14, "bold"))
    today_in_entry2.place(x = 300, y = 200)
    today_in_entry3 = Entry(rec_in_frame,textvariable= rec_te ,state = DISABLED , fg="#1c478b", relief=RIDGE,width = 10 , font=("Halvetica", 14, "bold"))
    today_in_entry3.place(x = 500, y = 200)
    today_in_entry4 = Entry(rec_in_frame, textvariable=rec_total_in, state=DISABLED,  fg="#1c478b", relief=RIDGE,width=10, font=("Halvetica", 14, "bold"))
    today_in_entry4.place(x=700, y=200)
    rec_in_btn = Button(rec_in_frame, text="Save", state = DISABLED ,command=save_income, bg="#1f7dad", width=14, fg="#ffffff", font=("Halvetica", 15, "bold"))
    rec_in_btn.place(x = 380, y = 240)

    def save_year():
        sy = year.get()
        if os.path.exists("Income/"+sy+".txt"):
            tmsg.showerror("Error", "Year already exist")
        else:
            f = open("Income/"+sy+".txt", "x")
            tmsg.showinfo("Message", "Year added")
            f.close()

    year = StringVar()
    ad_date_lbl = Label(rec_in_frame, text="Add Year", bg="#1c478b", fg="#ffffff", font=("Halvetica", 20, "bold")).place(x=350, y=400)
    add_date_lbl = Label(rec_in_frame, text="Enter year", bg="#1c478b", fg="#ffffff",font=("Halvetica", 14, "bold")).place(x=150, y=450)
    add_date_entry = Entry(rec_in_frame, textvariable=year, fg="#1c478b", relief=RIDGE, width=10, font=("Halvetica", 14, "bold"))
    add_date_entry.place(x=300, y=450)
    add_date_btn = Button(rec_in_frame, text="Add year", command=save_year, bg="#1f7dad", width=10,fg="#ffffff", font=("Halvetica", 15, "bold"))
    add_date_btn.place(x=230, y=500)
    rec_in_empty = Label(rec_in_frame, text=" ", bg="#1c478b").pack(pady=250, padx = 150)
    rec_in_frame.pack(fill=BOTH)


#----------------------------------------------------------Medicine form button-----------------------------------------

    rec_Medicine_frame = Frame(receptioninst_root, bg="#1f7dad")
    rec_heading_frm = Frame(rec_Medicine_frame, bg = "#1c478b")
    def reset():
        rec_med_entry.delete(0,END)
        rec_med_btn1.configure(state = NORMAL)
        patient_details_med_listbo.delete(0, END)
        rec_med_entry2.delete(0, END)
    def med_details():
        p_anme1 = rec_med_name.get()
        if os.path.exists("patients/"+p_anme1):
            number_of_files= len(os.listdir("patients/"+p_anme1+"/medician"))
            rec_med_btn1.configure(state = DISABLED)
            x = 0
            for x in range(number_of_files):
                patient_details_med_listbo.insert(END,"medicine"+str(x))

        else:
            tmsg.showerror("Error", "Patient not found")
    def search_med():
        bill_no = bill_n.get()
        p_nm = rec_med_name.get()
        if os.path.exists("patients/"+p_nm+"/medician/medicine"+bill_no+".txt"):
            medbill = Tk()
            medbill.geometry("1366x768")
            medbill.minsize(1365, 767)
            medbill.maxsize(1368, 769)
            medbill.configure(bg  = "black")
            list_scrollbar_med2 = Scrollbar(medbill, width=20)
            list_scrollbar_med2.pack(side=RIGHT, fill=Y)
            list_scrollbar_medx2 = Scrollbar(medbill, width=20, orient=HORIZONTAL)
            list_scrollbar_medx2.pack(side=BOTTOM, fill=X)
            patient_details_med_listbo2 = Listbox(medbill, xscrollcommand=list_scrollbar_medx2 ,yscrollcommand=list_scrollbar_med2.set, fg="#ffffff", bg="black", width=100, height=55, font=("Comic Sans Ms", 15, "bold"))
            patient_details_med_listbo2.pack(padx=20, pady= 20)
            list_scrollbar_med2.configure(command=patient_details_med_listbo2.yview)
            list_scrollbar_medx2.configure(command=patient_details_med_listbo2.xview)
            f = open("patients/"+p_nm+"/medician/medicine"+bill_no+".txt", "r")
            no_line = len(f.readlines())
            print(no_line)
            f.close()
            f = open("patients/" + p_nm + "/medician/medicine" + bill_no + ".txt", "r")
            y = 0
            for y in range(no_line):
                patient_details_med_listbo2.insert(END, f.readline())
            f.close()
            medbill.mainloop()

        else:
            tmsg.showerror("Error", "Bill number not found")

    rec_med_name = StringVar()
    rec_med_lbl = Label(rec_heading_frm, text="Medicines", bg="#1c478b", fg="#ffffff", font=("Halvetica", 20, "bold")).pack(pady = 10, padx = 200)
    rec_med_lbl1 = Label(rec_heading_frm, text="Enter patient name", bg="#1c478b", fg="#ffffff", font=("Halvetica", 12, "bold")).place(x = 200, y = 100)
    rec_med_entry = Entry(rec_heading_frm, textvariable = rec_med_name, fg="#1c478b", relief=RIDGE, width=20, font=("Halvetica", 14, "bold"))
    rec_med_entry.place(x = 380, y = 100)
    rec_med_btn1 = Button(rec_heading_frm,text = "Search patient",state = NORMAL ,bg="#80ff00", command = med_details ,fg="#ffffff", font=("Halvetica", 12, "bold"))
    rec_med_btn1.place(x = 300, y = 150)
    rec_med_btn2 = Button(rec_heading_frm, text = "Reset",bg="#ff1a1a", command = reset,fg="#ffffff", font=("Halvetica", 12, "bold")).place(x = 450, y = 150)
    rec_md_empty = Label(rec_heading_frm, text=" ", bg="#1c478b").pack(pady=65, padx=750)
    rec_heading_frm.pack()
    rec_med_list_frm = Frame(rec_Medicine_frame, bg = "#1c478b")

    bill_n = StringVar()

    list_scrollbar_med = Scrollbar(rec_med_list_frm, width=20)
    list_scrollbar_med.pack(side=RIGHT, fill=Y)
    patient_details_med_listbo = Listbox(rec_med_list_frm, yscrollcommand=list_scrollbar.set, fg="#ffffff", bg="grey", width=60, height=15, font=("Comic Sans Ms", 15, "bold"))
    patient_details_med_listbo.place(x = 300, y  = 10)
    list_scrollbar_med.configure(command=patient_details_med_listbo.yview)
    rec_md_empty = Label(rec_med_list_frm, text=" ", bg="#1c478b").pack(pady=265, padx=750)
    rec_med_lbl2 = Label(rec_med_list_frm, text="Enter Medicine bill number", bg="#1c478b", fg="#ffffff", font=("Halvetica", 12, "bold")).place(x  = 30, y = 30)
    rec_med_entry2 = Entry(rec_med_list_frm, textvariable=bill_n, fg="#1c478b", relief=RIDGE, width=15, font=("Halvetica", 14, "bold"))
    rec_med_entry2.place(x=30, y=50)
    rec_med_btn3 = Button(rec_med_list_frm, text="Search Bill", state=NORMAL, bg="#80ff00", command=search_med, fg="#ffffff", font=("Halvetica", 12, "bold"))
    rec_med_btn3.place(x=30, y=100)

    rec_med_list_frm.pack()

#---------------------------------------------------------Operation Button function-------------------------------------

    def rec_profile():
        rec_My_Profile_frame.pack(fill=BOTH)
        rec_Patient_frame.forget()
        rec_Bill_Generate_frame.forget()
        rec_Appointment_frame.forget()
        rec_Income_frame.forget()
        rec_Medicine_frame.forget()


        rec_profile_btn.configure(state=DISABLED)
        rec_patient_btn.configure(state=NORMAL)
        rec_bill_btn.configure(state=NORMAL)
        rec_appointment_btn.configure(state=NORMAL)
        rec_income_btn.configure(state=NORMAL)
        rec_med_btn.configure(state=NORMAL)

    def rec_patient():
        rec_My_Profile_frame.forget()
        rec_Patient_frame.pack(fill=X)
        rec_Bill_Generate_frame.forget()
        rec_Appointment_frame.forget()
        rec_Income_frame.forget()
        rec_Medicine_frame.forget()


        rec_profile_btn.configure(state=NORMAL)
        rec_patient_btn.configure(state=DISABLED)
        rec_bill_btn.configure(state=NORMAL)
        rec_appointment_btn.configure(state=NORMAL)
        rec_income_btn.configure(state=NORMAL)
        rec_med_btn.configure(state=NORMAL)

    def rec_bill():
        rec_My_Profile_frame.forget()
        rec_Patient_frame.forget()
        rec_Bill_Generate_frame.pack(fill=BOTH)
        rec_Appointment_frame.forget()
        rec_Income_frame.forget()
        rec_Medicine_frame.forget()

        rec_profile_btn.configure(state=NORMAL)
        rec_patient_btn.configure(state=NORMAL)
        rec_bill_btn.configure(state=DISABLED)
        rec_appointment_btn.configure(state=NORMAL)
        rec_income_btn.configure(state=NORMAL)
        rec_med_btn.configure(state=NORMAL)

    def rec_appointment():
        rec_My_Profile_frame.forget()
        rec_Patient_frame.forget()
        rec_Bill_Generate_frame.forget()
        rec_Appointment_frame.pack(fill=BOTH)
        rec_Income_frame.forget()
        rec_Medicine_frame.forget()


        rec_profile_btn.configure(state=NORMAL)
        rec_patient_btn.configure(state=NORMAL)
        rec_bill_btn.configure(state=NORMAL)
        rec_appointment_btn.configure(state=DISABLED)
        rec_income_btn.configure(state=NORMAL)
        rec_med_btn.configure(state=NORMAL)

    def rec_income():
        rec_My_Profile_frame.forget()
        rec_Patient_frame.forget()
        rec_Bill_Generate_frame.forget()
        rec_Appointment_frame.forget()
        rec_Income_frame.pack(fill=BOTH)
        rec_Medicine_frame.forget()


        rec_profile_btn.configure(state=NORMAL)
        rec_patient_btn.configure(state=NORMAL)
        rec_bill_btn.configure(state=NORMAL)
        rec_appointment_btn.configure(state=NORMAL)
        rec_income_btn.configure(state=DISABLED)
        rec_med_btn.configure(state=NORMAL)

    def rec_medicine():
        rec_My_Profile_frame.forget()
        rec_Patient_frame.forget()
        rec_Bill_Generate_frame.forget()
        rec_Appointment_frame.forget()
        rec_Income_frame.forget()
        rec_Medicine_frame.pack(fill=BOTH)


        rec_profile_btn.configure(state=NORMAL)
        rec_patient_btn.configure(state=NORMAL)
        rec_bill_btn.configure(state=NORMAL)
        rec_appointment_btn.configure(state=NORMAL)
        rec_income_btn.configure(state=NORMAL)
        rec_med_btn.configure(state=DISABLED)

    operations_btn_frame = Frame(receptioninst_root, bg="#1c478b")
    empty_lbl = Label(operations_btn_frame, text="  ", bg="#1c478b").pack(pady=20)
    rec_profile_btn = Button(operations_btn_frame, command=rec_profile ,text="My Profile", width=16, fg="#1c478b", bg="#ffffff", font=("Halvetica", 20, "bold"))
    rec_profile_btn.pack(padx=10, pady=10)
    rec_patient_btn = Button(operations_btn_frame, command=rec_patient ,text="Patient", width=16, fg="#1c478b", bg="#ffffff", font=("Halvetica", 20, "bold"))
    rec_patient_btn.pack(padx=10, pady=10)
    rec_bill_btn = Button(operations_btn_frame, command=rec_bill ,text="Bill Generate", width=16, fg="#1c478b", bg="#ffffff", font=("Halvetica", 20, "bold"))
    rec_bill_btn.pack(padx=10, pady=10)
    rec_appointment_btn = Button(operations_btn_frame, command=rec_appointment ,text="Appointment", width=16, fg="#1c478b", bg="#ffffff", font=("Halvetica", 20, "bold"))
    rec_appointment_btn.pack(padx=10, pady=10)
    rec_income_btn = Button(operations_btn_frame, command=rec_income ,text="Income", width=16 ,fg="#1c478b", bg="#ffffff", font=("Halvetica", 20, "bold"))
    rec_income_btn.pack(padx=10, pady=10)
    rec_med_btn = Button(operations_btn_frame, command=rec_medicine , text="Medicine", width=16, fg="#1c478b", bg="#ffffff", font=("Halvetica", 20, "bold"))
    rec_med_btn.pack(padx=10, pady=10)
    logout_btn = Button(operations_btn_frame, text="Log Out", command=lambda: logout(receptioninst_root), fg="#ffffff", width=16, bg="#f62c47", font=("Halvetica", 15, "bold"))
    logout_btn.pack(pady=5, padx=10)

    operations_btn_frame.pack(side=LEFT, anchor="w", fill=Y)

#-------------------------------------------------Login Screen---------------------------------------------------------
def login_form(root, val_of_login):
    root.destroy()

    #login form instance
    login_root = Tk()

    login_root.geometry("1366x768")
    login_root.minsize(1365, 767)
    login_root.maxsize(1368, 769)
    login_root.configure(bg="#1c478b")

    if val_of_login == 1:
        login_as = "Admin"
    elif val_of_login == 2:
        login_as = "Doctor"
    elif val_of_login == 3:
        login_as = "Recieptioninst"

    def back_to_menu(root):
        root.destroy()
        main_menu()

    #Heading frame
    heading_frame = Frame(login_root, bg="#1f7dad")

    heading_label = Label(heading_frame, text="Login as " + login_as, bg="#1f7dad", fg="#ffffff",font=("Comic Sans Ms", 35, "bold"), pady=2).pack(pady=10)
    heading_frame.pack(side=TOP, anchor="n", fill=BOTH)

    #Login_form
    login_frame = Frame(login_root, bg="#1c478b")

    #log check
    def check_login(log_as):
        usrname = uservalue.get()
        password = passvalue.get()

        if log_as == 1:
            if os.path.exists("Logins/Admin/" + usrname + ".txt"):
                f1 =open("Logins/Admin/" + usrname +".txt", "r")
                pas = f1.readline()
                if password == pas:
                    logged_as_admin(usrname, login_root)
                else:
                    tmsg.showwarning("Warning", "Invalid Password")
            else:
                tmsg.showwarning("Warning", "Invalid Username")

        elif log_as == 2:
            if os.path.exists("Logins/Doctor/" + usrname + ".txt"):
                f1 =open("Logins/Doctor/" + usrname +".txt", "r")
                nn = f1.readline()
                pas = f1.readline()
                if password + "\n" == pas:
                    logged_as_doctor(usrname, login_root)
                else:
                    tmsg.showwarning("Warning", "Invalid Password")
            else:
                tmsg.showwarning("Warning", "Invalid Username")

        elif log_as == 3:
            if os.path.exists("Logins/Recieptionist/" + usrname + ".txt"):
                f1 =open("Logins/Recieptionist/" + usrname +".txt", "r")
                nnn = f1.readline()
                pas = f1.readline()
                if password + "\n" == pas:
                    logged_as_recieptionist(usrname, login_root)
                else:
                    tmsg.showwarning("Warning", "Invalid Password")
            else:
                tmsg.showwarning("Warning", "Invalid Username")

    #variables
    uservalue = StringVar()
    passvalue = StringVar()

    empty_lbl = Label(login_frame, text="  ", bg="#1c478b").pack(pady=60)
    user_entry_lbl = Label(login_frame, text="Username: ", bg="#1c478b",fg="#ffffff", font=("Halvetica", 20, "bold")).pack()
    user_entry = Entry(login_frame, textvariable=uservalue, fg="#1c478b",relief=RIDGE , font=("Halvetica", 20, "bold"))
    user_entry.pack()

    pass_entry_lbl = Label(login_frame, text="Password: ", bg="#1c478b",fg="#ffffff", font=("Halvetica", 20, "bold")).pack()
    pass_entry = Entry(login_frame, textvariable=passvalue, show="*", relief=RIDGE , fg="#1c478b", font=("Halvetica", 20, "bold"))
    pass_entry.pack()

    login_btn = Button(login_frame, text="Login" , command= lambda:check_login(val_of_login), bg="#1f7dad", width=10, fg="#ffffff" , font=("Halvetica", 20, "bold"))
    login_btn.pack(pady=20)
    back_btn = Button(login_frame, text="Back", command=lambda: back_to_menu(login_root) , bg="#1f7dad", width=10, fg="#ffffff" , font=("Halvetica", 20, "bold"))
    back_btn.pack()

    login_frame.pack()

    login_root.mainloop()


#--------------------------------------------------Menu screen:---------------------------------------------------------
def main_menu():
    root = Tk()
    root.geometry("1366x768")
    root.minsize(1365, 767)
    root.maxsize(1368, 769)
# Heading Frame:
    heading_frame = Frame(root, bg="#1f7dad")

    heading_label = Label(heading_frame, text="Hospital Management System", bg="#1f7dad", fg="#ffffff", font=("Comic Sans Ms", 18, "bold"), pady=2).pack()

    date_label = Label(heading_frame, text=x1 ,bg="#1f7dad", fg="#ffffff", font=("Comic Sans Ms", 9, "bold")).pack()

    heading_frame.pack(side=TOP, anchor="n", fill=BOTH)

    #Buttons Frame:
    menu_btn_frame = Frame(root, bg="#1c478b")

    heading_lbl = Label(menu_btn_frame, text="Menu page",bg="#1c478b", fg="#ffffff" , font=("Halvetica", 40, "bold"))
    heading_lbl.pack(pady=60)

    admin_login_btn = Button(menu_btn_frame, text="Admin       ", command=lambda :login_form(root, 1), width=15, justify=CENTER ,fg="#1c478b", bg="#ffffff" , font=("Halvetica", 20, "bold"))
    admin_login_btn.pack(pady=10)
    doc_login_btn = Button(menu_btn_frame, text="Doctor        ", command=lambda :login_form(root, 2), width=15, justify=CENTER ,fg="#1c478b", bg="#ffffff" , font=("Halvetica", 20, "bold"))
    doc_login_btn.pack(pady=10)
    recp_login_btn = Button(menu_btn_frame, text="Recieptionist", command=lambda :login_form(root, 3), width=15, justify=CENTER ,fg="#1c478b", bg="#ffffff" , font=("Halvetica", 20, "bold"))
    recp_login_btn.pack(pady=10)
    exit_btn = Button(menu_btn_frame, text="Exit               ", command=lambda :exit_event(root), width=15, justify=CENTER ,fg="#1c478b", bg="#ffffff" , font=("Halvetica", 20, "bold"))
    exit_btn.pack(pady=10)
    empty_lbl = Label(menu_btn_frame, text="  ", bg="#1c478b").pack(pady=100)
    menu_btn_frame.pack(side=TOP, anchor="n", fill=BOTH)

    root.mainloop()

main_menu()