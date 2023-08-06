<?php

require_once "ClassPessoa.php";

final class  Professor extends Pessoa {
    private $especialidades;
    private $salario;
    
    function getespecialidades() {
        return $this-> especialidades;
    }

    function getsalario() {
        return $this-> salario;
    }

    function setespecialidades($v) {
        $this->especialidades = $v;

    }

    function setsalario($v) {
        $this->salario = $v;

    }

    function receberAumento($v) {
        $this->salario += $v;
    }
}








?>