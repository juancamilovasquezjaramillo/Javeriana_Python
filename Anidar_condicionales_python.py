#inicio
50
num_invitados = int(input("Ingrese el numero de invitados: "))

if (50 >= num_invitados):

    if(30 >= num_invitados):
                    print("Rentar - no alquilar sillas")
    else:
        rentchairs = num_invitados - 30
        print("Rentar - sillas a alquilar: ", rentchairs)

else:
    print("no rentar")
    
                          
