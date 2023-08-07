<?php
    $frase = "Eu vou estudar php";
    $cont = str_word_count($frase, 2);

    print_r($cont);
    echo "<br>";

    $explode = explode(" ", $frase);
    print_r($explode);
    echo "<br>";

    $str_split = str_split("Maria");
    print_r($str_split)

?>