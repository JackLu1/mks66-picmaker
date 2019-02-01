x = 500
y = 500
f = open('info.ppm', 'w')

def header():
    f.write('P3\n')
    f.write(str(x) + ' ' + str(y) + '\n')
    f.write('255\n')
def body():
    red = 1
    alternate = 0
    for col in range(0,x):
        for row in range(0,y):
            #f.write('255 0 0    ')
            # x / 25 % 2
            if row / 25 % 2 == alternate:
                f.write('255 0 0    ')
                red = 0
            else:
                f.write('0 0 0  ')
                red = 1
        f.write('\n')
        if col % 25 == 0:
            if alternate == 0:
                alternate = 1
            else:
                alternate = 0
header()
body()
