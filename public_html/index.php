<!DOCTYPE html>

<html lang="en">

<?php include 'php/header.php'; ?>

<!-- https://www.w3schools.com/howto/default.asp -->
<!-- https://www.tutorialrepublic.com/php-tutorial/php-mysql-login-system.php-->

<div id="mySidenav" class="sidenav">
  <a href="https://dualpowergeneration.sdsu.edu/">Home</a>
  <a href="https://github.com/BrandonMFong/DualPowerGeneration">Open Source</a>
  <a href="https://www.gofundme.com/f/senior-design-project-renewable-energy?utm_medium=email&utm_source=product&utm_campaign=p_email%2B5311-donation-receipt-wp-v5&utm_content=internal">GoFundMe</a>
  <a href="https://dualpowergeneration.sdsu.edu/datacenter">Data Center</a>
  <a href="pages/Slides.html">Slides</a>
  <!--<a href="javascript:void(0)" class="closebtn" onclick="closeNav()"></a>-->
</div>

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
	
	<!-- Web page content -->
	<div class="brand">Your Engineering Solutions</div>

	<div class="container">
		<div class="row">
			<div class="box">
				<div class="col-lg-12 text-center">
					<img style="padding: 10px" alt="" class="img-responsive img-full" src="img/DP_Group.jpg" />
					<img style="padding: 10px" alt="" class="img-responsive img-full" src="img/dp_group_photo.jpg" />
					<h2 class="brand-before"><small>Welcome to</small></h2>
					<h1 class="brand-name">Your Engineering Solutions</h1>

					<hr class="tagline-divider" />
					<h2><small><strong>Dual Power Generation</strong></small></h2>
					<div class="tab">
						<button class="tablink" onclick="openPage('Home', this, '')"><div class="btntxt">Home</div></button>
						<button class="tablink" onclick="openPage('Members', this, '')"><div class="btntxt">Members</div></button>
						<button class="tablink" onclick="openPage('Diagrams', this, '')"><div class="btntxt">Diagrams</div></button>
					</div>
				</div>
			</div>
		</div>
	</div>
	
	<div id="Diagrams" class="tabcontent">
		<div class="container">
			<div class="row">
				<div class="box">
					<div class="col-lg-12 text-center">
						<h2><small><strong>DC To AC Converter</strong></small></h2>
						<img  class="img-responsive img-full"  src="/img/DCAC_Converter.PNG" alt="ACDC Converter"/>
						
						<h2><small><strong>DC To DC Converter</strong></small></h2>
						<img  class="img-responsive img-full"  src="/img/DCDC_Converter.PNG" alt="DCDC Converter"/>
						
						<h2><small><strong>Max Power Tracker</strong></small></h2>
						<img  class="img-responsive img-full"  src="/img/Max_Pwr_Tracker_Coding_Diagram.PNG" alt="Max Power Tracker"/>
						
						<h2><small><strong>Solar Panel Manuevering</strong></small></h2>
						<img  class="img-responsive img-full"  src="/img/Solar_Panel_Coding_Diagram.PNG" alt="Solar Panel Manuevering"/>
						
					</div>
				</div>
			</div>
		</div>
	</div>
	
	<?php 
		include 'php/member.php';
		include 'php/abstract.php';
		include 'php/footer.php';
		include 'php/js.php';
	?>
	</div>
</body>
</html>
