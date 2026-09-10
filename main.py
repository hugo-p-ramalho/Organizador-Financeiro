import csv
import os
import matplotlib.pyplot as plt

def ver_grafico():
    if not gastos:
        print("Sem dados pro gráfico.\n")
        return
    
ARQUIVO = "gastos.csv"
gastos = []

# Carrega se já existir
if os.path.exists(ARQUIVO):
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for linha in reader:
            linha["valor"] = float(linha["valor"])
            gastos.append(linha)

def salvar():
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["descricao", "valor", "categoria"])
        writer.writeheader()
        writer.writerows(gastos)

def adicionar_gasto():
    descricao = input("O que comprou? ")
    valor = float(input("Quanto? R$ "))
    categoria = input("Categoria: ")
    gastos.append({"descricao": descricao, "valor": valor, "categoria": categoria})
    salvar()
    print("✓ Salvo e gravado no CSV!\na")

def ver_resumo():
    if not gastos:
        print("Nenhum gasto.\n")
        return
    total = 0
    por_categoria = {}
    for g in gastos:
        total += g["valor"]
        por_categoria[g["categoria"]] = por_categoria.get(g["categoria"], 0) + g["valor"]
    
    print("\n--- RESUMO ---")
    for cat, val in por_categoria.items():
        print(f"{cat}: R$ {val:.2f}")
    print(f"TOTAL GERAL: R$ {total:.2f}\n")

while True:
    print("1-Adicionar | 2-Resumo | 3-Gráfico | 4-Sair")
    op = input("> ")
    if op == "1": adicionar_gasto()
    elif op == "2": ver_resumo()
    elif op == "3": ver_grafico()
    elif op == "4": break

def ver_grafico():
    if not gastos:
        print("Sem dados pro gráfico.\n")
        return
    
    por_categoria = {}
    for g in gastos:
        por_categoria[g["categoria"]] = por_categoria.get(g["categoria"], 0) + g["valor"]

    categorias = list(por_categoria.keys())
    valores = list(por_categoria.values())

    plt.figure()
    plt.bar(categorias, valores)
    plt.title("Gastos por Categoria")
    plt.ylabel("R$ ")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig("grafico.png")
    print("✓ Gráfico salvo como grafico.png\n")