from bs4 import BeautifulSoup
import requests
import re
from azcrawler import agent 
sample="""

	<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml";>
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
	<meta name="KEYWORDS" content="air cargo, aircargo, air freight, airfreight, aviation, logistics, transportation, 
	airline, airport, freight forwarder, cargo agent, GSA, general sales agent, cargo handling agent, cargo handler, courier, express operator, charter broker, cargo broker, freighter aircraft,
	air cargo news, air freight news, aircargo news, airfreight news">
	<meta name="description" content="azfreight.com is a global news and information website for the international airfreight and aircargo industry">
	<script type="text/javascript">
	 if(top.location != window.location) {
	 window.parent.location = 'http://www.azfreight.com'; } 
	 </script> 
    <title>azFreight.com | azFreight.com | Directory and Tools</title>
	<script type="text/javascript" src="http://www.dakic-ia-300.com/js/43706.js"></script>
	<noscript><img src="http://www.dakic-ia-300.com/43706.png" style="display:none;" /></noscript>

    <base href="http://www.azfreight.com" />
        <script type="text/javascript">


</script>     
	<link href='https://fonts.googleapis.com/css?family=Open+Sans:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
    <link href="styles/main.css" rel="stylesheet" type="text/css" />
    <link href="styles/wrapper.css" rel="stylesheet" type="text/css" />
	<link href="styles/new_style.css" rel="stylesheet" type="text/css" />
    <script src="javascript/lib/prototype.js" type="text/javascript"></script>
    <script src="javascript/src/scriptaculous.js" type="text/javascript"></script>
    <script src="javascript/az.js" type="text/javascript"></script>
    <script src="http://www.azfreight.com/ox/www/delivery/spcjs.php?id=4" type="text/javascript"></script> 
	
  <link href="styles/channel_directory.css" rel="stylesheet" type="text/css" />
<!--- <link href="styles/new_style.css" rel="stylesheet" type="text/css" /> --->



</head>

<body>

	<div class="wrapper">

		<div class="wrapper_band"></div>
	<div class="header">
        	<a href="http://www.azfreight.com" class="logo">
            	<img src="new_images/az_logo.jpg" alt="AZFreight.com" />
            </a>
			<div id="sponsor" style="margin-top:10px !important" >    <script type="text/javascript"><!--- // <![CDATA[
    OA_show(22);
    // ]]>- ---></script>
    <noscript><a target="_blank" href="ox/www/delivery/ck.php?n=93d9f52"><img border="0" alt="" src="ox/www/delivery/avw.php?zoneid=22&amp;n=93d9f52" /></a></noscript>
    </div>		<ul class="nav_top">	
			<li class="nav_top_item nav_top_item1"><a target="_top" href="home.html">HOME</a></li>
			<!--- <li class="nav_top_item"><a target="_top" href="">NEWS</a></li>--->
			<li class="nav_top_item nav_top_active"><a target="_top" href="directory_and_tools.html"><b>AZ</b>FREIGHT DIRECTORY</a></li>
			<li class="nav_top_item"><a target="_top" href="events.html">EVENTS</a></li>
			<li class="nav_top_item"><a target="_top" href="contact_us.html">CONTACT</a></li>
			<li class="nav_top_item"><a target="_blank" href="http://www.aircargoweek.com"><img border="0" style="padding-top: 18px;" src="images/acwlogo_vsmall.jpg"></a></li>
			<li class="nav_top_item"><a target="_blank" href="http://www.azuraproductions.com"><img border="0" style="padding-top: 13px;" src="images/azplogo_vsmall.jpg"></a></li>

            <li class="nav_top_item nav_top_search"><form onsubmit="if($('site_search').value == 'Search the site...') return false; $('criteria').value = $('site_search').value; $('site_search').value='Searching...  Please wait.';" action="/site_search_results.htm" method="get" target="_top"><input type="hidden" id="criteria" name="criteria" />
                    <input type="text" id="site_search" title="Site Search" alt="Site Search" value="Search the site..." onFocus="clearValue('site_search', 'Search the site...');" onBlur="checkEmptyValue('site_search', 'Search the site...');" />
                    <input type="image" id="site_search_btn" src="new_images/site_search_btn.gif" width="30" height="20" style="cursor: pointer; border: 0; padding: 0;" />
                </form></li>
		</ul> 
 </div>        <div class="content">
					
        	<div class="content_left">
				<div class="featured_news">
                <div class="banner_468">
                         <script type="text/javascript"><!--- // <![CDATA[
    OA_show(54);
    // ]]>- ---></script>
    <noscript><a target="_blank" href="ox/www/delivery/ck.php?n=a707ab2"><img border="0" alt="" src="ox/www/delivery/avw.php?zoneid=54&amp;n=a707ab2" /></a></noscript>
                    </div><!-- banner_468 -->
                    <h2 class="green_header">Company listing</h2>
					 <div class="green_header_base"></div>
					
												<div class="featured_news_wrap">
					
						<div style="clear: both; _margin-top: 30px;"></div>
						<div style="width: 300px; float: left; display: inline-block; margin-top: 10px;">
						</div>
				
						<div class="office_directory">
							<ul>
																<li class="branch_unselected">Branch Office</li>
								<li class="headoffice_selected">Head Office</li>
								<li class="global_unselected">Global Head Office</li>
															</ul>
																					<!-- < php if($fedagsa==1){?><div style="line-height: 20px;"><a href="http://www.fedagsa.aero" target="_blank"><img src="images/fedagsa3.jpg" alt="FEDAGSA" title="FEDAGSA" align="absmiddle" border="0"/></a>&nbsp;Member</div>< php }?> -->
							
						</div><!-- end of office directory -->

						<div style="clear: left;"></div>
					
						<div class="listing_info">
							 
								<h2>A-Sonic Logistics (Thailand) Co Ltd</h2>
								<p>Cargo Agents/Freight Forwarders, Thailand</p>
													
														
							
														<div class="listing_info_box">
								<!-- <h3>address</h3> -->
								<ul>
									<li><strong>Bangkok</strong></li>
									<li>3241 Rama 4 Road</li>																		<li>Room 504 5th Floor</li>									<li>Boss Tower Building</li>									<li>Klongton, Klongtoey</li>									<li>Bangkok</li>									<li>10110</li>								</ul>
							</div>
													
							<!--- < php if(strlen($companydetails_row['telno']) + strlen($companydetails_row['add1']) + strlen($companydetails_row['add2']) + strlen($companydetails_row['add3']) + strlen($companydetails_row['add4']) + strlen($companydetails_row['add5']) + strlen($companydetails_row['add6']) + strlen($companydetails_row['telno']) + strlen($companydetails_row['email']) + strlen($companydetails_row['www_site']) + strlen($companydetails_row['telex']) + strlen($companydetails_row['skype']) + strlen($companydetails_row['mobile']) + strlen($companydetails_row['fax']) + strlen($companydetails_row['sita']) + strlen($companydetails_row['aftn'])>1)
							{ --->
														
							<div class="listing_info_box">
								<!-- <h3>contact</h3> -->
								<ul>
																	<li>Tel: +66 (0)2 260 6414</li>
																
																	
									  <li>Tel: +66 (0)2 260 6415 (Customer Service)</li>
																
																	
									  <li>Tel: +66 (0)2 260 6416/7 (Customer Service)</li>
																	
								<li>Fax: +66 (0)2 260-6418</li>								
								
								 <li>Email: enquiry@asonic-logisticsolutions.com</li>							   
							   
							   
								 <li>Website: www.asonic-logistics.com</li>							   
							   
							   
								 							   
							   
							   
								
																</ul>
					
							<!--- line below included  && $listtypenow != 'W' --->
								
																
								
								
								</p>
							</div><!-- listing info_box -->
						</div><!-- end of free listing_info -->
					</div><!-- end of featured_news_wrap -->
				</div><!-- featured_news -->

			</div><!-- content_left -->

            <div class="content_right">
				                <div class="quick_links">
                	<h2 class="green_header">AZfreight Directory section index</h2>
					 <div class="green_header_base"></div>
                    <ul>
						<li><a href="directory_and_tools.html">AZfreight Directory</a></li>
						<li><a href="search_personnel.html">Personnel Search</a></li>
						<li><a href="add_1.html"><strong>Add a Listing </strong></a><span style="background-color: rgb(121,177,154); color:#ffffff; padding: 2px 5px 2px 5px;"><B>FREE</b></span></li>
						<li><a href="directory_login.html">Edit Company Listing</a></li>
						<li><a href="track_and_trace.html">Track and Trace</a></li>
						<li><a href="airport_names_codes_results.html">Airport names/codes</a></li>
						<li><a href="airline_names_codes_results.html">Airline names/codes</a></li>
						<li><a href="country_codes_time_zones_results.html">Country codes/times</a></li>
						<li><a href="glossary.html">Glossary of Terms</a></li>
						<li><a href="resources_widgets.html">Widgets <span style="font-family:arial;">&amp;</span> Resources</a></li>
						<li><a href="advertisers.html">Featured Companies</a></li>
						<li><a href="get_featured.html">Get Featured!</a></li>
						<li><a href="datadirect.html">Buy our Data</a></li>
                    </ul>
                </div><!-- quick_links -->
<!--- was 	<li><a href="airline_names_codes_results.html">Airline names <span style="font-family:arial;">&amp;</span> codes</a></li> --->
				
				
				                <div class="quick_links">
                 	<h2 class="green_header">Featured Companies</h2>
					 <div class="green_header_base"></div>
					<div class="featured_companies" style="overflow: hidden;">
						<table>
													<tr>
														<td><a href="listing.html?id=c_37236">
							<img src="directory/logos/92A86319-5056-0102-EEF281B9BEC6F496.jpg" alt="Pt.trans Pratama Logistics" title="Pt.trans Pratama Logistics" class="featured_mini_logo" width="100px"/></a></td>
							<td><a href="listing.html?id=c_37236">Pt.trans Pratama Logistics</a></td>
														</tr>
							<tr><td colspan="2" class="light_divider" style="padding: 3px 0 3px 0;"></td></tr>
													<tr>
														<td><a href="listing.html?id=c_29521">
							<img src="directory/logos/D58A0FDA-5056-0102-EE437955E4F94E19.jpg" alt="Asia Grace International Logistics (Shanghai) Co Ltd" title="Asia Grace International Logistics (Shanghai) Co Ltd" class="featured_mini_logo" width="60px"/></a></td>
							<td><a href="listing.html?id=c_29521">Asia Grace International Logistics (Shanghai) Co Ltd</a></td>
														</tr>
							<tr><td colspan="2" class="light_divider" style="padding: 3px 0 3px 0;"></td></tr>
													<tr>
														<td><a href="listing.html?id=c_25437">
							<img src="directory/logos/4E3A1C6A-5056-0102-EE9210373FEC962B.jpg" alt="American Export Lines" title="American Export Lines" class="featured_mini_logo" width="100px"/></a></td>
							<td><a href="listing.html?id=c_25437">American Export Lines</a></td>
														</tr>
							<tr><td colspan="2" class="light_divider" style="padding: 3px 0 3px 0;"></td></tr>
													<tr>
														<td><a href="listing.html?id=c_33092">
							<img src="directory/logos/D201AE68-5056-0102-EEBE1C40B4519826.jpg" alt="Blackthorne International Transport GmbH" title="Blackthorne International Transport GmbH" class="featured_mini_logo" width="100px"/></a></td>
							<td><a href="listing.html?id=c_33092">Blackthorne International Transport GmbH</a></td>
														</tr>
							<tr><td colspan="2" class="light_divider" style="padding: 3px 0 3px 0;"></td></tr>
													<tr>
														<td><a href="listing.html?id=c_35013">
							<img src="directory/logos/D496E0B5-5056-0102-EE8AFFF0524B5A60.jpg" alt="NGL- Noble Global Logistics Services " title="NGL- Noble Global Logistics Services " class="featured_mini_logo" width="50px"/></a></td>
							<td><a href="listing.html?id=c_35013">NGL- Noble Global Logistics Services </a></td>
														</tr>
							<tr><td colspan="2" class="light_divider" style="padding: 3px 0 3px 0;"></td></tr>
												</table>
						<div style="clear:both;"></div>
						<a class="box_base_link" href="get_featured.html">Get Featured!</a>
    
					</div>
            
					<div style="clear: both;"></div>
                </div><!-- quick_links -->
				
				
				

			</div><!-- content_right -->

							
							
							
								
        </div><!-- content -->
        
	        <div style="clear: both;"></div>
		<div class="footer">
        	<a href="http://www.azurainternational.com" class="az_group"><img src="new_images/footer_azura.gif" alt="The A-Z Group Ltd trading as AZura International" /></a>
            <!--- <a href="rss_feeds.html" class="rss_wrap"><img src="new_images/icon_rss.gif" alt="RSS Icon" /><span>RSS Feed</span></a> --->
            <div class="footer_wrap">
                <ul class="footer_last">
                    <!--- <li><a href="sign_in.html">Log In / Register</a></li>--->
                    <li><a href="contact_us.html">Contact us</a></li>
                    <li><a href="products.html">Our Products</a></li>
                    <li><a href="subscribe.html">Subscribe</a></li>
					<li><a href="datadirect.html">Buy our data</a></li>
                </ul>
                <ul>
                    <!--- <li><a href="profile.html">My Profile</a></li> --->
                    <!-- <li><a href="careers.html">Careers and Training</a></li>-->
                    <!--- <li><a href="subscribe.html">Subscribe</a></li> --->
                </ul>
                <ul>
                    <li><a href="events.html">Industry Events</a></li>
                    <li><a href="tandc.html">Terms of use</a></li>
					<li><a href="privacypolicy.html">Privacy Policy</a></li>
                </ul>
                <ul>
                    <li><a href="home.html">Home</a></li>
                    <li><a href="directory_and_tools.html">AZfreight Directory</a></li>
                    <li><a href="add_1.html">Add a Directory Listing</a></li>
                    <li><a href="get_featured.html">Get Featured!</a></li>
                </ul>
            </div><!-- footer_wrap -->
            <div style="clear: both;"></div>
       </div><!-- footer -->
    </div><!-- wrapper -->
     <div class="footer_band"></div>

		
<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-16212653-3']);  
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>
    </div><!-- wrapper -->


</body>
</html>

"""


soup=BeautifulSoup(sample,'html.parser')

print (soup.find('div',class_='listing_info').find('h2').get_text())
listing_boxes= (soup.find('div',class_='listing_info').find_all('div',class_='listing_info_box'))

# if len(listing_boxes)>1:
# 	print (listing_boxes[0])
# 	print (listing_boxes[1])

print (soup.find('div',class_='listing_info').find('li').get_text())

elements=soup.find_all('li')
for ele in elements:
	print (ele.get_text())
	tel= re.compile(u'Tel: ([1-9\+\(\)\s]+)').findall(ele.get_text())
		# print ('chosen!%s'%ele)
	if tel is not None:
		print ('got tel!%s'%tel)