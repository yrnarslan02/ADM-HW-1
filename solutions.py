# challenge
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")


# problem 1

if __name__ == '__main__':
    print("Hello, World!")

#problem2
if __name__ == '__main__':
    a = int(input())
    b = int(input())

    result0 = a // b
    result1 = a / b

    print(result0)
    print(result1)

#loops
if __name__ == '__main__':
    n = int(input())

    for num in range(n):
        result = num ** 2
        print(result)

#write a function

def is_leap(year):
    leap = False
    
    
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True

    
    return leap

year = int(input())
print(is_leap(year))

#print function
if __name__ == '__main__':
    n = int(input())
    
    for y in range(1, n + 1):
        print(y, end='')

#arithmetic operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    result0 = a + b
    result1 = a - b
    result2 = a * b

    print(result0)
    print(result1)
    print(result2)

#find the runner up score
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    nums = list(set(arr))
    nums.sort()

    result = nums[-2]
    print(result)

#nested lists

if __name__ == '__main__':
    arr = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])

    nums = []

    for y in arr:
        nums.append(y[1])

    nums = sorted(set(nums))
    result = nums[1]

    names = []

    for y in arr:
        if y[1] == result:
            names.append(y[0])

    names.sort()

    for y in names:
        print(y)
    
#find the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    nums = student_marks[query_name]
    result = sum(nums) / len(nums)

    print(f"{result:.2f}")

#lists
if __name__ == '__main__':
    N = int(input())
    arr = []

    for y in range(N):
        nums = input().split()

        if nums[0] == 'insert':
            arr.insert(int(nums[1]), int(nums[2]))
        elif nums[0] == 'print':
            print(arr)
        elif nums[0] == 'remove':
            arr.remove(int(nums[1]))
        elif nums[0] == 'append':
            arr.append(int(nums[1]))
        elif nums[0] == 'sort':
            arr.sort()
        elif nums[0] == 'pop':
            arr.pop()
        elif nums[0] == 'reverse':
            arr.reverse()

#tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    nums = tuple(integer_list)

    result = 0x345678
    num = 1000003
    a = n

    for y in nums:
        result = ((result ^ y) * num) % (2**64)
        a = a - 1
        num = num + 82520 + a + a

    result = (result + 97531) % (2**64)

    if result >= 2**63:
        result = result - 2**64

    print(result)

#list comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    result = [[a, b, c] for a in range(x + 1)
              for b in range(y + 1)
              for c in range(z + 1)
              if a + b + c != n]

    print(result)

#String split and join


def split_and_join(line):
    nums = line.split(" ")
    result = "-".join(nums)
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#def print_full_name(first, last):
    result = "Hello " + first + " " + last + "! You just delved into python."
    print(result)


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

#mutations
def mutate_string(string, position, character):
    nums = list(string)
    nums[position] = character
    result = ''.join(nums)
    return result

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

#find a string 
ef count_substring(string, sub_string):
    result = 0

    for y in range(len(string) - len(sub_string) + 1):
        if string[y:y + len(sub_string)] == sub_string:
            result += 1

    return result

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
#string validators
if __name__ == '__main__':
    s = input()

    print(any(y.isalnum() for y in s))
    print(any(y.isalpha() for y in s))
    print(any(y.isdigit() for y in s))
    print(any(y.islower() for y in s))
    print(any(y.isupper() for y in s))

#Text Alignment
n = int(input())
h = 'H'

for y in range(n):
    print((h * (2*y+1)).center(2*n-1))

for y in range(n+1):
    print((h*n).center(2*n) + (h*n).center(6*n))

