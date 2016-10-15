def fibonacci(n):
    allFibonacciName=list();

    allFibonacciName.append(1);
    allFibonacciName.append(1);

    while len(allFibonacciName) != n:
            allFibonacciName.append(allFibonacciName[len(allFibonacciName)-2]+allFibonacciName[len(allFibonacciName)-1]);

    return allFibonacciName;

fibonacci(5);