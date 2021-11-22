#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Pokemon:
    def __init__(self):
        pass
    
    def insert(self):
        poke = Pokemon()
        poke.name = input('Enter Pokemon Name ')
        poke.type = input('Enter the Pokemon type ')
        pokedex.append(poke)
        
    def display(self,poke):
        print('Pokemon Name -> ',self.name)
        print('Pokemon Type -> ',self.typ,'\n')
        
        
    
        
        
        
if __name__ =="__main__":
    
    pokedex = []
    
    bulbapedia = Pokemon()
    
    run = True
    
    while(run):
        print('            Welcome to Bulbapedia               \n')
        print(' Press 1 to input data in the Pokedex ')
        print(' Press 2 to display Pokedex')
        print(' Press 0 to QUIT')
        ch = int(input())
        if ch == 1 :
            bulbapedia.insert()
            
        elif ch == 2 :
            for i in range(list.__len__()):
                 bulbapedia.display(pokedex[i])
            
        else:
            print( " GOODBYE ")
            
            run=False
            
    
   
    
   
        
    


# In[ ]:





# In[ ]:




