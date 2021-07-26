from tornado.web import RequestHandler
from models.models import Produto


class Index(RequestHandler):
    def get(self):
        produtos = Produto.get_produtos()
        self.render('index.html', produtos=produtos)


class Novo(RequestHandler):
    def get(self):
        self.render('novo.html')

    def post(self):
        descricao = self.get_argument('descricao', None)
        preco = self.get_argument('preco', None)

        produto = Produto(descricao=descricao, preco=preco)
        produto.salvar()

        self.redirect('/')


class Deletar(RequestHandler):
    def get(self, id):
        produto = Produto.get_produto(id)
        produto.deletar()

        return self.redirect('/')


class Alterar(RequestHandler):
    def get(self, id):
        produto = Produto.get_produto(id)
        produto.alterar()

        return self.redirect('/')
