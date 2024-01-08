import tkinter as tk

def on_click(event):
    current_text=result_var.get()
    button_text=event.widget.cget("text")

    if button_text=="=":
        try:
            result=eval(current_text)
            result_var.set(result)
        except Exception as e:
            result_var.set("Error")
    elif button_text=="C":
        result_var.set("")
    else:
        result_var.set(current_text+button_text)    

#Create the main window
root=tk.Tk()
root.title("Pramuditha - Calculator")

result_var=tk.StringVar()
result_var.set("")

#Creating and entry widget to display the result
result_entry=tk.Entry(root,textvariable=result_var,font=("Helvetica",18),justify="right")
result_entry.grid(row=1,column=5,columnspan=10)

#Button layout
button_layout=[("7",1,0),("8",1,1),("9",1,2),("/",1,3),
               ("4",2,0),("5",2,1),("6",2,2),("*",2,3),
               ("1",3,0),("2",3,1),("3",3,2),("-",3,3),
               ("0",4,0),(".",4,1),("=",4,2),("+",4,3),
               ("C",5,0)
]


#Creating the buttons
for (text,row,column) in button_layout:
    button=tk.Button(root,text=text,font=("Arial",14),padx=20,pady=20)
    button.grid(row=row,column=column,sticky="nsew")
    button.bind("<Button-1>", on_click)

for i in range(6):
    root.grid_rowconfigure(i,weight=1)
    root.grid_columnconfigure(i,weight=1)

root.mainloop()        


