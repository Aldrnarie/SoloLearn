#Given a list of numbers, output "bingo" if it contains the input number.

x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]

def bingo(num):
    if num in x:
        print("bingo")
    else:
        print("try again later")

print("Pick a number between 0 and 9000")
num = int(input())
bingo(num)
