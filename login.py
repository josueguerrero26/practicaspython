import customtkinter as tk

tk.set_appearance_mode('dark')
tk.set_default_color_theme('blue')

root = tk.CTk()
root.geometry('300x300')

def login():
    print('BIENVENIDO')

frame = tk.CTkFrame(master=root)
frame.pack(pady= 20, padx= 60, fill='both', expand=True)

label = tk.CTkLabel(master=frame, text='LOGIN')
label.pack(pady= 12, padx= 10)

entry = tk.CTkEntry(master=frame, placeholder_text='Usuario')
entry.pack(pady= 12, padx= 10) 

entry2 = tk.CTkEntry(master=frame, placeholder_text='Contraseña', show='*')
entry2.pack(pady= 12, padx= 10) 

button = tk.CTkButton(master=frame, text='Login', command=login)
button.pack(pady= 12, padx= 10)

root.mainloop()