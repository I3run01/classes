<?php
    $nome = "Guanabara";
    $novo = str_pad($nome, 30, "x", STR_PAD_BOTH);

    echo "Meu professo $novo é inteligente <br>";

    $txt = str_repeat("$nome ", 5);

    echo "Guanabara escrito 5 vezes é $txt  <br>";

    $frase = "Gosto de Estudar Java";

    $novafrase = str_replace("Java", "Python", $frase);

    echo "$novafrase <br>";

    $novafrase2 = str_ireplace("java", "Python", $frase);
    echo "$novafrase2"
?> 