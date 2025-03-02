import tkinter as tk
from tkinter import messagebox

# ฟังก์ชันการคำนวณ RER, MER, MAX_energy
def calculate():
    try:
        # รับน้ำหนักจากผู้ใช้
        weigh = float(weight_entry.get())
        RER = 70 * weigh ** 0.75
        RER_label.config(text=f"RER: {RER:.2f} kcal 🐾")

        # เลือกประเภทของสัตว์
        animal_type = animal_choice.get()
        if animal_type == 1:
            factor = 2.0
        elif animal_type == 2:
            factor = 1.5
        elif animal_type == 3:
            factor = 1.7
        elif animal_type == 4:
            factor = 1.5
        elif animal_type == 5:
            factor = 2.0
        elif animal_type == 6:
            factor = 5.0
        elif animal_type == 7:
            factor = 1.0
        elif animal_type == 8:
            factor = 3.0
        else:
            factor = 1.0

        MER = RER * factor
        MER_label.config(text=f"MER: {MER:.2f} kcal/day 🐕")

        # เลือกยี่ห้อของผลิตภัณฑ์
        food_brand = food_choice.get()
        if food_brand == 1:
            brand_factor = 1.7
        elif food_brand == 2:
            brand_factor = 3.2
        else:
            brand_factor = 1.0

        MAX_energy = MER / brand_factor
        MAX_energy_label.config(text=f"MAX Energy: {MAX_energy:.2f} g/day 🍽️")

    except ValueError:
        messagebox.showerror("Error", "กรุณาป้อนข้อมูลให้ถูกต้อง 😞")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("การคำนวณพลังงานสำหรับสัตว์เลี้ยง 🐾")
root.geometry("400x600")
root.config(bg="#F4C2C2")

# ข้อความแนะนำ
label = tk.Label(root, text="กรุณาป้อนน้ำหนัก (กิโลกรัม) 🐱:", font=("Arial", 14), bg="#F4C2C2", fg="#1E90FF")
label.pack(pady=10)

# ช่องกรอกน้ำหนัก
weight_entry = tk.Entry(root, font=("Arial", 14))
weight_entry.pack(pady=10)

# ส่วนเลือกประเภทของสัตว์
animal_label = tk.Label(root, text="กรุณาเลือกประเภทของสัตว์ 🐶:", font=("Arial", 14), bg="#F4C2C2", fg="#FF69B4")
animal_label.pack(pady=10)

animal_choice = tk.IntVar()
animal_options = [
    "ลูกสัตว์อายุน้อยกว่า 4 เดือน 🍼", 
    "ลูกสัตว์อายุ 4-6 เดือน 🐾", 
    "สัตว์โตเต็มวัย (ทำหมันเเล้ว) 🐕", 
    "สัตว์โตเต็มวัย (ยังไม่ทำหมัน) 🐈", 
    "สัตว์ใช้เเรงงานปานกลาง 💪", 
    "สัตว์ใช้เเรงงานมาก 🔥", 
    "สัตว์ต้องการลดน้ำหนัก 🐾", 
    "สัตว์ตั้งครรภ์/แม่ลูกอ่อน 🤰"
]

for i, option in enumerate(animal_options):
    tk.Radiobutton(root, text=option, variable=animal_choice, value=i+1, font=("Arial", 12), bg="#F4C2C2", fg="#FF69B4").pack()

# ส่วนเลือกยี่ห้อของผลิตภัณฑ์
food_label = tk.Label(root, text="กรุณาเลือกยี่ห้อของผลิตภัณฑ์ 🍲:", font=("Arial", 14), bg="#F4C2C2", fg="#1E90FF")
food_label.pack(pady=10)

food_choice = tk.IntVar()
food_options = ["Smartheart 🐾", "Pedigree 🐶"]
for i, option in enumerate(food_options):
    tk.Radiobutton(root, text=option, variable=food_choice, value=i+1, font=("Arial", 12), bg="#F4C2C2", fg="#1E90FF").pack()

# ปุ่มคำนวณ
calculate_button = tk.Button(root, text="คำนวณ ✨", font=("Arial", 14), bg="#FF69B4", fg="white", command=calculate)
calculate_button.pack(pady=20)

# แสดงผลลัพธ์
RER_label = tk.Label(root, text="RER: 0 kcal", font=("Arial", 14), bg="#F4C2C2", fg="#1E90FF")
RER_label.pack(pady=10)

MER_label = tk.Label(root, text="MER: 0 kcal/day", font=("Arial", 14), bg="#F4C2C2", fg="#FF69B4")
MER_label.pack(pady=10)

MAX_energy_label = tk.Label(root, text="MAX Energy: 0 g/day", font=("Arial", 14), bg="#F4C2C2", fg="#1E90FF")
MAX_energy_label.pack(pady=10)

# เริ่มต้น UI
root.mainloop()
