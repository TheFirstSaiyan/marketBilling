import sys
import os
import csv

file = open("itemlist.csv", "r")

reader = csv.reader(file)

D = {}

for row in reader:
    D["%s" % row[0]] = {"quantity": row[1], "cost": row[2]}

def addProduct(name2,quantity2,cost2):

    D[name2] = {"quantity":quantity2,"cost":cost2}

    print(D)


def deleteProduct(name):

    count=0

    for q in D.keys():

        if(q==name):

         count+=1

    if(count>0):

        del D[name]

        print(D)

    else:

        print("there is not an item called %s"%name)

        return

def isAvailable(name3):

        count=0

        for some in D.keys():

            if(some==name3):

                count=count+1

                print(D[name3])

        if(count==0):

                 print ("not available...\n")

                 yesorno=str(input("do u wish to add it..\n type Y for Yes\ntype N for No"))

                 if(yesorno=="Y"):

                    q=int(input("enter quantity"))

                    c=int(input("enter cost per item"))

                    addProduct(name,q,c)

                 else : return


def update(name):

    count=0
    for t in D.keys():
        if(t==name):
            count+=1
    if(count>0):
        quantity = input("enter new quantity")

        cost = input("enter new cost")

        D[name]["quantity"]=quantity

        D[name]["cost"]=cost

        print(D)
    else:
        print("not available...\n")

        yesorno = str(input("do u wish to add it..\n type Y for Yes\ntype N for No"))
        if (yesorno == "Y"):

            q = int(input("enter quantity"))

            c = int(input("enter cost per item"))

            addProduct(name, q, c)

        else:
            return



class Product:

    total=0

    def findtotal(self,name,quantity):

        if (int (D[name]["quantity"])-quantity<0):

            print("available ",D[name]["quantity"])

            Product.total=Product.total+ (int(D[name]["quantity"])*int(D[name]["cost"]))

            print("total",Product.total)

            D[name]["quantity"]=0

        else:

            D[name]["quantity"]=int(D[name]["quantity"])-quantity

            Product.total = Product.total+quantity*int(D[name]["cost"])

            print("total", Product.total)



    def checkStock(self,name):

        if(int(D[name]["quantity"])>0):

            return 1
        else:

            print('no stock remaining ')

            return 0


number = int(input("enter :\n1 to bill an item\n2 to add an item\n3 to check if an item is available\n4 to remove an item\n5 to update quantity and stock\n0 to exit\n "))

while not(number==0):

 if(number==1):

  name=str(input("enter name of product"))


  count=0
  for some in D.keys():

   if (name==some):

     count+=1

  if(count>0):

        quantity = int(input("enter quantity"))

        s=Product()

        if(s.checkStock(name)):

         s.findtotal(name,quantity)

  else:
        print("not available...\n")

        yesorno = str(input("do u wish to add it..\n type Y for Yes\ntype N for No"))
        if (yesorno == "Y"):
            q = int(input("enter quantity"))

            c = int(input("enter cost per item"))

            addProduct(name, q, c)


 if(number==2 ):

    name1 = input("enter name")

    quantity1 = input("enter quantity")

    cost1 = int(input("enter cost per item"))

    addProduct(name1,quantity1,cost1)


 if(number==3):

     name=input("enter name to check availability")

     isAvailable(name)


 if(number==4):

     name=str(input("enter product name to delete"))

     deleteProduct(name)

 if(number==5):

    name=input("enter product name")

    update(name)

 number= int(input("enter ur choice....."))