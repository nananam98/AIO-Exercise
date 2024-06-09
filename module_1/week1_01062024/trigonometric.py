def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def trigonometric(x = 3.14, n = 10):
    if n <= 0:
        print("n phải là số nguyên dương lớn hơn hoặc bằng 0")
    else:
        total_sin = 0
        total_cos = 0
        total_sinh = 0
        total_cosh = 0
        for i in range(n-1):
            sin = (-1)**i * ((x**(2*i + 1))/factorial(2*i + 1))
            cos = (-1)**i * ((x**(2*i))/factorial(2*i))
            sinh = (x**(2*i + 1))/factorial(2*i + 1)
            cosh = (x**(2*i))/factorial(2*i)

            total_sin += sin
            total_cos += cos
            total_sinh += sinh
            total_cosh += cosh
        print(f"sin({x}) = {total_sin}, cos({x}) = {total_cos}, sinh({x}) = {total_sinh}, cosh({x}) = {total_cosh}")

if __name__ == "__main__":
    trigonometric()