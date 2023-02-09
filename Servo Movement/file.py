from time import sleep

while True:
    file1 = open("file.txt", "r")
    lis = file1.read()
    a = lis.strip().split(',')
    try:
        print((320-float(a[0]))*3.125/1000)
        print(float(a[-1]))
        print((240-float(a[-1]))*4.166666/1000)
        #print(float(a[0]))
        
    except:
        print(a[0])
        print(a[-1])

