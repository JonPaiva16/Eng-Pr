"""
Gerenciador de pedidos para a atividade de refatoracao.

ATENCAO: este codigo foi escrito de proposito com varios code smells.
A tarefa do aluno e:
  1. Rodar os testes e confirmar que passam.
  2. Rodar o ruff e identificar os problemas.
  3. Refatorar mantendo todos os testes em verde.

Smells presentes (nao se limita a esses):
  - Long Method (processar_pedido)
  - Long Parameter List (7 parametros)
  - Magic Numbers (0.85, 0.90, 0.80, 15, 20, 18, 30, 200, 1.05, ...)
  - Duplicated Code (calculo de subtotal em dois lugares)
  - Primitive Obsession (cliente como strings, itens como dicts)
"""


class GerenciadorPedidos:

    def processar_pedido(self, cliente_nome, cliente_email, cliente_tipo,
                         itens, cupom, regiao, forma_pagamento):
        # calcula subtotal somando precos
        total = 0
        for item in itens:
            total = total + item['preco'] * item['quantidade']

        # desconto por tipo de cliente
        if cliente_tipo == 'vip':
            total = total * 0.85
        elif cliente_tipo == 'premium':
            total = total * 0.90

        # desconto por cupom
        if cupom == 'DESC10':
            total = total * 0.90
        elif cupom == 'DESC20':
            total = total * 0.80

        # calculo do frete por regiao
        if regiao == 'SP':
            frete = 15
        elif regiao == 'RJ':
            frete = 20
        elif regiao == 'MG':
            frete = 18
        else:
            frete = 30

        # frete gratis acima de certo valor
        if total > 200:
            frete = 0

        total_final = total + frete

        # juros de cartao de credito
        if forma_pagamento == 'cartao':
            total_final = total_final * 1.05

        # monta comprovante
        comprovante = "Pedido para " + cliente_nome + " (" + cliente_email + ")\n"
        comprovante = comprovante + "Total: R$ " + str(round(total_final, 2))

        return {
            'cliente': cliente_nome,
            'subtotal': total,
            'frete': frete,
            'total': round(total_final, 2),
            'comprovante': comprovante
        }

    def calcular_total_relatorio(self, pedidos):
        # NOTA: este metodo repete a logica de soma de itens
        total = 0
        for pedido in pedidos:
            for item in pedido['itens']:
                total = total + item['preco'] * item['quantidade']
        return total
