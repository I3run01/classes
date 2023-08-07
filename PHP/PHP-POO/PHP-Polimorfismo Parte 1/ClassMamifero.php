<?php

require_once "ClassAnimal.php";
class Mamifero extends Animal {
    private $corPelo;

    public function alimentar() {
        echo "<p>mamando<p>";

    }

    public function emitirSom() {
        echo "<p>Som de mamifero <p>";

    }

    public function locomover() {
        echo "<p>Correndo<p>";
        

    }
    
    public function getCorPelo()
    {
        return $this->corPelo;
    }


    public function setCorPelo($corPelo)
    {
        $this->corPelo = $corPelo;

        return $this;
    }
}





?>