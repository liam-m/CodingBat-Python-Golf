fix_teen=lambda n:(n,0)[12<n<15or 16<n<20]
no_teen_sum=lambda*a:sum(map(fix_teen,a))
