print ( '-=' * 20 )
print ( 'Analisador de triangulos' )
print ( '-=' * 20 )
x = float ( input ( 'O primeiro segmento:' ) )
y = float ( input ( 'O segundo segmento:' ) )
z = float ( input ( 'O terceiro segmento:' ) )
if x < y + z and y < x + z and z < x + y:
    print ( 'Os segmentos podem formar um triangulo.' )
else:
    print ( 'Os segmentos nao podem formar um triangulo.' )
