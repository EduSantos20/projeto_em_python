import os
from datetime import date
from mysql.connector.cursor import RE_SQL_INSERT_VALUES
from database import insert, select
consumo=0
quantidade=0
valor=0
codigo1={}
codigo2={}
codigo4={}
codigo3={}
codigo5={}
codigo6={}
valor1=0
valor2=0
valor3=0
valor4=0
valor5=0
valor6=0
quantidade1=0
quantidade2=0
quantidade3=0
quantidade4=0
quantidade5=0
quantidade6=0
nome_produto1=0
nome_produto2=0
nome_produto3=0
nome_produto4=0
nome_produto5=0
nome_produto6=0
nome_quarto=0
e_mail=0
valor_quarto=0
data_atual=date.today()
tipo_quarto=0
valor_do_quarto=0
telefone=0
nome=0
cpf=0
opc=0
diaria=0
digite = 0
quarto = {}
produto={}
while True:
    os.system('cls')
    # Estrutura de tela e validação
    print(" "*60,"Bem-vindo(a) ao Hotel Dubai!\n")
    print(" "*60,"< 1 > - Nova Hospedagem.")
    print(" "*60,"< 2 > - Cadastro de Item de Consumo.")
    print(" "*60,"< 3 > - Lançamento de Consumo.")
    print(" "*60,"< 4 > - Calcúlo de Hospedagem.")
    print(" "*60,"< 5 > – Sair")
    band = 1
    while digite <0 or digite >5 or band==1: 
        try:
            digite = int(input(" "*60,))
            band =0
        except ValueError:
            print(" "*60,"Erro! Informe um numero 1 a 5.")
            band =1
        if digite <0 or digite >5:
            print(" "*60,"Erro! Digite uma opção válida de 1 a 5.")
    os.system('CLS')
    # validação de Nova hospedagem
    if digite ==1:
        while True:
            opc1=0
            band=1
            print(" "*60,"Bem-vindo(a) ao Hotel Dubai!\n")
            print(" "*60,"=====Nova hospedagem=====\n")
            print(" "*60,"< 1 > – Cadastro do Responsável pela hospedagem (Nome / e-mail e telefone).")
            print(" "*60,"< 2 > – Detalhes da Hospedagem.")
            print(" "*60,"< 3 > - Retornar ao Menu Principal.\n")
            print(" "*60,"Informe a Opção desejada!")
            while opc1<0 or opc1>3 or band ==1:
                try:
                    opc1 = int(input(" "*60,))
                    band = 0
                except ValueError:
                    print(" "*60,"Erro! Digite uma opção de 1 a 3.")
                    band = 1
                if opc1<0 or opc1>3:
                    print(" "*60,"Erro! Digite uma opção de 1 a 3.")
            os.system('cls')
            if opc1 ==1:
                while True:
                    # validação do nome
                    print(" "*60,"Bem-vindo ao Hotel Dubai!")
                    print(" "*60,"< 1 > - Cadastro do responsável pela hospedagem (nome / e-mail / cpf e telefone)")
                    print(" "*20,"Digite seu nome:")
                    nome = str(input(" "*20,))
                    while nome.isnumeric():
                        os.system('cls')
                        print(" "*60,"Bem-vindo ao Hotel Dubai!")
                        print(" "*60,"< 1 > - Cadastro do responsável pela hospedagem (nome / e-mail / cpf e telefone)")
                        print(" "*20,"Digite seu nome:")
                        nome = str(input(" "*20,))
                        os.system('cls')
                    os.system('cls')
                    # validação do CPF
                    print(" "*60,"Bem-vindo ao Hotel Dubai!")
                    print(" "*60,"Cadastro do responsável pela hospedagem (nome / e-mail / cpf e telefone).")
                    print(" "*20,"Nome:",nome)
                    print(" "*20,"Digite seu CPF:")
                    cpf=0
                    try:
                        cpf = int(input(" "*20,))
                    except ValueError:
                        print(" "*20,"Erro! Informe seu CPF")
                        cpf = int(input(" "*20,))
                    os.system('cls')
                    # validação do e-mail
                    print(" "*60,"Bem-vindo ao Hotel Dubai!")
                    print(" "*60,"< 1 > - Cadastro do responsável pela hospedagem (nome / e-mail / cpf e telefone)")
                    print(" "*20,"Nome:",nome)
                    print(" "*20,"CPF:",cpf)
                    print(" "*20,"Digite seu E-mail:")
                    e_mail = str(input(" "*20,))
                    while e_mail.isnumeric():
                        os.system('cls')
                        print(" "*60,"Bem-vindo ao Hotel Dubai!")
                        print(" "*60,"< 1 > - Cadastro do responsável pela hospedagem (nome / e-mail / cpf e telefone)")
                        print(f" "*20,"Nome:",nome)
                        print(" "*20,"CPF:",cpf)
                        print(" "*20,"Digite seu E-mail:")
                        e_mail = str(input(" "*20,))
                        os.system('cls')
                    os.system('cls')
                    # validação do telefone
                    print(" "*60,"Bem-vindo ao Hotel Dubai!")
                    print(" "*60,"Cadastro do responsável pela hospedagem (nome / e-mail / cpf e telefone).")
                    print(" "*20,"Nome:",nome)
                    print(" "*20,"CPF:",cpf)
                    print(" "*20,"E-mail:",e_mail)
                    print(" "*20,"Digite seu Telefone:")
                    telefone=0
                    try:
                        telefone = int(input(" "*20,))
                    except ValueError:
                        print(' '*20,'Erro! Informe seu Telefone.')
                        telefone = int(input(' '*20,))
                    os.system('cls')

                    sql = 'insert into Cadastro_hospede(NOME,CPF,EMAIL,TELEFONE) values (%s,%s,%s,%s)'
                    val= (nome,cpf,e_mail,telefone)
                    insert(sql,val)

                    print("#"*168,)
                    print(" "*60,"Cadastro realizado com sucesso.")
                    print("#"*168,)
                    nome = nome
                    e_mail = e_mail
                    cpf = cpf
                    telefone = telefone
                    break
            if opc1==2:
                while True:
                    opc1=0
                    band=1
                    print(" "*60,"Bem-vindo(a) ao Hotel Dubai!")
                    print(" "*60,"< 1 > - Definição do tipo de quarto (individual, Duplo Casal ou Duplo Solteiro).")
                    print(" "*60,"< 2 > - Quantidade de diárias.")
                    print(" "*60,"< 3 > - Alimentação (Pensão Simples ou Pensão Completa.")
                    print(" "*60,"< 4 > - Voltar!\n")
                    print(" "*60,"Informe a Opção desejada!")
                    while opc1<0 or opc1>4 or band ==1:
                        try:
                            opc1 = int(input(" "*60,))
                            band = 0
                        except ValueError:
                            print(" "*60,"Erro! Digite uma opção de 1 a 4.")
                            band = 1
                        if opc1<0 or opc1>4:
                            print(" "*60,"Erro! Digite uma opção de 1 a 4.")
                    os.system('cls')
                    # validação para escolher o tipo e quarto, numero, diaria e pensão
                    if opc1 ==1:
                        s ='s'
                        while s=='s':
                            print(" "*60,"Bem-vindo(a) ao Hotel Dubai!")
                            print(" "*60,"Definição do tipo de quarto.\n")
                            print(" "*60," Individual")
                            print(" "*60," Duplo Casal")
                            print(" "*60," Duplo Solteiro")
                            print(" "*60,"Qual tipo de quarto o Senhor(a) deseja?")
                            nome_quarto = str(input(" "*60,))
                            while nome_quarto !='individual' and nome_quarto != "duplo casal" and nome_quarto !="duplo solteiro":
                                print(" "*60,"Erro! Informe o quarto desejado.")
                                nome_quarto = str(input(" "*60,))
                            os.system('cls')
                            print(" "*60,"O senhor(a) definio o tipo de quarto",nome_quarto,".\n")
                            print(" "*60,"O Hotel possui apenas 10 quartos, numerados de 1 (Um) a 10 (Dez).")
                            print(" "*60,"O Senhor(a) deseja ficar em qual quarto?")
                            opc = int(input(" "*60,))
                            while opc <1 or opc>10:
                                print(" "*60,"Erro! Quarto inválido.")
                                opc = int(input(" "*60,))
                            print(" "*60,"O Senhor(a) escolheu o quarto",opc,".\n")
                            print(" "*60,"Deseja escolher outro quarto (S/N)?")
                            s = str(input(" "*60,))
                            while s !='s' and s!='n':
                                print(" "*60,"Erro! Informe a letra (s/n)")
                                s= str(input(" "*60,))
                            os.system('cls')
                    if opc1 ==2:
                        print(" "*60,"Bem-vindo(a) ao Hotel Dubai")
                        print(" "*60,"Quantidade de diárias o senhor deseja.\n")
                        opc1 = int(input(" "*60,))
                        diaria = opc1
                    if opc1 ==3:
                        print(" "*60,"Bem-vindo(a) ao Hotel Dubai!\n")
                        print(" "*60,"Ops! Observção ao escolher a opção já vai mostra o seu valor.\n")
                        print(" "*60," Pensão Simples (ps)")
                        print(" "*40," Individual R$60,00 reais")
                        print(" "*40," Duplo Solteiro R$120,00 reais")
                        print(" "*40," Duplo Casal R$100,00 reais")
                        print(" "*60," Pensão Completa (pc)")
                        print(" "*40," Individual R$90,00 reais")
                        print(" "*40," Duplo Solteiro R$200,00 reais")
                        print(" "*40," Duplo Casal R$180,00 reais")
                        print(" "*60," Qual a opção que o senhor deseja?(ps) ou (pc)")
                        tipo_quarto = str(input(" "*60,))
                        while tipo_quarto != 'ps' and tipo_quarto != 'pc': # se tipo de quarto for diferente que ps ou pc tem que aparecer o erro
                            print('Erro! Informe as letras (pc ou ps)')
                            tipo_quarto = str(input(" "*60,))
                        os.system('cls')
                        if nome_quarto=='individual' and tipo_quarto=='ps': # 
                            valor_do_quarto=60
                        if nome_quarto=='individual'and tipo_quarto=='pc':
                            valor_do_quarto=90
                        if nome_quarto=='duplo solteiro'and tipo_quarto=='ps':
                            valor_do_quarto=120
                        if nome_quarto=='duplo solteiro'and tipo_quarto=='pc':
                            valor_do_quarto=200
                        if nome_quarto =='duplo casal'and tipo_quarto=='ps':
                            valor_do_quarto=100
                        if nome_quarto =='duplo casal'and tipo_quarto=='pc':
                            valor_do_quarto=180
                        valor_quarto= valor_do_quarto*diaria
                        data_atual = date.today()

                        sql = 'insert into Detalhe_hospedagem(NUMERO_QUARTO,TIPO_QUARTO,QUANTIDADE_DIARIA,ALIMENTACAO,VALOR_QUARTO,VALOR_TOTAL,CHECK_IN) values (%s,%s,%s,%s,%s,%s,%s)'
                        val= (opc,nome_quarto,diaria,tipo_quarto,valor_do_quarto,valor_quarto,data_atual)
                        insert(sql,val)

                    if opc1 ==4:
                        break

                    
            if opc1 ==3:
                opc1=0
                break
    # validação do cadastro do item de consumo
    if digite ==2:
        while True:
            opc2=0
            band=1
            print(" "*60,"Bem-vindo(a) ao Hotel Dubai!")
            print(" "*60,"=====Cadastro do item de consumo=====")
            print(" "*60,"< 1 > - Definir o código (númerico com 3 casas decimais) o valor do item e o nome.")
            print(" "*60,"< 2 > - Retornar ao Menu Principal.\n")
            print(" "*60,"Informe a Opção desejada!")
            while opc2<1 or opc2>2 or band ==1:
                try:
                    opc2 = int(input(" "*60,))
                    band = 0
                except ValueError:
                    print(" "*60,"Erro! Digite uma opção de 1 a 2.")
                    band = 1
                if opc2<0 or opc2>2:
                    print(" "*60,"Erro! Digite uma opção de 1 a 2.")
            if opc2 ==1:
                print(" "*60,"Bem-vindo(a) ao Hotel Dubai!\n")
                os.system('cls')
                print(" "*60,"Produtos para consumo.")
                produto = {
                    '[101] Guarana': 5.50,
                    '[102] Cerveja': 6,
                   '[103] Salgadinho': 3,
                    '[104] Batata chips': 12,
                    '[105] Sorvete':4,
                    '[106] Coca-cola':10
               }
                print(" "*60,"Lista de item:")
                print(" "*50,produto)
                s='s'
                while s=='s':
                    print(" "*60,"Informe o código do produto.")
                    codigo = int(input(" "*60,))
                    print(" "*60,"Informe o nome do item.")
                    nome_produto = str(input(" "*60,))
                    print(" "*60,"Informe o valor do produto.")
                    valor = float(input(" "*60,))
                    
                    if codigo ==101:
                        codigo1= codigo
                        nome_produto1=nome_produto
                        valor1= valor
                    if codigo==102:
                        codigo2=codigo
                        nome_produto2=nome_produto
                        valor2=valor
                    if codigo==103:
                        codigo3=codigo
                        nome_produto3=nome_produto
                        valor3=valor
                    if codigo==104:
                        codigo4=codigo
                        nome_produto4=nome_produto
                        valor4=valor

                    if codigo==105:
                        codigo5=codigo
                        nome_produto5=nome_produto
                        valor5=valor
                    
                    if codigo==106:
                        codigo6=codigo
                        nome_produto6=nome_produto
                        valor6=valor
                    print(" "*60,"Deseja escolher mais produto?(S/N)")
                    s= str(input(" "*60,))
                    while s !='s' and s!='n':
                        print(' '*60,'Erro! Infoeme a letra (s/n).')
                        s= str(input(" "*60,))
                    
                    print("#"*168,)
                    print(" "*60,"Produto cadastrado.")
                    print("#"*168,)

            if opc2==2:
                break
    # validação do lançamento de consumo 
    if digite ==3:
        while True:
            opc3=0
            print(" "*60,"Bem-vindo(a) ao Hotel Dubai!")
            print(" "*60,"=====Lançamento de Consumo=====")
            print(" "*60,"< 1 > - Determine o quarto para lançamento do consumo.")
            print(" "*60,"< 2 > - Código do item e a quantidade consumida.")
            print(" "*60,"< 3 > - Retornar ao Menu Principal.\n")
            print(" "*60,"Informe a Opção desejada!")
            band = 1
            while opc3 <0 or opc3 >3 or band==1:
                try:
                    opc3 = int(input(" "*60,))
                    band = 0
                except ValueError:
                    print(" "*60,"Erro! Digite uma opção de 1 a 3.")
                    band = 1
                if opc3 <0 or opc3 >3:
                    print(" "*60,"Erro! Digite uma opção de 1 a 3.")
            os.system('cls')
            if opc3 ==1:
                print(" "*60,"Bem-vindo(a) ao Hotel Dubai!\n")
                print(" "*60,"Qual quarto o senhor esta hospedado?")
                opc3 = int(input(" "*60,))
                while opc3!=opc:
                    print(" "*60,"Erro! Quarto inválido.")
                    opc3 = int(input(" "*60,))
            if opc3 ==2:
                s ='s'
                print(" "*60,"Bem-vindo(a) ao Hotel Dubai!\n")
                while s=='s':
                    print(" "*60,"Informe o código do item.")
                    codigo = int(input(" "*60,))
                    print(" "*60,"Informe a quantidade consumida.")
                    quantidade = int(input(" "*60,))
                    if codigo ==101:
                        codigo1= codigo
                        valor1=quantidade*valor
                        quantidade1=quantidade

                    if codigo==102:
                        codigo2=codigo
                        valor2=quantidade*valor
                        quantidade2=quantidade

                    if codigo==103:
                        codigo3=codigo
                        valor3 = quantidade*valor
                        quantidade3=quantidade

                    if  codigo==104:
                        codigo4=codigo
                        valor4= quantidade*valor
                        quantidade4 = quantidade

                    if  codigo==105:
                        codigo5=codigo
                        valor5= quantidade*valor
                        quantidade5 = quantidade
                    
                    if  codigo==106:
                        codigo6=codigo
                        valor6= quantidade*valor
                        quantidade6 = quantidade
                    print(" "*60,"Deseja escolher mais produto?(s/n)")
                    s= str(input(" "*60,))
                    while s !='s' and s!='n':
                        print(' '*60,'Erro! Informe a letra (s/n).')
                        s= str(input(" "*60,))
                    
                    sql= 'insert into Cadastro_consumo (NUMERO_QUARTO_CONSUMO,CODIGO_PRODUTO_CONSUMO,QUANTIDADE_CONSUMO) VALUES (%s,%s,%s)'
                    val= (opc,codigo,quantidade)
                    insert(sql,val)

                    os.system('cls')
            if opc3==3:
                break
    #validação do calculo da hospedagem   
    if digite ==4:
        while True:
            opc4=0
            print(" "*60,"Bem-vindo(a) ao Hotel Dubai!")
            print(" "*60,"=====Cálculo da Hospedagem=====.")
            print(" "*60,"< 1 > - Determine o quarto para o cálculo (0 a 10).")
            print(" "*60,"< 2 > - Retornar ao Menu Principal.\n")
            print(" "*60,"Informe a Opção desejada!")
            band =1
            while opc4<0 or opc4 >2 or band==1:
                try:
                    opc4 = int(input(" "*60,))
                    band = 0
                except ValueError:
                    print(" "*60,"Erro! Digite uma opção de 1 a 2.")
                    band = 1
                if opc4<0 or opc4>2:
                    print(" "*60,"Erro! Digite uma opção de 1 a 2 .")
            if opc4 ==1:
                os.system('cls')
                print(" "*60,"Qual quarto o senhor(a) ficou hospedado?")
                opc = input(" "*60,)
                consumo = valor1+valor2+valor3+valor4+valor5+valor6
                conta = (diaria * valor_do_quarto) + consumo
                os.system('cls')
                print(" "*20,'|---------------------------------------------------------------------------------------')
                print(" "*20,"| Confere os seus dados:")
                print(" "*20,"| Nome:",nome)
                print(" "*20,"| CPF:",cpf)
                print(" "*20,"| E-mail:",e_mail)
                print(" "*20,"| Telefone:",telefone)
                print(" "*20,'|---------------------------------------------------------------------------------------')
                hospedagem = select('SELECT * FROM Detalhe_hospedagem WHERE NUMERO_QUARTO ='+opc)
                if (len(hospedagem)>0):
                    print(" "*20,'| Data do CHECK-IN:',hospedagem[0][6])
                    print(' '*20,'| Número do quarto:',opc)
                    print(" "*20,'| Tipo do Quarto:',hospedagem[0][1])
                    print(" "*20,'| Quantidade de Diaria:',hospedagem[0][2])
                    print(" "*20,'| Alimentação:',hospedagem[0][3])
                    print(" "*20,'| Valor do quarto:',hospedagem[0][4])
                    print(" "*20,'| Valor Total do quarto e Alimentação:',hospedagem[0][5])
                    print(" "*20,'|---------------------------------------------------------------------------------------')
                print(" "*20,"| Esses são os produtos que o senhor(a) consumio.\n")
                print(" "*20,'|---------------------------------------------------------------------------------------')
                print(" "*20,"| Código:",codigo1,'Produto:',nome_produto1,'Quantidade:',quantidade1,"Valor:",valor1)
                print(" "*20,"| Código:",codigo2,"Produto:",nome_produto2,"Quantidade:",quantidade2,"Valor:",valor2)
                print(" "*20,"| Código:",codigo3,"Produto:",nome_produto3,"Quantidade:",quantidade3,"Valor:",valor3)
                print(" "*20,"| Código:",codigo4,"Produto:",nome_produto4,"Quantidade:",quantidade4,"Valor:",valor4)
                print(" "*20,"| Código:",codigo5,"Produto:",nome_produto5,"Quantidade:",quantidade5,"Valor:",valor5)
                print(" "*20,"| Código:",codigo6,"Produto:",nome_produto6,"Quantidade:",quantidade6,"Valor:",valor6)
                print(" "*20,'|---------------------------------------------------------------------------------------')
                print('')
                print(' '*50,'| Valor Total a pagar:',conta)
                print('')

            if opc4==2:
                break
        os.system('cls')
    # sair do programa
    if digite ==5:
        break
print(" "*60,"Volte Sempre!\n")
print("#"*168,)
print(" "*40,"Software desenvolvido por Abner Santos | Eduardo Santos | Magali Ribeiro")
print("#"*168,)
input()