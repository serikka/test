"""
You are given a string  and width .
Your task is to wrap the string into a paragraph of width .

Function Description

Complete the wrap function in the editor below.

wrap has the following parameters:

string string: a long string
int max_width: the width to wrap to
Returns

string: a single string with newline characters ('\n') where the breaks should be
"""


def wrap(string, max_width):
    a = textwrap.wrap(string, max_width)
    b = ''
    for i in range(len(a)):
        b += a[i] + '\n'
        #print(b)
    return (b[:-1])

