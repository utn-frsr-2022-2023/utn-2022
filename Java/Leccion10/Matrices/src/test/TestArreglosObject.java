package test;

import domain.Persona;

public class TestArreglosObject {

    public static void main(String[] args) {

        Persona personas [] = new Persona[2];
        
        personas[0] = new Persona("Jimbo");
        personas[1] = new Persona("Nelson");
        System.out.println("personas[0] = " + personas[0]);
        System.out.println("personas[1] = " + personas[1]);

        for (int i = 0; i < personas.length; i++) {

            System.out.println("personas " + i +  " = " + personas[i]);
        }

        String frutas[] = { "Banana", "Manzana", "Mango" }; // Sintaxis Resumida.

        for (int i = 0; i < frutas.length; i++) {

            System.out.println("frutas = " + frutas[i]);
        }


    }
}
