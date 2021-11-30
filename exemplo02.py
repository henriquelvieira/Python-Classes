class Cliente:
    """
    Exemplo de Classe em Python
    """
    def __init__(self, nome, email, plano):
        """
        :param nome: Nome do cliente
        :param email: Endereço de Email
        :param plano: Plano escolhido
        """
        self.nome = nome
        self.email = email
        self.lista_planos = ['basic', 'premium']

        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception(f'Plano inválido')

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            raise Exception(f'Plano inválido')

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f'Ver filme {filme}')
        elif self.plano == 'premium':
            print(f'Ver filme {filme}')
        else:
            raise Exception(f'Filme não disponível no seu plano, faça upgrade do seu plano')


cliente = Cliente("Henrique", "email@teste.com.br", "basic")
print(f'Plano: {cliente.plano}')


cliente.ver_filme("teste", "premium")

cliente.mudar_plano("premium")
print(f'Plano: {cliente.plano}')

cliente.ver_filme("teste", "premium")