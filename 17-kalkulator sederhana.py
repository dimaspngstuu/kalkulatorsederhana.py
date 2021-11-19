
angka_1 = float(input("masukan angka 1 ="))
operator = input("masukan +,/,-,* =")
angka_2 = float(input("masukan angka 2 ="))

if operator == "+" :
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah = {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah = {hasil} ")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah = {hasil} ")
elif operator == "*" or operator == "x":
    hasil = angka_1 * angka_2
    print(f"hasilnya adalah = {hasil} ")
else :
    print("maaf,syntax anda error")
print("terima kasih")
    