for y in range((n+1)//2):
    print((h*5*n).center(6*n))

for y in range(n+1):
    print((h*n).center(2*n) + (h*n).center(6*n))

for y in range(n):
    print((h*(2*(n-y)-1)).center(2*n-1).rjust(6*n-1))

#text wrap
import textwrap


def wrap(string, max_width):
    result = textwrap.fill(string, max_width)
    return result
    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

#designer door mat
n, m = map(int, input().split())

for y in range(n // 2):
    result = ".|." * (2 * y + 1)
    print(result.center(m, "-"))

print("WELCOME".center(m, "-"))

for y in range(n // 2 - 1, -1, -1):
    result = ".|." * (2 * y + 1)
    print(result.center(m, "-"))
#string formatting
def print_formatted(number):

    width = len(bin(number)[2:])

    for y in range(1, number + 1):
        a = str(y)
        b = oct(y)[2:]
        c = hex(y)[2:].upper()
        d = bin(y)[2:]

        print(a.rjust(width), b.rjust(width), c.rjust(width), d.rjust(width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

#alphabet rangoli
def print_rangoli(size):
    letters = "abcdefghijklmnopqrstuvwxyz"
    lines = []
    width = 4 * size - 3

    for y in range(size):
        nums = letters[size - 1:y:-1] + letters[y:size]
        result = "-".join(nums)
        lines.append(result.center(width, "-"))

    print("\n".join(lines[::-1] + lines[1:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

#capitalize
def solve(s):
    result = " ".join(y.capitalize() for y in s.split(" "))
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

#the minion game
def minion_game(string):
    kevin = 0
    stuart = 0
    vowels = "AEIOU"

    for y in range(len(string)):
        if string[y] in vowels:
            kevin += len(string) - y
        else:
            stuart += len(string) - y

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)

#merge the tools
def merge_the_tools(string, k):
    for y in range(0, len(string), k):
        part = string[y:y + k]
        result = ""

        for letter in part:
            if letter not in result:
                result += letter

        print(result)



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

#sWAP cASE
def swap_case(s):
    result = s.swapcase()
    return result
   

if __name__ == '__main__':
    s = input()
    result = swap_case(s)

#Introduction to Sets
def average(array):
    nums = set(array)
    result = sum(nums) / len(nums)
    return result

  
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

#no idea
n, m = map(int, input().split())
nums = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))

score = 0

for y in nums:
    if y in a:
        score += 1
    elif y in b:
        score -= 1

print(score)

#set.add()
n = int(input())
countries = set()

for y in range(n):
    country = input()
    countries.add(country)

print(len(countries))

#set.discard(), remove() & pop()
n = int(input())
s = set(map(int, input().split()))
N = int(input())

for y in range(N):
    cmd = input().split()

    if cmd[0] == "pop":
        s.remove(min(s))
    elif cmd[0] == "remove":
        s.remove(int(cmd[1]))
    elif cmd[0] == "discard":
        s.discard(int(cmd[1]))

print(sum(s))

#set.union() operation
n = int(input())
a = set(map(int, input().split()))

m = int(input())
b = set(map(int, input().split()))

print(len(a.union(b)))

#set.intersection() operation
n = int(input())
a = set(map(int, input().split()))

m = int(input())
b = set(map(int, input().split()))

print(len(a.intersection(b)))

#set.difference() operation
n = int(input())
a = set(map(int, input().split()))

m = int(input())
b = set(map(int, input().split()))

print(len(a.difference(b)))

#sets.symmetric_difference() operation
n = int(input())
a = set(map(int, input().split()))

m = int(input())
b = set(map(int, input().split()))

print(len(a.symmetric_difference(b)))

#set Mutations
n = int(input())
a = set(map(int, input().split()))
m = int(input())

for y in range(m):
    cmd = input().split()
    b = set(map(int, input().split()))

    if cmd[0] == "update":
        a.update(b)
    elif cmd[0] == "intersection_update":
        a.intersection_update(b)
    elif cmd[0] == "difference_update":
        a.difference_update(b)
    elif cmd[0] == "symmetric_difference_update":
        a.symmetric_difference_update(b)

print(sum(a))

#the captain's room
k = int(input())
rooms = list(map(int, input().split()))

a = set(rooms)

captain = (sum(a) * k - sum(rooms)) // (k - 1)

print(captain)

#check subset
t = int(input())

for i in range(t):
    n = int(input())
    a = set(map(int, input().split()))

    m = int(input())
    b = set(map(int, input().split()))

    print(a.issubset(b))

#check strict superset
a = set(map(int, input().split()))
n = int(input())

result = True

for i in range(n):
    b = set(map(int, input().split()))
    if not a > b:
        result = False

print(result)

#symmetric difference
m = int(input())
a = set(map(int, input().split()))

n = int(input())
b = set(map(int, input().split()))

result = sorted(a.symmetric_difference(b))

for i in result:
    print(i)

#defaultdict tutorial
from collections import defaultdict

n, m = map(int, input().split())
kelimeler = defaultdict(list)

for x in range(n):
    a = input()
    kelimeler[a].append(x + 1)

for x in range(m):
    b = input()
    if b in kelimeler:
        print(*kelimeler[b])
    else:
        print(-1)
    
#collections.namedtuple()
from collections import namedtuple
n = int(input())
Student = namedtuple('Student', input().split())
students = [Student(*input().split()) for _ in range(n)]
print(f"{sum(int(s.MARKS) for s in students) / n:.2f}")

#collections.OrderedDict()
from collections import OrderedDict

items = OrderedDict()
for _ in range(int(input())):
    *name, price = input().split()
    name = ' '.join(name)
    items[name] = items.get(name, 0) + int(price)

for name, total in items.items():
    print(name, total)

#word order
import sys

def coz():
    ham_veri = sys.stdin.read().split()
    if not ham_veri:
        return
    
    adet = int(ham_veri[0])
    kelime_listesi = ham_veri[1:adet+1]
    
    frekanslar = {}
    siralama = []
    
    for kelime in kelime_listesi:
        if kelime not in frekanslar:
            frekanslar[kelime] = 0
            siralama.append(kelime)
        frekanslar[kelime] += 1
        
    print(len(siralama))
    print(*(frekanslar[item] for item in siralama))

if __name__ == '__main__':
    coz()

#collections.deque()
from collections import deque
import sys

def main():
    satirlar = sys.stdin.read().splitlines()
    if not satirlar:
        return
        
    n = int(satirlar[0].strip())
    dq = deque()
    
    for s in satirlar[1:n+1]:
        parca = s.strip().split()
        if not parca:
            continue
        cmd = parca[0]
        
        if cmd == 'append':
            dq.append(parca[1])
        elif cmd == 'appendleft':
            dq.appendleft(parca[1])
        elif cmd == 'pop':
            dq.pop()
        elif cmd == 'popleft':
            dq.popleft()
            
    print(*(dq))

if __name__ == '__main__':
    main()

#company logo
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()

sayim = {}
for harf in s:
    sayim[harf] = sayim.get(harf, 0) + 1
    
sirali = sorted(sayim.items(), key=lambda x: (-x[1], x[0]))
    
for karakter, frekans in sirali[:3]:
     print(f"{karakter} {frekans}")

#piling up
from collections import deque
import sys

def main():
    veri = sys.stdin.read().split()
    if not veri:
        return
        
    t = int(veri[0])
    idx = 1
    
    for _ in range(t):
        n = int(veri[idx])
        idx += 1
        
        dq = deque(map(int, veri[idx:idx+n]))
        idx += n
        
        son_boy = float('inf')
        flag = True
        
        while dq:
            if dq[0] >= dq[-1]:
                val = dq.popleft()
            else:
                val = dq.pop()
                
            if val <= son_boy:
                son_boy = val
            else:
                flag = False
                break
                
        if flag:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()

#collections.counter()
from collections import Counter
import sys

def main():
    veri = sys.stdin.read().split()
    if not veri:
        return
        
    x = int(veri[0])
    ayakkabilar = Counter(map(int, veri[1:x+1]))
    
    n = int(veri[x+1])
    idx = x + 2
    
    kazanc = 0
    for _ in range(n):
        numara = int(veri[idx])
        fiyat = int(veri[idx+1])
        idx += 2
        
        if ayakkabilar[numara] > 0:
            kazanc += fiyat
            ayakkabilar[numara] -= 1
            
    print(kazanc)

if __name__ == '__main__':
    main()

#time delta
#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    format_str = '%a %d %b %Y %H:%M:%S %z'
    zaman1 = datetime.strptime(t1, format_str)
    zaman2 = datetime.strptime(t2, format_str)
    fark = abs(int((zaman1 - zaman2).total_seconds()))
    return str(fark)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

#calendar module
import calendar
import sys

def main():
    girdi = sys.stdin.read().split()
    if not girdi:
        return
        
    ay = int(girdi[0])
    gun = int(girdi[1])
    yil = int(girdi[2])
    
    haftanin_gunu_indeks = calendar.weekday(yil, ay, gun)
    gun_ismi = calendar.day_name[haftanin_gunu_indeks]
    
    print(gun_ismi.upper())

if __name__ == '__main__':
    main()

#exceptions
import sys

def main():
    veri = sys.stdin.read().splitlines()
    if not veri:
        return
        
    t = int(veri[0].strip())
    
    for satir in veri[1:t+1]:
        parca = satir.strip().split()
        if len(parca) < 2:
            continue
            
        try:
            val1 = int(parca[0])
            val2 = int(parca[1])
            sonuc = val1 // val2
            print(sonuc)
        except ZeroDivisionError as err:
            print("Error Code:", err)
        except ValueError as err:
            print("Error Code:", err)

if __name__ == '__main__':
    main()

#zipped
import sys

def main():
    veri = sys.stdin.read().split()
    if not veri:
        return
        
    ogrenci_sayisi = int(veri[0])
    ders_sayisi = int(veri[1])
    
    notlar = []
    idx = 2
    for _ in range(ders_sayisi):
        ders_notlari = [float(veri[idx + i]) for i in range(ogrenci_sayisi)]
        notlar.append(ders_notlari)
        idx += ogrenci_sayisi
        
    for ogrenci_notlari in zip(*notlar):
        ortalama = sum(ogrenci_notlari) / ders_sayisi
        print(f"{ortalama:.1f}")

if __name__ == '__main__':
    main()

#athlete sort
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input().strip())

    sirali_liste = sorted(arr, key=lambda x: x[k])
    
    for satir in sirali_liste:
        print(*(satir))

#ginortS
import sys

def main():
    metin = sys.stdin.readline().strip()
    if not metin:
        return
        
    kucukler = sorted([h for h in metin if h.islower()])
    buyukler = sorted([h for h in metin if h.isupper()])
    tekler = sorted([h for h in metin if h.isdigit() and int(h) % 2 != 0])
    ciftler = sorted([h for h in metin if h.isdigit() and int(h) % 2 == 0])
    
    sonuc = "".join(kucukler + buyukler + tekler + ciftler)
    print(sonuc)

if __name__ == '__main__':
    main()


#
cube = lambda x: x ** 3

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    liste = [0, 1]
    for _ in range(2, n):
        liste.append(liste[-1] + liste[-2])
    return liste


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

#re.split
regex_pattern = r"[.,]"   # Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))

#group(), groups() & groupdict()
import re
import sys

def main():
    metin = sys.stdin.readline().strip()
    if not metin:
        return
        
    eslesme = re.search(r'([a-zA-Z0-9])\1+', metin)
    
    if eslesme:
        print(eslesme.group(1))
    else:
        print("-1")

if __name__ == '__main__':
    main()

#re.findall() & re.finditer()
import re
import sys

def main():
    metin = sys.stdin.readline().strip()
    if not metin:
        return
        
    eslesmeler = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])([aeiouAEIOU]{2,})(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])', metin)
    
    if eslesmeler:
        for sonuc in eslesmeler:
            print(sonuc)
    else:
        print("-1")

if __name__ == '__main__':
    main()

#re.start() & re.end()
import re
import sys

def main():
    girdi = sys.stdin.read().splitlines()
    if len(girdi) < 2:
        return
        
    metin = girdi[0].strip()
    alt_metin = girdi[1].strip()
    
    if not alt_metin or alt_metin not in metin:
        print("(-1, -1)")
        return
        
    baslangic = 0
    bulundu_mu = False
    
    while True:
        eslesme = re.search(r'(?=(' + re.escape(alt_metin) + r'))', metin[baslangic:])
        if not eslesme:
            break
            
        gercek_baslangic = baslangic + eslesme.start(1)
        gercek_bitis = gercek_baslangic + len(alt_metin) - 1
        
        print(f"({gercek_baslangic}, {gercek_bitis})")
        bulundu_ mu = True
        
        baslangic = gercek_baslangic + 1

if __name__ == '__main__':
    main()

#regex substitution
import re
import sys

def main():
    veri = sys.stdin.read().splitlines()
    if not veri:
        return
        
    satir_sayisi = int(veri[0].strip())
    
    for i in range(1, satir_sayisi + 1):
        if i < len(veri):
            metin = veri[i]
            guncel_metin = re.sub(r'(?<=\s)&&(?=\s)', 'and', metin)
            guncel_metin = re.sub(r'(?<=\s)\|\|(?=\s)', 'or', guncel_metin)
            print(guncel_metin)

if __name__ == '__main__':
    main()

#validating roman numerals
regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))

