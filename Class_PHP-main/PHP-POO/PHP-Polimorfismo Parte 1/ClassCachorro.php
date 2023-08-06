<?php 

require_once "ClassMamifero.php"; 

class Cachorro extends Mamifero {
    private $osso = 'não enterrado';

    function enterrarOsso() {
        $this->osso = 'enterrado';
    }
    
    function abanarRabo() {
        echo "Abanando o rabo";
    }

    function locomover()
    {
        echo "correndo";
    }

    function emitirSom()
    {
        echo "AU-AU-Au";
    }
}

?>