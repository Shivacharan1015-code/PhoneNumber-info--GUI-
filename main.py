from tkinter import *
import json
import requests
import time

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
    key = 'Paste your API Key here'
    response = requests.get("http://apilayer.net/api/validate?access_key={}&number={}".format(key,number))

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

        
    

def searchall():
    num1 = input2.get()
    for i in range(1,100):
        number = str(i) + num1
        key = 'Paste your API Key here'
        response = requests.get("http://apilayer.net/api/validate?access_key={}&number={}".format(key,number))
        json_data = json.loads(response.text)
        print(i)
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
                time.sleep(5) 

        except:
            continue

        




input = Entry(root,width=30,borderwidth=5,fg="white",bg="Black")
input2 = Entry(root,width=30,borderwidth=5,fg="white",bg="black")
searchButton = Button(root,text="Search",command=getInfo,padx=30,pady=10)
searchall = Button(root,text="Search entire data",padx=30,pady=10,command=searchall)
input.grid(row=0,column=0,columnspan=2)
searchButton.grid(row=0,column=2)
input2.grid(row=1,column=0,columnspan=2)
searchall.grid(row=1,column=2)




root.mainloop()