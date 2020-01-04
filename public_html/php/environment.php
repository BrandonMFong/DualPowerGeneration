<?php
    /* ENVIRONMENT */
    // The purpose of this file is mainly to figure environment you are in
    // Whether it be local or on the server
    // This file has all the global variables that makes our site parameterized 
    // Please be cautious when editting this script for it may have big affects on the functionality of 
    // our Dualpowergeneration.sdsu.edu site
    global $css_bootstrap;
    global $css_business_casual;
    global $css_fonts;
    global $js;
	global $servername;
	global $username;
	global $password;
	global $dbname_datacenter;
    global $dbname_member;
    global $page_Home;
    global $page_DataCenter;
    global $currpage;
    
    // Testing what environment you are in
    switch($currpage)
    {
        case "DataCenter": // For the Data center
        {
            $css_bootstrap = '../css/bootstrap.min.css';
            $css_business_casual = '../css/business-casual.css';
            $css_fonts = '../font-awesome/css/font-awesome.min.css';
            $js_bootstrap = '../js/bootstrap.min.js';
            $js_jquery = '../js/jquery.js';
            if(file_exists('../logs/.is_local'))
            {
                $servername = "localhost";
                $username = "root";
                $password = "";
                $dbname_datacenter = "dualpower_DataCenter";
                $dbname_membmers = "dualpower_Members";
                $page_Home = "http://localhost/public_html/";
                $page_DataCenter = "http://localhost/public_html/datacenter/";
                break;
            }
            else 
            {
                $servername = "localhost";
                $username = "dualpower_BrandonMFong";
                $password = "dualpower27182";
                $dbname_datacenter = "dualpower_DataCenter";
                $dbname_membmers = "dualpower_Members";
                $page_Home = "https://dualpowergeneration.sdsu.edu/";
                $page_DataCenter = "https://dualpowergeneration.sdsu.edu/datacenter/";
                break;
            }
        }
        default: // Default is Home Page
        {
            $css_bootstrap = 'css/bootstrap.min.css';
            $css_business_casual = 'css/business-casual.css';
            $css_fonts = 'font-awesome/css/font-awesome.min.css';
            $js_bootstrap = 'js/bootstrap.min.js';
            $js_jquery = 'js/jquery.js';
            if(file_exists('logs/.is_local'))
            {
                $servername = "localhost";
                $username = "root";
                $password = "";
                $dbname_datacenter = "dualpower_DataCenter";
                $dbname_membmers = "dualpower_Members";
                $page_Home = "http://localhost/public_html/";
                $page_DataCenter = "http://localhost/public_html/datacenter/";
                break;
            }
            else 
            {
                $servername = "localhost";
                $username = "dualpower_BrandonMFong";
                $password = "dualpower27182";
                $dbname_datacenter = "dualpower_DataCenter";
                $dbname_membmers = "dualpower_Members";
                $page_Home = "https://dualpowergeneration.sdsu.edu/";
                $page_DataCenter = "https://dualpowergeneration.sdsu.edu/datacenter/";
                break;
            }
        }
    }   
?>