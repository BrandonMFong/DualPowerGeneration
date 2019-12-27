<!DOCTYPE html>
<html lang="en">

<?php 
	$currpage = "Data Center"; // Include this to distinguish the page for the other php
	include '../php/header.php'; 
	include '../php/sidenav.php'; 
?>

<body>
	<!-- Animated Icon -->
	<div id="main">
	<!-- Side menu button -->
	<hamburger>
		<div class="container_for_menu" onclick="myFunction(this)">
		  <div class="bar1"></div>
		  <div class="bar2"></div>
		  <div class="bar3"></div>
		</div>
	</hamburger>
	
	
	<div class="brand">Data Center</div>
	<!--https://www.youtube.com/watch?v=ka5m_kvQUFo-->
	<div class="container">
		<div class="row">
			<div class="box">
				<div class="col-lg-12 text-center">
					
					<?php 
						include '../php/data.php';
					?>

				</div>
			</div>
		</div>
	</div>



	<?php 
		//global $page;
		//$page = "Data Center"; 
		include '../php/footer.php';
		include '../php/js.php';
	?>
	
	</div>
</body>
</html>