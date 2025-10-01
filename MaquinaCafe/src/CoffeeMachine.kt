package com.example.coffeemachine

/**
 * Singleton que representa la máquina de café.
 */
object CoffeeMachine {
    // Estado actual de la máquina
    private var currentState: CoffeeMachineState = CoffeeMachineState.Idle

    /** Devuelve el estado actual */
    fun getState(): CoffeeMachineState = currentState

    /**
     * Inicia la preparación de un café.
     * @param brand marca del café
     */
    fun makeCoffee(brand: String = "Nescafé") {
        println("Estado actual: $currentState")
        when (currentState) {
            is CoffeeMachineState.Idle -> println("Máquina encendida. Empezando a hacer café de $brand...")
            is CoffeeMachineState.MakingCoffee -> println("¡Espera! La máquina ya está preparando café.")
            is CoffeeMachineState.ServingCoffee -> println("Ya hay café servido, cógelo antes de hacer otro.")
            is CoffeeMachineState.Error -> {
                val msg = (currentState as CoffeeMachineState.Error).message
                println("Error en la máquina: $msg")
            }
            is CoffeeMachineState.Maintenance -> {
                println("La máquina está en mantenimiento, no se puede usar.")
            }
            is Coffee -> {
                println("Estado genérico de café: ${(currentState as Coffee).description}")
            }
        }
    }    /** Limpia la máquina y vuelve al estado Idle */
    fun clean() {
        println("Limpiando la máquina...")
        currentState = CoffeeMachineState.Idle
        println("Máquina limpia. Estado: $currentState")
    }
    /** Pone la máquina en modo mantenimiento */
    fun maintenance(date: String, technician: String) {
        currentState = CoffeeMachineState.Maintenance(date, technician)
        println("Máquina en mantenimiento por $technician el $date")
    }
}
