def palindrome(N):
    for i in range(1,N+1):
      print((((10**i) - 1)//9)**2)

palindrome(int(input()))
