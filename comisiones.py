L = float(input("Ingrese las ventas del lunes : \n"))
M = float(input("Ingrese las ventas del Martes : \n"))
Mi = float(input("Ingrese las ventas del miercoles : \n"))
J = float(input("Ingrese las ventas del jueves : \n"))
V = float(input("Ingrese las ventas del viernes : \n"))
VT = L+M+Mi+J+V
if VT < 20000 :
    Comision = 0.05
else :
    Comision = 0.06
V_Comision = VT*Comision
print("La venta total es de :" , VT)
print("La comision total es de : ", V_Comision)