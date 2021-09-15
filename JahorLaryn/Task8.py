def main():
    lower_v_boundary = int(input("Enter lower vertical boundary"))
    upper_v_boundary = int(input("Enter upper vertical boundary"))
    lower_h_boundary = int(input("Enter lower horizontal boundary"))
    upper_h_boundary = int(input("Enter upper horizontal boundary"))
    width = upper_h_boundary - lower_h_boundary + 1
    height = upper_v_boundary - lower_v_boundary + 1
    table = [[" "] * (width + 1) for _ in range(height + 1)]

    for j in range(width):
        table[0][j + 1] = str(lower_h_boundary + j)
    for i in range(height):
        table[i + 1][0] = str(lower_v_boundary + i)

    for i in range(height):
        for j in range(width):
            table[i + 1][j + 1] = str((lower_h_boundary + j) * (lower_v_boundary + i))

    s = [[str(e) for e in row] for row in table]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = "\t".join("{{:{}}}".format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print("\n".join(table))


if __name__ == "__main__":
    main()
