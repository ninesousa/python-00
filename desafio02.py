import textwrap

def main():
    AGENCIA = "0001"
    LIMITE_SAQUES = 3

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
        escolha = menu()

        if escolha == "d": #depositar
            valor = float(input("Informe o valor do deposito: R$ "))           
            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif escolha == "s": #sacar
            valor = float(input("Informe o valor do saque: R$ "))
            
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )
            
        elif escolha == "e": # extrato
            mostrar_extrato(saldo, extrato=extrato)
        
        elif escolha == "u": # novo usuario
            novo_usuario(usuarios)
     
        elif escolha == "c": # nova conta
            numero_conta = len(contas) + 1
            conta = nova_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
                
        elif escolha == "l":# listas
            listar_contas(contas)
               
        elif escolha == "q":
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada")    
        
def menu():
    menu = """
    ~~~~~~~~~~~~~ MENU ~~~~~~~~~~~~~

    [d] \tDepositar
    [s] \tSacar
    [e] \tExtrato
    [u] \tNovo Usuário
    [c] \tNova Conta
    [l] \tListar Contas
    [q] \tSair
    "
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: \t R$ {valor:.2f}\n"
        print("\n ~~~~ Deposito realizado com sucesso! ~~~~ ")
    else:
        print("\nOperação falhou! O valor informado é inválido.")
        
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    
    if excedeu_saldo:
        print("\n Operação falhou! Você não tem saldo suficiente.")
    
    elif excedeu_limite:
        print("\n Operação falhou! O valor do saque excedeu o limite.")
    
    elif excedeu_saques:
        print("\n Operação falhou! Número máximo de saques excedido.")
        
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n ~~~ Saque Realizado com sucesso! ~~~")
            
    else:
        print("\n Operação falhou! O valor informado é inválido")
        
    return saldo, extrato, numero_saques
        
def mostrar_extrato(saldo, /, *, extrato):
    print("~~~~~~~~~ Extrato ~~~~~~~~~~")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: \t\t R$ {saldo:.2f}")
    print("~~~~~~~~~~~~~~~~~~")
       
def novo_usuario(usuarios):
    cpf = input("Informe o seu CPF: ")
    usuario = filtrar_user(cpf, usuarios)
    
    if usuario:
        print("\nJá existe usupario com esse CPF!")
        return
    
    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd--mm-aaaa): ")
    endereco = input("Endereço (Logadouro, n - Bairro - Cidade/UF) : ")
    
    usuarios.append({"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco})
    
    print("~~~ Usuário criado com sucesso! ~~~")
    
def filtrar_user(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def nova_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_user(cpf, usuarios)
    
    if usuario:
        print("\n ~~~ Conta criada com sucesso! ~~~")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: \t{conta["agencia"]}
            C/C: \t{conta["numero_conta"]} 
            Titular: \t{conta["usuario"]["nome"]} 
             
        """
        print("~" * 50)
        print(textwrap.dedent(linha))
        
main()