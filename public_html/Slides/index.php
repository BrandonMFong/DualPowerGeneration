<!DOCTYPE html>

<html lang="en">

	<?php 
		global $currpage;
		$currpage = "Slides"; // Include this to distinguish the page for the other php
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
		
		<!-- Web page content -->
		<div class="brand">Your Engineering Solutions</div>

		<div class="container">
			<div class="row">
				<div class="box">
					<div class="col-lg-12 text-center">
                        <style>
                            .google-slides-container{
                            position: relative;
                            width: 100%;
                            padding-top: 60%;
                            overflow: hidden;
                            }

                            .google-slides-container iframe{
                            position: absolute;
                            top: 0;
                            left: 0;
                            width: 100%;
                            height: 100%;
                            }
                        </style>
                        <div class="google-slides-container">
                            <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vTsZOY4Ymq5i6WHE3gdKE4qY3GD5icqJzhoZ6vKLid9XTRLw8E8NLZSsoT_H1-S3TPBHvSDOFRFvNrS/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
                        </div>
					</div>
				</div>
			</div>
		</div>
		
		<?php 
			include '../php/footer.php';
			include '../php/js.php';
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
