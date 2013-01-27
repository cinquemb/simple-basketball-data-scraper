from bs4 import BeautifulSoup
import requests
import re
from time import sleep

#for abbriviation information about headers
#http://www.databasebasketball.com/about/aboutstats.htm

#team names
nodes = ['BOS','NJ','NY','PHI','TOR','CHI','CLE','DET','IND','MIL','ATL','CHA','MIA','ORL','WSH','DEN','MIN','OKC','POR','UTAH','GS','LAC','LAL','PHX','SAC','DAL','HOU','MEM','NO','SA']


for node in nodes:
    #per game stats
    val_per = 'http://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=/teams/%s/2013.html&div=div_per_game&del_col=1,3,4,5,6,16,17,22,23' % (node)
    sleep(15)
    r_per = requests.get(val_per)
    data_per = r_per.text
    #where to start data parse
    start_per = data_per.index('<table')
    #where to end data parse
    end_per = data_per.index('</table>')
    s_per = str(data_per[start_per:end_per]+'</table>')
    soup_per = BeautifulSoup(s_per)
    rows_per = soup_per.find_all('tr')
    headers_per = soup_per.find_all('th')
    new_headers_per = []
    alldata_per = []
    
    #total stats for player
    val_total = 'http://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=/teams/%s/2013.html&div=div_totals&del_col=1,3,4,5,6,16,17,22,23' % (node)
    sleep(15)
    rows_total = requests.get(val_total)
    data_total = rows_total.text
    
    #where to start data parse
    start_total = data_total.index('<table')
    #where to end data parse
    end_total = data_total.index('</table>')
    s_total = str(data_total[start_total:end_total]+'</table>')
    soup_total = BeautifulSoup(s_total)
    rows_total = soup_total.find_all('tr')
    headers_total = soup_total.find_all('th')
    new_headers_total = []
    alldata_total = []
    
    #get each header value for total
    for header_total in headers_total:
        new_headers_total.append(header_total.string)
    
    for row_total in rows_total:
        col_total = row_total.find_all('td')
        #get data from each row corresponding to header total
        node_total = []
        for values_total in col_total:
            node_total.append(values_total.string)
    
        alldata_total.append(zip(new_headers_total,node_total))

    #get each header value per
    for header_per in headers_per:
        new_headers_per.append(header_per.string)

    for row_per in rows_per:
        col_per = row_per.find_all('td')
        #get data from each row corresponding to header per
        node_per = []
        for value_per in col_per:
            node_per.append(value_per.string)
    
        alldata_per.append(zip(new_headers_per,node_per))

    print alldata_per , alldata_total