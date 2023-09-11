from datetime import datetime, timedelta


class Datas:

  def __init__(self):
    self.momento_cadastro = datetime.today()

  def mes_cadastro(self):
    meses_do_ano = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho",
        "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]

    mes_cadastro = self.momento_cadastro.month - 1
    return meses_do_ano[mes_cadastro]

  def dia_semana(self):
    dia_semana_lista = [
        "Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira",
        "Sexta-Feira", "Sábado", "Domingo"
    ]
    dia_semana = self.momento_cadastro.weekday()
    return dia_semana_lista[dia_semana]

  def format_data(self):
    data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
    return data_formatada

  def tempo_cadastro(self):
    tempo_cadastro = (datetime.today() +
                      timedelta(days=30)) - self.momento_cadastro
    return tempo_cadastro


if __name__ == "__main__":
  data = Datas()

  print("Mês de Cadastro:", data.mes_cadastro())
  print("Dia da Semana de Cadastro:", data.dia_semana())
  print("Data Formatada:", data.format_data())
  print("Tempo de Cadastro:", data.tempo_cadastro())
