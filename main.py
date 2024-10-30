import speech_recognition as sr
import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to capture voice input and convert it to text
def voice_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for voice input...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"Recognized Text: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand the audio")
            messagebox.showwarning("Warning", "Could not understand the audio. Please try again.")
        except sr.RequestError:
            print("Error with the API")
            messagebox.showerror("Error", "There was an issue with the Speech Recognition API. Check your connection.")

# GUI form for banking sector data
class BankingFormApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Banking Sector Form")

        # Connect to SQLite database
        self.conn = sqlite3.connect("form_data.db")
        self.cursor = self.conn.cursor()
        
        # Create table with additional columns for Adhaar Card and Withdraw Amount
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY,
            full_name TEXT,
            account_number TEXT,
            phone_number TEXT,
            address TEXT,
            adhaar_card TEXT,
            withdraw_amount REAL
        )''')
        self.conn.commit()
        
        # Create form labels, fields, and store entry widgets in a list
        self.entries = []
        self.create_field("Full Name", 0)
        self.create_field("Account Number", 1)
        self.create_field("Phone Number", 2)
        self.create_field("Address", 3)
        self.create_field("Adhaar Card", 4)
        self.create_field("Withdraw Amount", 5)
        
        # Submit button
        submit_button = tk.Button(root, text="Submit", command=self.submit_form)
        submit_button.grid(row=7, column=1, pady=10)
        
    def create_field(self, label_text, row):
        label = tk.Label(self.root, text=label_text)
        label.grid(row=row, column=0, padx=10, pady=5, sticky="w")
        entry = tk.Entry(self.root, width=40)
        entry.grid(row=row, column=1, padx=10, pady=5)
        self.entries.append(entry)  # Store entry widget reference
        
        # Voice Input button
        voice_button = tk.Button(self.root, text="🎙️", command=lambda e=entry: self.fill_with_voice(e))
        voice_button.grid(row=row, column=2, padx=5, pady=5)

    def fill_with_voice(self, entry):
        text = voice_to_text()
        if text:
            entry.delete(0, tk.END)
            entry.insert(0, text)

    def submit_form(self):
        # Retrieve data directly from each entry widget in self.entries
        fields = [entry.get() for entry in self.entries]
        
        # Validate withdraw amount as a numeric value
        try:
            fields[5] = float(fields[5])  # Convert withdraw amount to float
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid numeric value for Withdraw Amount.")
            return

        # Display form data
        info = "\n".join(f"{self.root.grid_slaves(row=i, column=0)[0]['text']}: {fields[i]}" for i in range(6))
        messagebox.showinfo("Form Submitted", f"Details:\n{info}")

        # Insert data into SQLite database with new fields
        self.cursor.execute(
            "INSERT INTO submissions (full_name, account_number, phone_number, address, adhaar_card, withdraw_amount) VALUES (?, ?, ?, ?, ?, ?)", 
            fields
        )
        self.conn.commit()


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = BankingFormApp(root)
    root.mainloop()
