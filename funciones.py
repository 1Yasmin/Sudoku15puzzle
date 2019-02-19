
# Menu de inicio
def selectProblem():
    problema = input("Que juego desea solucionar. \n1.Sudoku \n2.15puzzle \n")
    select = True

    while select:
        # Sudoku problem
        if (problema == "1"):
            cadena = input("Ingrese el juego: \n")
            
            select = False
        # 15 puzzle problem
        elif (problema == "2"):
            cadena = input("Ingrese el juego: \n")
            # el 2 indica el tipo de juego
            arrPuzzle = [2]
            #guardar valores en una lista
            for i in cadena:
                num = int(i, 16)
                arrPuzzle.append(num)
            #print (arrPuzzle)
            return arrPuzzle
            select = False
        else:
            print("Porfavor coloque una opcion valida")
            problema = input("Que juego desea solucionar. \n1.Sudoku \n2.15puzzle \n")
        

