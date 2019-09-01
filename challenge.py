#-------------- Challenge ( Draw x in shape of F )------------#
"""
shape = [5, 2, 5, 2, 2]

for x_counts in shape:
    print("x" * x_counts)

"""

#-------------- using inner loop ---------------#


shape = [5, 2, 5, 2, 2]

for x_counts in shape:
    output = ''
    for count in range(x_counts):
        output += 'x'
    print(output)


"""
Output
--------

xxxxx
xx
xxxxx
xx
xx


"""

