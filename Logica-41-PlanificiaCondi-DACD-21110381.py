#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

class Action:
    def __init__(self, name, preconditions, effects):
        self.name = name
        self.preconditions = preconditions
        self.effects = effects

    def is_applicable(self, state):
        return all(p in state for p in self.preconditions)

    def apply(self, state):
        if self.is_applicable(state):
            new_state = state.copy()
            for effect in self.effects:
                if effect[0] == '-':
                    new_state.remove(effect[1:])
                else:
                    new_state.add(effect)
            return new_state
        else:
            return None

class ConditionalPlanner:
    def __init__(self, actions, initial_state, goal_state):
        self.actions = actions
        self.initial_state = initial_state
        self.goal_state = goal_state

    def plan(self):
        current_state = self.initial_state.copy()
        plan = []

        while current_state != self.goal_state:
            applicable_actions = [action for action in self.actions if action.is_applicable(current_state)]
            if not applicable_actions:
                return None  # No se puede alcanzar el estado objetivo

            for action in applicable_actions:
                new_state = action.apply(current_state)
                if new_state:
                    current_state = new_state
                    plan.append(action)
                    break

        return plan

# Definir acciones
actions = [
    Action("AgarrarLeche", {"LecheEnLaNevera"}, {"-LecheEnLaNevera", "LecheEnLaBolsa"}),
    Action("IrASupermercado", {"Dinero", "SupermercadoAbierto"}, {"-Dinero", "LecheEnLaNevera"}),
    Action("ComprarLeche", {"Dinero", "SupermercadoAbierto"}, {"-Dinero", "LecheEnLaBolsa"}),
]

# Definir estado inicial y estado objetivo
initial_state = {"LecheEnLaNevera", "Dinero", "SupermercadoAbierto"}
goal_state = {"LecheEnLaBolsa"}

# Crear planificador y planificar
planner = ConditionalPlanner(actions, initial_state, goal_state)
plan = planner.plan()

# Mostrar el plan resultante
if plan:
    print("Plan encontrado:")
    for action in plan:
        print(action.name)
else:
    print("No se puede encontrar un plan para alcanzar el estado objetivo.")

    