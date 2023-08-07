<?php

require_once "ClassPessoa.php";
class Aluno extends Pessoa {
    private $matr;
    private $curso;

    public function cancelarMatr() {
        echo "<p>Matrícula será cnacelada </p>";
    }

    function getmatr() {
        return $this->matr;
    }

    function getcurso() {
        return $this->curso;
    }

    function sermatr($v) {
        $this->matr = $v;
    }

    function setcurso($v) {
        $this->curso = $v;
    }


}





?>