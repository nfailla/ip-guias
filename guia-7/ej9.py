# Toma dos enteros y devuelve su suma + 1
def rt (x: int, g: int) -> int:
  g = g + 1
  return x + g

g: int = 0
# Toma un entero, incrementa en 1 la variable global g,
# y devuelve la suma del entero y el nuevo valor de g
def ro (x: int) -> int:
  global g
  g = g + 1
  
  return x + g

# ----------------------------------------------------------------------------------------------------
# estado a
# vale g==0
eval1: int = ro(1)
# estado b
# vale g==1 ; eval1==g@b + 1
eval2: int = ro(1)
# estado c
# vale g==2 ; eval2==g@c + 1
eval3: int = ro(1)
# estado d
# vale g==3 ; eval3==g@d + 1

# ----------------------------------------------------------------------------------------------------

# estado a
# vale g==0
eval4: int = rt(1, 0)
# estado b
# vale g==0 ; eval4==2
eval5: int = rt(1, 0)
# estado c
# vale g==0 ; eval5==2
eval6: int = rt(1, 0)
# estado d
# vale g==0 ; eval6==2