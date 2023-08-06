<?php 

require_once "ClassAnimal.php";

class Peixe extends Animal
{
    # code...
    private $corEscama;

    public function alimentar() {
        echo "<p>Comendo substâncias<p>";

    }

    public function emitirSom() {
        echo "<p>Peixe não faz som <p>";

    }

    public function locomover() {
        echo "<p>nadando<p>";
        

    }

    /**
     * Get the value of corEscama
     */ 
    public function getCorEscama()
    {
        return $this->corEscama;
    }

    /**
     * Set the value of corEscama
     *
     * @return  self
     */ 
    public function setCorEscama($corEscama)
    {
        $this->corEscama = $corEscama;

        return $this;
    }
}






?>