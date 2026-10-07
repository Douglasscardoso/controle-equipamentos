
class Emprestimo:
    def __init__(self, pessoa, equipamento, quantidade):
        self.pessoa = pessoa 
        self.equipamento = equipamento
        self.quantidade = quantidade

    def registrar(self, emprestimos):
        resultado = self.equipamento.emprestar(self.quantidade)
        resposta = isinstance(resultado,int)

        if resposta:
             print("registrado")
             emprestimos.append(self)
        else:
            print("não foi possível registrar")
            print(resultado)

      

