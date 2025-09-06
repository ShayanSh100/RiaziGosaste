from Funcs import *
import os

def main_function():
    while True:
        show_menu()
        choice = input("| Enter your choice (1-15 or exit): ".ljust(30)).lower()
        os.system("cls")
        if choice == "1":
            n = int(input("Enter n for random matrix: "))
            matrix, x, y = generate_random_matrix_to_csv(n, "matrix.csv")
            print("Random Matrix (saved to matrix.csv):")
            printMatrix(matrix)
            input()

        elif choice == "1.5":
            matrix, x, y = read_matrix_from_csv("matrix.csv")
            print("Matrix Loaded from CSV:")
            printMatrix(matrix)
            input()
        elif choice == "2":
            matrixA, satrA, sotonA = matrix()
            matrixB, satrB, sotonB = matrix()
            C = zarb_boli(matrixA, satrA, sotonA, matrixB, satrB, sotonB)
            if C:
                print("ZarbBoli:\n")
                printMatrix(C[0])
            input()
        elif choice == "3":
            matrix_graph, a, b = matrix()
            show_graph(matrix_graph)
            input()
        elif choice == "4":
            matrix1, c1, d1 = matrix()
            matrix2, c2, d2 = matrix()
            if c1 == c2 and d1 == d2:
                res = vast_rasand(matrix1, matrix2)
                printMatrix(res)
            input()
        elif choice == "5":
            n = int(input("n ra Baraye Rn Vared Konid"))
            matrixn, n1, n2 = matrix()
            matn, m1, m2 = zarb_boli(matrixn, n1, n2, matrixn, n1, n2)
            for i in range(2, n):
                matn, m1, m2 = zarb_boli(matn, m1, m2, matrixn, n1, n2)
            printMatrix(matn)
            input()
        elif choice == "6":
            matrix5, x5, y5 = matrix()
            Khasiat(matrix5, x5, y5)
            input()
        elif choice == "7":
            matrix6, x6, y6 = matrix()
            Baz, Tagh, Tara = Bastar(matrix6, x6, y6)
            print("Bastar Baztabi :\n")
            printMatrix(Baz)
            print("Bastar Tagharoni :\n")
            printMatrix(Tagh)
            print("Bastar Tarayayi :\n")
            printMatrix(Tara)
            input()
        elif choice == "7.5" :
            matrix1,x1,y1 = matrix()
            Warshall(matrix1,x1,y1)
        elif choice == "10":
            matrix7, x7, y7 = matrix()
            matrix8, x8, y8 = matrix()
            res = RoS(matrix7, x7, y7, matrix8, x8, y8)
            if res:
                printMatrix(res)
            input()
        elif choice == "11":
            m, _, _ = matrix()
            GMatrixMojavaret(m)
            input()
        elif choice == "12":
            m, _, _ = matrix()
            print(Daraje(m))
            input()
        elif choice == "13":
            m, _, _ = matrix()
            res = MotamamMatrix(m)
            printMatrix(res)
            input()
        elif choice == "14":
            m1, _, _ = matrix()
            m2, _, _ = matrix()
            print(ZirGraph(m1, m2))
            input()
        elif choice == "15":
            m, _, _ = matrix()
            print("HamBand?", HamBand(m))
            input()
        elif choice == "16":
            n = int(input("Enter n for random matrix: "))
            matrix, _, _ = generate_random_matrix_to_csv(n, "matrix.csv")
            print("Random Matrix (saved to matrix.csv):")
            printMatrix(matrix)

            print("\nComparing Warshall algorithms ...")
            rs, rd = compare_warshall_speeds(matrix)
            input()
        elif choice == "exit":
            break
        os.system("cls")
        
if __name__ == "__main__" :
    main_function()

