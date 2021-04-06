from tabulate import tabulate
from datetime import date, timedelta
import requests
import pandas as pd
import os

os.system('mode con: cols=180 lines=30')

result = requests.get("https://s3-ap-southeast-1.amazonaws.com/open-ws/weektimetable").content.decode("utf-8")
data = result.replace("'","").replace('[',"").replace("]","")
arr = pd.DataFrame(eval(data))
t2 = (arr.loc[(arr["INTAKE"] == "UC2F2008CS(IS)") & (arr["GROUPING"] == "G2")])
startdate = date.today() - timedelta(days=date.today().weekday())
enddate = startdate + timedelta(days=6)
t2 = t2.loc[(t2['DATESTAMP_ISO'] >= str(startdate)) & (t2['DATESTAMP_ISO'] <= str(enddate))]

# print(t2.head())
t2 = t2.drop(['COLOR','SAMACCOUNTNAME','DATESTAMP_ISO','LOCATION','INTAKE','LECTID','GROUPING', 'TIME_TO_ISO', 'CLASS_CODE', 'TIME_FROM_ISO'], axis=1)
# print(t2.loc[(t2['DATESTAMP_ISO'] >= str(startdate)) & (t2['DATESTAMP_ISO'] <= str(enddate))])
# display(HTML(t2.loc[(t2['DATESTAMP_ISO'] >= str(startdate)) & (t2['DATESTAMP_ISO'] <= str(enddate))].to_html()))
print(tabulate(t2, headers='keys', tablefmt='psql'))
input("prompt: ")
