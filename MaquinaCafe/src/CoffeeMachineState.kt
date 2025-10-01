package com.example.coffeemachine

/**
 * Estados posibles de la máquina de café.
 * Sealed class asegura que todos los estados estén controlados.
 */
sealed class CoffeeMachineState {

    /** La maquina no está haciendo nada (esperando). */
    object Idle : CoffeeMachineState()

    /** La máquina está preparando café ahora mismo. */
    object MakingCoffee : CoffeeMachineState()

    /**
     * Café servido y listo para recoger.
     * Hereda de la clase base Coffee.
     * @param brand marca/nombre del café servido
     */
    data class ServingCoffee(val brand: String, val size: String = "M") : Coffee("Café $brand, tamaño $size")

    /**
     * Estado de error con mensaje explicativo.
     * @param message texto del error
     */
    data class Error(val message: String) : CoffeeMachineState()

    /**
     * Nuevo estado añadido: mantenimiento.
     * @param date fecha del mantenimiento
     * @param technician nombre del técnico
     */
    data class Maintenance(val date: String, val technician: String) : CoffeeMachineState()
}
/**
 * Clase base que representa un café genérico.
 * Se usa para demostrar herencia.
 */
open class Coffee(open val description: String) : CoffeeMachineState()
