# try:
#     age:int = int(input("Leeftijd: "))
#     age += 1
#     print(age)
# except:
#     # print(age)
#     print("Foutje")

# try:
#     age:int = int(input("Leeftijd: "))
#     age += 1
#     print(age)
# except ValueError as v:
#     print(v)
# except:
#     # print(age)
#     print("Foutje")

# print("Verder")

# try:
#     age:int = int(input("Leeftijd: "))
#     age += 1
#     print(agee)
# except ValueError as v:
#     print(v)
# except Exception as e:
#     # print(age)
#     print("Foutje")
#     print(e)

# print("Verder")

try:
    age: int = int(input("Leeftijd: "))
except:
    print("Foutje")
else:
    print(f"{age = }")
