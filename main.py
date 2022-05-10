# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
count = [0, 1]
ToH4_arr = ['']
for i in range(2, 100):
    count.append(-1)

for i in range(1, 100):
    ToH4_arr.append("")


def main():
    n = int(input('Enter number of disks: '))
    ToH4(n, 'A', 'B', 'C', 'D')
    ToH4moves(n)
    for i in range(0,n+1):
        print(ToH4_arr[i])

    print(count[n])


def ToH4(n, a, b, c, d):
    if ToH4_arr[n] != '':
        return ToH4_arr[n]
    elif n == 0:
        return ToH4_arr[0]
    elif n == 1:
        ToH4_arr[1] = print(f"Move disk 1 from rod {a} to rod {b}")
        return ToH4_arr[1]
    else:
        ToH4_arr[n] = ToH4(n-2, a, c, d, b) + f"Move disk {n-1} from rod {a} to rod {d} \n" + f"Move disk {n} from rod {a} to rod {b} \n" + f"Move disk {n-1} from rod {d} to rod {b} \n" + ToH4(n-2, c, b, a, d)
        return ToH4_arr[n]


def ToH4moves(n):
    if count[n] > -1:
        return count[n]
    elif n % 2 == 0:
        count[n] = ToH4moves(n-1)+2
        return count[n]
    else:
        count[n] = ToH4moves(n-1)+1
        return count[n]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
