valores = [
    5,
    4 + 2j,
    "OBA",
    True,
    None,      
    [1, 2, 3], 
    (4, 5, 6), 
    {7, 8, 9},
    {"a": 1, "b": 2}
]

for valor in valores: 
    print(f"Valor: {valor} - Tipo: {type(valor)} - Nome: {type(valor)}")
