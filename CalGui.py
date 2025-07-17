import tkinter as tk

#Function to do all the maths
def click(event):
    current = entry.get() #get the input from the entry box
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(current) #if the user has pressed = then evaluate the whole string
            entry.delete(0 , tk.END) #delete the previous entry so that user dont have to delete manually
            entry.insert(tk.END , str(result))
        except:
            entry.delete(0 , tk.END)
            entry.insert(tk.END , "Error")
    elif text == "C":
        entry.delete(0 , tk.END)
    elif text == "⌫":
        entry.delete(len(current)-1 , tk.END)
    else:
        entry.insert(tk.END , text) #Else just keep inserting unless user press =

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

#Entry widget so that user can enter data
entry = tk.Entry(root , font="Aerial 20" , borderwidth=5 , relief = tk.RIDGE)
entry.pack(padx=5 , pady=5 , fill=tk.BOTH)

#Now buttons 2d array
Buttons = [
    ["7" , "8" , "9" , "/"],
    ["4" , "5" , "6" , "*"],
    ["1" , "2" , "3" , "-"],
    ["C" , "0" , "=" , "+"],
    ["⌫"]
]

#Make frame for each row and for each column set the height , font etc
for row in Buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True , fill="both")
    for item in row:
        btn = tk.Button(frame , text=item , font="Aerial 18" , height=2 , width=5 , relief=tk.RIDGE)
        btn.pack(side = "left" ,expand=True , fill="both")
        btn.bind("<Button-1>" , click) #add the function

root.mainloop()