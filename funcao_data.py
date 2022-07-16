from datetime import date

def mes():
    mes_numero = date.today().month
    meses = ['janeiro', 'fevereiro', 'maarço', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    return meses[mes_numero - 1]



