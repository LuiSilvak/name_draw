# Importando biblioteca
import random

def sorteio_de_nomes():
    print("=== Sorteio de Nomes ===")
    print("Digite os nomes separados por vírgula (,).")
    entrada = input("Lista de nomes: ")

    # Divide os nomes em uma lista, removendo espaços extras
    nomes = [nome.strip() for nome in entrada.split(",") if nome.strip()]

    if not nomes:
        print("Nenhum nome válido foi fornecido. Tente novamente.")
        return
    
    # Sorteia um nome aleatoriamente
    vencedor = random.choice(nomes)
    print(f"\nO nome sorteado foi: {vencedor}")


if __name__ == "__main__":
    sorteio_de_nomes()