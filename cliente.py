#!/usr/bin/python
#-*- coding: utf-8 -*-

class Cliente:
    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf

    def alterar_cadastro(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf        

    def excluir_cadastro(self)
