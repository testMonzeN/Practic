'''
Вам дана последовательность строк.
В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
Буквой считается символ из группы \w.
Sample Input:

this is a text
"this' !is. ?n1ce,
Sample Output:

htis si a etxt
"htis' !si. ?1nce,
'''
import sys
import re

for line in sys.stdin:
    pattern = r'\b(\w)(\w)(\w*)\b'
    line = line.rstrip()

    updated_line = re.sub(pattern, r'\2\1\3', line)
    print(updated_line)

# хотел плакать qwq