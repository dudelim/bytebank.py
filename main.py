from CPF_CNPJ import Documento
from validate_docbr import CNPJ

#cpf = Cpf("15316264754")
#print(cpf_um)

exemplo_cnpj = "35379838000112"
exemplo_cpf = "32007832062"

#cnpj = CNPJ()
#print(cnpj.validate9exemplo_cnpj))

documento = Documento.cria_documento(exemplo_cnpj)
print(documento)
