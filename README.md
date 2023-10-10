# ETL-of-csv-files-with-python.

Junção automática de arquivos csv com Python para não programadores.

Muitas vezes, no nosso dia a dia, temos que trabalhar com diversos arquivos em csv. Mas as vezes precisamos trabalhar com arquivos de milhões de linhas, e, tanto o Excel, quanto o Power Query, possuem um limite que, em algumas ocasiões, não atendem às nossas necessidades. E pior... as vezes precisamos concatenar (juntar) diversos arquivos CSV diferentes em 1 só. Outro problema é se forem dezenas de arquivos, não é nada divertido juntar tudo manualmente.

Digamos que você queira consolidar as vendas de 2 anos da empresa, e cada mês está em arquivo csv diferente com 500 mil linhas cada, isso resultaria em 12 milhões de linhas no total. Certamente você teria dificuldade de rodar isso no Excel e até no Power Query. E mesmo que conseguisse, seria bem trabalhoso juntar um por um.

Pra solucionar esse problema que eu já vivi algumas vezes enquanto não programava ainda, escrevi esse script em Python para ajudar quem também tem esse problema, mesmo que nunca tenha programado nada (mas você precisará ter o Python instalado). 

Mostrei também como automatizar essa extração todo mês no final.
