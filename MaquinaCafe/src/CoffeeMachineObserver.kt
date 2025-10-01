package com.example.coffeemachine

interface CoffeeMachineObserver {
    fun onStateChanged(newState: CoffeeMachineState)
}
