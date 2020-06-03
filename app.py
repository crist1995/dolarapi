def value():

 from lxml import html
 import requests
 from datetime import date


 page = requests.get('http://www.sii.cl/valores_y_fechas/dolar/dolar2020.htm')
 tree = html.fromstring(page.content)
 today= int(str(date.today()).split('-')[2])

 clues={}
 date=[]
 price=[]
 clues['date']=date
 clues['price']=price

 for k in range(1,4):
  for i in range(1,12):
   string='//*[@id="mes_junio"]/div/table/tbody/tr['+str(i)+']/th['+str(k)+']/strong/text()'
   dia=tree.xpath(string)
   if(len(dia)>0):
    string='//*[@id="mes_junio"]/div/table/tbody/tr['+str(i)+']/td['+str(k)+']/text()'
    valor=tree.xpath(string)
    clues['date'].append(dia)
    clues['price'].append(valor)
 value=0
 for i in range(len(clues['date'])):
  if(int(clues['date'][i][0])== today):
   value=clues['price'][i]
 return value
