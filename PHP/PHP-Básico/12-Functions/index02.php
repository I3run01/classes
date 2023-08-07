<?php
function soma() {
    $p = func_get_args();
    $t = func_num_args();
    $s = 0;

    for ($i=0; $i < $t; $i++) { 
        # code...
        $s = $s + $p[$i];
    }
    return $s;
}
    


    $r = soma(3, 5, 2);
    echo "$r";
?>

