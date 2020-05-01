def calculate_LCS(A, B):
	n = len(A)
	m = len(B)
	C = [[0 for i in range(0, m + 1)] for j in range(0, n + 1)]
	D = [[0 for i in range(0, m + 1)] for j in range(0, n + 1)]

	for i in range(1, n + 1):
		for j in range(1, m + 1):
			if A[i - 1] == B[j - 1]:
				C[i][j] = C[i - 1][j - 1] + 1
				D[i][j] = 0
			elif C[i][j-1] >= C[i - 1][j]:
				C[i][j] = C[i][j - 1]
				D[i][j] = 1
			else:
				C[i][j] = C[i - 1][j]
				D[i][j] = 2

	i = n
	j = m
	S = ''

	while(i > 0 and j > 0):
		if(D[i][j] == 0):
			S = A[i - 1] + S
			i -= 1
			j -= 1
		elif(D[i][j] == 2):
			i -= 1
		else:
			j -= 1
	return str(C[n][m]), S

print("Masukkan string X: ", end = "")
X = input()

print("Masukkan string Y: ", end = "")
Y = input()

length, sequence = calculate_LCS(X, Y)

print("-----------------------------------------------------------")

if(length == "0"):
    print("Tidak terdapat common subsequence dari kedua string tersebut.")
    exit()

print("Panjang Longest Common Subsequence (LCS) adalah ", end = "")
print(length)

print("Longest Common Subsequence-nya adalah ", end = "")
print(sequence)