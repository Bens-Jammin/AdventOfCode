from re import findall, sub
import re


def day_1_part_1(filename):
    
    print("hello")
    total = 0
    with open(filename, 'r') as file:
        lines = file.readlines()
        file.close()
    
    for line in lines:
        numbers = findall('[0-9]+', line)
        first_number = int(numbers[0][0]) * 10
        last_number = int(numbers[-1][-1])

        total += first_number + last_number

    print(total)

# was too busy preparing for finals + forgot how to python, not my implementation
# https://github.com/fuglede/adventofcode/blob/master/2023/day01/solutions.py
def f(line):
   for i, n in enumerate(['one','two','three','four','five','six','seven','eight','nine']):
       line = line.replace(n, n + str(i+1) + n)
   x = re.findall(r'(\d)', line)
   return int(x[0] + x[-1])



def main():
    file_name = 'day1.txt'
    print(sum(map(f, open(file_name))))


if __name__ == '__main__':
    main()