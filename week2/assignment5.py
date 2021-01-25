#Linear Preceptors:
#Set parameters. Training rate 0.2 and weighted values starting at 0.2

w0 = [0.2,0.2,0.2]

training = 0.01

l0 = [ 1, 0, 0]
l1 = [ 1, 0, 1]
l2 = [ 1, 1, 0]
l3 = [ 1, 1, 1]

x = [[ 1, 0, 0],[ 1, 0, 1],[ 1, 1, 0],[ 1, 1, 1]]
for a in x:
    print(a)

labels = [-1,-1,-1,1]
output = 0
lambdaax = 0.0
labelcount = 0
print(w0)
#EQUATIONS THAT IM GOING TO USE

#for l0:
#   [1, 0, 0] * [0.2, 0.2, 0.2]
#   1(0.2) + 0(0.2) + 0(0.2) = 0.2 (on) -> 1

#   w[0]: lambda = 0.1 ( -1 - 1) * 1 = -0.2-> w[0] = 0.2 - 0.2 = 0
#   w[1]: lambda = 0.1 ( -1 - 1) * 0 = 0-> w[1] = 0.2 + 0 = 0.2
#   w[2]: lambda = 0.1 ( -1 - 1) * 0 = 0-> w[2] = 0.2 + 0 = 0.2


#for l1:
#   [1, 0, 1] * [0.2, 0.2, 0.2]
#   1(0.2) + 0(0.2) + 0(0.2) = 0.2 (on) -> 1

#   w[0] = 0.1 ( -1 - 1) * 1 =-0.2  -> w[0] = 0 - 0.2 = -0.2
#   w[1] = 0.1 ( -1 - 1) * 0 = 0-> w[1] = 0.2 + 0 = 0.2
#   w[2] = 0.1 ( -1 - 1) * 1 = -0.2 -> w[2] = 0.2 - 0.2 = 0


# do the same for the rest of lists...

for a in x:
    for element in a:
        element = w0[element] * element
        output = output + element

    if (output > 0):
        output = 1

    if(output <= 0):
        output = -1

    for n in range(0,3):
        lambdax = 0.01 * (labels[labelcount] - output) * a[n]
        print(lambdax)
        w0[n] = w0[n] + lambdax
    labelcount += 1
    print(w0)
    print(labelcount)
