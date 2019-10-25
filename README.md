# clear-csv-helios
Código criado para remover caracateres especiais dos nomes em listas do Helios Voting (https://vote.heliosvoting.org/)

<h2> Como funciona </h2>
        0 Faça o clone ou o download do repositório
        1 copie o arquivo que deseja 'limpar' para o diretório do repositório
            1.1 o arquivo deve ter a extensão csv no formato recomendado pelo helios voting (id_unico,email,nome)
                este código vai remover acentos apenas dos nomes
        2 na linha seguinte ao primeiro comentário (#) coloque o nome do arquivo que você deseja alterar
        3 [opcional] modifique o prefixo após o segundo comentário #
            
            
            
<h4>Créditos </h4>            
A rotina de remoção dos caracteres é baseada neste GIST: https://gist.github.com/boniattirodrigo/67429ada53b7337d2e79
      no presente código foi apenas implementada um solução pontual para listas do helios voting
