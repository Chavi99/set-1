def leap(a):
    if a % 4 == 0 and (a % 400 == 0 or a % 100 != 0):
        print("yes")
    else:
        print("no")
a=int(input())
leap(a)
