<?php
require_once "ClassAnimal.php";

class Mamifero extends Animal02 {
    protected $corPelo;

    function emitirSom()
    {
        echo "<p>Som de mamifero";
    }


    /**
     * Get the value of corPelo
     */ 
    public function getCorPelo()
    {
        return $this->corPelo;
    }

    /**
     * Set the value of corPelo
     *
     * @return  self
     */ 
    public function setCorPelo($corPelo)
    {
        $this->corPelo = $corPelo;

        return $this;
    }
}
