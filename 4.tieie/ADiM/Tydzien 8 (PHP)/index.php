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
    $sql = "SELECT * FROM users"
    $data = mysqli_query($conn, "")
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>