<?php
    $frase = "Estou aprendendo PHP";
    $pos = strpos($frase, "PHP");
    echo "$frase<br>A string goi encontrada na posição $pos <br>";

    $posM = stripos($frase, "php");
    echo "$frase<br>A string goi encontrada na posição $pos <br>";

    $cont = substr_count($frase, "PHP");
    echo "PHP é encontrado $cont vezes <br>";

    $site = "Curso em video";
    $sub = substr($site, 0, 5);
    echo "$sub<br>"

    


?>