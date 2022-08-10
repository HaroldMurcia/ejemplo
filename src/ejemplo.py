# codigo ejemplo
import sys

print("Universidad de Ibagué")
print("\t Programa de Electrónica" )

if __name__ == "__main__":
    vi = sys.argv[1]
    R1 = sys.argv[2]
    R2 = sys.argv[3]
    # string to float
    vi = float(vi)
    R1 = float(R1)
    R2 = float(R2)
    Vo = vi*R2/(R1+R2)
    print("El resultado del divisor de voltaje es: ", Vo, " voltios")