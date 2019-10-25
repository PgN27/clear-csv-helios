''' 
    O intuito do código abaixo é remover caracteres especiais de listas de votantes para eleições
    baseadas no sistema Helios Voting (https://vote.heliosvoting.org/)

    Como funciona:
        1 copie o arquivo que deseja 'limpar' para o mesmo diretório deste código
            1.1 o arquivo deve ter a extensão csv no formato recomendado pelo helios voting (id_unico,email,nome)
                este código vai remover acentos apenas dos nomes
        2 na linha seguinte ao primeiro comentário (#) coloque o nome do arquivo que você deseja alterar
        3 [opcional] modifique o prefixo após o segundo comentário #

    A rotina de remoção dos caracteres é baseada neste GIST: https://gist.github.com/boniattirodrigo/67429ada53b7337d2e79
        no presente código foi apenas implementada um solução pontual para listas do helios voting
'''
import removerAcentosECaracteresEspeciais as rmspec 
import csv


#Troque o nome do arquivo para o nodo daquele que você deseja ´Limpar´
nm_f = 'teste.csv'


f = open(nm_f, 'r', encoding="utf8")
leitor = csv.reader(f)
contador = 0
dados = []

for reg in leitor:
    voter_id, email, nm = reg[0], reg[1], rmspec.rmspechar(reg[2])
    if (nm != reg[2]):
        contador += 1 
    dados.append([voter_id,email,nm])
f.close()

#Troque o nome do prefixo do arquivo modificado se desejar
prefixo = "modificado"


''' 
Caso queira sobrescrever o arquivo original comente ou exclua a linha abaixo
        tenha sempre uma cópia de backup do arquivo original
        {procedimento não recomendado}
        
'''
nm_f = prefixo + '-' + nm_f
f = open(nm_f, 'w', newline='')
escritor = csv.writer(f,delimiter=',')

for linha in dados:
    escritor.writerow(linha)
f.close()

print(f"Foram removidos caracteres especiais de {contador} registros")