#validating phone numbers
import re
import sys

def main():
    veri = sys.stdin.read().splitlines()
    if not veri:
        return
        
    satir_sayisi = int(veri[0].strip())
    
    for i in range(1, satir_sayisi + 1):
        if i < len(veri):
            numara = veri[i].strip()
            if re.match(r"^[789]\d{9}$", numara):
                print("YES")
            else:
                print("NO")

if __name__ == '__main__':
    main()

#validating and parsing email addresses
import email.utils
import re
import sys

def main():
    veri = sys.stdin.read().splitlines()
    if not veri:
        return
        
    satir_sayisi = int(veri[0].strip())
    eposta_deseni = re.compile(r'^[a-zA-Z][\w\.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$')
    
    for i in range(1, satir_sayisi + 1):
        if i < len(veri):
            satir = veri[i].strip()
            isim, eposta = email.utils.parseaddr(satir)
            
            if eposta_deseni.match(eposta):
                print(email.utils.formataddr((isim, eposta)))

if __name__ == '__main__':
    main()

#hex color code
import re
import sys

def main():
    veri = sys.stdin.read().splitlines()
    if not veri:
        return
        
    satir_sayisi = int(veri[0].strip())
    css_metni = "\n".join(veri[1:satir_sayisi + 1])
    
    bloklar = re.findall(r'\{([^}]*)\}', css_metni)
    renk_deseni = re.compile(r'#[0-9a-fA-F]{3,6}\b')
    
    for blok in bloklar:
        renkler = renk_deseni.findall(blok)
        for renk in renkler:
            print(renk)

