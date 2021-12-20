# Created 24.5.2021
# Challenge from https://edabit.com/challenge/TZXG9RfcZ7T3o43QF
# Ones and Zeros

# Explanation:
# Write a function that returns True 
# if every consecutive sequence of ones is followed by a consecutive sequence of zeroes of the same length.
# Example same_length("110011100010") ➞ True , same_length("101010110") ➞ False


def same_length(seq: str) -> bool:
    current = ""
    start = seq[0]
    counts = {"0": 0, "1": 0}

    for sign in seq:
        if sign == current:
            counts[sign] += 1
        else:
            if sign == start:
                if counts["0"] != counts["1"]:
                    return False
            current = sign
            counts[sign] += 1
    
    if counts["0"] == counts["1"]:
        return True
    else: 
        return False


def test():
    print(same_length("110011100010")) # -> True
    print(same_length("101010110")) # -> False
    print(same_length("111100001100")) # -> True
    print(same_length("111")) # -> False
    print(same_length("110010101")) # -> False
    print(same_length("1")) # -> False

def main():
    test()


main()