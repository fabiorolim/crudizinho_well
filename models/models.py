from db import execute_


class Produto:

    def __init__(self, id=None, descricao=None, preco=None, ativo=1):
        self.id = id
        self.descricao = descricao
        self.preco = preco
        self.ativo = ativo

    # query = "CREATE TABLE IF NOT EXISTS produto (id INTEGER PRIMARY KEY AUTOINCREMENT, descricao TEXT, preco REAL, ativo INTEGER)"
    # _execute(query)

    def salvar(self):
        query = f"INSERT INTO produto (descricao, preco, ativo) VALUES ('{self.descricao}', '{self.preco}', '{self.ativo}')"
        execute_(query)

    def alterar(self):
        query = f'UPDATE produto SET ativo={int(not (self.ativo))} WHERE id={self.id}'
        execute_(query)

    def deletar(self):
        query = f"DELETE FROM produto WHERE id='{self.id}'"
        execute_(query)

    @staticmethod
    def get_produtos():
        query = 'SELECT * from produto'
        produtos = execute_(query)

        list_produtos = list(map(lambda produto: Produto(*produto), produtos))

        return list_produtos

    @staticmethod
    def get_produto(id):
        query = f'SELECT * FROM produto WHERE id={id}'
        produto = execute_(query)
        produto_ = Produto(*produto[0])

        return produto_
