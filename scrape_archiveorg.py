import requests
import wget

# Making a GET request
r = requests.get('https://archive.org/download/PSVITA_VPK')

# check status code for response received
# success code - 200
print(r)

# print content of request
strContent=str(r.content)
strLines=strContent.split("<td>")
iCnt=0
for line in strLines:    
    if "href" in line:
        lineorg = line        
        line=line.split("=")[1].split(">")[0]
        strFolder = lineorg.split(">")[1].split("</")[0]
        if "rar" in line:
            print(f"Line {iCnt} :  {line.strip()}    {strFolder}")
            filename="https://archive.org/download/PSVITA_VPK/" + line.strip().replace('"','')
            print(f"Downloading {filename}")
            wget.download(filename)

    iCnt+=1



