f_in = open('input.txt', 'r')
f_out = open('result.txt', 'w+')
print('converting input file to upper-case ...')
f_out.write(f_in.read().upper())
