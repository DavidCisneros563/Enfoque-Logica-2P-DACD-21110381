#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

from pysat.solvers import Glucose3

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

class SATPlan:
    def __init__(self, actions, initial_state, goal_state):
        self.actions = actions
        self.initial_state = initial_state
        self.goal_state = goal_state

    def plan(self):
        solver = Glucose3()

        # Asignar variables a los literales de estado inicial y objetivo
        state_variables = {literal: index for index, literal in enumerate(self.initial_state | self.goal_state, 1)}
        goal_variables = {literal: index for index, literal in enumerate(self.goal_state, len(state_variables) + 1)}

        # Codificar cláusulas para el estado inicial
        for literal in self.initial_state:
            solver.add_clause([state_variables[literal]])

        # Codificar cláusulas para el objetivo
        for literal in self.goal_state:
            solver.add_clause([goal_variables[literal]])

        # Codificar cláusulas para las acciones y efectos
        for action in self.actions:
            for state_literal in self.initial_state:
                if state_literal in action.preconditions:
                    solver.add_clause([-state_variables[state_literal], state_variables[action.effects[0]]])

        # Resolver
        if solver.solve():
            plan = []
            for literal, variable_index in goal_variables.items():
                if solver.get_model()[variable_index - 1] > 0:
                    plan.append(literal)
            return plan
        else:
            return None

# Definir acciones
actions = [
    Action("AgarrarLeche", {"LecheEnLaNevera"}, {"-LecheEnLaNevera", "LecheEnLaBolsa"}),
    Action("IrASupermercado", {"Dinero", "SupermercadoAbierto"}, {"-Dinero", "LecheEnLaNevera"}),
    Action("ComprarLeche", {"Dinero", "SupermercadoAbierto"}, {"-Dinero", "LecheEnLaBolsa"}),
]

# Definir estado inicial y estado objetivo
initial_state = {"LecheEnLaNevera", "Dinero", "SupermercadoAbierto"}
goal_state = {"LecheEnLaNevera"}

# Crear planificador y planificar
planner = SATPlan(actions, initial_state, goal_state)
plan = planner.plan()

# Mostrar el plan resultante
if plan:
    print("Plan encontrado:")
    for action in plan:
        print(action)
else:
    print("No se puede encontrar un plan para alcanzar el estado objetivo.")

    