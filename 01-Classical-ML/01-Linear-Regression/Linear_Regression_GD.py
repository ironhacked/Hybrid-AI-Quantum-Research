
# Training data
x = [1, 2, 3]
y = [5, 8, 11]

# Initial parameters
w = 0.0
b = 0.0

learning_rate = 0.1
iterations = 10000

n = len(x)

for i in range(iterations):

    # Calculate predictions
    predictions = [w * x[j] + b for j in range(n)]

    # Calculate gradients
    dw = 0
    db = 0

    for j in range(n):
        error = predictions[j] - y[j]

        dw += 2 * x[j] * error
        db += 2 * error

    dw = dw / n
    db = db / n

    # Update BOTH parameters
    w = w - learning_rate * dw
    b = b - learning_rate * db

    if (i + 1) % 100 == 0:
        loss = sum(
            (y[j] - (w * x[j] + b))**2
            for j in range(n)
        ) / n

        print(i + 1, "w:", w, "b:", b, "loss:", loss)

print("\nFinal parameters:")
print("w =", w)
print("b =", b)


