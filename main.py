import sys
sys.path.append('/home/dicoding')

import hello

hello.helloWorld()

wawa = hello.Reviewer("Wawa", "12")

wawa.review()

print(sys.path)