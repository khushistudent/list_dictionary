menu={"Samosa":20,"Tea":10,"Coffee":15}
cart=[] #empty list
while True:
    user=input(" enter item : ")
    for key,value in menu.items():
        if user==menu:
             if key==user:
              
              cart.append(user)
             print(cart)
             break
        else:
            print("not")
       
        
    if user=="done":
        break