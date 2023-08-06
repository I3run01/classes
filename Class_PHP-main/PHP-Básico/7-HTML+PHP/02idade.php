 <?php
    $nome = isset( $_GET["nome"])?$_GET["nome"]: ["não informado"];
    $ano = $_GET["ano"];
    $sexo = $_GET["sexo"];

    $idade = date("Y") - $ano;
    echo "$nome tem $idade anos e é um(a) $sexo"
 ?>
