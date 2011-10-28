#!/usr/bin/env python
"""
Exercise to hand in for week two:

print_grid(integer) returns a grid like Downey 3.5.  Do something reasonable.
"""
def print_grid(n):
    """\
    print_grid(n), takes integer n and prints a grid where each of the
    four gridlets has n pipes on a side.

    Therefore, print(1) looks like
    >>> print_grid(1)
    + - + - +
    |   |   |
    + - + - +
    |   |   |
    + - + - +

    and print_grid(3) looks like
    >>> print_grid(3)
    + - - - + - - - +
    |       |       |
    |       |       |
    |       |       |
    + - - - + - - - +
    |       |       |
    |       |       |
    |       |       |
    + - - - + - - - +
    """
    hsect = n*" -" + " +"
    plus_line = "+" + 2*hsect

    psect = n*"  " + " |"
    pipe_line = "|" + 2*psect

    for j in range(2):
        print plus_line
        for i in range(n):
            print pipe_line
    print plus_line

if __name__ == '__main__':
    import sys
    print "sys.argv =", sys.argv
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
        print "Read first arg as", n, "\n"
    else:
        n = 5
        print "Default size = 5:\n"
    print_grid(n)
    print "\n",
