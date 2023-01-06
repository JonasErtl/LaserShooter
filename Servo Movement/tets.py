from time import sleep
file1 = open("file.txt", "r")


while True:
    sleep(0.1)
    lis = file1.read()
    lis.strip()
    a = lis.split(',')
    print(a[-2:])
