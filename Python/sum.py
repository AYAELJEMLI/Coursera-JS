import re

def sum_file(filename):
    total = 0
    with open(filename, 'r') as file:
        for line in file:
            numbers = re.findall(r'\d+', line)  
            total += sum(int(number) for number in numbers)  
    return total

#filen = r"http://py4e-data.dr-chuck.net/regex_sum_42.txt" the answer is 445833
filen = r"http://py4e-data.dr-chuck.net/regex_sum_2216923.txt"
result = sum_file(filen)
print(f"The sum of all numbers in the file is: {result}")
