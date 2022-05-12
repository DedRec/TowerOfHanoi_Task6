# count = [0, 1]
ToH4_arr = ['']
flag = 0
found = [0]
# for i in range(2, 100):
#     count.append(-1)

for i in range(1, 100):
    ToH4_arr.append("")
    found.append(0)


def main():
    global ToH4_arr
    n = int(input('Enter number of disks: '))
    ToH4(n, 'A', 'B', 'C', 'D')
    # ToH4moves(n)
    for i in range(0,n+1):
        print(ToH4_arr[i])

    # print(count[n])


def ToH4(n, a, b, c, d):
    global flag
    global ToH4_arr
    if flag == 1:
        if n == 0:
            return ToH4_arr[0]
        elif n == 1:
            ToH4_arr[1] = f"Move disk 1 from rod {a} to rod {b}\n"
            return ToH4_arr[1]
        elif ToH4_arr[n] != '' and found[n] == 1:
            return ToH4_arr[n]
        else:
            ToH4_arr[n] = ToH4(n - 2, a, c, d,
                               b) + f"Move disk {n - 1} from rod {a} to rod {d} \n" + f"Move disk {n} from rod {a} to rod {b} \n" + f"Move disk {n - 1} from rod {d} to rod {b} \n"
            ToH4_arr[n] += ToH4(n - 2, c, b, a, d)
            flag = 1
            return ToH4_arr[n]
    if n == 0:
        return ToH4_arr[0]
    elif n == 1:
        ToH4_arr[1] = f"Move disk 1 from rod {a} to rod {b}\n"
        return ToH4_arr[1]
    elif ToH4_arr[n] != '':
        return ToH4_arr[n]
    else:
        ToH4_arr[n] = ToH4(n-2, a, c, d, b) + f"Move disk {n-1} from rod {a} to rod {d} \n" + f"Move disk {n} from rod {a} to rod {b} \n" + f"Move disk {n-1} from rod {d} to rod {b} \n"
        ToH4_arr[n] += ToH4(n-2, c, b, a, d)
        flag = 1
        return ToH4_arr[n]


# def ToH4moves(n):
#     if count[n] > -1:
#         return count[n]
#     elif n % 2 == 0:
#         count[n] = ToH4moves(n-1)+2
#         return count[n]
#     else:
#         count[n] = ToH4moves(n-1)+1
#         return count[n]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # con = 'y'
    # while con == 'y':
    main()
        #con = input('continue? (y/n)')

