select nome, ano from cursos;

select * from cursos;

select * from gafanhotos;

select nome, cursopreferido from gafanhotos;

select gafanhotos.nome, gafanhotos.cursopreferido, cursos.nome, cursos.ano
from gafanhotos inner join cursos
on gafanhotos.cursopreferido = cursos.idcurso;

select g.nome, g.cursopreferido, c.nome, c.ano
from gafanhotos as g inner join cursos as c
on g.cursopreferido = c.idcurso;

select g.nome, g.cursopreferido, c.nome, c.ano
from gafanhotos as g left outer join cursos as c
on g.cursopreferido = c.idcurso;

select g.nome, g.cursopreferido, c.nome, c.ano
from gafanhotos as g right outer join cursos as c
on g.cursopreferido = c.idcurso;