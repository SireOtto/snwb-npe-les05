import argparse

parser = argparse.ArgumentParser(description="Test")

parser.add_argument("-n", type=int, help="Een nummer")
parser.add_argument("-age", type=int, help="Een leeftijd", default=18)
parser.add_argument("-m", type=int, help="Create a home directory")

args = parser.parse_args()

for i in range(args.n):
    print("Hi there")

print(args.age)

print(args.m)

print("test")