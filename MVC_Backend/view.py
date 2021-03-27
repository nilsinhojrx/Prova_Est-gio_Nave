from controller import PessoaCtrl
from dal import PessoaDal

while True:
    
    d = input("Olá. Seja bem vindo. Digite o que deseja fazer: Registrar / Visualizar / Buscar /Sair ")
    
    if (d == 'Sair' or d == 'sair' or d =='SAIR'): # Sair
        
        s = input("Tem certeza que deseja sair? ( sim / não )")
        if (s == 'sim' or s =='SIM' or s=='Sim'):
             print("Obrigado por usar nosso sistema! ")
             break
         
        elif (s == 'não' or s == 'Não' or s =='NÃO'):
            continue
    
    elif(d == 'Registrar' or d == 'registrar' or d=='REGISTRAR' ): # Registrar dados
        
        nome, idade, cpf = input("Digite o nome: "), int(input("Digite sua idade: ") ), input("Digite o CPF: ");
        try:
            PessoaCtrl.cadastrar(nome, idade, cpf)
        except:
            print("Informe valores válidos!")

    elif(d == 'Visualizar' or d == 'visualizar' or d == 'VISUALIZAR'): # Visualizar dados
        PessoaDal.ler() 
        
    elif(d == 'buscar' or d == 'Buscar' or d == 'BUSCAR'): # Buscar daods específicos
         valor = input("Digite o valor que você deseja buscar: ")
         PessoaDal.buscar(valor)
    
    else:
        print("Resposta ínvalida. Tente novamente!")
        continue


    
    
    