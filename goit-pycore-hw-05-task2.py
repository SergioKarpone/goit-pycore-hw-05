import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    # \b - межа слова
    # \d+ - цифри
    # (?:\.\d+)? - обробка після крапки
    pattern = r'\b\d+(?:\.\d+)?\b'
    
    # Знаходимо всі відповідності в тексті
    for match in re.finditer(pattern, text):
        number_str = match.group(0)
        # Перетворюємо  на float
        yield float(number_str)

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    # Виклик генератора
    number_generator = func(text)
    
    # Підсумок всіх елементів
    return sum(number_generator)

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)

print(f"Загальний дохід: {total_income}")