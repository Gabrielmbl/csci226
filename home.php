<?php
	echo '<h2>Welcome '.$_SESSION['login'].'</h2>';
?>

<?php 
//from: https://www.youtube.com/watch?v=YaZJZ01MKP4
//modified by Gabriel Lucena, 2021
?>
<HTML><TITLE>YourBlinds</TITLE>
<BODY>
<p>What would you like your blinds to do?</a>
<div> 
	<?php
	if(isset($_POST['semiautomatic'])){
		shell_exec("sudo python3 /var/www/html/semiauto_client.py");
	}
	if(isset($_POST['close'])){	
		shell_exec("sudo python3 /var/www/html/close_client.py");
	}
	if(isset($_POST['open'])){	
		shell_exec("sudo python3 /var/www/html/open_client.py");
	}

	?>

	<form method="post">
		<input type="submit" name="semiautomatic" value="Semiautomatic">
		<input type="submit" name="close" value="Close">
		<input type="submit" name="open" value="Open">

	</form>

</div>
<?php
	echo '<a href="?logout">Logout</a>';
?>

</body>

</html>
