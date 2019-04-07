
import urllib.request
import json
import os
import sys
chave="a0fe0e1"

while 1:
    os.system("CLS")
    print('Bem vindo ao aplicativo de filmes por:EDUARDO DE PAULA XAVIER')
    print("informe a opcao desejada: ")
    print("\n DIGITE h->para ajuda")
    print("\n DIGITE k->para trocar a chave:(ORIGINAL=a0fe0e1)")
    print("\n DIGITE s->para procurar")
    print("\n DIGITE t->para sinopse")
    print("\n DIGITE e->para fechar a aplicacao")
    print("\n::ATENCAO COM A TECLA ESPACO, SUBSTITUIR POR (+)::\n")
    selecao=input("..:")
    
    if selecao==("h"):
        print("  -Aperte 's' para digitar um filme a ser buscado,\n   as opcoes de filmes disponiveis serao mostradas.\n")
        print("  -Aperte 't' para procurar a sinopse de um filme,\n   as informacoes do filme desejado serao mostradas.\n")
        print("  -ATENCAO:: PARA FILMES COM MAIS DE UM NOME:: O 'ESPACO' DEVE SER SUBSTITUIDO POR '+':"
              +"\n   EXEMPLO: 'Batman Begins' deve ser escrito como 'Batman+Begins' no campo de busca.\n")
        print("  -E necessario uma chave para ter acesso ao OMDb, a original utilizada e 'a0fe0e1',\n   caso seja necessario aperte 'k' para trocar a chave:\n")
        os.system("PAUSE")
             
    elif selecao==("k"):
        chave=input("insira nova chave: ")
    elif selecao==("s"):
        
        filme=input("insira o filme: ")
        
        response= urllib.request.urlopen('http://www.omdbapi.com/?apikey='+chave+'&s='+filme).read()
        json_obj=str(response,'utf-8')
        data=json.loads(json_obj)

        for item in (data['Search']):
            print ('Titulo: '+item['Title']+', Ano: '+(item['Year'])+' Tipo: '+(item['Type']))
        os.system("PAUSE")

    elif selecao==("t"):
        filme= input("insira o filme: ")
        response= urllib.request.urlopen('http://www.omdbapi.com/?apikey='+chave+'&t='+filme).read()
        json_obj=str(response,'utf-8')
        data=json.loads(json_obj)
        print('Titulo: '+data['Title']+'\nAno: '+data['Year']+'\nIndicacao: '
              +data['Rated']+'\nLancado: '+data['Released']+'\nDuracao: '
              +data['Runtime']+'\nGenero: '+data['Genre']+'\nDirecao: '
              +data['Director']+'\nEscritor: '+data['Writer']+'\nAtores: '
              +data['Actors']+'\nSinopse :'+data['Plot']+'\nLingua: '
              +data['Language']+'\nPais: '+data['Country']
              +'\nPremios: '+data['Awards']+'\nPoster: '+data['Poster']
              +'\nTipo: '+data['Type'])
        os.system("PAUSE")
    elif selecao==('e'):
        sys.exit()
    else:
        print("comando inexistente")
        os.system("PAUSE")


