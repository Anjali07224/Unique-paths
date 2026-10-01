# Unique Paths using Dynamic Programming

# Accept number of rows and columns
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

if rows <= 0 or cols <= 0:
    print("Rows and columns must be positive.")
else:
    # Create a DP table
    dp = [[0 for j in range(cols)] for i in range(rows)]

    # Initialize first row and first column
    for i in range(rows):
        dp[i][0] = 1

    for j in range(cols):
        dp[0][j] = 1

    # Calculate unique paths
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    # Display total unique paths
    print("Total unique paths:", dp[rows-1][cols-1])
