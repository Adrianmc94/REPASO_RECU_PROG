import org.junit.jupiter.api.*
import com.example.coffeemachine.*

class CoffeeMachineTest {

    @BeforeEach
    fun resetMachine() {
        CoffeeMachine.clean() // Asegura que empieza en Idle
    }

    @Test
    fun `estado inicial debe ser Idle`() {
        Assertions.assertEquals(CoffeeMachineState.Idle, CoffeeMachine.getState())
    }

    @Test
    fun `hacer café cambia estado a ServingCoffee`() {
        CoffeeMachine.makeCoffee("Marcilla")
        val state = CoffeeMachine.getState()
        Assertions.assertTrue(state is CoffeeMachineState.ServingCoffee)
        if (state is CoffeeMachineState.ServingCoffee) {
            Assertions.assertEquals("Marcilla", state.brand)
        }
    }

    @Test
    fun `no se puede hacer café si ya hay uno servido`() {
        CoffeeMachine.makeCoffee("Bonka")
        val previousState = CoffeeMachine.getState()
        CoffeeMachine.makeCoffee("Nescafé") // Este no debería cambiar el estado
        val currentState = CoffeeMachine.getState()
        Assertions.assertEquals(previousState, currentState)
    }

    @Test
    fun `limpiar la máquina la deja en Idle`() {
        CoffeeMachine.makeCoffee("Lavazza")
        CoffeeMachine.clean()
        Assertions.assertEquals(CoffeeMachineState.Idle, CoffeeMachine.getState())
    }
}
