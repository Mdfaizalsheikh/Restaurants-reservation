import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

class RestaurantReservationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Reservation System")

        
        self.reservations = {}
        self.tables = 10

        
        self.create_widgets()

    def create_widgets(self):
        
        self.date_label = tk.Label(self.root, text="Select Date (YYYY-MM-DD):")
        self.date_label.grid(row=0, column=0, padx=10, pady=10)
        self.date_entry = tk.Entry(self.root)
        self.date_entry.grid(row=0, column=1, padx=10, pady=10)


        self.time_label = tk.Label(self.root, text="Select Time (HH:MM):")
        self.time_label.grid(row=1, column=0, padx=10, pady=10)
        self.time_entry = tk.Entry(self.root)
        self.time_entry.grid(row=1, column=1, padx=10, pady=10)

        
        self.book_button = tk.Button(self.root, text="Book Table", command=self.book_table)
        self.book_button.grid(row=2, column=0, columnspan=2, pady=10)

        
        self.view_button = tk.Button(self.root, text="View Reservations", command=self.view_reservations)
        self.view_button.grid(row=3, column=0, columnspan=2, pady=10)

    def book_table(self):
        date_str = self.date_entry.get()
        time_str = self.time_entry.get()

        try:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
            time = datetime.strptime(time_str, "%H:%M").time()
            datetime_res = datetime.combine(date, time)

            if datetime_res < datetime.now():
                messagebox.showerror("Error", "You cannot book a table in the past.")
                return

            if date not in self.reservations:
                self.reservations[date] = []

            daily_reservations = self.reservations[date]
            if len(daily_reservations) >= self.tables:
                messagebox.showerror("Error", "No tables available for this date.")
                return

            
            for reservation in daily_reservations:
                if reservation["time"] == time:
                    messagebox.showerror("Error", "This time slot is already booked.")
                    return

            
            daily_reservations.append({"time": time})
            messagebox.showinfo("Success", f"Table booked for {date_str} at {time_str}.")
        except ValueError:
            messagebox.showerror("Error", "Invalid date or time format.")

    def view_reservations(self):
        reservations_window = tk.Toplevel(self.root)
        reservations_window.title("Reservations")

        row = 0
        for date, daily_reservations in sorted(self.reservations.items()):
            for reservation in sorted(daily_reservations, key=lambda x: x["time"]):
                reservation_label = tk.Label(reservations_window, text=f"{date} at {reservation['time'].strftime('%H:%M')}")
                reservation_label.grid(row=row, column=0, padx=10, pady=5)
                row += 1

        if row == 0:
            empty_label = tk.Label(reservations_window, text="No reservations.")
            empty_label.grid(row=0, column=0, padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantReservationSystem(root)
    root.mainloop()
