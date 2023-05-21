# 1)
# estado a
x=5
# estado b
# vale x==5
y=7
# estado c
# vale x==5 ; y==7

# 2)
# estado a
x=5
# estado b
# vale x==5
y=7
# estado c
# vale x==5 ; y==7
z=x+y
# estado d
# vale x==5 ; y==7 ; z==x@c + y@c

# 3)
# estado a
x=5
# estado b
# vale x==5
x="hora"
# estado c
# vale x=="hora"

# 4)
# estado a
x=True
# estado b
# vale x==True
y=False
# estado c
# vale x==True ; y==False
res=x and y
# estado d
# vale x==True ; y==False ; res==x@c and y@c

# 5)
# estado a
x=False
# estado b
# vale x==False
res = not(x)
# estado c
# vale x==False ; res==not x@b
