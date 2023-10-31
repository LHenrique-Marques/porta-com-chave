class menu(): #Classe que trabalha com as escolhas do usuario
    def __init__(self):
        self.menu = None

    
    def mostra(self): #Metodo para mostrar as opções possiveis dentro do menu
        print(""""
        ----------- Menu De Escolhas ------------------
        0 - Fechar programa
        1 - Gerenciar Chaves
        2 - Gerenciar Porta
        """)

    def escolhe(self): #Metodo PRINCIPAL no funcionamento do código, método de interação com o menu
        c = porta() #Instanciando e acrescentando a classe "porta"
        d = chave() #Instanciando e acrescentando a classe "chave"

        while True: #criando uma condição para manter o loop na escolha do usuario para que se ele digitar 0 feche o programa.
            self.mostra() #chamando o metodo que mostra as opções
            escolha = int(input("O que você deseja fazer ?")) #Escolha do usuario de qual o seu caminho Obs: Escolha é pelo indice

            # Menu da chave
            if escolha == 1:
                while True:
                    print(f"""
                    ----Bem vindo ao painel de administração de chaves---
                    ---------------O que deseja fazer ?------------------
                    0 - Voltar ao menu principal
                    1 - Adicionar Chave
                    2 - Remover Chave
                    """)
                    escolha = int(input("Escolha: "))
                    if escolha == 1:
                        print(d)
                        d.adiciona_chave()
                        
                    elif escolha == 2:
                        print(d)
                        d.remove_chave()


                    elif escolha == 0:
                        break
                # Menu da Porta
            elif escolha == 2:
                while True:
                    print("""
                    0 - Volta ao menu principal
                    1 - Coloca chave
                    2 - Tira a chave
                    3 - Tranca a Porta
                    4 - Destranca a Porta
                    5 - Fecha a Porta
                    6 - Abre a Porta
                    
                    """)
                    escolha = int(input("Escolha: "))
                    if escolha == 1:
                        test = d.valida_chave()
                        if test == True:
                            c.coloca_chave()
                        else:
                            print("Esta chave não é valida")
                        print(c)
                    elif escolha == 2:
                        c.retira_chave()
                        print(c)

                    elif escolha == 3:
                        c.tranca_porta()
                        print(c)

                    elif escolha == 4:
                        c.destranca_porta()
                        print(c)

                    elif escolha == 5:
                        c.fecha_porta()
                        print(c)

                    elif escolha == 6:
                        c.abre_porta()
                        print(c)
                    elif escolha == 0:
                        break





            elif escolha == 0:
                break



class porta():
    def __init__(self):
        self.trancada = False
        self.aberta = True
        self.chave = False
        
    def __repr__(self):
        
        if self.trancada == False:
            tranca = "Destrancada"
        else:
            tranca = "Trancada"
        
        if self.aberta == True:
            aberta = "Aberta"
        else:
            aberta = "Fechada"
        
        if self.chave == True:
            chave = "Com chave"
        else:
            chave = "Sem chave"
            
        return f"""
        Status Da Porta 
        {tranca} , {aberta} ,{chave}
        """
            
            
            
            
    def coloca_chave(self):
        if self.chave == False:
            self.chave = True
            
        else:
            print("Ja tem uma chave neste cadeado, tente retirar primeiro para depois colocar uma nova")
        
        
    def retira_chave(self):
        if self.chave == True:
            self.chave = False
        else:
            print("Está porta não contem chave")
            
    def tranca_porta(self):
        if self.chave == True:

            if self.trancada == True:
                print("Já esta trancada...")
            else:
                self.trancada = True
        else:
            print("Está sem chave, nao foi possivel trancar")
    
    def destranca_porta(self):
        if self.chave == True:

            if self.trancada == False:
                print("Já esta destrancada...")
            else:

                self.trancada = False

        else:
            print("Está sem chave, nao foi possivel destrancar")
    
    
    
    def fecha_porta(self):
        
        if self.trancada == False:

            if self.aberta == False:
                print("Ja está fechada...")
            else:
                self.aberta = False
        
        else:
            print("Não foi possivel fechar a porta,pois está trancada.")
            
    def abre_porta(self):
        if self.trancada == False:

            if self.aberta == True:
                print("Já está Aberta...")

            else:
                self.aberta = True
        
        else:
            print("Não foi possivel abrir a porta pois esta trancada.")



class chave():
    def __init__(self):
        self.chaves = ["luizinho","henrique","marques"]
        self.valor = False
    def __repr__(self):
        return f"{self.chaves}"

    def adiciona_chave(self):
        nova = input("Digite uma chave nova:")
        if nova.lower() not in self.chaves:
            self.chaves.append(nova.lower())


    def remove_chave(self):
        remover = input("""
        Qual a chave que você deseja remover ?
        Chave: 
        """)
        if remover.lower() in self.chaves:
            self.chaves.remove(remover.lower())
        
        else:
            print("Esta chave não existe")


    def valida_chave(self):
        valida = input("Digite a sua chave: ")
        if valida in self.chaves:
            return True
        else:
            return False



