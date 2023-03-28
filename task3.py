#context menu
is_running = True

while is_running :
    user_choose = input("""Do you want to 
        a)  buy something
        b)  quit
    """)
                            
    if user_choose == "a" :
        print("show products")
    if user_choose == "b" :
        is_running = False
    else:
        is_running = True
        

    
    
    
    
