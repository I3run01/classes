<?php
    class Notebook {
        private $cor;
        private $processador;
        private $marca;

        public function __construct($c, $p, $m) {
            $this -> cor = $c;
            $this -> processador = $p;
            $this -> marca = $m;
        }

        public function getCor() {
            return $this->cor;
        }

        public function setCor($valor) {
            $this->cor = $valor;
        }

        public function getProcessador() {
            return $this->processador;
        }

        public function setProcessador($valor) {
            $this->processador = $valor;
        }

        public function getMarca() {
            return $this->marca;
        }

        public function setMarca($valor) {
            $this->marca = $valor;
        }

        
    
    }

    





?>