from datetime import datetime
from database import criar_tabela, inserir_insumo, listar_insumos
from relatorios import gerar_relatorio_estoque



def menu():
    print("\n=== CONTROLE DE INSUMOS ===")
    print("1 - Cadastrar insumo")
    print("2 - Listar estoque")
    print("3 - Gerar relatório")
    print("4 - Sair")


def cadastrar_insumo():
    nome = input("Nome: ")
    tipo = input("Tipo: ")
    quantidade = float(input("Quantidade: "))
    unidade = input("Unidade (kg, L, un): ")
    data = datetime.now().strftime("%d/%m/%Y")

    inserir_insumo(nome, tipo, quantidade, unidade, data)
    print("✅ Insumo cadastrado!")


def listar_estoque():
    insumos = listar_insumos()

    if not insumos:
        print("Estoque vazio.")
        return

    print("\n--- ESTOQUE ---")
    for insumo in insumos:
        print(f"{insumo[1]} - {insumo[3]} {insumo[4]}")


def main():
    criar_tabela()

    while True:
        menu()
        opcao = input("Opção: ")



        if opcao == "1":
            cadastrar_insumo()
        elif opcao == "2":
            listar_estoque()
        elif opcao == "3":
            gerar_relatorio_estoque()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


main()
