<?php 
require_once "ClassPessoa.php";

class Gafanhoro extends Pessoa {
    private $login;
    private $totAssistidos;

    function __construct($nome, $idade, $sexo, $login)
    {
        parent::__construct($nome, $idade, $sexo);
        $this->login = $login;
        $this->totAssistidos = 0;
    }

    function viuMaisUm() {
        $this->totAssistidos ++ ;
    }

    
    
    /**
     * Get the value of login
     */ 
    public function getLogin()
    {
        return $this->login;
    }

    /**
     * Set the value of login
     *
     * @return  self
     */ 
    public function setLogin($login)
    {
        $this->login = $login;

        return $this;
    }

    /**
     * Get the value of totAssistidos
     */ 
    public function getTotAssistidos()
    {
        return $this->totAssistidos;
    }
}


?>