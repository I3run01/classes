<?php
require_once "ClassPessoa.php";
class Funcionario extends Pessoa {
    private $setor;
    private $trabalhando;

    public function mudarTrabalho() {
        $this->trabalhando = ! $this->trabalhando;
    }

    function getsetor() {
        return $this->setor;
    }

    function gettrabalhando() {
        return $this->trabalhando;
    }

    function setsetor($v) {
        $this->setor = $v;
    }

    function settrabalhando($v) {
        $this->trabalhando = $v;
    }



}






?>