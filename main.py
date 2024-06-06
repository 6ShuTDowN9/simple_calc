import customtkinter
calc_window = customtkinter.CTk()
calc_window.geometry("350x400")
button = customtkinter.CTkButton(calc_window, text = "hello kitty", width=100, height=80)
button.pack()
calc_window.mainloop()
print("test")