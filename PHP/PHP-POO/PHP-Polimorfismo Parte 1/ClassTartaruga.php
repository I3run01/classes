<?php 
require_once "ClassReptil.php";

class Tartaruga extends Repitil {

    function locomover()
    {
        echo "locomovendo bem devagar";
    }

    function emitirSom()
    {
        echo "Som de tartaruga";
    }

    function alimentar()
    {
        echo "Comendo folhas";
    }
}

?>