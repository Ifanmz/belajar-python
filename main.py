import sys
sys.path.append('/home/dicoding')

import hello
import calculator

hello.helloWorld()

wawa = hello.Reviewer("Wawa", "12")

wawa.review()

print(sys.path)

number = calculator.Kalkulator(3)

print("hasil kali dari 3 * 4 adalah: ", number.kali(4))