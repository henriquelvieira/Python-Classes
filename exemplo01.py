class ControleRemoto:
    """
    Exemplo de Classe em Python
    """
    def __init__(self, cor, altura, profundidade, largura):
        """
        :param cor: Cor do Controle
        :param altura: Altura do Controle
        :param profundidade: Profundidade do Controle
        :param largura: Largura do Controle
        """
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

    def passarCanal(self, botao):
        """
        Função para passagem de canais

        :param botao: Botão que foi pressionado (+,-)
        :return print com o resultado do botão que foi pressionado
        """
        if botao.upper() == "+":
            print("Aumentar Canal")
        elif botao.upper() == "-":
            print("Diminuir Canal")


controle_remoto = ControleRemoto("preto", "10cm", "3cm", "5cm")
print(controle_remoto.cor)
print(controle_remoto.altura)
print(controle_remoto.profundidade)
print(controle_remoto.largura)

controle_remoto.passarCanal("+")
        
        