<?php

class Caneta {
    public $modelo;
    public $cor;
    private $ponta;
    protected $carga;
    protected $tampada;

    public function rabiscar() {
        if ($this->tampada == true ) {
            echo "<p> Erro! Não posso rabiscar <br>";
        }

        else {
            echo "<p>Estou rabiscando...</p> <br>";
        }
    }

    public function tampar() {
        $this->tampada = true;
        

    }

    public function destampar(){
        $this->tampada = false;

    }
    

}



?>
