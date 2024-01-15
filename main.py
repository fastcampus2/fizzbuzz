def fizz():
    for i in range(1, 15+1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        
        if i % 3 == 0:
            print('fizz')
        
        else:
            print(i)


if __name__ == '__main__':
    fizz()
