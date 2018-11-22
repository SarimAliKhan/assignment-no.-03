#PRACTICE PROBLEM 3.40
def partition(names):
    return[firstname for firstname in names
           if firstname[0].lower() in 'abcdefghijklm']

x = partition(['Sarim','Zuhair','Jawad','Hasan','Abdullah'])
x.sort()
print(*x,sep = '\n')
