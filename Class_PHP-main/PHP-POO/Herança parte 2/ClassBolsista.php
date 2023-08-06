<?php

require_once "ClassAluno.php";
class Bolsista extends Aluno{
    private $bolsa;
    
    public function renovarBolsa() {
        echo "Renovar Bolsa";
    }

    public function pagarMensalidade() {
        echo "<p> $this->nome é bolsita, Então paga com desconto";
    }

    function getbolsa() {
        return $this->bolsa;
    }

    function setbolsa($v) {
        $this->bolsa = $v;
    }

}
    






?>