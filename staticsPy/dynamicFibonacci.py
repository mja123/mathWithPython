def fibonacci(num, memory = {}):
    if ((num == 1) or (num == 0)):
        return num
    try:
        return memory[num]
    except KeyError:
        result = fibonacci(num - 1, memory) + fibonacci(num - 2, memory)
        memory[num] = result
        print(f'num: {num}, memory: {memory}')
        return result

if (__name__ == '__main__'):
    number = int(input("Choose the number to calculate: "))
    print(fibonacci(number))