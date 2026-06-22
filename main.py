from tkinter import *
import Flightapi

# ---------------- WINDOW ---------------- #

window = Tk()
window.title("Flight Search")
window.geometry("700x500")
window.config(bg="#F5F7FA")
window.resizable(False, False)

# ---------------- HEADER ---------------- #

header = Frame(window, bg="#1E3A8A", height=70)
header.pack(fill="x")

title = Label(
    header,
    text="✈ Flight Search",
    font=("Segoe UI", 22, "bold"),
    bg="#1E3A8A",
    fg="white"
)
title.pack(pady=15)

# ---------------- MAIN CARD ---------------- #

card = Frame(
    window,
    bg="white",
    bd=1,
    relief="solid"
)
card.pack(padx=25, pady=30, fill="both", expand=True)

# ---------------- RESULTS TITLE ---------------- #

results_label = Label(
    card,
    text="Cheapest Flight",
    font=("Segoe UI", 16, "bold"),
    bg="white",
    fg="#1F2937"
)
results_label.pack(pady=(20, 10))

# ---------------- FLIGHT INFO ---------------- #

flight_info = Label(
    card,
    text=str(Flightapi.cheapest_flights),
    font=("Segoe UI", 12),
    bg="white",
    fg="#374151",
    wraplength=600,
    justify="left"
)
flight_info.pack(padx=20, pady=10)

# ---------------- FOOTER ---------------- #

footer = Label(
    window,
    text="Powered by Flight API",
    font=("Segoe UI", 9),
    bg="#F5F7FA",
    fg="gray"
)
footer.pack(pady=10)

window.mainloop()