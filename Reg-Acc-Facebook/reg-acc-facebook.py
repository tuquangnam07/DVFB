a = int(input("Nhập Số a: "))
b = int(input("Nhập Số b: "))
phep_tinh = input("Nhập phép tính (+, -, *, /): ")
if phep_tinh == "+":
    print(f"Kết quả: {a} + {b} = {a + b}")
elif phep_tinh == "-":
    print(f"Kết quả: {a} - {b} = {a - b}")
elif phep_tinh == "*":
    print(f"Kết quả: {a} * {b} = {a * b}")
elif phep_tinh == "/":
    if b != 0:
        print(f"Kết quả: {a} / {b} = {a / b}")
    else:
        print("Lỗi: Không thể chia cho 0.")
else:
    print("Phép tính không hợp lệ.")