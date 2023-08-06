<?php 

$banco = new mysqli('localhost', 'root', '', 'bd_games');

if ($banco->connect_errno) {
    echo "<p> encontrei o erro $banco->errno --> $banco->connect_error </p>";
    die();
}

$busca = $banco->query('select * from generos');

?>