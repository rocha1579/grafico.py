import matplotlib.pyplot as plt
import sys
import random
import pandas as pd


x = [round(random.random(), 2), 2, random.random(), 5, 6, 7, 8, 9]
y = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto']
media = sum(x) / len(y) 
df = pd.DataFrame({'Mês':y, 'Quantidade:':x })

senha = input('Digite a senha:\n')
class Comandos:
    def exibe_dados():
        print(f'Dados Escritos {df}')
    if senha == '123':
        print('OK')
        print(exibe_dados())
    else:
        print('Senha incorreta!')
        sys.exit()
dado = input('deseja adicionar um dado? \n')
class Comandos2(Comandos):
    def adiciona_dado():
        cameras = float(input('Digite a quantidade de cameras vendidas: \n'))
        x.insert(0,cameras)
        mês = input('Digite o mês: \n')
        y.insert(0,mês)
        return print(f'Dados atualizados')
    def processa_dado(dado):
        if dado.lower() == 'sim':
            qtd_cameras = Comandos2.adiciona_dado()
        elif dado.lower() == 'não':
            plt.show()
        else:
            sys.exit()
Comandos2.processa_dado(dado)

media0 = input('Deseja ver a média de vendas?\n')
class Comandos3(Comandos):
    def mostrar_media():
        if media0 == 'sim':
            print(f'A média de vendas foi: {media:.2f}')
        else:
            sys.exit()           
Comandos3.mostrar_media()

plt.bar(y, x, color='blue')
# plt.plot(y,x, color='red')
plt.xlabel('Eixo x')
plt.xlabel('Mês')

plt.title('Estoque de cameras 2025')
plt.savefig('grafico.png',)
plt.show()

