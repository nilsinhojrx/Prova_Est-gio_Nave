from dal import PessoaDal; from model import Pessoa;

class PessoaCtrl:
    @classmethod
    def cadastrar(cls, nome, idade , cpf):

        if len(nome) > 2 and (0 < int(idade) < 100) and len(cpf) == 11 and cpf.isnumeric() == True:
            px = Pessoa(nome,idade,cpf)
            PessoaDal.salvar(px)
            print('Salvo com sucesso!')
        else:
            print('Erro ao cadastrar!')
