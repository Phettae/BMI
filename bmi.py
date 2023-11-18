def calculate_bmi(weight, height):
    return weight / (height ** 2) #ยกกำลัง 2 /w/h

def determine_bmi_category(bmi):
    if bmi >= 40:
        return "อ้วนขั้นสูงสุด"
    elif bmi >= 35:
        return "อ้วนขั้นที่ 2"
    elif bmi >= 28.5:
        return "อ้วนขั้นที่ 1"
    elif bmi >= 23.5:
        return "น้ำหนักเกิน"
    elif bmi >= 18.5:
        return "อยู่ในเกณฑ์ปกติ"
    else:
        return "น้ำหนักต่ำกว่าเกณฑ์"

while True:
    weight = float(input("โปรดป้อนน้ำหนักของคุณ (กิโลกรัม): ")) #ป้อน
    height = float(input("โปรดป้อนส่วนสูงของคุณ (เมตร): "))

    bmi = calculate_bmi(weight, height)
    category = determine_bmi_category(bmi)

    print(f"ค่า BMI ของคุณคือ {bmi:.2f} ซึ่งอยู่ในกลุ่ม: {category}")

    repeat = input("ต้องการทำการคำนวณอีกหรือไม่? (yes/no): ") #ทำงานอีกครั้ง
    if repeat.lower() != "yes":
        break
