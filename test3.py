import tkinter as tk
from tkinter import ttk, messagebox
import csv

class WeightLossTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weight Loss Tracker")
        self.entry_date = None
        self.entry_weight = None
        self.entry_bmi = None
        self.date_combobox = None
        self.date_combobox_2 = None

        self.create_widgets()
        self.update_date_combobox()

    def save_data(self):
        # Function to save data to a CSV file
        date = self.entry_date.get()
        weight = float(self.entry_weight.get())
        bmi = float(self.entry_bmi.get())

        # Append data to the CSV file
        with open("test4.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, weight, bmi])

        self.update_date_combobox()  # Update the dropdown with the latest date
        messagebox.showinfo("Success", "Data saved successfully!")

    def retrieve_data(self):
        # Function to retrieve data from the CSV file based on the selected date
        date = self.date_combobox.get()

        # Search for the data in the CSV file
        found = False
        with open("test4.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == date:
                    found = True
                    weight = float(row[1])
                    bmi = float(row[2])
                    messagebox.showinfo("Data Found", f"Weight: {weight} kg\nBMI: {bmi}")
                    # Add code to compare results and calculate weight loss here
                    # Display the weight loss result using a messagebox or other means
                    break

        if not found:
            messagebox.showinfo("Data Not Found", "No data found for the selected date.")

    def compare_data(self):
        # Function to compare data between two selected dates
        date1 = self.date_combobox.get()
        date2 = self.date_combobox_2.get()

        # Search for the data in the CSV file
        data1, data2 = None, None
        with open("test4.csv", "r") as file:
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

    def update_date_combobox(self):
        # Function to update the dropdown with dates from the CSV file
        self.date_combobox.set("")  # Clear the current selection
        self.date_combobox_2.set("")  # Clear the current selection
        with open("test4.csv", "r") as file:
            reader = csv.reader(file)
            dates = sorted(set(row[0] for row in reader if row))  # Get unique dates and sort them
            self.date_combobox["values"] = dates
            self.date_combobox_2["values"] = dates

    def create_widgets(self):
        # Create and place labels, entry widgets, and buttons
        label_date = tk.Label(self.root, text="Date (YYYY-MM-DD):")
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

        # Create the date dropdowns (Comboboxes)
        self.date_combobox = ttk.Combobox(self.root, values=[], state="readonly")
        self.date_combobox.grid(row=5, column=0, columnspan=2)
        self.date_combobox_2 = ttk.Combobox(self.root, values=[], state="readonly")
        self.date_combobox_2.grid(row=5, column=2, columnspan=2)

        # Create the "Compare" button
        compare_button = tk.Button(self.root, text="Compare", command=self.compare_data)
        compare_button.grid(row=6, column=0, columnspan=4)

def main():
    root = tk.Tk()
    app = WeightLossTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
