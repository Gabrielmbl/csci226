<?php 
	//from: https://www.youtube.com/watch?v=YaZJZ01MKP4
	//modified by Gabriel Lucena, 2021
	session_start() 
?>
<!DOCTYPE html>
<html>
<head>
	<title>YourBlinds</title>
</head>
<body>
	<?php
		if(!isset($_SESSION['login'])){ //if my session login doesn't exist, then you include login.php
			include('login.php');
			if(isset($_POST['action']) ){ //if I press return
				
				$login = 'gabriel';
				$password = '12345';
				
				$loginForm = $_POST['login']; //gets the login that I type in my login page
				$passwordForm = $_POST['password']; //gets the password that I type in my password page
				
				if($login == $loginForm && $password == $passwordForm){ //if the they match
					system("cd /var/www/html/ && sudo python3 blinds_server.py"); //start my blinds server
					$_SESSION['login'] = $login; //it means that it logged in
					header('Location: index.php'); //head back here, then it's going to fall into else, which goes to home.php
				}else{
					echo 'Invalid Login or Passowrd.';
				}
			}
		}else{//If there is already a login session, then include home.php
			include('home.php');
			if(isset($_GET['logout'])){ //if I press logout
				unset($_SESSION['login']); //detaches from session login
				session_destroy(); // destroys session
				header('Location: index.php'); //heads back to index.php
			}
		}
	?>
</body>
</html>
