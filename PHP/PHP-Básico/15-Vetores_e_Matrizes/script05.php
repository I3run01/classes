<?php
    $v = array("A", "B", "C");
    print_r($v);
    var_dump($v);
    $tam = count($v);

    echo "Meu vetor tem " .  count($v). " Elementos <br>";

    $n = array(3, 5, 8, 2);
    
    array_push($n, 7);

    array_pop($n);
    print_r($n);
    echo "<br>";

    array_unshift($n, 2);
    print_r($n);

    array_shift($n);
    echo "<br>";
    print_r($n);
?>