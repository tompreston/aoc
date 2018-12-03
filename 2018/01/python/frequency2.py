def find_freq(f):
    res_freqs = []
    total = 0
    i = 0

    while True:
        # keep track of progress
        print(i, len(res_freqs), len(set(res_freqs)))
        i += 1

        for line in f:
            total += int(line)
            res_freqs.append(total)

            if res_freqs.count(total) == 2:
                return total

if __name__ == "__main__":
    with open("freq.txt", "r") as f:
        print(find_freq(f))
