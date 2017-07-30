# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
#from pyquery import PyQuery as pq
#from lxml import etree
import re
import json

def fileRead(filePath):
	f = open(filePath,"r")
	soup = BeautifulSoup(f, 'html.parser') 
	f.close()
	return soup

def unicodeToStr(unicode):
	return unicode.encode('utf-8')

def tableValue2(i,value):
	if(i!=0):
		j = 0
		menuFlg = False 
		for td in value.tr:
			tagFlg = False
			#if(td.string!=None and td.string.isspace()==False):
			#print td.string
			#print type(td)
			#print td
			#print str(td).replace('<br/>','')
			# 식당명
			gubun = "" 

			if(str(td).count('menu_st') == 1):
				gubun = "건물"
				tagFlg = True
			# 메뉴

			if(str(td).count('mft style2') == 1):
				if(j==1):
					gubun = "구분"
				else: 
					gubun = "식당"

				tagFlg = True
			if(str(td).count('center') == 1):
				gubun = "메뉴"
				tagFlg = True
			#print td
			#print td
			if(tagFlg):
				print type(td)
				#print gubun + ":" + unicodeToStr(td.get_text())
				print td.get_text()
				#print unicodeToStr(td.get_text())
				#print str(i) +","+str(j) +" : " + str(td)
				print ""
			#print td.get_text()
			
			#print td["class"] 
			#if(td['class'] == "menu_st")
			#	print(td)
			j = j + 1
 
soup = fileRead("text")
# �?�씠�? �뙆�뵿
title = soup.findAll("title")[0].text
print(soup.title.string)

print type(soup.title)


sdetail = soup.find(id="sdetail")
#print(sdetail)
tables = sdetail.find_all('table')
i = 0 

for table in tables:

	tableValue2(i, table)

		
	i = i + 1 





#tables = sdetail.findAll('table')

#print tables
#print sdetail.table.findAll("table")[1].find("tr").find("td")
#print type(sdetail.table.findAll("table")[1].find("td"))
#print(sdetail.table.findAll("table")[2])

#x = 0
#for table in tables:
#   print str(x) + " : " + unicodeToStr(table)

   #print table
#   x =  x + 1
#todate = sdetail.find("span",{"class":"menu_date"}).find("font").findAll("strong")[0].text
#print(sdetail)



#todate = sdetail.find("span",{"class":"menu_date"}).find("font")
#print(todate)
#print(todate.find_all('strong'))
#table = sdetail.find('table').find('p').find_all('table')
#x = 0
#for s in table:
#   print str(x) + " : "
#   print s
#   x =  x + 1
#print(table)

#for혻strong_tag혻in혻todate.find_all('strong'):
#혻혻혻혻print혻strong_tag.text,혻strong_tag.next_sibling 



#print(re.compile('<body.*/body>', todate, re.I|re.S))
#print(todate) 
#print(html2text(todate))

#print(sdetail)



