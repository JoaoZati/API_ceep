import requests


def input_ceep():
    while 1:
        try:
            ceep = input('Digite seu cep: ')
            if len(ceep) == 8:
                return ceep
            print("[+] O CEP deve conter apenas 8 digitos.\n")
            novamente = input("Deseja tentar novamente?\n"
                              "Digite qualquer tecla para continuar e N para sair: ").upper()
        except:
            print('Opção invalida')

        if novamente == 'N':
            print("Até mais...")
            exit()


def get_ceep():
    while 1:
        ceep = input_ceep()
        r = requests.get(f'https://viacep.com.br/ws/{ceep}/json/')
        data = r.json()

        if 'erro' not in data:
            print("\n[+] Dados do CEP encontado.\n")
            print("| Estado: {}".format(data['uf']))
            print("| CEP: {}".format(data['cep']))
            print("| Cidade: {}".format(data['localidade']))
            print("| Logradouro: {}".format(data['logradouro']))
            print("| Complemento: {}".format(data['complemento']))
            print("| Bairro: {}".format(data['bairro']))
            break

        print("O CEP {} não consta no banco de dados!".format(ceep))
        novamente_main = input("Deseja tentar novamente?\n"
                               "Digite qualquer tecla para continuar e N para sair: ").upper()

        if novamente_main == 'N':
            print("Até mais...")
            exit()


if __name__ == '__main__':
    get_ceep()
