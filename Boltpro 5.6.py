# =========================
# BOLTPRO ENGINEERING SUITE
# =========================

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# =========================
# ROOT WINDOW
# =========================

root = tk.Tk()

# ซ่อนหน้าหลักก่อน
root.withdraw()

# =========================
# SPLASH SCREEN
# =========================

splash = tk.Toplevel()

splash.overrideredirect(True)

splash.configure(bg="white")

# ขนาด splash
splash_width = 500
splash_height = 500

# จัดกลางจอ
screen_width = splash.winfo_screenwidth()
screen_height = splash.winfo_screenheight()

x = int((screen_width / 2) - (splash_width / 2))
y = int((screen_height / 2) - (splash_height / 2))

splash.geometry(
    f"{splash_width}x{splash_height}+{x}+{y}"
)

# =========================
# LOAD LOGO
# =========================

# ไฟล์โลโก้ต้องชื่อ:
# boltpro_logo.png
# และอยู่โฟลเดอร์เดียวกับ main.py

image = Image.open("boltpro_logo.png")

image = image.resize((280, 280))

logo = ImageTk.PhotoImage(image)

logo_label = tk.Label(
    splash,
    image=logo,
    bg="white"
)

logo_label.pack(
    pady=(70, 20)
)

# =========================
# APP TITLE
# =========================

title = tk.Label(
    splash,
    text="BoltPro",
    bg="white",
    fg="#ff8800",
    font=("Arial", 28, "bold")
)

title.pack()

subtitle = tk.Label(
    splash,
    text="Engineering Suite",
    bg="white",
    fg="#666666",
    font=("Arial", 12)
)

subtitle.pack(
    pady=(5, 0)
)

# =========================
# BOLT SIZES
# =========================

bolt_sizes = {
    "M4": 0.004,
    "M5": 0.005,
    "M6": 0.006,
    "M8": 0.008,
    "M10": 0.010,
    "M12": 0.012,
    "M14": 0.014,
    "M16": 0.016,
    "M18": 0.018,
    "M20": 0.020
}

# =========================
# MATERIALS
# =========================

materials = {
    "Steel": {
        "4.6": 4000,
        "8.8": 8000,
        "10.9": 12000,
        "12.9": 15000
    },

    "Stainless": {
        "304": 5200,
        "316": 5800
    },

    "Aluminum": {
        "6061": 3100,
        "7075": 5500
    },

    "Titanium": {
        "Grade 2": 9000,
        "Grade 5": 14000
    },

    "Brass": {
        "Standard": 2500
    }
}

# =========================
# UPDATE GRADES
# =========================

def update_grades(event=None):

    material = material_var.get()

    grades = list(
        materials[material].keys()
    )

    grade_combo["values"] = grades

    if grades:
        grade_combo.set(grades[0])

# =========================
# RESULT PAGE
# =========================

def show_result_window(result_text):

    main_frame.pack_forget()

    result_frame = tk.Frame(
        root,
        bg="#202124"
    )

    result_frame.pack(
        fill="both",
        expand=True
    )

    # HEADER
    header = tk.Frame(
        result_frame,
        bg="#ff8800",
        height=65
    )

    header.pack(fill="x")

    header.pack_propagate(False)

    title = tk.Label(
        header,
        text="Calculation Result",
        bg="#ff8800",
        fg="white",
        font=("Arial", 18, "bold")
    )

    title.pack(pady=16)

    # RESULT BOX
    result_box = tk.Label(
        result_frame,
        text=result_text,
        bg="#2b2b2b",
        fg="white",
        justify="left",
        anchor="nw",
        font=("Consolas", 12),
        padx=20,
        pady=20
    )

    result_box.pack(
        padx=25,
        pady=25,
        fill="both",
        expand=True
    )

    # BACK BUTTON
    def go_back():

        result_frame.destroy()

        main_frame.pack(
            fill="both",
            expand=True
        )

    ttk.Button(
        result_frame,
        text="BACK",
        command=go_back
    ).pack(
        fill="x",
        padx=25,
        pady=(0, 25)
    )

# =========================
# CALCULATE
# =========================

def calculate():

    size = bolt_var.get()
    material = material_var.get()
    grade = grade_var.get()
    length_text = entry_length.get()

    if not size or not material or not grade or not length_text:

        messagebox.showerror(
            "Error",
            "Please fill all fields"
        )

        return

    try:

        length = float(length_text)

        d = bolt_sizes[size]

        F = materials[material][grade]

        K = float(
            k_var.get().split(" - ")[0]
        )

        # Torque
        T = K * F * d

        # lb-ft
        lbft = T * 0.73756

        # Clamp Force
        clamp_force = T / (K * d)

        result = f"""
SYSTEM READY

Material : {material}
Bolt Size : {size}
Grade     : {grade}
Length    : {length} mm

K Factor  : {K}

========================

Torque
{T:.2f} N·m

{lbft:.2f} lb-ft

========================

Clamp Force
{clamp_force:.2f} N
"""

        show_result_window(result)

    except ValueError:

        messagebox.showerror(
            "Error",
            "Invalid number"
        )

# =========================
# CLEAR
# =========================

def clear():

    entry_length.delete(0, tk.END)

    bolt_combo.set("M6")

    material_combo.set("Steel")

    update_grades()

    k_combo.set(
        "0.20 - Dry Bolt"
    )

# =========================
# OPEN MAIN APP
# =========================

def open_main():

    splash.destroy()

    root.deiconify()

# เปิดหลัง 2 วิ
root.after(2000, open_main)

# =========================
# MAIN WINDOW
# =========================

