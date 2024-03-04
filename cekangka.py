
def cek_angka(a, b, c):
    if a != b and a != c and b != c:
        if a + b == c or a + c == b or b + c == a:
            return True
    return False


a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))
c = int(input("Masukkan nilai c: "))


print("jadi ke 3 bilangan ini bernilai :", cek_angka(a, b, c))
# Contoh tester
print(cek_angka(2, 3, 5))  
print(cek_angka(1, 2, 3))  
print(cek_angka(1, 2, 4))  
print(cek_angka(1, 1, 2))  
