<?php 
require_once "ClassAnimal.php";

class Ave extends Animal
{
    # code...
    private $corPena;

    public function alimentar() {
        echo "<p>Comendo frutas<p>";

    }

    public function emitirSom() {
        echo "<p>Som de Ave<p>";

    }

    public function locomover() {
        echo "<p>voando<p>";
    }

    public function getCorPena()
    {
        return $this->corPena;
    }

    public function setCorPena($corPena)
    {
        $this->corPena = $corPena;

        return $this;
    }
}



?>