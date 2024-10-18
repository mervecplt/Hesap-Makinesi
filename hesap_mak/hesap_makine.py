def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def carpma(a, b):
    return a * b

def bolme(a, b):
    if b != 0:
        return a / b
    else:
        return "Bölme işleminde bölen sıfır olamaz!"

def hesap_makinesi():
    print("Hesap Makinesi")
    print("İşlemler:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")

    secim = input("İşlemi seçin (1/2/3/4): ")

    if secim in ['1', '2', '3', '4']:
        num1 = float(input("İlk sayıyı girin: "))
        num2 = float(input("İkinci sayıyı girin: "))

        if secim == '1':
            print(f"Sonuç: {num1} + {num2} = {toplama(num1, num2)}")
        elif secim == '2':
            print(f"Sonuç: {num1} - {num2} = {cikarma(num1, num2)}")
        elif secim == '3':
            print(f"Sonuç: {num1} * {num2} = {carpma(num1, num2)}")
        elif secim == '4':
            print(f"Sonuç: {num1} / {num2} = {bolme(num1, num2)}")
    else:
        print("Geçersiz seçim!")

# Hesap makinesini çalıştır
hesap_makinesi()