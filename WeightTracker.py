#Imports tkinter modules
import tkinter as tk
from tkinter import ttk, messagebox
import csv
from datetime import datetime

#Defines the WeightlossstrackerApp class
class WeightLossTrackerApp:
    #State classes for main windows and other variables
    def __init__(self, root):
        self.root = root
        self.root.title("Weight Loss Tracker")
        self.entry_date = None
        self.entry_weight = None
        self.entry_bmi = None
        self.date_combobox = None
        self.date_combobox_2 = None

        self.create_widgets()  #Creates GUI widgets
        self.update_date_combobox()  #Populates date dropdowns (Combobox) with data from the CSV file

    #Check that date is in valid format (DD-MM-YYYY)
    def is_valid_date(self, date_str):
        try:
            #Changes the date to string and checks if valid
            datetime.strptime(date_str, "%d-%m-%Y")
            return True
        except ValueError:
            return False

    #Function to save data to CSV
    def save_data(self):
        date = self.entry_date.get()
        weight = self.entry_weight.get()
        bmi = self.entry_bmi.get()

        if not self.is_valid_date(date):
            messagebox.showerror("Invalid Date", "Please enter a valid date in the format DD-MM-YYYY.")
            return

        try:
            weight = float(weight)
            bmi = float(bmi)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid weight and BMI values.")
            return

        #Append data to the CSV file
        with open("Tracking.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, weight, bmi])

        self.update_date_combobox()  #Update the dropdown with the latest date
        messagebox.showinfo("Success", "Data saved successfully!")

    #Retrieve the date from the CSV file
    def retrieve_data(self):
        date = self.date_combobox.get()

        #Search for the data in the CSV file
        found = False
        with open("Tracking.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == date:
                    found = True
                    weight = float(row[1])
                    bmi = float(row[2])
                    messagebox.showinfo("Data Found", f"Weight: {weight} kg\nBMI: {bmi}")
                    break

        if not found:
            messagebox.showinfo("Data Not Found", "No data found for the selected date.")

    #compare data between two selected dates
    def compare_data(self):
        date1 = self.date_combobox.get()
        date2 = self.date_combobox_2.get()

        #Search for the data in the CSV file
        data1, data2 = None, None
        with open("Tracking.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == date1:
                    data1 = (float(row[1]), float(row[2]))
                elif row and row[0] == date2:
                    data2 = (float(row[1]), float(row[2]))

        if not data1 or not data2:
            messagebox.showinfo("Data Error", "Both selected dates must have data.")
            return

        weight1, bmi1 = data1
        weight2, bmi2 = data2
        weight_diff = weight1 - weight2
        bmi_diff = bmi1 - bmi2

        message = (
            f"Data for {date1}:\nWeight: {weight1} kg\nBMI: {bmi1}\n\n"
            f"Data for {date2}:\nWeight: {weight2} kg\nBMI: {bmi2}\n\n"
            f"Weight Difference: {weight_diff:.2f} kg\nBMI Difference: {bmi_diff:.2f}"
        )

        messagebox.showinfo("Comparison Result", message)

    #Update the dropdown with dates from the CSV file
    def update_date_combobox(self):
        self.date_combobox.set("")  #Clear the current selection
        self.date_combobox_2.set("")  #Clear the current selection
        with open("Tracking.csv", "r") as file:
            reader = csv.reader(file)
            dates = sorted(set(row[0] for row in reader if row))  #Get unique dates and sort them
            self.date_combobox["values"] = dates
            self.date_combobox_2["values"] = dates

    #Create and place labels, entry widgets, and buttons on the GUI
    def create_widgets(self):
        label_date = tk.Label(self.root, text="Date (DD-MM-YYYY):")
        label_date.grid(row=0, column=0)
        self.entry_date = tk.Entry(self.root)
        self.entry_date.grid(row=0, column=1)

        label_weight = tk.Label(self.root, text="Weight (kg):")
        label_weight.grid(row=1, column=0)
        self.entry_weight = tk.Entry(self.root)
        self.entry_weight.grid(row=1, column=1)

        label_bmi = tk.Label(self.root, text="BMI:")
        label_bmi.grid(row=2, column=0)
        self.entry_bmi = tk.Entry(self.root)
        self.entry_bmi.grid(row=2, column=1)

        save_button = tk.Button(self.root, text="Save Data", command=self.save_data)
        save_button.grid(row=3, column=0, columnspan=2)

        retrieve_button = tk.Button(self.root, text="Retrieve Data", command=self.retrieve_data)
        retrieve_button.grid(row=4, column=0, columnspan=2)

        #Create the date dropdowns (Comboboxes)
        self.date_combobox = ttk.Combobox(self.root, values=[], state="readonly")
        self.date_combobox.grid(row=5, column=0, columnspan=2)
        self.date_combobox_2 = ttk.Combobox(self.root, values=[], state="readonly")
        self.date_combobox_2.grid(row=5, column=2, columnspan=2)

        #Create the "Compare" button
        compare_button = tk.Button(self.root, text="Compare", command=self.compare_data)
        compare_button.grid(row=6, column=0, columnspan=4)

#Main function to run the application
def main():
    root = tk.Tk()
    app = WeightLossTrackerApp(root)
    root.mainloop()

main()
