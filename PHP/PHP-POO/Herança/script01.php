<?php
require_once "ClassAluno.php";
require_once "ClassFuncionario.php";
require_once "ClassPessoa.php";
require_once "ClassProfessor.php";
// Programa principal

$p1 = new Pessoa();
$p2 = new Aluno();
$p3 = new Professor();
$p4 = new Funcionario();

$p1 -> setnome('Pedro');
$p2 -> setnome('Maria');
$p3 -> setnome('Cláudia');
$p4 -> setnome('Fabiana');

$p2 -> setcurso('Informática');
$p3 -> setsalario(2500.75);
$p4 -> setsetor('Estoque');



var_dump($p1);
var_dump($p2);
var_dump($p3);
var_dump($p4);

?>