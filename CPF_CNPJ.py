#Biblioteca que valida CPF/CNPJ
from validate_docbr import CPF, CNPJ

class Documento:
  @staticmethod
  def cria_documento(documento):
    if len(documento) == 11:
      return DOC_CPF(documento)
    elif  len(documento) == 14:
      return DOC_CNPJ(documento)
    else:  
      raise ValueError("Documento Inválido!")

class DOC_CPF:
  def __init__(self, documento):
   if self.valida(documento):
     self.cpf = documento
   else:
     raise ValueError ("CPF Inválido!")
     
  def __str__(self):
    return self.format()

  #Valida o CPF
  def valida(self, documento):
    validador = CPF()
    return validador.validate(documento)
    
  #Formata o CPF
  def format(self):
    mascara = CPF()
    return mascara.mask(self.cpf)

class DOC_CNPJ:
  def __init__(self, documento):
   if self.valida(documento):
     self.cnpj = documento
   else:
     raise ValueError ("CNPJ Inválido!")

  def __str__(self):
    return self.format()

  #Valida o CNPJ
  def valida(self, documento):
    validador = CNPJ()
    return validador.validate(documento)
    
  #Formata o CNPJ
  def format(self):
    mascara = CNPJ()
    return mascara.mask(self.cnpj)

  




