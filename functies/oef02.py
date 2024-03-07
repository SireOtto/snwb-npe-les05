def checkAge(age: int, name: str = "Jos", extra: str = "✅"):
    if age < 18:
        age_old: str = "jonger"
        create_sentence(age_old, name)
    else:
        age_old: str = "ouder"
        print("+18")
        create_sentence(age_old, name)
    print(extra)

def create_sentence(age_old: str, name):
    print(f"{name}, Je bent {age_old} dan 18")

name : str = input("Geef uw naam: ")
age : int = int(input("Geef uw leeftijd: "))

checkAge(age, name)
checkAge(age)
checkAge(extra="❤️", age=age)