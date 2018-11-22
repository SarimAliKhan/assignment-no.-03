a = eval('2*3+1')
print(a)

b = eval('hello')
print(b)
#it will give error because hello in not defined
"""Traceback (most recent call last):
  File "C:/Users/hp/Desktop/3.17.py", line 4, in <module>
    b = eval('hello')
  File "<string>", line 1, in <module>
NameError: name 'hello' is not defined"""
c = eval("'hello' + ' ' + 'world!'")
print(c)

d = eval("'ASCII'.count('I')")
print(d)

e = eval('x = 5')
print(e)
#it will give error due to syntax error
"""Traceback (most recent call last):
  File "C:/Users/hp/Desktop/3.17d).py", line 1, in <module>
    e = eval('x = 5')
  File "<string>", line 1
    x = 5
      ^
SyntaxError: invalid syntax"""
