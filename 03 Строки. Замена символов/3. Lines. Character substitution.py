# С клавиатуры вводится строка. В строке заменить пробелы звездочкой. 
# Если встречается подряд несколько пробелов, то их следует заменить одним знаком "*", 
# пробелы в начале и конце строки удалить.

# Формат ввода
# Какая-нибудь строка типа этой .

# Формат вывода
# Какая-нибудь*строка*типа*этой*.

txt = input().split()

print('*'.join(txt))