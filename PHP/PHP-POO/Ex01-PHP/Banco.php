<?php
    class ContaBK {
        public $numConta;
        protected $tipo;
        private $dono;
        private $saldo;
        private $status;

        public function __construct($dono, $conta) {
            $this -> dono = $dono;
            $this -> numConta = $conta;
            $this -> status = false;
            $this -> saldo = 0;
        }

        public function abrirConta($valor) {
            if ($this->status == true) {
                echo "Conta já aberta";
                return;
            }
                          
            $this -> status = true;
            if($valor == 'CC') {
                $this->saldo = 50;
                $this->tipo = 'CC';
            }
            else if($valor == 'CP') {
                $this->saldo = 150;
                $this->tipo = 'CP';
            }
            else echo "Informar se é CC ou CP<br>";
            
            
        }

        public function fecharConta() {
            if ($this -> saldo > 0 ) {
                echo "Saque todo o dinheiro, antes de fechar a conta";

            }

            else if ($this -> saldo < 0) {
                echo "Quite os seus débitos, antes de zerar a conta";

            }

            else {
                $this -> status = false;
            }
        }

        public function sacar($valor = 0) {
            if ($this -> saldo < $valor) echo "Saldo insuficiente, você possui R$ {$this -> saldo}";

            else $this->saldo = $this -> saldo - $valor;
        }

        public function deposito($valor) {
            if ($this -> status == false) echo "Conta fechada, abra ela primeiro";

            else $this -> saldo = $this -> saldo + $valor;
        }

        public function pagarMensal() {
            if ($this -> tipo == 'CC') $this -> saldo = $this -> saldo - 12;
            else $this->saldo = $this -> saldo - 20;
        }

        public function GetNumConta() {
            return $this -> numConta;
        }

        public function GetTipo() {
            return $this -> tipo;
        }

        public function GetDono() {
            return $this -> dono;
        }

        public function Getsaldo() {
            return $this -> saldo;
        }

        public function GetStatus() {
            return $this -> status;
        }

        public function SetNumConta($valor) {
            $this -> numConta = $valor;
        }

        public function SetTipo($valor) {
            $this -> tipo = $valor;
        }

        public function SetDono($valor) {
            $this -> dono = $valor;
        }

        public function SetSaldo($valor) {
            $this -> saldo = $valor;
        }

        public function SetStatus($valor) {
            $this -> status = $valor;
        }



    }





?>