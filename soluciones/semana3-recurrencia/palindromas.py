from sys import stdin
p=(stdin.readline().strip())

p=p.lower()

def letra(frase,x,y,pal):
    if pal>0:
        if frase[x]==frase[y]:
            letra(frase,x+1,y-1,pal-1)
        else:
            print("Incorrecta")

    else:
        print("Correcta")

letra(p,0,len(p)-1,len(p))
