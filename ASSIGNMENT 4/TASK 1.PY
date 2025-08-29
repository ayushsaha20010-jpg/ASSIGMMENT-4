try:
    with open ("sample.txt", "r") as file:

        for line in file:
            print(line.strip())
except FileNotFoundError:

    print("error: the file 'sample.txt' does not exits. ")