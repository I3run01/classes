<?php
require_once 'ClassLutador.php';
class Luta {
    //Atributos
    private $desafiado;
    private $desafiante;
    private $rounds;
    private $aprovado;

    //Métodos Públicos
    public function marcarLuta($l1, $l2) {
        if ($l1->getcategoria() == $l2->getcategoria() && $l1 !== $l2) {
            $this->aprovado = true;
            $this-> desafiado = $l1;
            $this-> desafiante = $l2;
        } else {
            $this -> aprovado = false;
            $this -> desafiado = null;
            $this -> desafiante = null; 
        }

    }

    public function lutar() {
        if($this->aprovado) {
            $this->desafiado -> apresentar();
            $this->desafiante -> apresentar();
            $vencedor = rand(0,2);
            switch($vencedor) {
                case 0:
                    echo "<p> Empate de luta <br>";
                    $this ->desafiado -> empatarluta();
                    $this ->desafiante -> empatarluta();
                    break;
                case 1:
                    echo "<p>". $this->desafiado->getnome(). " venceu<br>";
                    $this -> desafiado -> ganharluta();
                    $this -> desafiante -> perderluta();
                    break;
                case 2:
                    echo "<p>". $this->desafiante->getNome(). " venceu<br>";
                    $this -> desafiado->perderluta();
                    break;
            }
        } else {
            echo "<p> Luta não pode acontecer</p>";
        }

    }

    function getdesafiado() {
        return $this->desafiado;
    }

    function getdesafiante() {
        return $this->desafiante;
    }

    function getrounds() {
        return $this->rounds;
    }

    function getaprovado() {
        return $this->aprovado;
    }

    function setdesafiado($v) {
        $this->desafiado = $v;
    }

    function setdesafiante($v) {
        $this->desafiante = $v;
    }


    function setrounds($v) {
        $this->rounds = $v;
    }


    function setaprovado($v) {
        $this->aprovado = $v;
    }

}





?>