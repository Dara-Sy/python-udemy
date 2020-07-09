#Define a function called generate_evens
#It should return a list of even numbers between 1 and 50(not including 50)

def generate_evens():    
    even_list=[]
    for i in range(1, 50):   
        if i % 2 == 0: 
            even_list.append(i)
    print(even_list)
    return even_list

generate_evens()
