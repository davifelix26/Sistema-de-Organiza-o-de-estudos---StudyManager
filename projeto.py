# Funções do Gerenciador de tarefas
lista_tarefas = []
sessoes_estudos = []
def adicionar_tarefas(materia, tema, data_entrega, atencao, tipo_tarefa):
    estrutura_tarefa = {
        "Disciplina":materia,
        "Conteudo":tema,
        "Prazo":data_entrega,
        "Prioridade":atencao,
        "Tipo":tipo_tarefa,
        "Status": 'Pendente',
    }
    lista_tarefas.append(estrutura_tarefa)
    print("Tarefa adicionada com sucesso!")
def ver_tarefas():
    if not lista_tarefas:
        print("TAREFA VAZIA")
    else:
        print(10 * "=", "TAREFAS", 10 * "=")
        for c, i in enumerate(lista_tarefas):
            print(f"[{c+1}]\t{i['Disciplina']}")
            print(f"\tTipo: {i['Tipo']}")
            print(f"\tTema: {i['Conteudo']}")
            print(f"\tData: {i['Prazo']}")
            print(f"\tPrioridade: {i['Prioridade']}")
            print(f"\tStatus: {i['Status']}")
def concluir_tarefas(elemento):
    if 1 <= elemento <= len(lista_tarefas):
        if lista_tarefas[elemento-1]['Status'] == 'Concluído':
            print("Essa tarefa já foi concluída")
        else:
            lista_tarefas[elemento-1]['Status'] = 'Concluído'
            print("Tarefa concluída com sucesso!".upper())
    else:
        print("Esta tarefa não existe tente novamente.")
    """
    0 1 tarefa
    1 2 tarefa
    2 3 tarefa
    3 4 tarefa
    4  5
    """

def remover_tarefas(posicao):
    if 1 <= posicao <= len(lista_tarefas):
        lista_tarefas.pop(posicao-1)
        print("TAREFA REMOVIDA COM SUCESSO. A TAREFA {} FOI REMOVIDA COM SUCESSO!".format(posicao))
    else:
        print("ESSA TAREFA NÃO EXISTE. TENTE NOVAMENTE.")
# Funções do Gerenciador de Estudos
def adicionar_sessao_estudos(nome_materia, tema, dia, horario_inicial, horario_final, objetivo):
    estrutura_sessao = {
        "Materia":nome_materia,
        "Conteudo":tema,
        "Data":dia,
        "Horario_inicial":horario_inicial,
        "Horario_final":horario_final,
        "Finalidade":objetivo,
        "Status":"Pendente"
    }
    sessoes_estudos.append(estrutura_sessao)
    print("Sessão adicionada com sucesso!")
def ver_sessao():
    if not sessoes_estudos:
        print("Sua sessão de estudos está vazia.")
    else:
        print("=" * 10, "SESSÕES DE ESTUDOS", "=" * 10)
        for c, v in enumerate(sessoes_estudos):
            print(f"[{c+1}]\n{v['Data']} - {v['Horario_inicial']} ás {v['Horario_final']}")
            print(f"{v['Materia']}\n{v['Conteudo']}")
            print(f"Objetivo: {v['Finalidade']}")
