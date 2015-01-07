round10=lambda n:n-n%10+[10,0][n%10<5]
round_sum=lambda*a:sum(map(round10,a))
