<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    
    <?php 
    require_once 'banco.php';
    ?>

    <div id="corpo">
        <h1>Escolha o seu jogo</h1>
        <table class="listagem">
            <?php 
            if (!$busca) {
                echo "<tr><td>Nenhum registro encontrado</td></tr>";
            }
            
            
            ?>

            <tr>
                <td>Foto</td>
                <td>Nome</td>
                <td>Adm</td>
            </tr>
            <tr>
                <td>Foto</td>
                <td>Nome</td>
                <td>Adm</td>
            </tr>
            <tr>
                <td>Foto</td>
                <td>Nome</td>
                <td>Adm</td>
            </tr>
            <tr>
                <td>Foto</td>
                <td>Nome</td>
                <td>Adm</td>
            </tr>
        </table>
    </div>
    <?php $banco->close();?>
</body>
</html>