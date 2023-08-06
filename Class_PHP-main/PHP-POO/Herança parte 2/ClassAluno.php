<?php
require_once "ClassPessoa.php";

class Aluno extends Pessoa {
    private $matricula;
    private $curso;

    public function pagarMensalidade() {
        echo "<p>Pagando mensalidade do aluno $this->nome";
    }

    function getmatricula() {
        return $this->matricula;
    }
    
    function getcurso() {
        return $this->curso;
    }

    function setmatricula($v) {
        $this->matricula = $v;
    }

    function setcurso($v) {
        $this->curso = $v;

    }
}

?>