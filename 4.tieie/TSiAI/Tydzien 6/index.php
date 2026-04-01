<?php
$host = "localhost";
$user = "root";
$pwd = "";
$db = "egzamin";
$conn = mysqli_connect($host, $user, $pwd, $db);

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
echo "Connected successfully";
    $sql = "SELECT * FROM users";
    $result = mysqli_query($conn, $sql);
    while ($row = $result->fetch_row()) {
      $data = $row;
    }
    var_dump($data)

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?= $data['1']; ?> Witaj
</body>
</html>