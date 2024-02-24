def mean(data):
    total = sum(data)
    return total / len(data)


def std_dev(data):
    mdata = mean(data)
    stddev = sum((x - mdata)**2 for x in data) / len(data)
    return stddev**0.5


macks = []
if __name__ == "__main__":
    for i in range(5):
        while True:
            num = float(input("Enter a real number: "))
            macks.append(num)
            break
    
print(f"The mean is {mean(macks):.3f} and the standard deviation is {std_dev(macks):.3f}.")
