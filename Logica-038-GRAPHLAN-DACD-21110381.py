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

class GraphPlan:
    def __init__(self, actions, initial_state, goal_state):
        self.actions = actions
        self.initial_state = initial_state
        self.goal_state = goal_state

    def plan(self, level=0, mutexes=None):
        if mutexes is None:
            mutexes = []

        if self.goal_state.issubset(self.initial_state):
            return []

        if level == 0:
            return None  # No se puede alcanzar el estado objetivo desde el estado inicial

        plan = []
        all_actions = self.actions.copy()
        all_actions.update(mutexes)

        # Expandir acciones en el nivel actual
        for action in all_actions:
            prev_layer = self.plan(level - 1, mutexes | {action})  # Buscar en el nivel anterior con el mutex añadido
            if prev_layer is not None:
                new_state = action.apply(self.initial_state)
                if new_state is not None:
                    plan.append(action)
                    self.initial_state = new_state
                    return plan + prev_layer

        return None

# Definir acciones
actions = {
    Action("AgarrarLeche", {"LecheEnLaNevera"}, {"-LecheEnLaNevera", "LecheEnLaBolsa"}),
    Action("IrASupermercado", {"Dinero", "SupermercadoAbierto"}, {"-Dinero", "LecheEnLaNevera"}),
    Action("ComprarLeche", {"Dinero", "SupermercadoAbierto"}, {"-Dinero", "LecheEnLaBolsa"}),
}

# Definir estado inicial y estado objetivo
initial_state = {"LecheEnLaNevera", "Dinero", "SupermercadoAbierto"}
goal_state = {"LecheEnLaNevera"}

# Crear planificador y planificar
planner = GraphPlan(actions, initial_state, goal_state)
plan = planner.plan(level=2)

# Mostrar el plan resultante
if plan:
    print("Plan encontrado:")
    for action in plan:
        print(action.name)
else:
    print("No se puede encontrar un plan para alcanzar el estado objetivo.")

    