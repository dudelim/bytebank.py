from CPF_CNPJ import Documento
from Telefones import Telefones
from Datas import Datas
from CEP import BuscaEndereco
import re

#Exemplos: CPF E CNPJ
documento1 = Documento.cria_documento("29894042015")  #Cria um CPF válido
print(f"CPF: {documento1}")

documento2 = Documento.cria_documento("13956549000104")  #Cria um CNPJ válido
print(f"CNPJ: {documento2}")

#Exemplo: Telefone
numero = Telefones("1234567891234")  #Cria um número de telefone válido
print(numero.format_numero())

#Exemplos: Datas
data = Datas()
print("Mês de Cadastro:", data.mes_cadastro())
print("Dia da Semana de Cadastro:", data.dia_semana())
print("Data:", data.format_data())
print("Tempo de Cadastro:", data.tempo_cadastro())

#Exemplo: CEP
cep_digitado = input("Digite um CEP válido (apenas números): ")
endereco = BuscaEndereco(cep_digitado)
bairro, cidade, uf = endereco.acessa_CEP()

if bairro and cidade and uf:
  print("Bairro:", bairro)
  print("Cidade:", cidade)
  print("Estado:", uf)
else:
  print("CEP não encontrado.")
