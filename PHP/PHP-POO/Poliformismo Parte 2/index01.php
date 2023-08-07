<?php 
require_once "ClassAnimal.php";
require_once "ClassMamifero.php";
require_once "ClassLobo.php";
require_once "ClassCachorro.php";

$m = new Mamifero();

$m -> emitirSom();

$lobo = new Lobo;

$lobo -> emitirSom();

$cachorro = new Cachorro;

$cachorro -> reagirDono(false);




?>