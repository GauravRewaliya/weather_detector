# weather_detector
guided by shapeAi in an bootcamp , helps to utilise APIs



an example "to understand coad easly"
=>
 import requests  ##to bring prebuild fun to request , interect with websits
 
 link = "https://i.insider.com/5e820b04671de06758588fb8?width=700"  
r  = requests.get(link)  ##request to get data 
 ##print ( r.content) //to view contant as binary  
 ##print (r.text ) // to view data as text
 
 with open('comic.png','wb') as f: ##file buffer f  //similar to c
  f.write(r.content) ## write in file  <= link_data.contant
  
  ##try and run the above program
