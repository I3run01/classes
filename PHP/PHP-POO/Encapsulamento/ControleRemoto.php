<?php
require_once 'Controlador.php';
    class ControleRemoto {
        private $volume;
        private $ligado;
        private $tocando;
        private $colorido;
        private $normal;

        function __construct () {
            $this->volume = 50;
            $this -> ligado = false;
            $this -> tocando = false;
            $this -> colorido = true;
            $this -> normal = true;
        }
        function getcolorido() {
            return $this->colorido;
        }
    
        function setcolorido($v) {
            $this -> colorido = $v;
        }

        function getnormal() {
            return $this->normal;
        }
    
        function setnormal($v) {
            $this -> normal = $v;
        }
    
        function getVolume() {
            return $this->volume;
        }
    
        function setVolume($v) {
            $this -> volume = $v;
        }
    
        function getligado() {
            return $this->ligado;
        }
    
        function setligado($v) {
            $this -> ligado = $v;
        }
    
        function gettocando() {
            return $this->tocando;
        }
    
        function settocando($v) {
            $this -> tocando = $v;
        }
    
        function ligar() {
            $this -> setligado(true);
    
        }
    
        function desligar() {
            $this -> setligado(false);
            
        }
    
        function abrirMenu() {
            echo "<br>Está ligado". ($this->getligado())?"Sim":"Não";
            echo "<br> Está tocando? " .($this->gettocando())?"SIM":"Não";
            echo "<br>Volume: " . $this-> getVolume();
            
            for ($i=0; $i <= $this->getVolume() ; $i+=10 ) { 
                echo "|";
            }
    
            echo "<br>";
    
            
        }
    
        function fecharMenu() {
            echo "<br>Fechando o menu...";
            
        }
    
        function maisVolume() {
            if($this->getligado()){
                $this -> setVolume($this->getVolume() + 5);
            }
            
        }
    
        function menosVolume() {
            if ($this -> getligado()) {
                $this -> setVolume($this -> getVolume() - 5);
            }
            
        }
    
        function ligarMudo() {
            if ($this -> getLigado() && $this-> getVolume() > 0) {
                $this -> setligado(0);
            }
            
        }
    
        function desligarMudo() {
            if ($this -> getligado() && $this->getVolume() == 0) {
                $this -> setVolume(50);
            }
        }
    
        function play() {
            if($this-> getligado() && !($this->gettocando())) {
                $this -> setTocando(true);
            }
            
        }
    
        function pause() {
            if($this -> getligado() && $this->gettocando()) {
                $this -> settocando(false);
    
            }
            
        }

        function colorido() {
            $this -> colorido = true;
        }

        function PretoEBranco() {
            $this -> colorido = false;
        }

        function normal() {
            $this -> normal = true;
        }

        function lento() {
            $this -> normal = false;
        }

        
    }
?>

    