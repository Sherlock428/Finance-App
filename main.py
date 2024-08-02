from utilitario import (cadastrar_categoria, cadastrar_transacao, exibir_transacao, exibir_categorias, saldo_total, deletar_categorias, atualizar_categoria)
import os

def main():
    while True:
        saldo = saldo_total()
        os.system('cls')
        print(f"""
{'=' * 30}
{'SUAS FINANÇAS'.center(30)}
{'=' * 30}
{'SEU SALDO:'} R${saldo:.2f}
{'-' * 30}
[1] Cadastrar Transação
[2] Cadastrar Categorias
[3] Exibir Transações
[4] Editar Categorias

[0] Sair
""")
        
        try:
            opcao = int(input("Selecione: "))

            if opcao == 1:
                os.system('cls')
                print(f"{'=' * 30}\n"
                      f"{'Adicionar Transação'.center(30)}\n"
                      f"{'=' * 30}\n")
                cadastrar_transacao()
            elif opcao == 2:
                os.system('cls')
                print(f"{'=' * 30}\n"
                      f"{'Cadastrar Categorias'.center(30)}\n"
                      f"{'=' * 30}")
                cadastrar_categoria()
            elif opcao  == 3:
                os.system('cls')
                print(f"{'=' * 30}\n"
                      f"{'Exibir Transação'.center(30)}\n"
                      f"{'=' * 30}\n")
                exibir_transacao()
            elif opcao == 4:
                os.system('cls')
                print(f"""
{'=' * 30}
{'Editar Categoria'.center(30)}
{'=' * 30}

[1] Ver Categorias
[2] Remover
[3] Atualizar

[0] Retornar ao Menu
""")
                o = int(input("Selecione: "))

                if o == 1:
                    os.system('cls')
                    print(f"{'=' * 30}\n"
                          f"{'Categorias'.center(30)}\n"
                          f"{'=' * 30}\n")
                    exibir_categorias()
                    input("\n[Enter] -> Retornar ao Menu")
                elif o == 2:
                    os.system('cls')
                    print(f"{'=' * 30}\n"
                          f"{'Remover Categoria'.center(30)}\n"
                          f"{'=' * 30}\n")
                    deletar_categorias()
                    input("\n[Enter] -> Retornar ao Menu")
                elif o == 3:
                    os.system('cls')
                    print(f"{'=' * 30}\n"
                          f"{'Atulizar Categoria'.center(30)}\n"
                          f"{'=' * 30}\n")
                    atualizar_categoria()
                    input("\n[Enter] -> Retornar ao Menu")
            elif opcao == 0:
                break
        except (ValueError, TypeError):
            print("ERROR:")
            input("Retornar: ")

if __name__ == "__main__":
    main()


































# Categorias

# receita = cadastrar_categoria(nome="Receita")
# despesas = cadastrar_categoria(nome="Despesas")
# despesas_fixa = cadastrar_categoria(nome="Despesas Fixa")
# viagem = cadastrar_categoria(nome="Viagens")

# Transações

# t1 = cadastrar_transacao(descricao="Salario", valor=10000, categoria=receita)
# t1 = cadastrar_transacao(descricao="Internet", valor=-70, categoria=despesas_fixa)
# t1 = cadastrar_transacao(descricao="Disney", valor=-3000, categoria=viagem)

# total = saldo_total()
# print(total)