if __name__ == '__main__':
    main()

#html parser - part 1
from html.parser import HTMLParser

class OzelHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for name, value in attrs:
            print(f"-> {name} > {value}")

    def handle_endtag(self, tag):
        print(f"End   : {tag}")

    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for name, value in attrs:
            print(f"-> {name} > {value}")

n = int(input())

html = ""
for y in range(n):
    html += input() + "\n"

parser = OzelHTMLParser()
parser.feed(html)

#html parser - part 2

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)

    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)

n = int(input())

html = ""
for y in range(n):
    html += input() + "\n"

parser = MyHTMLParser()
parser.feed(html)

#detect HTML tags, attributes and attribute values
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for name, value in attrs:
            print(f"-> {name} > {value}")

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for name, value in attrs:
            print(f"-> {name} > {value}")

n = int(input())

html = ""
for y in range(n):
    html += input() + "\n"

parser = MyHTMLParser()
parser.feed(html)

#validating UID
n = int(input())

for y in range(n):
    uid = input()

    upper = 0
    digit = 0

    for x in uid:
        if x.isupper():
            upper += 1
        if x.isdigit():
            digit += 1

    if len(uid) == 10 and upper >= 2 and digit >= 3 and uid.isascii() and uid.isalnum() and len(set(uid)) == 10:
        print("Valid")
    else:
        print("Invalid")

