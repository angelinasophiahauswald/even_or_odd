def even_or_odd(num):
    num = int(num)
    if num % 2 == 0:
        return "even"
    if num % 2 != 0:
        return "odd"

if __name__ == "__main__":
    num = input()
    print(even_or_odd(num))