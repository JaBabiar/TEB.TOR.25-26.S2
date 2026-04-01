<?php
// $_GET['jakasZmienna'] - https://localhost.com/index.php?jakasZmienna=1
//$_POST['jakasZmienna] - W network tab


?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <section>
        <h2>FORM GET</h2>
        <form action="" method="GET">
            <input type="text" name="imie" id="imie">
            <input type="submit" value="submit">
        </form>
        <?= $_GET['imie'] ?>
    </section>

    <section>
        <h2>FORM POST</h2>
        <form action="" method="POST">
            <input type="text" name="imie" id="imie">
            <input type="submit" value="submit">
        </form>
        <?= $_POST['imie'] ?>
    </section>
</body>
</html>