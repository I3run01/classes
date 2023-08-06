SELECT j.cod, j.nome, g.genero, p.produtora, j.descricao, j.nota, j.capa FROM jogos j
join generos g
on j.genero = g.cod
join produtoras p 
on j.produtora = p.cod;