root.title(
    "BoltPro Engineering Suite"
)

root.geometry("390x844")

root.configure(bg="#202124")

# =========================
# STYLE
# =========================

style = ttk.Style()

style.theme_use("clam")

# LABEL
style.configure(
    "TLabel",
    background="#2b2b2b",
    foreground="white",
    font=("Arial", 12)
)

# BUTTON
style.configure(
    "TButton",
    background="#3a3a3a",
    foreground="white",
    font=("Arial", 12),
    padding=14
)

style.map(
    "TButton",
    background=[
        ("active", "#505050")
    ]
)

# ACCENT BUTTON
style.configure(
    "Accent.TButton",
    background="#ff8800",
    foreground="white",
    font=("Arial", 12, "bold"),
    padding=14
)

style.map(
    "Accent.TButton",
    background=[
        ("active", "#ffaa33")
    ]
)

# COMBOBOX
style.configure(
    "TCombobox",
    fieldbackground="#3a3a3a",
    background="#3a3a3a",
    foreground="white"
)

# DARK DROPDOWN
root.option_add(
    "*TCombobox*Listbox.background",
    "#2b2b2b"
)

root.option_add(
    "*TCombobox*Listbox.foreground",
    "white"
)

root.option_add(
    "*TCombobox*Listbox.selectBackground",
    "#ff8800"
)

root.option_add(
    "*TCombobox*Listbox.selectForeground",
    "white"
)

# =========================
# MAIN FRAME
# =========================

main_frame = tk.Frame(
    root,
    bg="#202124"
)

main_frame.pack(
    fill="both",
    expand=True
)

# =========================
# HEADER
# =========================

header = tk.Frame(
    main_frame,
    bg="#ff8800",
    height=65
)

header.pack(fill="x")

header.pack_propagate(False)

header_title = tk.Label(
    header,
    text="BoltPro Engineering Suite",
    bg="#ff8800",
    fg="white",
    font=("Arial", 18, "bold")
)

header_title.pack(pady=16)

# =========================
# INPUT FRAME
# =========================

input_frame = tk.LabelFrame(
    main_frame,
    text=" Bolt Configuration ",
    bg="#2b2b2b",
    fg="white",
    font=("Arial", 11, "bold"),
    bd=2
)

input_frame.pack(
    padx=28,
    pady=25,
    fill="both"
)

# =========================
# BOLT SIZE
# =========================

ttk.Label(
    input_frame,
    text="Bolt Size"
).pack(
    pady=(20, 8)
)

bolt_var = tk.StringVar()

bolt_combo = ttk.Combobox(
    input_frame,
    textvariable=bolt_var,
    values=list(bolt_sizes.keys()),
    state="readonly"
)

bolt_combo.pack(
    pady=8,
    padx=20,
    ipady=8,
    fill="x"
)

bolt_combo.set("M6")

# =========================
# MATERIAL
# =========================

ttk.Label(
    input_frame,
    text="Material"
).pack(
    pady=(20, 8)
)

material_var = tk.StringVar()

material_combo = ttk.Combobox(
    input_frame,
    textvariable=material_var,
    values=list(materials.keys()),
    state="readonly"
)

material_combo.pack(
    pady=8,
    padx=20,
    ipady=8,
    fill="x"
)

material_combo.set("Steel")

material_combo.bind(
    "<<ComboboxSelected>>",
    update_grades
)

# =========================
# GRADE
# =========================

ttk.Label(
    input_frame,
    text="Material Grade"
).pack(
    pady=(20, 8)
)

grade_var = tk.StringVar()

grade_combo = ttk.Combobox(
    input_frame,
    textvariable=grade_var,
    values=[],
    state="readonly"
)

grade_combo.pack(
    pady=8,
    padx=20,
    ipady=8,
    fill="x"
)

update_grades()

# =========================
# K VALUE
# =========================

ttk.Label(
    input_frame,
    text="K Factor"
).pack(
    pady=(20, 8)
)

k_var = tk.StringVar()

k_combo = ttk.Combobox(
    input_frame,
    textvariable=k_var,
    values=[
        "0.10 - Heavy Grease",
        "0.15 - Light Oil",
        "0.20 - Dry Bolt",
        "0.25 - Rust/Friction"
    ],
    state="readonly"
)

k_combo.pack(
    pady=8,
    padx=20,
    ipady=8,
    fill="x"
)

k_combo.set(
    "0.20 - Dry Bolt"
)

# =========================
# THREAD LENGTH
# =========================

ttk.Label(
    input_frame,
    text="Thread Length (mm)"
).pack(
    pady=(20, 8)
)

entry_length = tk.Entry(
    input_frame,
    bg="#3a3a3a",
    fg="white",
    insertbackground="white",
    relief="flat",
    font=("Arial", 12)
)

entry_length.pack(
    pady=(8, 25),
    padx=20,
    ipady=12,
    fill="x"
)

# =========================
# CALCULATE BUTTON
# =========================

ttk.Button(
    main_frame,
    text="CALCULATE",
    style="Accent.TButton",
    command=calculate
).pack(
    fill="x",
    padx=28,
    pady=(15, 10)
)

# =========================
# CLEAR BUTTON
# =========================

ttk.Button(
    main_frame,
    text="CLEAR",
    command=clear
).pack(
    fill="x",
    padx=28,
    pady=8
)

# =========================
# FOOTER
# =========================

footer = tk.Label(
    main_frame,
    text="BoltPro v3.0",
    bg="#202124",
    fg="#888888",
    font=("Arial", 9)
)

footer.pack(
    pady=(20, 10)
)

# =========================
# START
# =========================

root.mainloop()