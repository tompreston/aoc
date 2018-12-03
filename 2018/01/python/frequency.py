if __name__ == "__main__":
    total = 0
    with open("freq.txt", "r") as f:
        for line in f:
            total += int(line)
    print(total)
