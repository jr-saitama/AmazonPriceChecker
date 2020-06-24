import requests
from bs4 import *
import smtplib
import socket


def get_data():
        url_list =  []
        """ url_list = []
        user_input = int(input('enter the number of items : '))
        print("\nCopy and paste the urls of the items you need one after the other\n\n")
        
        for i in range(user_input-1):
            temp_url = input()
            url_list.append(temp_url) """

        with open('urls.txt', 'r') as f:
            read_lines = f.readlines()

        user_agent = read_lines[0].strip('\n')
        url_list.extend(read_lines[1:])
        
        # url_list = ["https://www.amazon.in/HP-Pentium-14-inch-Windows-14q-cs0018TU/dp/B07THRK915/"]    
        no_url = len(url_list)
        price_dict ={"item_name":[], "price":[]}
        for i in range(no_url):
            url = url_list[i]
            if(url[12]=='a'):
                # user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"
                headers = {"User-Agent" : user_agent}
                page = requests.get(url, headers=headers)

                soup = BeautifulSoup(page.content, "html.parser")

                title = soup.find(id="productTitle").get_text()
                title = title.strip("\n")
                price_dict['item_name'].append(title)
                price = soup.find(id="priceblock_ourprice").get_text()
                price = price[2:]
                price = int(float(price.replace(",","")))
                price_dict['price'].append(price)
                print("item_name : " + str(price_dict['item_name'][i]))
                print("price : " + str(price_dict['price'][i]) + "\n")

            """ elif(url[12]=='f'):
                headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"}
                page = requests.get(url, headers=headers)

                soup = BeautifulSoup(page.content, "html.parser")

                title = soup.find("div", class_="_9E25nV").get_text()
                title = title.strip("\n")
                price_dict['item_name'].append(title)
                price = soup.find("div", class_="_1vC4OE _3qQ9m1").get_text()
                price = price[2:]
                price = int(float(price.replace(",","")))
                price_dict['price'].append(price)
                print(price_dict) """

                    
                    
        server = smtplib.SMTP('smtp.gmail.com', 25)
        server.ehlo()
        server.starttls()
        server.ehlo()

        
        server.login("myfirstcompanyinengineering@gmail.com" , "jqqnmpckvzgmonhs")
        subject = "today's amazon prices of your whishlisted items"

        body = price_dict

        msg = f"Subject:{subject}\n\n{body}"

        server.sendmail("myfirstcompanyinengineering@gmail.com", "naveenkumarburugupally@gmail.com",msg)

        print('email is sent')

        server.quit()

get_data()
input()
