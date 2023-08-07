<?php

require_once "ClassAve.php";
require_once "ClassMamifero.php";
require_once "ClassPeixe.php";
require_once "ClassReptil.php";
require_once "ClassArara.php";
require_once "ClassCanguro.php";
require_once "ClassCanguro.php";
require_once "ClassCachorro.php";
require_once "ClassCobra.php";
require_once "ClassGoldfish.php";


$m = new Mamifero;
$m -> setPeso(33.5);
$a = new Ave;

var_dump($m);
$m -> locomover();
$a -> locomover();

$ca01 = new Cachorro;

$ca01 -> locomover();
$ca01 -> emitirSom();

?>