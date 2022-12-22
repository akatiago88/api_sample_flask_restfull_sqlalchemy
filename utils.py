from models import Pessoas
from models import Usuarios


def insere_pessoas():
    pessoa = Pessoas(nome='Jose', idade=30)
    print(pessoa)
    pessoa.save()


def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Tiago').first()
    print(pessoa.idade)


def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Jose').first()
    pessoa.idade = 18
    pessoa.save()


def excluir_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Jose').first()
    pessoa.delete()


def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()


def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
    # insere_usuario('admin', 'admin')
    consulta_todos_usuarios()
    # insere_pessoas()
    # consulta_pessoas()
    # altera_pessoa()
    # excluir_pessoa()
