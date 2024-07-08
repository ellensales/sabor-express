from modelos.restaurante import Restaurante

restaurante_sushi = Restaurante("Sushi House", "Japonesa")
returante_pizza = Restaurante("Pizza House", "Italiana")

restaurante_sushi.receber_avaliacao("João", 4)
restaurante_sushi.receber_avaliacao("Maria", 5)
restaurante_sushi.receber_avaliacao("José", 3)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()