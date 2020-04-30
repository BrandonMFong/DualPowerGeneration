<!DOCTYPE html>

<html lang="en">

	<?php 
		global $currpage;
		$currpage = "Home"; // Include this to distinguish the page for the other php
		include 'php/header.php';
		include 'php/sidenav.php'; 
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
		
		<!-- Web page content -->
		<div class="brand">Your Engineering Solutions</div>

		<div class="container">
			<div class="row">
				<div class="box">
					<div class="col-lg-12 text-center">
						<style>
							.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } 
							.embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }
						</style>
						<div class='embed-container'>
							<iframe src='https://www.youtube.com/embed/BoU5vMe_PXg' frameborder='0' allowfullscreen></iframe>
						</div>
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
		<!-- <script type="text/javascript">
			function resizeIframe(iframe) 
			{
				iframe.height = iframe.contentWindow.document.body.scrollHeight + "px";
			}
		</script>  -->
	</body>
</html>
