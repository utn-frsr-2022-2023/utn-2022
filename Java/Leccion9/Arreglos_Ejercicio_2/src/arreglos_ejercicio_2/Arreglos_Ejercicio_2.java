package arreglos_ejercicio_2;

import java.util.Scanner;

public class Arreglos_Ejercicio_2 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int numeros[] = new int[5];

        for (int i = 0; i < numeros.length; i++) {
            System.out.print("Ingrese un numero: ");
            numeros[i] = sc.nextInt();
        }

        for (int i = numeros.length -1; i >= 0; i--) {

            System.out.println("numeros = " + numeros[i]);
        }

    }
}
