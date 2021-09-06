from tkinter import *
import json
import requests

root = Tk()
root.title("Search Window")

def errorWindow():
    subroot2 = Tk()
    subroot2.title("Error Window")
    error = Label(subroot2,text="The number you entered is incorrect, Input a valid number with correct country code")
    error.grid(row=0,column=0,columnspan=3)

    subroot2.mainloop()


def getInfo():
    number = input.get()
    key = 'Paste your API key here'
    response = requests.get("http://apilayer.net/api/validate?access_key={}&number={}".format(key,number))

    json_data = json.loads(response.text)
    try:
        valid = json_data['valid']

    except:
        errorWindow()

        
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

        subRoot1.mainloop()

    else:
        errorWindow()





input = Entry(root,width=30,borderwidth=5,fg="white",bg="Black")
searchButton = Button(root,text="Search",command=getInfo,padx=30,pady=10)
quitButton = Button(root,text="Quit",command=root.quit,padx=30,pady=10)
input.grid(row=0,column=0,columnspan=2)
searchButton.grid(row=1,column=1)
quitButton.grid(row=1,column=0)




root.mainloop()