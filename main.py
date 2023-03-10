import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.geometry("1000x850")

frame = customtkinter.CTkFrame(master=root)
frame.pack(padx=60, pady=20, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System")
label.pack(padx=10, pady=12)

user_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
user_entry.pack(padx=10, pady=12)

password_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Username", show="*")
password_entry.pack(padx=10, pady=12)


def login():
	user_input = user_entry.get()
	print('button pressed')
	print(user_input)


button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(padx=10, pady=12)

root.mainloop()



