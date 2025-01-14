from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError

Base = declarative_base()

class Fornecedor(Base):
    __tablename__ = 'fornecedores'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    telefone = Column(String(50))
    email = Column(String(50))
    endereco = Column(String(100))


class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    descricao = Column(String(200), nullable=False)
    preco = Column(Integer)
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))

    fornecedor = relationship("Fornecedor")


if __name__ == "__main__":
    engine = create_engine('sqlite:///desafio.db', echo=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    #Inserindo Fornecedores
    try:
        with Session() as session:
            fornecedores:list = [
                Fornecedor(nome="Tech Supplies Ltda", telefone="(11) 98765-4321", email="contato@techsupplies.com", endereco="Rua das Inovações, 123, São Paulo - SP"),  
                Fornecedor(nome="Global Distribuidora", telefone="(21) 99876-5432", email="vendas@globaldist.com.br", endereco="Av. Central, 456, Rio de Janeiro - RJ"),  
                Fornecedor(nome="Papelaria Moderna", telefone="(31) 91234-5678", email="suporte@papelariamoderna.com", endereco="Rua das Flores, 789, Belo Horizonte - MG"),  
                Fornecedor(nome="Mundo Eletrônicos", telefone="(51) 99987-6543", email="contato@mundoeletronicos.com", endereco="Av. Industrial, 101, Porto Alegre - RS"),  
                Fornecedor(nome="Alimentos Naturais", telefone="(81) 93456-7890", email="info@alimentosnaturais.com", endereco="Rua do Mercado, 202, Recife - PE")  
            ]
            session.add_all(fornecedores)
            session.commit()
    except SQLAlchemyError as e:
        print(f"Erro ao inserir fornecedores: {e}")

    try:
        with Session() as session:
            produtos:list = [
                Produto(nome="Notebook Gamer", descricao="Notebook com processador Intel i7, 16GB RAM e SSD de 512GB", preco=6500.00, fornecedor_id=1),
                Produto(nome="Caderno Universitário", descricao="Caderno 200 folhas com capa dura e design moderno", preco=25.90, fornecedor_id=3),
                Produto(nome="Fone de Ouvido Bluetooth", descricao="Fone com tecnologia noise-canceling e bateria de longa duração", preco=350.00, fornecedor_id=4),
                Produto(nome="Pacote de Farinha de Trigo", descricao="Farinha de trigo integral 1kg, ideal para pães e bolos", preco=8.50, fornecedor_id=5),
                Produto(nome="Mouse Sem Fio", descricao="Mouse ergonômico com sensor óptico de alta precisão", preco=75.00, fornecedor_id=1),
            ]
            session.add_all(produtos)
            session.commit()
    except SQLAlchemyError as e:
        print(f"Erro ao inserir produtos: {e}")