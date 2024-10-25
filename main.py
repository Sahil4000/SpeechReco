import speech_recognition as sr
import tkinter as tk
from tkinter import messagebox

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
        
        # Creating form labels and fields
        self.create_field("Full Name", 0)
        self.create_field("Account Number", 1)
        self.create_field("Phone Number", 2)
        self.create_field("Address", 3)
        
        # Submit button
        submit_button = tk.Button(root, text="Submit", command=self.submit_form)
        submit_button.grid(row=5, column=1, pady=10)
        
    def create_field(self, label_text, row):
        label = tk.Label(self.root, text=label_text)
        label.grid(row=row, column=0, padx=10, pady=5, sticky="w")
        entry = tk.Entry(self.root, width=40)
        entry.grid(row=row, column=1, padx=10, pady=5)
        
        # Voice Input button
        voice_button = tk.Button(self.root, text="🎙️", command=lambda e=entry: self.fill_with_voice(e))
        voice_button.grid(row=row, column=2, padx=5, pady=5)
    
    def fill_with_voice(self, entry):
        text = voice_to_text()
        if text:
            entry.delete(0, tk.END)
            entry.insert(0, text)

    def submit_form(self):
        # Get all entries and show as a message box (can replace with form submission functionality)
        info = "\n".join(f"{self.root.grid_slaves(row=i, column=0)[0]['text']}: {self.root.grid_slaves(row=i, column=1)[0].get()}" for i in range(4))
        messagebox.showinfo("Form Submitted", f"Details:\n{info}")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = BankingFormApp(root)
    root.mainloop()
import speech_recognition as sr
import tkinter as tk
from tkinter import messagebox

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
        
        # Creating form labels and fields
        self.create_field("Full Name", 0)
        self.create_field("Account Number", 1)
        self.create_field("Phone Number", 2)
        self.create_field("Address", 3)
        
        # Submit button
        submit_button = tk.Button(root, text="Submit", command=self.submit_form)
        submit_button.grid(row=5, column=1, pady=10)
        
    def create_field(self, label_text, row):
        label = tk.Label(self.root, text=label_text)
        label.grid(row=row, column=0, padx=10, pady=5, sticky="w")
        entry = tk.Entry(self.root, width=40)
        entry.grid(row=row, column=1, padx=10, pady=5)
        
        # Voice Input button
        voice_button = tk.Button(self.root, text="🎙️", command=lambda e=entry: self.fill_with_voice(e))
        voice_button.grid(row=row, column=2, padx=5, pady=5)
    
    def fill_with_voice(self, entry):
        text = voice_to_text()
        if text:
            entry.delete(0, tk.END)
            entry.insert(0, text)

    def submit_form(self):
        # Get all entries and show as a message box (can replace with form submission functionality)
        info = "\n".join(f"{self.root.grid_slaves(row=i, column=0)[0]['text']}: {self.root.grid_slaves(row=i, column=1)[0].get()}" for i in range(4))
        messagebox.showinfo("Form Submitted", f"Details:\n{info}")

# Run the application
if __name__ == "__main__":
    print("running")
    root = tk.Tk()
    app = BankingFormApp(root)
    root.mainloop()


