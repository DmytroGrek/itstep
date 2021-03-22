# Напишіть функцію highlight(text: str, str_to_select: str, decoration: str) -> str,
# яка буде приймати певний рядок з текстом, рядок того що потрібно виділити в тексті та
# символи якими виділити цей текст зліва та зправа. Виділяти потрібно всі входження str_to_select.
# Функція має повернути видозмінений рядок з усіма виділеннями.
import re


def highlight(text: str, str_to_select: str, decoration: str) -> str:
    result = re.sub(str_to_select, decoration+str_to_select+decoration, text)
    return result


quote = 'Guns. LOTS Of Guns.'
print(highlight(quote, 'Guns', '**'))
# '**Guns**. LOTS Of **Guns**.'
print(highlight(quote, 'guns', '**'))
# 'Guns. LOTS Of Guns.'
