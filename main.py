import sys
from tkinter import *
from tkinter import ttk, Toplevel

from data import *

# TEST GITHUB

# *************************
# *** main root configs ***
root = Tk()
root.title("CormoRent ")
root.geometry("600x600")
root.resizable(False, False)
# hide main root which will be empty
root.withdraw()

# ***********************************
# *** child_login configs ***
child_login: Toplevel = Toplevel(root)
child_login.geometry("600x600")
child_login.resizable(False, False)

# ***********************************
# *** guest_home configs ***
guest_home: Toplevel = Toplevel(root)
guest_home.geometry("600x600")
guest_home.resizable(False, False)
guest_home.withdraw()

# ***********************************
# *** admin_home configs ***
admin_home: Toplevel = Toplevel(root)
admin_home.geometry("600x600")
admin_home.resizable(False, False)
admin_home.withdraw()

# ***********************************
# *** admin_home configs ***
admin_data: Toplevel = Toplevel(root)
admin_data.geometry("600x600")
admin_data.resizable(False, False)
admin_data.withdraw()


# Functions
def exit_software_from_child_login():
    print("[[[[INFO]]]]\n Login Page was closed")
    sys.exit()


def validate_login(username_parameter, pw_parameter):
    username_data = username_parameter
    password_data = pw_parameter

    for user_list in users:

        if username_data == user_list["username_in_sys"]:
            if password_data == user_list["password_in_sys"]:
                user_list["online status"] = "ONLINE"
                print("[[[[INFO]]]]             Entered Username: ", username_data)
                print("[[[[INFO]]]]             Entered Password: ", password_data)
                username.initialize("")
                password.initialize("")
                child_login.withdraw()
                connected_user_str.set(user_list["username_in_sys"])


                if user_list["type"] == "guest":
                    guest_home.deiconify()
                    print(f"[[[[INFO]]]]          USER <{user_list['name']}> CONNECTED AS GUEST")



                elif user_list["type"] == "admin":
                    admin_home.deiconify()
                    print(f"[[[[INFO]]]]          USER <{user_list['name']}> CONNECTED AS ADMIN")


            else:
                user_list["online status"] = "OFFLINE"
                print("STATUS: ", user_list["online status"])
                print("Login failed")


def search_customer(username_p):
    customer_input = username_p
    for cust in users:
        print("the searched username was : ", customer_input)
        if cust["username_in_sys"] == customer_input:
            data_search_result.set(cust)



def quit_home():  # always from guest or admin home
    child_login.deiconify()
    guest_home.withdraw()
    admin_home.withdraw()
    print("[[[[INFO]]]]         CormoRent App was closed => Back to LOGIN")


#   **************************************************************
#   *******************LOGIN GUI *********************************
#   **************************************************************
login_failed_label = ttk.Label(child_login, text="Username or Password is wrong")
login_failed_label.place(x=120, y=120)
user_name_label = ttk.Label(child_login, text="Username :")
user_name_label.place(x=10, y=40)
username = StringVar()
user_name_entry = ttk.Entry(child_login, textvariable=username)
user_name_entry.place(x=120, y=40)
password_label = ttk.Label(child_login, text="password :")
password_label.place(x=10, y=80)
password = StringVar()
password_entry = ttk.Entry(child_login, textvariable=password, show="*")
password_entry.place(x=120, y=80)
login_button = ttk.Button(child_login, text="Login",
                          command=lambda: validate_login(username.get(), password.get()))
login_button.place(x=120, y=150)
quit_login_button = ttk.Button(child_login, text="QUIT APP", command=lambda: exit_software_from_child_login())
quit_login_button.place(x=120, y=500)








#   **************************************************************
#   *******************GUEST HOME GUI ****************************
#   **************************************************************
connected_user_str = StringVar()

chose_your_car_label_guest_home = ttk.Label(guest_home,
                                            text="Chose a car and click on 'Search' to check\n the prices and "
                                                 "availability", relief="", borderwidth=2)
chose_your_car_label_guest_home.place(x=120, y=20)

welcome_label_guest_home = ttk.Label(guest_home, text=f'Welcome {connected_user_str}')
welcome_label_guest_home.place(x=400, y=0)
brand_label_guest_home = ttk.Label(guest_home, text="Chose a brand")
brand_label_guest_home.place(x=10, y=100)
model_label_guest_home = ttk.Label(guest_home, text="Chose a model")
model_label_guest_home.place(x=10, y=140)
combobox_brand_guest_home = ttk.Combobox(guest_home, values=[car_choice[0]["brand"], car_choice[1]["brand"],
                                                             car_choice[2]["brand"]])
combobox_brand_guest_home.place(x=120, y=100)
combobox_model_guest_home = ttk.Combobox(guest_home, values=[car_choice[0]["model"], car_choice[1]["model"],
                                                             car_choice[2]["model"]])
combobox_model_guest_home.place(x=120, y=140)
submit_button_guest_home = ttk.Button(guest_home, text="Search")
submit_button_guest_home.place(x=120, y=200)
quit_button_guest_home = ttk.Button(guest_home, text="QUIT APP", command=lambda: quit_home())
quit_button_guest_home.place(x=120, y=500)










#   **************************************************************
#   *******************ADMIN HOME GUI ****************************
#   **************************************************************


label_welcome_admin_home = ttk.Label(admin_home, text=f'Welcome {connected_user_str}')
label_welcome_admin_home.place(x=400, y=0)
label_search_customer_admin_home = ttk.Label(admin_home, text="Name :")
label_search_customer_admin_home.place(x=10, y=100)

cust_name = StringVar()  # <----  we access the saved input through the StringVar function with .get() and .set()
entry_search_cust_admin_home = ttk.Entry(admin_home, textvariable=cust_name)  # <-- input from app
entry_search_cust_admin_home.place(x=120, y=80)



# Button -> it goes from here to "textvariable" above get the input from the entry
butt_search_customer_admin_home = ttk.Button(admin_home, text='search',
                                             command=lambda: search_customer(cust_name.get()))
butt_search_customer_admin_home.place(x=120, y=400)



data_search_result = StringVar()    # <-- above in the main Function where we get the result
                                    # we use .set() to say that where ever we put  "data_search_result"
                                    # it shows us the stored value
label_show_results_admin_home = ttk.Label(admin_home, textvariable=data_search_result, borderwidth=20,
                                          background="green",
                                          foreground="black")

label_show_results_admin_home.configure()
label_show_results_admin_home.place(x=250, y=250, height=300, width=250)
quit_button_admin_home = ttk.Button(admin_home, text="QUIT APP", command=lambda: quit_home())
quit_button_admin_home.place(x=120, y=500)



# ********************************************************

#   **************************************************************
#   *       loop the main root window ( DON'T TOUCH ME )         *
#   **************************************************************
root.mainloop()
