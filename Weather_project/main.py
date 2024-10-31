    from tkinter import *           # Built-in library to create GUI for applications.
    from PIL import ImageTk, Image  # For handling images in Tkinter.
    from tkinter import ttk         # Provides additional widgets like dropdown lists.
    import requests

    def data_get():
        city = city_name.get()
        # Correct the f-string syntax and ensure the city is properly interpolated.
        data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=9f82136d1116521b6da50e9d97f0ac38')
        
        w_label_value.config(text=data["weather"][0]["main"])
        w1_label_value.config(text=data["weather"][0]["description"])
        w2_label_value.config(text=str(data["main"]["temp"] - 273.15))  
        w3_label_value.config(text=data["main"]["pressure"])
        

    root = Tk()

    root.title('Weather Program')
    root.geometry('800x600')  # Specific size of window.
    root.config(bg='#87CEEB')

    # Create a combobox for city selection
    city_name = StringVar()
    name_list = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat",
                "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala",
                "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha",
                "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh",
                "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli",
                "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi", "Puducherry"]

    com = ttk.Combobox(root, values=name_list, width=30, font=("futura", 12, "bold"), textvariable=city_name)
    com.place(x=150, y=85, height=50, width=450)

    # Set a placeholder text
    placeholder_text = "Select a State"
    com.set(placeholder_text)

    # Placeholder management for combobox
    def on_click(event):
        if com.get() == placeholder_text:
            com.set("")

    def on_focus_out(event):
        if com.get() == "":
            com.set(placeholder_text)

    com.bind("<FocusIn>", on_click)
    com.bind("<FocusOut>", on_focus_out)

    # Weather details labels
    w_label = Label(root, text="Weather Climate", font=("futura", 12, "bold"))
    w_label.place(x=150, y=200, height=40, width=210)

    w1_label = Label(root, text="Weather Description", font=("futura", 12, "bold"))
    w1_label.place(x=150, y=260, height=40, width=210)

    w2_label = Label(root, text="Temperature", font=("futura", 12, "bold"))
    w2_label.place(x=150, y=320, height=40, width=210)

    w3_label = Label(root, text="Pressure", font=("futura", 12, "bold"))
    w3_label.place(x=150, y=380, height=40, width=210)

    # Dynamic labels for API data
    w_label_value = Label(root, font=("futura", 12, "bold"))
    w_label_value.place(x=450, y=200, height=40, width=210)

    w1_label_value = Label(root, font=("futura", 12, "bold"))
    w1_label_value.place(x=450, y=260, height=40, width=210)

    w2_label_value = Label(root, font=("futura", 12, "bold"))
    w2_label_value.place(x=450, y=320, height=40, width=210)

    w3_label_value = Label(root, font=("futura", 12, "bold"))
    w3_label_value.place(x=450, y=380, height=40, width=210)

    # Search button with corrected command
    btn = Button(root, text="Search", font=("futura", 12, "bold"), command=data_get)
    btn.place(x=650, y=85, height=50, width=120)

    # Run the application's main loop
    root.mainloop()
