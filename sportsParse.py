from bs4 import BeautifulSoup
import requests
import re
from time import sleep

#for abbriviation information about headers
#http://www.databasebasketball.com/about/aboutstats.htm

#team names
nodes = ['BOS','NJ','NY','PHI','TOR','CHI','CLE','DET','IND','MIL','ATL','CHA','MIA','ORL','WSH','DEN','MIN','OKC','POR','UTAH','GS','LAC','LAL','PHX','SAC','DAL','HOU','MEM','NO','SA']

for node in nodes:
    val1 = 'http://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=/teams/%s/2013.html&div=div_totals' % (node)
    sleep(15)
    r1 = requests.get(val1)
    data1 = r1.text
    #where to start data parse
    start = data1.index('<table')
    #where to end data parse
    end = data1.index('</table>')
    s = str(data1[start:end]+'</table>')
    soup = BeautifulSoup(s)
    rows = soup.find_all('tr')
    headers = soup.find_all('th')
    new_headers = []
    alldata = []
    
    #get each header value
    for header in headers:
        new_headers.append(header.string)
    
    for row in rows:
        col = row.find_all('td')
        #get data from each row corresponding to header
        node = []
        for values in col:
            node.append(values.string)
    
        alldata.append(zip(new_headers,node))

    print alldata