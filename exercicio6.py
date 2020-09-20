Nome  =  0
cpf  =  0
senha  =  0

Nome2  =  0
cpf2  =  0
senha2  =  0

Nome3  =  0
cpf3  =  0
senha3  =  0

Nome4  =  0
cpf4  =  0
senha4  =  0

Nome5  =  0
cpf5  =  0
senha5  =  0



idade  =  int ( input ( "Qual a sua idade:" ))
if  15 < idade <  70 :
    peso  =  int ( input ( "Qual é seu peso em kg:" ))
    if  peso > 49 :
        sono =  int ( input ( "Quantas horas de sono você teve nas ultimas 24 horas:" ))
        if  sono > 6 :
            
            print ( "Você esta apto a fazer a doação" )
            escolha  =  int ( input ( "Voce quer se cadastar? 1 para sim 0 para não:" ))
            if  escolha > 0 :
                Nome  =  input ( "Digite seu nome completo:" )
                Cpf  =  int ( input ( "Digite seu Cpf:" ))
                Senha  =  int ( input ( "Digite sua senha:" ))
                    
                Nome2  =  input ( "Digite seu nome completo:" )
                Cpf2  =  int ( input ( "Digite seu Cpf:" ))
                Senha2  =  input ( "Digite sua senha:" )
                    
                Nome3  =  input ( "Digite seu nome completo:" )
                Cpf3  =  int ( input ( "Digite seu Cpf:" ))
                Senha3  =  input ( "Digite sua senha:" )
                   
                Nome4  =  input ( "Digite seu nome completo:" )
                Cpf3  =  int ( input ( "Digite seu Cpf:" ))
                Senha3  =  input ( "Digite sua senha:" )
                   
                Nome5  =  input ( "Digite seu nome completo:" )
                Cpf4  =  int ( input ( "Digite seu Cpf:" ))
                Senha4  =  input ( "Digite sua senha:" )
                  
                
               
                    


                print ( "As informações do paciente 1 são:" , Nome , "" , cpf , "" , senha )
                print ( "As informações do paciente 2 são:" , Nome2 , "" , cpf2 , "" , senha2 )
                print ( "As informações do paciente 3 são:" , Nome3 , "" , cpf3 ,   "" , senha3 )
                print ( "As informações do paciente 4 são:" , Nome4 , "" , cpf4 , "" , senha4 )
                print ( "As informações do paciente 5 são:" , Nome5 , "" , cpf5 , "" , senha5 )

                    
            
            
                 


            
            else :
                print ( "obrigado por doar sangue" )
         
         
        else :
            print ( "você não dormiu o suficiente para fazer a doação de sangue" )

        
        
    else :
        print ( "Seu peso está abaixo do necessario para poder doar " )
        
    
else :
     print ( "você nao tem idade pra poder doar sangue" )