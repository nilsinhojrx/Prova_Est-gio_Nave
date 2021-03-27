#DAL: Data Access Layer ( Camada Para Acesso dos Dados)
from model import Pessoa

class PessoaDal:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('pessoas.txt','a') as arq:
            arq.writelines(pessoa.nome + " " + str(pessoa.cpf) + " " + str(pessoa.idade) + " " + "Anos" + '\n')

    @classmethod 
    def ler(cls): 
        with open('pessoas.txt','r') as arq:
            for a in arq:
                print(a)
                
    @classmethod 
    def buscar(cls, busca):
        with open('pessoas.txt', 'r') as arq:
            contagem = 0
                        
            for i in arq.readlines():
                
                if busca in i.split():
                        contagem += 1
                        resposta = i
                        print(resposta)
                else:
                    continue

            if (contagem == 0):
                print("Valor não encontrado. Tente novamente.")
                        
            
           
                        
                
                
            
        

