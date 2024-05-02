import datetime

def begruessung():
    now = datetime.datetime.now()
    if now < now.replace(hour=12, minute=0, second=0):
        begruessung = "Guten Morgen"
    elif now < now.replace(hour=18, minute=0, second=0):
        begruessung = "Guten Tag"
    else:
        begruessung = "Guten Abend"

    print(f"Willkommen beim Temperaturenumrechner! ")
    print(f"{begruessung}. Heute ist der {now.strftime('%d.%m.%Y')} um {now.strftime('%H:%M')} Uhr.")

def berechne_celsius_kelvin(zahl1):
    kelvin = zahl1 + 273.15
    print(f"Das Ergebnis ist {kelvin} Kelvin!")

def berechne_kelvin_celsius(zahl2):
    celsius = zahl2 - 273.15
    print(f"Das Ergebnis ist {celsius} Celsius!")

def berechne_kelvin_fahr(zahl3):
    fahrenheit = (zahl3 - 273.15) * 9/5 + 32
    print(f"Das Ergebnis ist {fahrenheit} Fahrenheit!")

def berechne_fahr_celsius(zahl4):
    celsius = (zahl4 - 32) * 5 / 9
    print(f"Das Ergebnis ist {celsius} Celsius!")

def auswahl():
    while True:
        print("Wählen Sie aus, was Sie berechnen möchten!")
        print("(1) Umrechnung von Celsius nach Kelvin")
        print("(2) Umrechnung von Kelvin nach Celsius")
        print("(3) Umrechnung von Kelvin nach Fahrenheit")
        print("(4) Umrechnung von Fahrenheit nach Celsius")

        auswahl = input("Bitte geben Sie Ihre Auswahl ein: ")

        if auswahl == "1":
            zahl1 = input("Geben Sie die Celsius ein: ")
            if zahl1.isnumeric():
                berechne_celsius_kelvin(float(zahl1))
                break
            else:
                print("Bitte geben Sie eine gültige Zahl ein!")
        elif auswahl == "2":
            zahl2 = input("Geben Sie die Kelvin ein: ")
            if zahl2.isnumeric():
                berechne_kelvin_celsius(float(zahl2))
                break
            else:
                print("Bitte geben Sie eine gültige Zahl ein!")
        elif auswahl == "3":
            zahl3 = input("Geben Sie die Kelvin ein: ")
            if zahl3.isnumeric():
                berechne_kelvin_fahr(float(zahl3))
                break
            else:
                print("Bitte geben Sie eine gültige Zahl ein!")
        elif auswahl == "4":
            zahl4 = input("Geben Sie die Fahrenheit ein: ")
            if zahl4.isnumeric():
                berechne_fahr_celsius(float(zahl4))
                break
            else:
                print("Bitte geben Sie eine gültige Zahl ein!")
        else:
            print("Ungültige Auswahl!")

def main():
    begruessung()
    auswahl()

if __name__ == "__main__":
    main()
