<?php
    $n = array(3, 5, 8, 2);

    $n[] = 7;

    print_r($n);

    echo "<br>";


    $c = range(5, 20, 5);

    print_r($c);

    echo "<br>";
    foreach ($c as $key) {
        echo "$key";
    }

    echo "<br>";

    $v = array(1 => "A", 3 => "B", 6 => "C", 8 => "D");
    print_r($v);

    echo "<br>";
    unset($v[6]);
    print_r($v)
?>