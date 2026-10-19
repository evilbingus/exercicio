materiais = {
    "mouse": 10,
    "teclado": 6,
    "cabo": 20
}
 
nome = input("Qual material deseja retirar? ").lower()
 
try:
    quantidade = int(input("Quantas unidades? "))
 
    if nome not in materiais:
        print("Material não encontrado no estoque!")
 
    elif quantidade <= 0:
        print("A quantidade deve ser maior que zero!")
 
    elif quantidade > materiais[nome]:
        print("Estoque insuficiente!")
        print(f"Quantidade disponível: {materiais[nome]}")
 
    else:
        materiais[nome] -= quantidade
        print("Retirada realizada com sucesso!")
 
    print("\nEstoque atual:")
    print(materiais)
 
except ValueError:
    print("Digite uma quantidade numérica válida!")
 