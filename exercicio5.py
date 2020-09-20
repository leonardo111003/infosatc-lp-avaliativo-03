m  =  0
mediaM  =  0
f  =  0
mediaF  =  0
idgeralM   =  0
idgeralF  =  0
pessoas  =  int ( entrada ( "Escreva o total de pessoas" ))
enquanto ( f + m < pessoas ):
    sexo  =  entrada ( "M para masculino e F" )
    if ( sexo == "M" ):
      m  =  m  +  1
      idM  =  float ( input ( "Escreva sua idade:" ))
      idgeralM  =  idgeralM  +  idM
      mediaM  =  idgeralM / m
    elif ( sexo == "F" ):
        f  =  f  +  1
        idF  =  float ( input ( "Escreva sua idade:" ))
        idgeralF  =  idgeralF  +  idF
        mediaF  =  idgeralF / f
    mais :
         passar
print ( "Idade media dos homens:" , mediaM )
print ( "Idade media das mulheres:" , mediaF )