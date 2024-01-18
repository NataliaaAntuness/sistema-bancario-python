from datetime import datetime

class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo
        self.saques_diarios = 0
        self.limite_saques_diarios = 3
        self.limite_diario_valor = 500
        self.ultima_data_saque = None

    def _resetar_limites_diarios(self):
        hoje = datetime.now().date()
        if self.ultima_data_saque != hoje:
            self.saques_diarios = 0
            self.limite_diario_valor = 500
            self.ultima_data_saque = hoje

    def deposito(self, valor):
        self.saldo += valor
        return f'Depósito de {valor} realizado. Saldo atual: {self.saldo}'

    def saque(self, valor):
        self._resetar_limites_diarios()

        if self.saques_diarios >= self.limite_saques_diarios or valor > self.limite_diario_valor:
            return 'Limite diário de saques atingido ou valor excede o limite diário.'

        if self.saques_diarios >= self.limite_saques_diarios - 1:
            return 'Alerta: Você atingiu o limite máximo de saques para o dia.'

        if valor > self.saldo:
            return 'Saldo insuficiente.'
        else:
            self.saldo -= valor
            self.saques_diarios += 1
            self.limite_diario_valor -= valor
            return f'Saque de {valor} realizado. Saldo atual: {self.saldo}'

    def extrato(self):
        return f'Saldo atual: {self.saldo}. Limite diário restante: {self.limite_diario_valor}'



conta = ContaBancaria()

print(conta.deposito(100))
print(conta.saque(30))
print(conta.saque(40))
print(conta.saque(50))
print(conta.saque(60))
print(conta.extrato())
