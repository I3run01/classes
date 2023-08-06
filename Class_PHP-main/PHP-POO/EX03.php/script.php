<?php
require_once "ClassPessoa.php";
require_once "ClassLivro.php";

$pessoas = [
    $p00 = new Pessoa('Julia', 33, 'feminino'),
    $p01 = new Pessoa('Matheus', 40, 'masculino'),
    $p02 = new Pessoa('Carlos', 33, 'masculino'),
];

$livros = [
    $l0 = new Livro('La la la', 'Pernabranca', 2, $pessoas[0]),
];
 
$livros[0]->abrir();
$livros[0]->voltarPag();

$livros[0]->setleitor($pessoas[1]);
var_dump($livros);
$livros[0] -> detalhes();

?>