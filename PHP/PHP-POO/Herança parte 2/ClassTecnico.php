<?php

require_once "ClassAluno.php";

class Tecnico extends Aluno {
    private $registro_profissional;

    function getregistro_profissional() {
        return $this->registro_profissional;
    }

    function setregistro_profissional($v) {
        $this->registro_profissional = $v;
    }
    
    function praticar() {
        echo "$this->nome está praticando";
    }
}





?>