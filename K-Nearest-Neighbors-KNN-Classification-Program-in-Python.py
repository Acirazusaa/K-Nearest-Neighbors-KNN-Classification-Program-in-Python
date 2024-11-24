import math

def train_knn(x, y, labels):
    print("Training KNN model...")
    return x, y, labels

def classify(x, y, labels, testX, testY, k):
    distances = []
    for i in range(len(x)):
        dx = x[i] - testX
        dy = y[i] - testY
        distances.append(math.sqrt(dx * dx + dy * dy))

    # Find k nearest neighbors
    nearest_indices = []
    for _ in range(k):
        min_index = -1
        for j in range(len(distances)):
            if (min_index == -1 or distances[j] < distances[min_index]) and j not in nearest_indices:
                min_index = j
        if min_index != -1:
            nearest_indices.append(min_index)

    # Find most common label
    label_counts = {}
    for i in nearest_indices:
        label = labels[i]
        if label in label_counts:
            label_counts[label] += 1
        else:
            label_counts[label] = 1

    max_count = 0
    max_label = ''
    for label, count in label_counts.items():
        if count > max_count:
            max_count = count
            max_label = label

    return max_label

# Main program
print("Welcome to KNN Program!\n")
print("Group 16\n")
print("Tan Adrian Jude, and Magistrado Zach Stephan\n")

x = []
y = []
labels = []

while True:
    print("Please select an operation:")
    print("1. Train KNN Model")
    print("2. Classify New Data")
    print("3. Exit Program")

    try:
        selection = int(input("Selection: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.\n")
        continue

    if selection == 1:
        try:
            n = int(input("Please enter the number of data points: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")
            continue

        x = []
        y = []
        labels = []

        for i in range(n):
            print(f"Enter x and y coordinates of data point {i + 1}:")
            try:
                x_i = float(input("x = "))
                y_i = float(input("y = "))
                label_i = input("Label = ")
            except ValueError:
                print("Invalid input. Please re-enter this data point.")
                continue

            x.append(x_i)
            y.append(y_i)
            labels.append(label_i)

        train_knn(x, y, labels)

    elif selection == 2:
        if not x:
            print("No KNN model is trained yet!")
            continue

        try:
            testX = float(input("Enter x coordinate of the test point: "))
            testY = float(input("Enter y coordinate of the test point: "))
            k = int(input("Enter the value of k: "))

            if k <= 0 or k > len(x):
                print(f"Invalid k value. Please choose k between 1 and {len(x)}.")
                continue

            test_label = classify(x, y, labels, testX, testY, k)
            print(f"The test point ({testX}, {testY}) is classified as {test_label}")
        except ValueError:
            print("Invalid input. Please try again.")

    elif selection == 3:
        print("Exiting program...")
        break

    else:
        print("Invalid selection. Please try again.\n")
