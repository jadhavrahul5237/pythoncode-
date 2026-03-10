# Function call on anather function


def fun1():
    print("This is Function 1")

def fun2():
    print("This is Function 2")
    fun1()
fun2()
