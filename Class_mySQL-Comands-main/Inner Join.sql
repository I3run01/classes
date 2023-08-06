create table gafanhoto_assiste_curso (
	id int not null auto_increment,
    data date,
    idgafanhotos int,
    idcurso int,
    primary key (id),
    foreign key (idgafanhotos) references gafanhotos(id),
    foreign key (idcurso) references cursos(idcurso)
) default charset = utf8;

insert into gafanhoto_assiste_curso values
(default, '2014-03-01', '1', '2');

select * from gafanhoto_assiste_curso;

select * 
from gafanhotos as g join gafanhoto_assiste_curso as a
on g.id = a.idgafanhotos;

select g.nome, c.nome, a.idcurso from gafanhotos as g 
join gafanhoto_assiste_curso as a on g.id = a.idgafanhotos
join cursos as c on c.idcurso = a.idcurso
order by g.nome;

select g.nome, c.nome, a.id from gafanhoto_assiste_curso as a
join gafanhotos as g on g.id = a.idgafanhotos
join cursos as c on c.idcurso = a.idcurso;
