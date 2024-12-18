import time
from selenium import webdriver
from selenium.webdriver.common.by import By
def Youtube():
    nav = webdriver.Chrome()
    nav.get('https:/youtube.com/')
    nav.find_element(By.NAME, 'search_query').send_keys('Rafa e Luis')
    nav.find_element(By.CLASS_NAME, 'ytSearchboxComponentSearchButton').click()
    nav.quit()
    
def Tempo():
    
    agua = webdriver.Chrome()
    agua.get('https://g1.globo.com/previsao-do-tempo/pr/maringa.ghtml')
    cidade = agua.find_element(By.CLASS_NAME, 'forecast-header__place').text
    dados = agua.find_element(By.CLASS_NAME, 'forecast-header__summary').text
    print("cidade: ", cidade)
    print("dados: ", dados)

def SistemaIFS(username, password):
    # Pegar nome completo, semestre e campus.
    try:
        ifs = webdriver.Chrome()
        ifs.get('https://sigaa.ifs.edu.br/sigaa/verTelaLogin.do')
        ifs.find_element(By.NAME, 'user.login').send_keys(username)
        ifs.find_element(By.NAME, 'user.senha').send_keys(password)
        nome = ifs.find_element(By.CLASS_NAME, 'txt36').text
        print(nome)
        ifs.find_element(By.CLASS_NAME, 'login100-form-btn').click()
        ifs.find_element(By.NAME, 'j_id_jsp_1309985458_1:j_id_jsp_1309985458_4').click()
        ifs.find_element(By.PARTIAL_LINK_TEXT, "Portal do Discente").click()
        periodo = ifs.find_element(By.CLASS_NAME, 'periodo-atual').text
        usuario = ifs.find_element(By.CLASS_NAME, 'usuario').text
        unidade = ifs.find_element(By.CLASS_NAME, 'unidade').text
        matricula = ifs.find_element(By.XPATH, '//*[@id="agenda-docente"]/table/tbody/tr[1]/td[2]').text
        sil = f'O aluno {usuario} está matriculado no {unidade} com a matricula {matricula}, está no periodo {periodo}'
        dados = ifs.find_elements(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[2]').text
        
        #sil = f'O aluno {usuario} está matriculado no {unidade} com a matricula {matricula}, está no periodo {periodo}, o curso é {curso}, e entrou no semestre {entrada}, STATUS: {status}'
        print(sil)
        ifs.find_element(By.CLASS_NAME, 'sair-sistema').click()
    except:
        print("erro")
    finally:
        ifs.quit()
    return sil
    
# nav.get('https://morea-ifs.org/')
# nav.find_element(By.TAG_NAME, 'h1').text

