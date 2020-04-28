from tkinter import *
from functools import partial

# Variavel Global
cor_background = '#91B4FF'


class Application(object):
    def __init__(self, master=None):
        # Fonte Padrão
        self.fonte_padrao = ('verdana', 18, 'bold')

        # Containers titulo e entrada de texto
        self.widget2 = Frame(master)
        self.widget2['pady'] = 20
        self.widget2['bg'] = cor_background
        self.widget2.pack()

        # Containers para checkbuttons
        self.widget1 = Frame(master)
        self.widget1['bg'] = cor_background
        self.widget1.pack()

        # Container do Teclado
        self.widget3 = Frame(master)
        self.widget3['bg'] = cor_background
        self.widget3.pack()

        # Containers do Resultado
        self.widget4 = Frame(master)
        self.widget4['pady'] = 18
        self.widget4['bg'] = cor_background
        self.widget4.pack()

        # checkbutton da para o modo binominal
        self.bino_select = False
        self.modo_binomial = Checkbutton(self.widget1)
        self.modo_binomial['text'] = 'Modo Binomial'
        self.modo_binomial['font'] = ('verdana', 13, 'bold')
        self.modo_binomial['activebackground'] = cor_background
        self.modo_binomial['bg'] = cor_background
        self.modo_binomial['command'] = self.ativa_binomial
        self.modo_binomial.pack(side=LEFT)

        # checkbutton para o modo padrão
        self.padr_select = True
        self.modo_padrao = Checkbutton(self.widget1)
        self.modo_padrao['text'] = 'Modo Padrão'
        self.modo_padrao['font'] = ('verdana', 13, 'bold')
        self.modo_padrao['activebackground'] = cor_background
        self.modo_padrao['bg'] = cor_background
        self.modo_padrao['command'] = self.ativa_padrao
        self.modo_padrao.select()
        self.modo_padrao.pack(side=LEFT)

        # titulo da calculadora
        self.titulo = Label(self.widget2)
        self.titulo['text'] = 'CALCULADORA'
        self.titulo['font'] = self.fonte_padrao
        self.titulo['pady'] = 15
        self.titulo['bg'] = cor_background
        self.titulo.pack()

        # Colocando a entrada do usuário
        self.entrada = Entry(self.widget2)
        self.entrada['font'] = ('verdana', 18)
        self.entrada['width'] = 23
        self.entrada.pack()

        # texto do resultado
        self.resultado = Label(self.widget4)
        self.resultado['fg'] = 'blue'
        self.resultado['font'] = ('verdana', 18)
        self.resultado['relief'] = 'ridge'
        self.resultado['width'] = 23
        self.resultado['height'] = 1
        self.resultado['pady'] = 10
        self.resultado['bg'] = 'white'
        self.resultado.pack()

        # Metodo que cria botões
        self.cria_botoes(self.widget3)

    def mostra_elementos(self):
        pass

    def someElemntos(self):
        pass
        # pack_forget() --> esquece elementos
        # destroy() --> destroi os elementos

    def coloca_texto(self, texto):
        """
        Função que coloca o valor dos botões na entrada
        """
        self.entrada.insert(END, texto)

    def exclui_texto(self):
        """
        Função que deleta o texto da entrada
        """
        self.entrada.delete(0, END)

    def delete_num(self):
        """
        Função que exclui o ultimo digito da entrada
        """
        ultimo_dig = self.entrada.get()
        self.entrada.delete(len(ultimo_dig) - 1)

    def cria_botoes(self, frame):
        """
        Função que cria os botões
        """
        botoes = ('C', '(', ')', '/', '7', '8', '9', '*', '4', '5', '6', '+',
                  '1', '2', '3', '-', '.', '0', '<<', '=')

        for x in range(len(botoes)):
            if x % 4 == 0:
                subframe = Frame(frame)
                subframe.pack()

            # Teclado da calculadora
            self.configura_botao(subframe, botoes[x])

    def configura_botao(self, frame, texto):
        """
        Função que configura os botões do teclado
        """
        self.botoes = Button(frame)
        self.botoes['text'] = texto
        self.botoes['width'] = 6
        self.botoes['font'] = ('verdana', 15)
        self.botoes['height'] = 1
        self.botoes['relief'] = 'groove'
        self.botoes.pack(side=LEFT)

        if texto.isnumeric() or texto in '()/+*-':
            self.botoes['command'] = partial(self.coloca_texto, texto)
            self.botoes['bg'] = '#E6E6E6' if texto.isnumeric() else '#A4A4A4'

        elif texto == '=':
            self.botoes['bg'] = '#2E64FE'
            self.botoes['fg'] = 'white'
            self.botoes['command'] = self.calcular

        elif texto.isalpha():
            self.botoes['bg'] = '#A4A4A4'
            self.botoes['command'] = self.exclui_texto

        else:
            self.botoes['bg'] = '#E6E6E6'
            self.botoes['command'] = self.delete_num

    def mensagem(self, text, cor='red'):
        """
        Mensagem Personalizada
        """
        self.resultado['text'] = text
        self.resultado['fg'] = cor

    def calcular(self):
        """
        Funcão que calcula a conta na calculadora
        """
        conta = self.entrada.get()

        try:
            resultado = eval(conta)
        except:
            self.exclui_texto()
            self.mensagem('Conta Inválida')
        else:
            self.exclui_texto()
            self.resultado['text'] = ''
            self.entrada.insert(0, str(resultado))

    def ativa_binomial(self):
        """
        Funcão ativa modo binomial
        """
        self.bino_select = not self.bino_select

        if self.bino_select:
            self.mensagem('Modo Binominal Ativado', 'green')
            if self.padr_select:
                self.padr_select = False
                self.modo_padrao.deselect()
        else:
            self.mensagem('Modo Binominal Desativado')

    def ativa_padrao(self):
        """
        Função que ativa modo padrão
        """
        self.padr_select = not self.padr_select

        if self.padr_select:
            self.mensagem('Modo Padrão Ativado', 'green')
            if self.bino_select:
                self.bino_select = False
                self.modo_binomial.deselect()
        else:
            self.mensagem('Modo Padrão Desativado')


# cria a janela
root = Tk()

# Dá um título a tela
root.title('Calculadora de Estatística')

# Tamanho da janela
root.geometry('420x480')

# Dá um ícone ao aplicativo
root.wm_iconbitmap('icones/calculator-icon_34473.ico')

# Definir cor de background
root['bg'] = cor_background

# instanciando minha classe
Application(root)

# inicia a janela
root.mainloop()
