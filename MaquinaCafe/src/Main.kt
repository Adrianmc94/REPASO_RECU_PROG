package com.example.coffeemachine

fun main() {
        println("--- Encendiendo la máquina ---")
        CoffeeMachine.makeCoffee("Lavazza")

        println("\n--- Intentando hacer café de nuevo ---")
        CoffeeMachine.makeCoffee()

        println("\n--- Limpiando la máquina ---")
        CoffeeMachine.clean()

        println("\n--- Otro café ---")
        CoffeeMachine.makeCoffee("Starbucks")

        println("\n--- Poniendo la máquina en mantenimiento ---")
        CoffeeMachine.maintenance("30/09/2025", "Carlos el técnico")
}
