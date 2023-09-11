# bytebank.py

Código feito em Python Orientado a Objetos para atender as solicitações de construção da biblioteca de classes para o banco fictício ByteBank.

## Documento - CPF e CNPJ
- A classe **_FACTORY_** é responsável por decidir se instanciará a classe **__DOC_CPF__** ou **__DOC_CNPJ__**, de acordo com o documento passado para a classe - é utilizada uma biblioteca externa para validar tanto o CPF quanto o CNPJ.

## Telefone
- É feita a validação e formatação de um número de telefone com a utilização de expressões regulares.

## Cadastro
- São utilizadas as bibliotecas **_datetime_** e **_timedelta_** para que as informações de cadastro do usuário sejam salvas e exibidas, além de também mostrar o tempo de cadastro do mesmo.
- A formatação **_strftime__** e alguns métodos são utilizados para mostrar os dias da semana e os meses do ano dentro dos padrões nacionais.
  
## CEP
- A Classe **_BuscaEndereco_** é responsável por formatar e validar o CEP, além de acessar  uma API ou WebService _online_ em tempo real que enviará o CEP e receberá uma informação serializada do endereço do usuário, contendo informações de ruas, bairros, estados e outros.
