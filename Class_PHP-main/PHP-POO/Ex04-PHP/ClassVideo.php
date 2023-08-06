<?php 
require_once "InterfaceAcoesVideo.php";

class Video implements AcoesVideo {
    private $titulo;
    private $avaliacao;
    private $views;
    private $curtidas;
    private $reproduzindo;

    function __construct($titulo)
    {
        $this->titulo = $titulo;
        $this->avaliacao=null;
        $this->views=0;
        $this->curtidas = 0;
        $this->reproduzindo = false;
    }

    function play() {
        $this->reproduzindo = true;

    }

    function pause() {
        $this->reproduzindo=false;
    }
    
    function like() {
        $this->curtidas+=1;

    }




    /**
     * Get the value of titulo
     */ 
    public function getTitulo()
    {
        return $this->titulo;
    }

    /**
     * Set the value of titulo
     *
     * @return  self
     */ 
    public function setTitulo($titulo)
    {
        $this->titulo = $titulo;

        return $this;
    }

    /**
     * Get the value of avaliacao
     */ 
    public function getAvaliacao()
    {
        return $this->avaliacao;
    }

    /**
     * Get the value of views
     */ 
    public function getViews()
    {
        return $this->views;
    }

    /**
     * Get the value of curtidas
     */ 
    public function getCurtidas()
    {
        return $this->curtidas;
    }

    /**
     * Get the value of reproduzindo
     */ 
    public function getReproduzindo()
    {
        return $this->reproduzindo;
    }

    /**
     * Set the value of views
     *
     * @return  self
     */ 
    public function setViews()
    {
        $this->views ++;

        return $this;
    }

    /**
     * Set the value of avaliacao
     *
     * @return  self
     */ 
    public function setAvaliacao($avaliacao)
    {
        if ($this->views <= 1) $this->avaliacao = $avaliacao;
        else $this->avaliacao = ($this->avaliacao + $avaliacao)/2;

        return $this;
    }
}

?>