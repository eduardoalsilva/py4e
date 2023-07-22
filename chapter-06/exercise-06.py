
palavra = input("Entre com a string: ")
letra = input("Entre com a letra que quer encontrar: ")
sub_palavra = input("Entre com a parte da palavra que quer encontrar: ")
nova_parte = input("Entre com a parte que quer trocar pela sub palavra: ")
indice = palavra.find(letra)

print("A letra {} está no índice {} da palavra {}.".format(letra, indice, palavra))

nova_palavra = palavra.replace(sub_palavra, nova_parte)

print("A palavra {} sem a sub_palavra {} e com a nova parte {} fica assim: {}.".format(palavra, sub_palavra, nova_parte, nova_palavra))

nova_palavra = nova_palavra.strip('a')

print("A nova palavra com strip fica assim: {}".format(nova_palavra))
