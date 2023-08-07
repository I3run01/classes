<?php 
require_once "ClassVideo.php";
require_once "ClassGafanhoto.php";
require_once "ClassVisualizacao.php";

$v = new Video('Mamonas Assassinas');

$v -> play();
$v -> play();
$v -> play();
$v -> play();
$v -> pause();

$p = new Gafanhoro('Rodrigo', 23, 'masc', 'Rodring123');

$filme = new Visualizacao($p, $v);
$filme -> avaliarPorc(90);
$filme2 = new Visualizacao($p, $v);
$filme2 -> avaliarNota(4);

$filme3 = new Visualizacao($p, $v);
$filme3 -> avaliarNota(1);



var_dump($filme);

?>