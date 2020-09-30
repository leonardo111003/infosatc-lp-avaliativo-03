Nome  =  0
cpf  =  0
senha  =  0
idade  =  int ( input ( "Qual a sua idade:" ))
if  15 < idade <  70 :
    peso  =  int ( input ( "Qual é seu peso em kg:" ))
    if  peso > 49 :
        sono =  int ( input ( "Quantas horas de sono você teve nas ultimas 24 horas:" ))
        if  sono > 6 : 
            print ( "Você pode fazer a doação" )
            escolha  =  int ( input ( "Voce quer se cadastar? 1 para sim 0 para não:" ))
            if  escolha > 0 :
                Nome  =  input ( "insira seu nome :" )
                Cpf  =  int ( input ( "Digite o Cpf:" ))
                Senha  =  int ( input ( "insira sua senha:" ))
                print ( "As informações do paciente são:" , Nome , "" , cpf , "" , senh)a
            else :
                print ( "obrigado por doar sangue" )  
        else :
            print ( "você não dormiu o suficiente para fazer a doação de sangue" )      
    else :
        print ( "Seu peso está abaixo do necessario para poder doar " )        
else :
     print ( "você nao tem idade pra poder doar sangue" )
