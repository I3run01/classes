<?php
    $num = isset($_GET["num"])?$_GET["num"]:0;

    $primo = "s";
    for($c = 2; $c < $num; $c++) {;
        if ($num % $c == 0) {
            $primo = "n";
            echo "$num é divisivel por $c <br>";
        }
    }

    if($primo == "s") {
        echo "$num é um número primo";
    }

    else {
        echo "$num não é um número é um número primo";
    }
?>

