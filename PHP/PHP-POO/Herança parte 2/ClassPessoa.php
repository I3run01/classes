<?php

abstract class Pessoa {
    protected $nome;
    protected $idade;
    protected $sexo;
    public final function fazerAniversario() {
        $this -> idade ++;

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