def max_pairwise_product(numbers):
    num1 = max(numbers)
    numbers.remove(num1)
    num2 = max(numbers)
    return num1*num2


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
