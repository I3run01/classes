<?php
    class Lutador {
        private $nome;
        private $nacionalidade;
        private $idade;
        private $altura;
        private $peso;
        private $categoria;
        private $vitorias;
        private $derrotas;
        private $empates;
        
        public function __construct($nome, $nacionalidade, $idade, $altura, $peso, $vitorias, $derrotas, $empates ) {
            $this -> nome = $nome;
            $this -> nacionalidade = $nacionalidade;
            $this -> idade = $idade;
            $this -> altura = $altura;
            $this -> peso = $peso;
            $this -> categoria = $this -> categoria();
            $this -> vitorias = $vitorias;
            $this -> derrotas = $derrotas;
            $this -> empates = $empates;
        }

        private function categoria() {
            if($this->peso < 70.4) return 'Peso leve';
            else if($this->peso >= 70.4 && $this->peso <= 83.9) return 'Peso médio';
            else return 'Peso pesado';
        }

        function apresentar() {
            echo "O lutador {$this->nome} já consta com {$this->vitorias} vitórias, {$this->derrotas} derrotas e {$this->empates}";

        }

        function status() {
            echo "O lutador {$this->nome} tem {$this->altura}m de altura, ele é {$this->nacionalidade} e tem {$this->idade} anos<br>";
        }

        function ganharluta() {
            $this -> vitorias += 1; 
        }

        function perderluta() {
            $this -> derrotas += 1;
        }

        function empatarluta() {
            $this -> empates += 1;
        }

        function getnome() {
            return $this->nome;
        }

        function getnacionalidade() {
            return $this->nacionalidade;
        }

        function getidade() {
            return $this->idade;
        }

        function getaltura() {
            return $this->altura;
        }

        function getcategoria() {
            return $this->categoria;
        }

        function getvitorias() {
            return $this->vitorias;
        }

        function getderrotas() {
            return $this->derrotas;
        }

        function getempates() {
            return $this->empates;
        }

        function getpeso() {
            return $this->peso;
        }

        function setnome($v) {
            $this->nome = $v;
        }

        function setnacionalidade($v) {
            $this->nacionalidade = $v;
        }

        function setidade($v) {
            $this->idade = $v;
        }

        function setaltura($v) {
            $this->altura = $v;
        }

        function setcategoria($v) {
            $this->categoria = $v;
        }

        function setvitorias($v) {
            $this->vitorias = $v;
        }

        function setderrotas($v) {
            $this->derrotas = $v;
        }

        function setempates($v) {
            $this->empates = $v;
        }

        function setpeso($v) {
            $this->peso = $v;
        }



    }
    
?>