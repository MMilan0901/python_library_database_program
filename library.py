import pandas as pd
import tkinter as tk

# The database of the library
library_data = {'ID': ['0321', '8346', '9181', '4501', '0069', '9921'],
                'Title': ['On the Road', 'Winnetou', 'Old Man and the Sea', 'Little Cookbook', 'Winnie and the Pooh', 'Calculus I.'],
                'Author': ['Jack Kerouac', 'Karl May', 'Ernest Heminghway', 'Jane Doe', 'A. A. Milne', 'Dr. John Doe Phd.'],
                'Genre': ['Novel', 'Novel', 'Novel', 'Cooking', 'Children', 'Science'],
                'Section': ['A255', 'A798', 'A111', 'Z811', 'K991', 'W815'],
                'Lent': [True, False, False, True, False, True]}

df = pd.DataFrame(library_data)

# Creating the GUI application

def app_details():
    book = entry_bookID.get().strip()

    book_data = df[df['ID'] == book]

    details = tk.Toplevel(root)
    details.title("Library Database Program")
    details.geometry("500x400")

    if not book_data.empty:
        book_info = f"""
        Book ID: {book_data.iloc[0]['ID']}
        Title: {book_data.iloc[0]['Title']}
        Author: {book_data.iloc[0]['Author']}
        Genre: {book_data.iloc[0]['Genre']}
        Section: {book_data.iloc[0]['Section']}
        Lent: {'Yes' if book_data.iloc[0]['Lent'] else 'No'}
        """
    else:
        book_info = "Book not found. Please check the Book ID."

    book_label = tk.Label(details, text=book_info, justify="left")
    book_label.pack(pady=20, padx=20)
    

def app_exit():
    root.destroy()

root = tk.Tk()
root.title("Library Database Program")
root.geometry("500x400")

label_bookID = tk.Label(root, text="Book ID: ")
label_bookID.pack(pady=10)
entry_bookID = tk.Entry(root)
entry_bookID.pack()

button_lend = tk.Button(root, text="Show details", command=app_details)
button_lend.pack()

button_exit = tk.Button(root, text="Exit", command=app_exit)
button_exit.pack()

root.mainloop()


