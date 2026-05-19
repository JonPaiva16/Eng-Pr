class Calculadora:
    def soma(self, n1, n2):
        res = n1 + n2
        return res



    def subtracao(self, n1, n2):
        res = n1 - n2
        return res

    def multiplicacao(self, n1, n2):
        res = n1 * n2
        return res

    def divisao(self, n1, n2):

        if n2 == 0:
            raise ValueError("Não pode dividir por zero")

        res = n1 / n2

        return res

    def potenciacao(self, n1, n2):
        res = n1 ** n2
        return res