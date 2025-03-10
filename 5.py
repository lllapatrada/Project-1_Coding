weigh = int(input("กรุณาป้อนน้ำหนัก (กิโลกรัม): "))
RER = 70*weigh**0.75

print("RER", "{:.2f}".format(RER), "kcal")
print("\nกรุณาเลือกประเภทของสัตว์:")
print("1: ลูกสัตว์อายุน้อยกว่า 4 เดือน")
print("2: ลูกสัตว์อายุ 4-6 เดือน")
print("3: สัตว์โตเต็มวัย (ทำหมันเเล้ว)")
print("4: สัตว์โตเต็มวัย (ยังไม่ทำหมัน)")
print("5: สัตว์ใช้เเรงงานปานกลาง")
print("6: สัตว์ใช้เเรงงานมาก")
print("7: สัตว์ต้องการลดน้ำหนัก")
print("8: สัตว์ตั้งครรภ์/แม่ลูกอ่อน")
choose_number = int(input("กรุณาป้อนหมายเลข: "))

if choose_number == 1:
    factor = 2.0
elif choose_number == 2:
    factor = 1.5
elif choose_number == 3:
    factor = 1.7
elif choose_number == 4:
    factor = 1.5
elif choose_number == 5:
    factor = 2.0
elif choose_number == 6:
    factor = 5.0
elif choose_number == 7:
    factor = 1.0
elif choose_number == 8:
    factor = 3

else:
    factor = 1.0

MER = RER*factor
print("MER", "{:.2f}".format(MER), "kcal/day")
print("\nกรุณาเลือกยี่ห่อของผลิตภัณฑ์:")


print("1: Smartheart")
print("2: Pedigree")
Choose_food_brand= int(input("กรุณาป้อนหมายเลข: "))

if choose_number == 1:
    factor = 1.7
elif choose_number == 2:
    factor = 3.2

MAX_energy  =MER/Choose_food_brand
print(" MAX_energy", "{:.2f}".format(MAX_energy), "g/day")