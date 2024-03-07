def checkAge():
    if age < 18:
        age_old: str = "jonger"
        create_sentence()
    else:
        age_old: str = "ouder"
        print("+18")
        create_sentence()

def create_sentence():
    print(f"{name}, Je bent {age_old} dan 18")

name : str = input("Geef uw naam: ")
age : int = int(
    input("Geef uw leeftijd: "))

checkAge()