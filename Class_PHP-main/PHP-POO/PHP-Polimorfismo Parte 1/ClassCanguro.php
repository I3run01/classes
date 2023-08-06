<?php 
require_once "ClassMamifero.php";
class Canguro extends Mamifero {
    private $bolsa;

    function locomover()
    {
        echo "Pulando";
    }

    /**
     * Get the value of bolsa
     */ 
    public function getBolsa()
    {
        return $this->bolsa;
    }

    /**
     * Set the value of bolsa
     *
     * @return  self
     */ 
    public function setBolsa($bolsa)
    {
        $this->bolsa = $bolsa;

        return $this;
    }
}


?>