# Menu principal
while True:
    print(58 * "=", end='\n')
    print("\t\t\t\t\tSTUDYMANAGER\t\t", end='\n')
    print(58 * "=", end='\n\n')
    print("1 - Gerenciar Tarefas")
    print("2 - Gerenciar Estudos")
    print("0 - Sair")
    try:
        opcao = int(input("Escolha uma opção: ".strip()))
        if opcao == 1:
            # Menu Principal do Gerenciador de Tarefas
            while True:
                print(10 * "=", "TAREFAS", 10 * "=", end='\n\n')
                print("1 - Adicionar Tarefas")
                print("2 - Ver Tarefas")
                print("3 - Concluir Tarefas")
                print("4 - Remover Tarefas")
                print("0 - Voltar ao menu")
                try:
                    entrada = int(input("Escolha uma opção: ".strip()))
                    if entrada == 1:
                        disciplina = input("Informe o nome da materia: ").strip()
                        conteudo = input("Informe o qual o tema da sua tarefa ou trabalho: ").strip().capitalize()
                        prazo = input("Informe a data em que a tarefa será entregue: ").strip()
                        print("Prioridade:\n1 - Alta\n2 - Media\n3 - Baixa\n")
                        prioridade = int(input("Escolha uma das opções: "))
                        while True:
                            if prioridade == 1:
                                prioridade = 'Alta'
                                break
                            elif prioridade == 2:
                                prioridade = 'Media'
                                break
                            elif prioridade == 3:
                                prioridade = 'Baixa'
                                break
                            else:
                                print("Prioridade:\n1 - Alta\n2 - Media\n3 - Baixa\n")
                                print("Por favor, informe apenas as opções acima.")
                                prioridade = int(input("Escolha uma das opções: "))
                        print("1 - Prova\n2 - Trabalho\n3 - Lição de casa")
                        tipo = int(input("Informe uma dessas opções: "))
                        while True:
                            if tipo == 1:
                                tipo = 'Prova'
                                break
                            elif tipo == 2:
                                tipo = 'Trabalho'
                                break
                            elif tipo == 3:
                                tipo = 'Lição de casa'
                                break
                            else:
                                print("Opção inválida. Tente novamente.")
                                print("1 - Prova\n2 - Trabalho\n3 - Lição de casa")
                                tipo = int(input("Informe uma dessas opções: "))
                        adicionar_tarefas(disciplina, conteudo, prazo, prioridade, tipo)
                    elif entrada == 2:
                        ver_tarefas()
                    elif entrada == 3:
                        ver_tarefas()
                        if not lista_tarefas:
                            print("A sua lista está vazia")
                        else:
                            try:
                                concluir = int(input("Informe o número da lista que você deseja concluir: "))
                                concluir_tarefas(concluir)
                            except ValueError:
                                print("HOUVE UM ERRO, TENTE NOVAMENTE.")
                    elif entrada == 4:
                        if not lista_tarefas:
                            print("SUA LISTA DE TAREFAS ESTÁ VAZIA. TENTE NOVAMENTE.")
                        else:
                            ver_tarefas()
                            remove = int(input("Informe o número da tarefa que você deseja remover: "))
                            remover_tarefas(remove)
                    elif entrada == 0:
                        print("Voltando ao menu principal...")
                        break
                    else:
                        print("Informe apenas uma das opções acima.".upper())
                except ValueError:
                    print("Valor inválido, por favor tente novamente")
                except KeyboardInterrupt:
                    break
        elif opcao == 2:
            # Menu Principal do Gerenciador de Estudos
            while True:
                print(10 * "=", "ESTUDOS", 10 * "=", end='\n\n')
                print("1 - Adicionar Sessão de Estudos.")
                print("2 - Ver Sessões de Estudos.")
                print("0 - Voltar ao menu")
                try:
                    entrada2 = int(input("Escolha uma das opções: ".strip()))

                    if entrada2 == 1:
                        materia_sessao = input("Informe a matéria de sessão: ").strip().capitalize()
                        conteudo = input("Informe o conteúdo da matéria: ").strip().capitalize()
                        data = input("Informe a data para você ir estudar: ").strip()
                        horario_inicio = input("Informe um horário inicial em que irá estudar: ").strip()
                        horario_fim = input("Informe um horário final em irá parar de estudar:  ").strip()
                        finalidade = input("Informe seu objetivo com essa sessão: ").capitalize().strip()
                        adicionar_sessao_estudos(materia_sessao, conteudo, data, horario_inicio, horario_fim, finalidade)
                    elif entrada2 == 2:
                        ver_sessao()
                    elif entrada2 == 0:
                        print("Voltando ao menu principal...")
                        break
                    else:
                        print("Informe apenas uma das opções acima.".upper())
                except ValueError:
                    print("Escolha inválida, por favor tente novamente.")
                except KeyboardInterrupt:
                    break
        elif opcao == 0:
            print("Saindo do sistema...")
            break
        else:
            print("Informe apenas uma das opções acima.".upper())
    except ValueError:
        print("Você informou um valor inválido. Tente Novamente.".upper())
    except KeyboardInterrupt:
        break
