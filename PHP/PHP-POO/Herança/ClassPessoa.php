<?php
class Pessoa {
    private $nome;
    private $idade;
    private $sexo;

    public function fazerAniversario() {
        $this->idade++;
    }


    function getnome() {
        return $this->nome;
    }

    function getidade() {
        return $this->idade;
    }

    function getsexo() {
        return $this->sexo;
    }

    function setnome($v) {
        $this->nome = $v;
    }

    function setidade($v) {
        $this->idade = $v;
    }

    function setsexo($v) {
        $this->sexo = $v;
    }

}







?>