#validating credit card numbers
import re

n = int(input())

for y in range(n):
    num = input()

    pattern = r'^[456]\d{3}(-?\d{4}){3}$|^[456]\d{15}$'

    if re.fullmatch(pattern, num):
        check = num.replace("-", "")

        if re.search(r'(\d)\1{3}', check):
            print("Invalid")
        else:
            print("Valid")
    else:
        print("Invalid")

#validating postal codes
regex_integer_in_range = r"^[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"(?=(\d)\d\1)"

import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

#matrix script
import re

n, m = map(int, input().split())

arr = []
for y in range(n):
    arr.append(input())

result = ""

for x in range(m):
    for y in range(n):
        result += arr[y][x]

result = re.sub(r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])', ' ', result)

print(result)

#detect floating point number
import re

n = int(input())

for y in range(n):
    num = input()
    print(bool(re.fullmatch(r'[+-]?\d*\.\d+', num)))

#XLM1 
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):

    score = len(node.attrib)
    for child in node:
        score += get_attr_number(child)
    return score

def main():
    veri = sys.stdin.read().splitlines()
    if not veri:
        return
        
    satir_sayisi = int(veri[0].strip())
    xml_metni = "\n".join(veri[1:satir_sayisi + 1])
    
    agac = etree.ElementTree(etree.fromstring(xml_metni))
    toplam_puan = get_attr_number(agac.getroot())
    
    print(toplam_puan)


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

