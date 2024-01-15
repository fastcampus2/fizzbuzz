START = 1
END = 15

for i in range(START, START + END):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        print(i)
