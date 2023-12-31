# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

# instalar la biblioteca pgmpy. 
pip install pgmpy

from pgmpy.models import DecisionNetwork

# Crear una instancia de la red de decisi�n
decision_network = DecisionNetwork()

# Definir las variables de decisi�n y sus valores
decision_network.add_node("Lluvia", ["Si", "No"])
decision_network.add_node("Traje", ["Si", "No"])
decision_network.add_node("Llevar_Paraguas", ["Si", "No"])

# Definir la relaci�n entre las variables de decisi�n
decision_network.add_edge("Lluvia", "Llevar_Paraguas")
decision_network.add_edge("Traje", "Llevar_Paraguas")

# Asignar una tabla de decisi�n a la variable de decisi�n "Llevar_Paraguas"
decision_network.add_cpds(
    "Llevar_Paraguas",
    {
        "Lluvia": {"Si": 0.9, "No": 0.2},
        "Traje": {"Si": 0.7, "No": 0.1},
        "Llevar_Paraguas": {"Si": 1.0, "No": 0.0},
    }
)

# Verificar la consistencia de la red de decisi�n
assert decision_network.check_model()

# Imprimir la tabla de decisi�n de "Llevar_Paraguas"
print("Tabla de decisi�n de 'Llevar_Paraguas':")
print(decision_network.get_cpds("Llevar_Paraguas"))
