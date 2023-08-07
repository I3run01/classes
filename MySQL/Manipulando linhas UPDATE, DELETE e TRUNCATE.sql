select * from cursos;

update cursos
set nome = 'PHP' , ano = '2015'
where idcursos = '4';

update cursos
set nome = 'Java', ano = '2015', carga = '40'
where idcursos = '5'
limit 1;

delete f  rom cursos
where idcursos = '10'
limit 1;

truncate table cursos;
