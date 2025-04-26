def main(s=False, j=False):
    if not s:
        j = input().strip()
        s = input().strip()
        # with open("input.txt") as f:
        #     s = f.readline()

    sum = 0
    for i in s:
        if i in j:
            sum += 1

    return sum


if __name__ == '__main__':
    res = main()

    print(res)
    #
    # with open("output.txt", "w") as f:
    #     f.write(str(res))
