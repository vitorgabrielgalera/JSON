alunos = {
    "Giovana": {
        "idade": 20,
        "curso": "Sistemas de Informação",
        "semestre": 4
    },
    "Geoge": {
        "idade": 22,
        "curso": "Análise e Desenvolvimento de Sistemas",
        "semestre": 2
    },
    "Vitor": {
        "idade": 19,
        "curso": "Sistemas de Informação",
        "semestre": 3
    },
    "Marcelo": {
        "idade": 23,
        "curso": "Ciência da Computação",
        "semestre": 6
}
}
print(alunos["Giovana"]["idade"])

import json

with open("alunos.json", "w", encoding="utf-8") as f:
    json.dump(alunos, f, indent=4, ensure_ascii=False)