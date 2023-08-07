<?php
require_once "ClassPessoa.php";
class Professor extends Pessoa {
    private $especialidade;
    private $salario;

    public function receberAumento($aum) {
        $this->salario += $aum;
    }

    function getespecialidade() {
        return $this->especialidade;
    }

    function getsalario() {
        return $this->salario;
    }

    function serespecialidade($v) {
        $this->especialidade = $v;
    }

    function setsalario($v) {
        $this->salario = $v;
    }

}




?>