projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]
try:
    for projeto in projetos:
        print(f'projeto: {projeto}')
except:
    print('Ocorreu um erro')

print('*************************')
print('Outro código')

for i in range(len(projetos)):
    try:
        print(i)
    except:
        print('Erro')

print('******************************************')
print('Novas perguntas')
# encomendas = []
encomendas = input('Digite o número das encomendas separado por vírgulas: ').split(',')
try:
    for encomenda in encomendas:
        print(int(encomenda))
except ValueError:
    print('Código errado')

print('********************************************')
print('Nova pergunta')
Encomendas_ = [123, '908', 234]
for i in range(len(Encomendas_)):
    try:
        print(int(Encomendas_[i]))
    except ValueError:
        print(f'a encomenda {Encomendas_[i]} não é um número válido')

print('\n NOVO CÓDIGO \n')
try:
    incomendas = []
    for i in range(3):
        incomendas.append(input(f'Digite o número da encomenda {i+1}: '))
        print(f'incomenda {incomendas[-1]} foi adicionada')
except Exception as e:
    print(f'Erro: {e}')