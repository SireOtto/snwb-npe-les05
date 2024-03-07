# def checkAge(age: int, name: str = "Jos", extra: str = "✅"):
#     if age < 18:
#         return create_sentence("jonger", name)
#     return create_sentence("ouder", name)

def checkAge(age: int, name: str = "Jos", extra: str = "✅"):
    """
    Check the age of a person and return a sentence based on their age.

    Parameters:
    - age (int): The age of the person.
    - name (str): The name of the person. Default is "Jos".
    - extra (str): An extra string to include in the sentence. Default is "✅".

    Returns:
    - str: A sentence describing the age of the person.

    """
    age_old = "jonger" if age < 18 else "ouder"
    return create_sentence(age_old, name)


def create_sentence(age_old: str, name):
    return f"{name}, Je bent {age_old} dan 18"

name : str = input("Geef uw naam: ")
age : int = int(input("Geef uw leeftijd: "))
result = checkAge(age, name)
print(result)
checkAge(age)
checkAge(extra="❤️", age=age)