#XLM2
import xml.etree.ElementTree as etree
import sys

maxdepth = 0

def depth(elem, level):
    global maxdepth
    level += 1
    if level > maxdepth:
        maxdepth = level
    for child in elem:
        depth(child, level)

def main():
    veri = sys.stdin.read().splitlines()
    if not veri:
        return
        
    satir_sayisi = int(veri[0].strip())
    xml_metni = "\n".join(veri[1:satir_sayisi + 1])
    
    agac = etree.ElementTree(etree.fromstring(xml_metni))
    depth(agac.getroot(), -1)
    print(maxdepth)


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

#Decorators 
import operator

def person_lister(f):
    def inner(people):
        # Kisileri yaslarina gore (2. eleman, int donusturerek) siraliyoruz
        siralanmis = sorted(people, key=lambda x: int(x[2]))
        # Siralanmis kisileri fonksiyonumuza (f) gondererek formatli cikti uretiyoruz
        return [f(p) for p in siralanmis]
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

#standardize mobile number using decorators
def wrapper(f):
    def fun(l):

        standart_numaralar = []
        for num in l:
            temiz_num = num[-10:]
            formatli = f"+91 {temiz_num[:5]} {temiz_num[5:]}"
            standart_numaralar.append(formatli)
        # Siralama islemini yapip fonksiyonu cagiriyoruz
        f(sorted(standart_numaralar))
    return fun
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

#Birthday cake candles
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
   
    en_uzun = max(candles)
    return candles.count(en_uzun)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


#number line jumps
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    if v1 > v2 and (x2 - x1) % (v1 - v2) == 0:
        return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

#viral advertising
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    paylasan = 5
    toplam_begeni = 0
    for _ in range(n):
        begenen = paylasan // 2
        toplam_begeni += begenen
        paylasan = begenen * 3
    return toplam_begeni

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

#Recursive Digit Sum
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    ilk_toplam = sum(int(basamak) for basamak in n) * k
    
    def yardimci(sayi_str):
        if len(sayi_str) == 1:
            return int(sayi_str)
        toplam = sum(int(d) for d in sayi_str)
        return yardimci(str(toplam))
        
    return yardimci(str(ilk_toplam))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

