from tkinter import *
from tkinter import ttk
import json
import requests
import time

from requests.models import codes

root = Tk()
root.title("Search Window")

def errorWindow():
    subroot2 = Tk()
    subroot2.title("Error Window")
    error = Label(subroot2,text="The number you entered is incorrect, Input a valid number with correct country code")
    error.grid(row=0,column=0,columnspan=2,rowspan=2)

    subroot2.mainloop()


def getInfo():
    number = input.get()
    key = 'Paste your API key here'
    response = requests.get("http://apilayer.net/api/validate?access_key={}&number={}&country_code=IN".format(key,number))

    json_data = json.loads(response.text)
    try:
        valid = json_data['valid']
        if valid:
            subRoot1 = Tk()
            subRoot1.title("Result Window")
            numberLabel = Label(subRoot1,text=json_data['number'])
            ccLabel = Label(subRoot1,text=json_data['country_code'])
            cnLabel = Label(subRoot1,text=json_data['country_name'])
            loactionLabel = Label(subRoot1,text=json_data['location'])
            carrierLabel = Label(subRoot1,text=json_data['carrier'])
            ltLabel = Label(subRoot1,text=json_data['line_type'])

            numberLabel.grid(row=0,column=0)
            ccLabel.grid(row=0,column=1)
            ltLabel.grid(row=1,column=0)
            cnLabel.grid(row=1,column=1)
            carrierLabel.grid(row=2,column=0)
            loactionLabel.grid(row=2,column=1)


        else:
            errorWindow()

    except:
        errorWindow()

        
codes = ["AF","AL","DZ","AS","AD","AO","AI","AQ","AG","AR","AM","AW","AC","AU","AT","AZ","BS","BH","BD","BB","BY","BE","BZ","BJ","BM","BT","BO","BA","BW","BR","VG","BN","BG","BF","MM","BI","KH","CM","CA","CV","KY","CF","TD","CL","CN","CO","KM","CG","CD","CK","CR","CL","HR","CU","CY","CZ","DK","DJ","DM","DO","EC","EG","SV","GQ","ER","EE","ET","FK","FO","FJ","FI","FR","GF","PF","GA","GM","GE","DE","GH","GI","GR","GL","GD","GP","GU","GT","GN","GW","GY","HT","VA","HN","HK","HU","IS","IN","ID","IR"]    
# codes = ["AF","AL","DZ","AS","AD","AO","AI","AQ"]
total = len(codes)
def searchall():
    number = input2.get()
    for i,j in enumerate(codes):
        time.sleep(2)
        key = 'Paste your API key here'
        response = requests.get("http://apilayer.net/api/validate?access_key={0}&number={1}&country_code={2}".format(key,number,j))
        json_data = json.loads(response.text)
        print(j)
        per = ((i+1)/total) * 100
        progress['value'] = per
        track = Label(root,text="Country Code= "+j +", " + str(per)+ "%")
        track.grid(row=2,column=2)
        root.update()
        try:
            valid = json_data['valid']
            if valid:
                subRoot1 = Tk()
                subRoot1.title(" Window")
                numberLabel = Label(subRoot1,text=json_data['number'])
                ccLabel = Label(subRoot1,text=json_data['country_code'])
                cnLabel = Label(subRoot1,text=json_data['country_name'])
                loactionLabel = Label(subRoot1,text=json_data['location'])
                carrierLabel = Label(subRoot1,text=json_data['carrier'])
                ltLabel = Label(subRoot1,text=json_data['line_type'])

                numberLabel.grid(row=0,column=0)
                ccLabel.grid(row=0,column=1)
                ltLabel.grid(row=1,column=0)
                cnLabel.grid(row=1,column=1)
                carrierLabel.grid(row=2,column=0)
                loactionLabel.grid(row=2,column=1)
                print("Sucess")
                

        except:
            continue

        

    progress['value'] = 100


input = Entry(root,width=30,borderwidth=5,fg="white",bg="Black")
input2 = Entry(root,width=30,borderwidth=5,fg="white",bg="black")
searchButton = Button(root,text="Search",command=getInfo,padx=30,pady=10)
progress = ttk.Progressbar(root,orient=HORIZONTAL,length=290,mode="determinate")
searchallb = Button(root,text="Search entire data",padx=30,pady=10,command=searchall)

input.grid(row=0,column=0,columnspan=2)
searchButton.grid(row=0,column=2)
input2.grid(row=1,column=0,columnspan=2)
searchallb.grid(row=1,column=2)
progress.grid(row=2,column=0,rowspan=2)




root.mainloop()