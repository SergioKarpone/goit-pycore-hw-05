import sys

# Велика глибина рекурсії при великих 'n'
sys.setrecursionlimit(2000)

def caching_fibonacci():
    # Словник для зберігання вже обчислених чисел Фібоначчі (кеш)
    cache = {}

    def fibonacci(n):
        # Обробка базових випадків
        if n <= 0:
            return 0
        if n == 1:
            return 1
        
        # Перевірка кешу
        if n in cache:
            return cache[n]

        # Рекурсія
        result = fibonacci(n - 1) + fibonacci(n - 2)
        
        # Збереження результату
        cache[n] = result
        return result

    # Повертаємо внутрішню функцію із зімиканням
    return fibonacci

fib = caching_fibonacci()

print("Обчислення чисел Фібоначчі")

# Обчислюємо F(10)
n1 = 10
result1 = fib(n1)
print(f"F({n1}) = {result1}") 

# Обчислення F(15) (лише F(11)-F(15)) 
n2 = 15
result2 = fib(n2)
print(f"F({n2}) = {result2}") 

# Обчислення F(10) (використвується кешуванню)
n3 = 50
result3 = fib(n3)
print(f"F({n3}) = {result3}")