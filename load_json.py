import json

#abre o arquivos que contém o dicionário

#Método 1 usando o with
#with open("alunos.json", "r", encoding="utf-8") as f:
    #alunos = json.load(f)

#Método 2 usando open
alunos = json.load(open("alunos.json", "r", encoding="utf-8"))

while True:
    print("Digite a opção desejada:")
    print("1 - Cadastrar aluno")
    print("2 - Buscar aluno")
    print("3 - sair")

    opcao = input("opção: ")

    #cadastrar o aluno
    if opcao == "1":
        novo_aluno = input("Qual o nome do aluno? ")
        if alunos.get(novo_aluno, False):
            print("aluno já cadastrado!")
            continue
        novo_idade = input("Qual a idade do aluno? ")
        novo_curso = input("Qual o curso do aluno? ")
        novo_semestre = input("Em que semestre o aluno está? ")    
        alunos[novo_aluno] = {
            "idade": novo_idade,
            "curso": novo_curso,
            "semestre": novo_semestre
        }

        json.dump(alunos, open("alunos.json", "w", encoding="utf-8"), indent=4, ensure_ascii=False)

    #buscar aluno
    if opcao == "2": 
        input_aluno = input("Digite o nome do aluno: ")

        dados = alunos.get(input_aluno, False)

        if dados:
            print("Dados do aluno: ", input_aluno)
            print(alunos[input_aluno])

        else:
            print("Aluno não encontrado")

    #sair do programa
    if opcao == "3":
        break