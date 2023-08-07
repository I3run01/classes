select * from cursos
where nome like 'p%';

select * from cursos
where nome like '%a';

select * from cursos
where nome like '%a%';

select * from cursos
where nome not like '%a%';

select * from cursos
where nome like 'ph%p';

select * from cursos
where nome like 'ph%p_';

select distinct nacionalidade from gafanhotos
order by nacionalidade;

select count(*) from cursos where carga > 40;

select max(carga) from cursos;

select min(carga) from cursos where ano = 2016;

select sum(totaulas) from cursos where ano = 2016;

select avg(totaulas) from cursos where ano = 2016;