#insertionsort1
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    deger = arr[-1]
    indeks = n - 2
    
    while indeks >= 0 and arr[indeks] > deger:
        arr[indeks + 1] = arr[indeks]
        print(*(arr))
        indeks -= 1
        
    arr[indeks + 1] = deger
    print(*(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

#insertionsort2
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):

    for i in range(1, n):
        anahtar = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > anahtar:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = anahtar
        print(*(arr))
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

#Shape and reshape
import numpy
import sys

def main():
    veri = sys.stdin.read().split()
    if not veri:
        return
    sayilar = numpy.array(veri, int)
    print(numpy.reshape(sayilar, (3, 3)))

if __name__ == '__main__':
    main()

#transpose and flatten
import numpy
import sys

def main():
    veri = sys.stdin.read().splitlines()
    if not veri:
        return
        
    n, m = map(int, veri[0].split())
    matris = numpy.array([list(map(int, satir.split())) for satir in veri[1:n+1]])
    
    print(numpy.transpose(matris))
    print(matris.flatten())

if __name__ == '__main__':
    main()

#Concatenate
import numpy
import sys

def main():
    veri = sys.stdin.read().splitlines()
    if not veri:
        return
        
    n, m, p = map(int, veri[0].split())
    
    birinci_dizi = numpy.array([list(map(int, satir.split())) for satir in veri[1:n+1]])
    ikinci_dizi = numpy.array([list(map(int, satir.split())) for satir in veri[n+1:n+m+1]])
    
    print(numpy.concatenate((birinci_dizi, ikinci_dizi), axis=0))

if __name__ == '__main__':
    main()

#zeros and ones
import numpy
import sys

def main():
    veri = sys.stdin.read().split()
    if not veri:
        return
        
    boyutlar = tuple(map(int, veri))
    
    print(numpy.zeros(boyutlar, dtype=int))
    print(numpy.ones(boyutlar, dtype=int))

if __name__ == '__main__':
    main()

#eye and identity
import numpy
import sys

numpy.set_printoptions(legacy='1.13')

def main():
    veri = sys.stdin.read().split()
    if not veri:
        return
        
    n, m = map(int, veri)
    print(numpy.eye(n, m))

if __name__ == '__main__':
    main()

#array mathematics
import numpy
import sys

def main():
    veri = sys.stdin.read().splitlines()
    if not veri:
        return
        
    n, m = map(int, veri[0].split())
    
    a = numpy.array([list(map(int, satir.split())) for satir in veri[1:n+1]], dtype=int)
    b = numpy.array([list(map(int, satir.split())) for satir in veri[n+1:n+2*n+1]], dtype=int)
    
    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a % b)
    print(a ** b)

if __name__ == '__main__':
    main()

#floor, ceil and rint
import numpy
import sys

numpy.set_printoptions(legacy='1.13')

def main():
    veri = sys.stdin.read().split()
    if not veri:
        return
        
    a = numpy.array(veri, float)
    
    print(numpy.floor(a))
    print(numpy.ceil(a))
    print(numpy.rint(a))

if __name__ == '__main__':
    main()

#sum and prod
import numpy
import sys

def main():
    veri = sys.stdin.read().splitlines()
    if not veri:
        return
        
    n, m = map(int, veri[0].split())
    matris = numpy.array([list(map(int, satir.split())) for satir in veri[1:n+1]])
    
    toplam_dizi = numpy.sum(matris, axis=0)
    print(numpy.prod(toplam_dizi))

if __name__ == '__main__':
    main()

#min and max
import numpy
import sys

def main():
    veri = sys.stdin.read().splitlines()
    if not veri:
        return
        
    n, m = map(int, veri[0].split())
    matris = numpy.array([list(map(int, satir.split())) for satir in veri[1:n+1]])
    
    min_dizi = numpy.min(matris, axis=1)
    print(numpy.max(min_dizi))

if __name__ == '__main__':
    main()

#mean, var, std
import numpy

n, m = map(int, input().split())

arr = []
for y in range(n):
    arr.append(list(map(int, input().split())))

arr = numpy.array(arr)

print(numpy.mean(arr, axis=1))
print(numpy.var(arr, axis=0))
print(round(numpy.std(arr), 11))

#dot and cross
import numpy

n = int(input())

a = []
b = []

for y in range(n):
    a.append(list(map(int, input().split())))

for y in range(n):
    b.append(list(map(int, input().split())))

a = numpy.array(a)
b = numpy.array(b)

print(numpy.dot(a, b))

#inner and outer
import numpy

a = numpy.array(list(map(int, input().split())))
b = numpy.array(list(map(int, input().split())))

print(numpy.inner(a, b))
print(numpy.outer(a, b))

#polynomials
import numpy

a = list(map(float, input().split()))
x = float(input())

print(numpy.polyval(a, x))

#linear algebra
import numpy

n = int(input())

a = []
for y in range(n):
    a.append(list(map(float, input().split())))

a = numpy.array(a)

print(round(numpy.linalg.det(a), 2))

#arrays
import numpy

def arrays(arr): 
    a = numpy.array(arr, float)
    return a[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)