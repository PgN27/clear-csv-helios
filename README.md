# clear-csv-helios
Código criado para remover caracateres especiais dos nomes em listas do Helios Voting (https://vote.heliosvoting.org/)

# Como funciona 
<br>
<ol>
<li>Faça o clone ou o download do repositório </li>
<li>Copie o arquivo que deseja 'limpar' para o diretório do repositório </li> 
        <ol><li>o arquivo deve ter a extensão csv no formato recomendado pelo helios voting (id_unico,email,nome) <br>
                este código vai remover caracteres epeciais apenas dos nomes  </li></ol>
<li>Na linha seguinte ao primeiro comentário (#) coloque o nome do arquivo que você deseja alterar </li>
<li>[opcional] Modifique o prefixo após o segundo comentário # </li><br>
</ol>
            
<h4>Créditos</h4>

A rotina de remoção dos caracteres é baseada neste GIST: https://gist.github.com/boniattirodrigo/67429ada53b7337d2e79 <br> 
criado por <a href="https://gist.github.com/boniattirodrigo">Rodrigo Boniatti</a>. <br>
No presente código foi apenas implementada uma solução pontual para listas do helios voting a partir de arquivos *.csv
