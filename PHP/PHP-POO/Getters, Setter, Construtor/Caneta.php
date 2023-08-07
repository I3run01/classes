<?php
class Caneta {
    private $modelo;
    private $cor;
    private $ponta;
    protected $tampada;

    public function __construct($m, $c, $p) {
        //Caneta pode ser também __construct
        $this ->modelo = $m;
        $this ->cor = $c;
        $this -> ponta = $p;
        $this -> tampar();

    }
    public function tampar() {
        $this->tampada = true;
    }
    
    public function getModelo() {
        return $this->modelo;
    }

    public function setModelo($m) {
        $this->modelo = $m;
    }

    public function getPonta() {
        return $this -> ponta;
    }

    public function setPonta($p) {
        return $this -> ponta = $p;
    }
}





?>