

try:
    f = open('practices.rtf')
    if f.name ==
except FileNotFoundError as e:
    print(e)
except  Exception as e:
    print(e)
# within out try block, we are running a code which throws an excption, it then prints out on the
#its suppose to catch problems/erros we could run into

else:
   print(f.read())
   f.close()
finally:
    print("executing finally")