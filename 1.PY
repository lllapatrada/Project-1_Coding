import tkinter as tk
from tkinter import messagebox

# ฟังก์ชั่นการเปลี่ยนสีเป็นชมพูฟ้า
def rainbow_text(text):
    colors = ["#FF69B4", "#00BFFF"]  # สีชมพูและฟ้า
    colored_text = ""
    for i, char in enumerate(text):
        colored_text += f"<{colors[i % len(colors)]}>{char}</>"
    return colored_text

def calculate():
    try:
        # รับน้ำหนักจากผู้ใช้
        weigh = float(weight_entry.get())
        RER = 70 * weigh**0.75
        
        # แสดงผล RER
        rer_text = f"RER: {RER:.2f} kcal 🐶"
        rer_label.config(text=rer_text, fg="#FF69B4")  # สีชมพู
        
        # เลือกประเภทของสัตว์
        selected_animal = animal_var.get()
        
        # กำหนดปัจจัยตามประเภทของสัตว์
        if selected_animal == 1:
            factor = 2.0
        elif selected_animal == 2:
            factor = 1.5
        elif selected_animal == 3:
            factor = 1.7
        elif selected_animal == 4:
            factor = 1.5
        elif selected_animal == 5:
            factor = 2.0
        elif selected_animal == 6:
            factor = 5.0
        elif selected_animal == 7:
            factor = 1.0
        elif selected_animal == 8:
            factor = 3
        else:
            factor = 1.0
        
        # คำนวณ MER
        MER = RER * factor
        mer_text = f"MER: {MER:.2f} kcal/day 💖"
        mer_label.config(text=mer_text, fg="#00BFFF")  # สีน้ำเงินฟ้า
        
        # เลือกยี่ห้อของอาหาร
        selected_food = food_var.get()
        
        # กำหนดปัจจัยตามยี่ห้อ
        if selected_food == 1:
            food_factor = 1.7
        elif selected_food == 2:
            food_factor = 3.2
        
        # คำนวณ MAX Energy
        MAX_energy = MER / food_factor
        max_energy_text = f"MAX Energy: {MAX_energy:.2f} g/day 🐾"
        max_energy_label.config(text=max_energy_text, fg="#FF69B4")  # สีชมพู
    
    except ValueError:
        messagebox.showerror("Invalid Input", "กรุณากรอกน้ำหนักให้ถูกต้องค่ะ! 😿")

# สร้างหน้าต่างหลักของ GUI
root = tk.Tk()
root.title("คำนวณพลังงานสำหรับสัตว์เลี้ยง")

# สร้าง widget ต่างๆ
weight_label = tk.Label(root, text="กรุณาป้อนน้ำหนัก (กิโลกรัม):", font=("Arial", 12), fg="#FF69B4")  # สีชมพู
weight_label.pack()

weight_entry = tk.Entry(root, font=("Arial", 12))
weight_entry.pack()

# การเลือกประเภทสัตว์
animal_label = tk.Label(root, text="กรุณาเลือกประเภทของสัตว์:", font=("Arial", 12), fg="#00BFFF")  # สีน้ำเงินฟ้า
animal_label.pack()

animal_var = tk.IntVar()
animal_options = [
    "ลูกสัตว์อายุน้อยกว่า 4 เดือน 🐾",
    "ลูกสัตว์อายุ 4-6 เดือน 🐱",
    "สัตว์โตเต็มวัย (ทำหมันเเล้ว) 🐶",
    "สัตว์โตเต็มวัย (ยังไม่ทำหมัน) 🐕",
    "สัตว์ใช้เเรงงานปานกลาง 🐩",
    "สัตว์ใช้เเรงงานมาก 🐕‍🦺",
    "สัตว์ต้องการลดน้ำหนัก 🐈",
    "สัตว์ตั้งครรภ์/แม่ลูกอ่อน 🐾"
]

for idx, option in enumerate(animal_options, 1):
    tk.Radiobutton(root, text=option, variable=animal_var, value=idx, font=("Arial", 10)).pack()

# การเลือกยี่ห้ออาหาร
food_label = tk.Label(root, text="กรุณาเลือกยี่ห่อของผลิตภัณฑ์:", font=("Arial", 12), fg="#FF69B4")  # สีชมพู
food_label.pack()

food_var = tk.IntVar()
food_options = ["Smartheart 🍖", "Pedigree 🦴"]

for idx, option in enumerate(food_options, 1):
    tk.Radiobutton(root, text=option, variable=food_var, value=idx, font=("Arial", 10)).pack()

# ปุ่มคำนวณ
calculate_button = tk.Button(root, text="คำนวณ 💥", command=calculate, font=("Arial", 14), bg="#FF69B4", fg="white")  # สีชมพู
calculate_button.pack()

# แสดงผลลัพธ์
rer_label = tk.Label(root, text="RER: - kcal 🐶", font=("Arial", 14), fg="#FF69B4")  # สีชมพู
rer_label.pack()

mer_label = tk.Label(root, text="MER: - kcal/day 💖", font=("Arial", 14), fg="#00BFFF")  # สีน้ำเงินฟ้า
mer_label.pack()

max_energy_label = tk.Label(root, text="MAX Energy: - g/day 🐾", font=("Arial", 14), fg="#FF69B4")  # สีชมพู
max_energy_label.pack()

# เริ่มการทำงานของ GUI
root.mainloop()