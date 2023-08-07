<?php

require_once "ClassPessoa.php";
require_once "interfaceLivro.php";

class Livro implements interfaceLivro {
    private $titulo;
    private $autor;
    private $totPaginas;
    private $pagAtual;
    private $aberto;
    private $leitor;

    public function __construct($titulo, $autor, $totPaginas, $leitor) {
        $this->titulo = $titulo;
        $this->autor = $autor;
        $this->totPaginas = $totPaginas;
        $this->leitor = $leitor;
        $this->aberto = false;
        $this ->pagAtual = 0;
    }

    public function detalhes() {
        echo "Titulo: {$this->titulo}<br>Autor: {$this->autor}<br>Total de páginas: {$this->totPaginas}<br>Página atual: {$this->pagAtual}<br>Se está aberto: {$this->aberto}<br>Nome do leitor: {$this->leitor->getnome()}<br>";
    }

    public function abrir() {
        if($this->aberto) echo "livro já aberto";  
        else $this->aberto = true;
    }

    public function fechar() {
        if ($this->aberto) $this->aberto = false;
        else "livro já está fechado";

    }

    public function folhar() {
        if ($this->aberto) echo "Você folhou as páginas";
        else echo "Abra o livro primeiro";
           
    }

    public function avancarPag() {
        if($this->aberto && $this->pagAtual < $this->totPaginas) $this->pagAtual += 1;
        else if($this->pagAtual == $this->totPaginas) echo "Você chegou na última página";

        else "Abra o livro primeiro";


    }

    public function voltarPag() {
        if($this->aberto && $this->pagAtual > 0) $this->pagAtual -= 1;
        else if($this->pagAtual == 0 ) echo "Você está na primeira página";
        else echo "livro fechado, abra-o primeiro";
 
    }

    function gettitulo() {
        return $this -> titulo;

    }

    function getautor() {
        return $this -> autor;

    }

    function gettotPaginas() {
        return $this -> totPaginas;

    }

    function getpagAtual() {
        return $this -> pagAtual;

    }

    function getaberto() {
        return $this -> aberto;

    }

    function getleitor() {
        return $this -> leitor -> getnome();

    }

    function settitulo($v) {
        $this->titulo = $v;
    }

    function setautor($v) {
        $this->autor = $v;
    }

    function settotPaginas($v) {
        $this->totPaginas = $v;
    }

    function setpagAtual($v) {
        if ($v > $this->totPaginas) echo "<br>Página informada é maior que o total do livro";
        else $this->pagAtual = $v;
        
    }

    function setaberto($v) {
        $this->aberto = $v;
    }

    function setleitor($v) {
        $this->leitor = $v;
    }
}






?>