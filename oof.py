x = 500
y = 500
f = open('info.ppm', 'w')

def header():
    f.write('P3\n')
    f.write(str(x) + ' ' + str(y) + '\n')
    f.write('255\n')
def body():
    for i in range(0,x):
        print(i)
header()
body()
