<?php 
require_once "ClassVideo.php";
require_once "ClassGafanhoto.php";

class Visualizacao {
    private $espectador;
    private $filme;

    function __construct($espectador, $filme)
    {
        $this->espectador = $espectador;
        $this->filme = $filme;
        $this->filme -> setViews();
        $this->espectador -> viuMaisUm();
    }

    function avaliar() {
        $this->filme->setAvaliacao(5) ;
    }

    function avaliarNota($v) {
        $this->filme->setAvaliacao($v);
    }

    function avaliarPorc($v) {

        if ( $v < 20 ) $this->filme->setAvaliacao(2);
        else if ($v >= 20 && $v < 60) $this->filme->setAvaliacao(3);
        else $this->filme->setAvaliacao(5);
    }

    /**
     * Get the value of espectador
     */ 
    public function getEspectador()
    {
        return $this->espectador;
    }

    /**
     * Set the value of espectador
     *
     * @return  self
     */ 
    public function setEspectador($espectador)
    {
        $this->espectador = $espectador;

        return $this;
    }

    /**
     * Get the value of filme
     */ 
    public function getFilme()
    {
        return $this->filme;
    }

    /**
     * Set the value of filme
     *
     * @return  self
     */ 
    public function setFilme($filme)
    {
        $this->filme = $filme;

        return $this;
    }
}


?>