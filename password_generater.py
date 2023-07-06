import tkinter as tk
import string
import random



#functions
def password_generator():
    amount_upper = entr_amount_uppercased.get() #instead of taking as a parameter variable style can be used for three of them 
    amount_lower = entr_amount_lowercased.get() #man cannot get tk variable directly that's why .get() is used in that case
    amount_digit = entr_amount_random_number.get()
    
    random_number = "".join(random.choices(string.digits, k= int(amount_digit)))  #join method is used because radnom.ch... is also a list
    random_uppercase = "".join(random.choices(string.ascii_uppercase, k= int(amount_upper))) #amount_upper is taking as string, it is converted into int   
    random_lowercase = "".join(random.choices(string.ascii_lowercase, k= int(amount_lower))) #join method is used because radnom.ch... is also a list

    list_of_password_elements = [str(random_number), random_uppercase, random_lowercase] # list is made with components
    random.shuffle(list_of_password_elements)  # list is mixed

    password = "".join(list_of_password_elements)  # "" and spaces are deleted with "".join() and it is made together as a single word

    return password

def generate_button():
    value = password_generator()
    lbl_new_password.config(text= value) #  instead of config, (lbl_new_password["text"] = value) can be used. up to you
    
def exit_button():
    password_app_window.destroy() # destroy the window


# tkinter interface
password_app_window = tk.Tk()
password_app_window.geometry("400x150")

main_frame = tk.Frame(password_app_window) #frame is created in order to make things tidy
main_frame.pack()

password_app_window.title("Password Generator")
lbl_new_password = tk.Label(text="Your new password will be appear in here!") #label will be used to show the password 
lbl_new_password.pack()

entry_lower= tk.IntVar() #take the entry and assign to a tk variable (not a casual variable)
entr_amount_lowercased = tk.Entry(master=main_frame, textvariable=entry_lower)
entr_amount_lowercased.pack()
entr_amount_lowercased.insert(0,"amount of lower case")  #informative text is put to inform the client/user


entry_upper= tk.IntVar()
entr_amount_uppercased = tk.Entry(master=main_frame, textvariable=entry_upper)
entr_amount_uppercased.pack()
entr_amount_uppercased.insert(0,"amount of upper case")


entry_digit= tk.IntVar()
entr_amount_random_number = tk.Entry(master=main_frame, textvariable=entry_digit)
entr_amount_random_number.pack()
entr_amount_random_number.insert(0,"amount of digit")


btn_generate = tk.Button(text="Generate", command=generate_button)
btn_generate.pack()
btn_exit= tk.Button(text="Exit", command=exit_button)
btn_exit.pack()

password_app_window.mainloop() #to show the window .mainloop() is used
