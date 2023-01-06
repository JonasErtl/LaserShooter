from time import sleep

while True:
    file1 = open("file.txt", "r")
    sleep(1)
    print(file1.read())
