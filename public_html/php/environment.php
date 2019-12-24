<?php
    global $css_bootstrap;
    global $css_business_casual;
    global $css_fonts;
    global $js;
	global $servername;
	global $username;
	global $password;
	global $dbname_datacenter;
	global $dbname_member;
    
<<<<<<< HEAD
    if(file_exists('logs/.is_local'))
=======
    if(file_exists('logs/.is_local')) // This is for testing if we are testing locally
>>>>>>> start on bash script to insert data to our remote server
    {
        $css_bootstrap = 'http://localhost/PUBLIC_HTML/css/bootstrap.min.css';
        $css_business_casual = 'http://localhost/PUBLIC_HTML/css/business-casual.css';
        $css_fonts = 'http://localhost/PUBLIC_HTML/font-awesome/css/font-awesome.min.css';
        $js_bootstrap = 'http://localhost/PUBLIC_HTML/js/bootstrap.min.js';
        $js_jquery = 'http://localhost/PUBLIC_HTML/js/jquery.js';
        $servername = "localhost";
        $username = "root";
        $password = "";
        $dbname_datacenter = "dualpower_DataCenter";
        $dbname_membmers = "dualpower_Members";
    }
    else
    {
        $css_bootstrap = 'https://duapowergeneration.sdsu.edu/css/bootstrap.min.css';
        $css_business_casual = 'https://duapowergeneration.sdsu.edu/css/business-casual.css';
        $css_fonts = 'https://duapowergeneration.sdsu.edu/font-awesome/css/font-awesome.min.css';
        $js_bootstrap = 'https://duapowergeneration.sdsu.edu/js/bootstrap.min.js';
        $js_jquery = 'https://duapowergeneration.sdsu.edu/js/jquery.js';
        $servername = "localhost";
        $username = "dualpower_BrandonMFong";
        $password = "dualpower27182";
        $dbname_datacenter = "dualpower_DataCenter";
        $dbname_membmers = "dualpower_Members";
    }
?>