#CODE BY ROBERT SANTANA
import os

class ErrorMessages:
    def __init__(self) -> None:
        pass
    
    def InvalidValue():
        print("Operação falhou! O valor informado é inválido!")
    def InvalidOption():
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        
class Valores:
    
    def __init__(self, saldo, limite, numeroDeSaques, limiteSaques) -> None: #CONSTRUCTOR
        self.saldo = saldo
        self.limite = limite
        self.numeroDeSaques = numeroDeSaques
        self.limiteSaques = limiteSaques
        self.extrato = []

    def SetSaldo(self,saldo):
        self.saldo = saldo
        
    def SetNumeroDeSaques(self, numeroDeSaques):
        self.numeroDeSaques = numeroDeSaques

    def RealizarDeposito(self, valor):
        self.saldo += valor
        self.extrato.append(f"Depósito: R$ {valor:.2f}")
    
    def RealizarSaque(self, valor):
        if (valor > self.saldo):
            print("Operação falhou! Você não tem saldo suficiente!")
        elif (valor > self.limite):
            print("Operação falhou! O valor do saque excede o limite.")
        elif (self.numeroDeSaques > self.limiteSaques):
            print("Operação falhou! Número de saques excedido")
        else:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            self.numeroDeSaques += 1
            
    def ImprimirExtrato(self):
        print("\n================ EXTRATO ====================")
        
        if(len(self.extrato) == 0):
            print("Não foram realizadas movimentações.")
        else:
            for item in self.extrato:
                print(item)
        
        print("\nSaldo: R$%.2f" % self.saldo)
        print("===============================================")
    
def ClearScreen():
    if os.name == "nt":
        os.system("cls")

def ContextMenu():
    print("""
    [d] deposito
    [s] saque
    [e] extrato
    [q] sair
    =>
    """)

def GetValue(text):
    valor = float(input(f"{text}"))
    return valor
        

if __name__ == "__main__":
    
    contaBancaria = Valores(0, 500, 0, 3)
    error = ErrorMessages()
    while (True):
        ContextMenu()
        
        opcao = input()
        ClearScreen()
        match opcao:
            case "d":
                valor = GetValue("Informe o valor de depósito: ")
                if(valor > 0):
                    contaBancaria.RealizarDeposito(valor)
                else:
                    error.InvalidValue()
                
            case "s":
                valor = GetValue("Informe o valor do saque:")
                if (valor > 0):
                    contaBancaria.RealizarSaque(valor)
                else:
                    error.InvalidValue()
                    
            case "e":
                contaBancaria.ImprimirExtrato()
            
            case "q":
                exit()
            
            case _:
                error.InvalidOption()
        input("\nAperte qualquer tecla para mais operações:")
        ClearScreen()

