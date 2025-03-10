import tkinter as tk
from tkinter import ttk, messagebox

def calculate():
    try:
        weight = float(entry_weight.get())
        RER = 70 * weight ** 0.75
        animal_type = combo_animal.get()
        food_brand = combo_food.get()
        
        factor = factors.get(animal_type, 1.0)
        MER = RER * factor
        kcal_per_g = food_energy_per_gram.get(food_brand, 3.5)
        food_amount = MER / kcal_per_g
        
        result_label.config(text=f"🌟 ผลลัพธ์ 🌟\n🐶 RER: {RER:.2f} kcal\n🐱 MER: {MER:.2f} kcal/day\n🥣 อาหารที่ต้องกิน: {food_amount:.2f} g/day 🍗")
    except ValueError:
        messagebox.showerror("ข้อผิดพลาด", "กรุณาป้อนน้ำหนักให้ถูกต้อง")

root = tk.Tk()
root.title("คำนวณปริมาณอาหารสำหรับสัตว์เลี้ยง 🐾")
root.geometry("400x500")
root.configure(bg="#FFF5E1")

style = ttk.Style()
style.configure("TLabel", foreground="#FF69B4", background="#FFF5E1", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12))
style.configure("TCombobox", background="#FFD1DC", foreground="black", font=("Arial", 12))

factors = {
    "ลูกสัตว์อายุน้อยกว่า 4 เดือน 🐾": 2.0,
    "ลูกสัตว์อายุ 4-6 เดือน 🐾": 1.5,
    "สัตว์โตเต็มวัย (ทำหมันแล้ว) 🐾": 1.7,
    "สัตว์โตเต็มวัย (ยังไม่ทำหมัน) 🐾": 1.5,
    "สัตว์ใช้แรงงานปานกลาง ⚖️": 2.0,
    "สัตว์ใช้แรงงานมาก ⚖️": 5.0,
    "สัตว์ต้องการลดน้ำหนัก 🏃": 1.0,
    "สัตว์ตั้งครรภ์/แม่ลูกอ่อน ✨": 3.0
}

food_energy_per_gram = {
    "Smartheart ⭐": 3.5,
    "Pedigree 🐾": 3.2
}

label_weight = ttk.Label(root, text="🐾 น้ำหนักสัตว์เลี้ยง (กก.)")
label_weight.pack(pady=5)
entry_weight = ttk.Entry(root)
entry_weight.pack(pady=5)

label_animal = ttk.Label(root, text="🐾 ประเภทของสัตว์")
label_animal.pack(pady=5)
combo_animal = ttk.Combobox(root, values=list(factors.keys()), state="readonly")
combo_animal.pack(pady=5)

label_food = ttk.Label(root, text="🍲 ยี่ห้ออาหาร")
label_food.pack(pady=5)
combo_food = ttk.Combobox(root, values=list(food_energy_per_gram.keys()), state="readonly")
combo_food.pack(pady=5)

button_calculate = ttk.Button(root, text="⚖️ คำนวณ", command=calculate)
button_calculate.pack(pady=10)

result_label = ttk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()




