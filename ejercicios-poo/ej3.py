clase  Triángulo ():
    def  inicializar ( self , lado1 , lado2 , lado3 ):
        uno mismo lado1 = lado1
        uno mismo lado2 = lado2
        uno mismo lado3 = lado3
        si  uno mismo . lado1 > yo . lado2  y  uno mismo . lado1 > yo . lado3 :
            uno mismo alcalde = uno mismo . lado1
        elif  auto . lado2 > yo . lado1  y  uno mismo . lado2 > yo . lado3 :
            uno mismo alcalde = uno mismo . lado2
        más :
            uno mismo alcalde = uno mismo . lado3
    def  imprimir ( auto ):
        print ( "El lado mayor es:" , self . mayor )
        si  uno mismo . lado1 == yo . lado2  y  uno mismo . lado2 == yo . lado3 :
            print ( "El triangulo es equilatero" )
        más :
            print ( "no es equilátero" )

trinagulo1 = Triángulo ()
trinagulo1 . inicializar ( 1 , 2 , 3 )
trinagulo1 . imprimir ()

triangulo2 = triangulo ()
triangulo2 . inicializar ( 4 , 4 , 4 )
triangulo2 . imprimir ()