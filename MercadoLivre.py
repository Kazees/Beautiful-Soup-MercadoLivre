import requests
from bs4 import BeautifulSoup
import pandas as pd

#Transformar os produtos em uma planilha
lista_produtos=[]

URL='https://lista.mercadolivre.com.br/'
nome_produto=input('Produto desejado:')

#print(URL+nome_produto)

pesquisa=requests.get(URL+nome_produto)
#print(pesquisa.text)

site=BeautifulSoup(pesquisa.text,'html.parser')
#print(site.prettify())

produtos=site.findAll('div',attrs={'class':'andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16 andes-card--animated'})
#print(produto.prettify())

for produto in produtos:
    link_produto=produto.find('a',attrs={'class':'ui-search-link'})
    titulo=produto.find('h2',attrs={'class': 'ui-search-item__title'})

    simbolo=produto.find('span',attrs={'class':'andes-money-amount__currency-symbol'})
    real=produto.find('span',attrs={'class':'andes-money-amount__fraction'})
    centavos=produto.find('span',attrs={'class':'andes-money-amount__cents andes-money-amount__cents--superscript-16'})

    #print('Titulo do produto:',titulo.text)
    #print('Link do produto:',link_produto['href'])

    if(centavos):
        #print('Preço do produto:',simbolo.text+real.text+','+centavos.text)
        lista_produtos.append([titulo.text,link_produto['href'],simbolo.text+real.text+','+centavos.text])

    else:
        #print('Preço do produto:', simbolo.text + real.text)
        lista_produtos.append([titulo.text, link_produto['href'], simbolo.text + real.text])

    print('\n')

planilha=pd.DataFrame(lista_produtos,columns=['Título do produto','Link','Preço'])
planilha.to_excel('produtos.xlsx',index=False)