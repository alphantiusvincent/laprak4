def cekdigitbelakang(a, b, c):
   
    digita = a % 10
    digitb = b % 10
    digitc = c % 10
    
    if inputa == inputb == inputc :
        return True
    elif inputa == inputb or inputa == inputc or inputb == inputc:
        return True
    else:
            return False


inputa = int(input("Masukkan nilai untuk a: "))
inputb = int(input("Masukkan nilai untuk b: "))
inputc = int(input("Masukkan nilai untuk c: "))

print(cekdigitbelakang(inputa, inputb, inputc))