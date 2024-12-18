import requests

def time_time():
    list, n = [], 0
    while n != 1:
        n = int(input("CEP: "))
        list.append(n)
    list.pop(len(list) - 1)
    for i in list:
        print('')
        printe = requests.get(f'https://viacep.com.br/ws/{i}/json/').json()
        for n in printe: 
            if printe[n] != '': print(n,":", printe[n])

def feriado():
    ano = input()
    k = requests.get(f'https://brasilapi.com.br/api/feriados/v1/{ano}').json()
    for i,n in k:
        print(k[i][n])

def bank(): pass

def cnpj():
    cnpj_get = input()
    cnpj_get = cnpj_get.replace(".",'').replace("/",'').replace("-",'').replace(" ",'')
    cnpj = requests.get(f'https://brasilapi.com.br/api/cnpj/v1/{cnpj_get}').json()
    for i in range(5): print("")
    for i in cnpj:
        if i != '' and cnpj[i] != None and cnpj[i]  != '': print(i,":",cnpj[i])

def cnpj_cnpj(cnpj):
    cnpj = cnpj.replace(".",'').replace("/",'').replace("-",'').replace(" ",'')
    return requests.get(f'https://brasilapi.com.br/api/cnpj/v1/{cnpj}').json()

def cep_cep(cep):
    cep = cep.replace(".",'').replace("-",'').replace(" ",'')
    return requests.get(f'https://viacep.com.br/ws/{cep}/json/').json()

def time_time(time):
    return requests.get(f'http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=São Paulo&state=SP&token=b1c48f2cfb09f6849cecb2e48fafce03').json()

def feriado_feriado(ano):
    return requests.get(f'https://brasilapi.com.br/api/feriados/v1/{ano}').json()