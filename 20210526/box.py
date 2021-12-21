"""Created 26.5.2021
Challenge from https://edabit.com/challenge/dy3WWJr34gSGRPLee
Making a box

Explanation:
Create a function that creates a box based on dimension n."""

from typing import List


def make_box(dim: int) -> List[str]:
    end_line = "#" * dim
    box = [end_line]

    for i in range(2, dim + 1):
        if (i % dim == 0):
            line = end_line
        else:
            line = "#" + (" " * (dim - 2)) + "#"

        box.append(line)

    return  box


def test():
    print(make_box(2)) # -> ['##', '##']
    print(make_box(1)) # -> ['#']
    print(make_box(4)) # -> ['####', '#  #', '#  #', '####']
    print(make_box(6)) # -> ['######', '#    #', '#    #', '#    #', '#    #', '######']


def main():
    test()


if __name__ == "__main__":
    main()