def Multi(m,n):
    if n==1:
        return m
    else:
      return (m+Multi(m,n-1))
print(Multi(4,4))