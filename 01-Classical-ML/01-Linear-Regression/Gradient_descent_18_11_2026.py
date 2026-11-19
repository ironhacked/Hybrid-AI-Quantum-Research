w=0

learning_gradient=0.1

for i in range(10):
    loss=(w-3)**2
    gradient=2*(w-3)
    w=w-(learning_gradient * gradient)
    print(i+1, loss, w)