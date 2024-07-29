class Medico:
    def __init__(self, nome, especialidade, numero_registro):
        self.nome = nome
        self.especialidade = especialidade
        self.numero_registro = numero_registro

class Paciente:
    def __init__(self, nome, data_nascimento, telefone):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.telefone = telefone

class Consulta:
    def __init__(self, data, horario, medico, paciente):
        self.data = data
        self.horario = horario
        self.medico = medico
        self.paciente = paciente

class Clinica:
    def __init__(self):
        self.medicos = {}
        self.pacientes = {}
        self.consultas = []
        self.indice_consulta = 1

    def cadastrar_medico(self):
        nome = input("Digite o nome do médico: ")
        especialidade = input("Digite a especialidade do médico: ")
        numero_registro = input("Digite o número de registro do médico: ")
        self.medicos[numero_registro] = {"nome": nome, "especialidade": especialidade}

    def cadastrar_paciente(self):
        nome = input("Digite o nome do paciente: ")
        data_nascimento = input("Digite a data de nascimento do paciente (no formato AAAA-MM-DD): ")
        telefone = input("Digite o telefone do paciente: ")
        self.pacientes[nome] = {"data_nascimento": data_nascimento, "telefone": telefone}

    def agendar_consulta(self):
        medico_registro = input("Digite o número de registro do médico: ")
        paciente_nome = input("Digite o nome do paciente: ")

        if medico_registro in self.medicos and paciente_nome in self.pacientes:
            data_consulta = input("Digite a data da consulta (no formato DD/MM/AAAA): ")
            horario_consulta = input("Digite o horário da consulta: ")

            consulta = {
                "indice": self.indice_consulta,
                "data": data_consulta,
                "horario": horario_consulta,
                "medico": self.medicos[medico_registro]["nome"],
                "paciente": paciente_nome
            }
            self.consultas.append(consulta)
            self.indice_consulta += 1
            print(f"Consulta agendada com sucesso! Índice da consulta: {consulta['indice']}")
        else:
            print("Médico ou paciente não encontrado.")

    def excluir_consulta(self):
        indice = int(input("Digite o índice da consulta a ser excluída: "))
        for consulta in self.consultas:
            if consulta["indice"] == indice:
                self.consultas.remove(consulta)
                print(f"Consulta de índice {indice} excluída com sucesso.")
                return
        print(f"Consulta de índice {indice} não encontrada.")

    def alterar_consulta(self):
        indice = int(input("Digite o índice da consulta a ser alterada: "))
        for consulta in self.consultas:
            if consulta["indice"] == indice:
                data_consulta = input("Digite a nova data da consulta (no formato DD/MM/AAAA): ")
                horario_consulta = input("Digite o novo horário da consulta: ")
                consulta["data"] = data_consulta
                consulta["horario"] = horario_consulta
                print(f"Consulta de índice {indice} alterada com sucesso.")
                return
        print(f"Consulta de índice {indice} não encontrada.")

    def listar_consulta(self):
        print("\nConsultas agendadas:")
        for consulta in self.consultas:
            print(f"Índice: {consulta['indice']}")
            print(f"Data: {consulta['data']}")
            print(f"Horário: {consulta['horario']}")
            print(f"Médico: {consulta['medico']}")
            print(f"Paciente: {consulta['paciente']}")
            print("-" * 20)

    def cancelar_consulta(self):
        indice = int(input("Digite o índice da consulta a ser cancelada: "))
        for consulta in self.consultas:
            if consulta["indice"] == indice:
                self.consultas.remove(consulta)
                print(f"Consulta de índice {indice} cancelada com sucesso.")
                return
        print(f"Consulta de índice {indice} não encontrada.")

    def menu_principal(self):
        while True:
            print("\n===== Menu =====")
            print("1. Cadastrar médico")
            print("2. Cadastrar paciente")
            print("3. Agendar consulta")
            print("4. Excluir consulta")
            print("5. Alterar consulta")
            print("6. Listar consultas")
            print("7. Cancelar consulta")
            print("0. Sair")

            opcao = input("Digite o número da opção desejada: ")
            if opcao == "1":
                self.cadastrar_medico()
            elif opcao == "2":
                self.cadastrar_paciente()
            elif opcao == "3":
                self.agendar_consulta()
            elif opcao == "4":
                self.excluir_consulta()
            elif opcao == "5":
                self.alterar_consulta()
            elif opcao == "6":
                self.listar_consulta()
            elif opcao == "7":
                self.cancelar_consulta()
            elif opcao == "0":
                print("Encerrando o programa. Até logo!")
                break
            else:
                print("Opção inválida. Digite um número válido.")

clinica = Clinica()
clinica.menu_principal()
