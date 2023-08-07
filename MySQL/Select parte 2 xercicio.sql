select * from gafanhotos;

select * from gafanhotos
where sexo = 'f';

select * from gafanhotos
where nascimento between '2000-01-01'and '2015-12-15'; 

select * from gafanhotos
where sexo = 'M' and profissao = 'programador';

select * from gafanhotos
where nome like 'j%' and sexo = 'F'and nacionalidade = 'Brasil';

select nome, nacionalidade from gafanhotos
where sexo = 'M' and nome = '%silva%' and nacionalidade != 'Brasil' and peso < 100;

select max(altura) from gafanhotos
where sexo = 'M' and nacionalidade = 'Brasil';

select avg(peso) from gafanhotos;

select min(peso) from gafanhotos
where sexo = 'F' and nacionalidade != 'Brasil' and nascimento between '1990-01-01' and '2000-12-31';

select count(*) from gafanhotos 
where sexo = 'F' and altura > 1.90;