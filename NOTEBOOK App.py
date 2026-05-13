import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def save_note():
    
    note_content = text_area.get("1.0", "end-1c")
    
    if note_content.strip() == "":
        messagebox.showwarning("Empty Note", "Please write something first!")
        return

    now = datetime.now()
    date_string = now.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"note_{date_string}.txt"

    # Save as a text file
    with open(filename, "w", encoding="utf-8") as file:
        file.write(note_content)

    messagebox.showinfo("Success", f"Your note has been saved as '{filename}'!")
    text_area.delete("1.0", "end") 

# Create App Window
root = tk.Tk()
root.title("My Notebook")
root.geometry("400x450")

# Label
label = tk.Label(root, text="Write your note below:", font=("Arial", 12, "bold"))
label.pack(pady=10)

# Text Area (Text Box)
text_area = tk.Text(root, font=("Arial", 12), height=15, width=40)
text_area.pack(padx=20, pady=5)

# Save Button
save_btn = tk.Button(root, text="Save Note", bg="#4CAF50", fg="white", 
                     font=("Arial", 10, "bold"), command=save_note)
save_btn.pack(pady=15)

root.mainloop()
