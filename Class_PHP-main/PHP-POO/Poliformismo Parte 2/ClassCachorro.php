<?php 
require_once "ClassMamifero.php";

class Cachorro extends Mamifero
{
    function emitirSom()
    {
        echo "au-au-au";
    }

    function reagirFrase($frase) {
        if($frase == "Toma comida" || $frase == "Olá") {
            echo "<p>Abanar e Latir<br>";
        }

        else {
            echo "<br>Rosnar";
        }
    }

    function reagirHora($hora, $min) {
        if ($hora < 12) {
            echo "<br> Abanar";
        }

        elseif ($hora >= 18 ) {
            echo "<br> Ignorar";
        }

        else {
            echo "<br> Abanar e Latir";
        }

    }

    function reagirDono($dono) {
        if ($dono) {
            echo "<br> Abanar";
        }

        else {
            echo "<br> Rosnar e Latir";
        }

    }

    function reagirIdadePeso($idade, $peso) {
        if($idade < 5) {
            if ($peso < 10) {
                echo "<br> Abanar";
            }

            else {
                echo "<br> Latir";
            }
        }

        else {
            if ($peso < 10) {
                echo "<br> Rosnar";
            }

            else {
                echo "<br> Ignorar";
            }
        }
    }
}


?>