string_match=lambda a,b:sum(c==d for c,d in zip(zip(a,a[1:]),zip(b,b[1:])))
