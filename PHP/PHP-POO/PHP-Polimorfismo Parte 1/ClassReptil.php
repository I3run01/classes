<?php 
require_once "ClassAnimal.php";

class Repitil extends Animal {
    private $corEscama;

    public function alimentar() {
        echo "<p>Comendo vegetais<p>";

    }

    public function emitirSom() {
        echo "<p>Som de repétil <p>";

    }

    public function locomover() {
        echo "<p>Rastejando<p>";
        

    }

    public function getCorEscama()
    {
        return $this->corEscama;
    }

    public function setCorEscama($corEscama)
    {
        $this->corEscama = $corEscama;

        return $this;
    }
}


?>