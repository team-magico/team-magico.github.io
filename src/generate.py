# C.A. - Inria - 2022
# Simple site generator

from pathlib import Path
import os
import glob

TEMPLATE_DIR = "template"

'''
            <li><a class="current" href="index.html">Home</a></li>
	    <li><a href="partners.html">Partners</a></li>
	      <!--
		  <li>Menu1</li>
	      <li><a href="Menu2">Menu2</a></li>
	      -->
	     <!-- br -->
'''

MENU_CONTENT_HEADER = '''
	<div id="leftside">
	  <h2 class="hide">Sample menu:</h2>
	  <ul class="avmenu">
'''
MENU_CONTENT_FOOTER = '''             
	  </ul>
	</div>

        <div id="extras">
          <img src="img/logo-inria.png"  class="center" alt="Inria Logo" />
          <img src="https://www.iitbhu.ac.in/contents/iitbhu/img/other/emblem.jpg"  class="center" alt="IIT(BHU) Varanasi Logo" width="100%" />
          <img src="https://www.iitg.ac.in/core/img/iitglogo.jpg"  class="center" alt="IIT Guwahati Logo" width="100%" />
          <h2>Related links:</h2>
          <ul>
            <li><a href="http://www.inria.fr/">Inria</a></li>
            <li><a href="https://www.iitbhu.ac.in/">IIT (BHU) Varanasi</a></li>
            <li><a href="https://www.iitg.ac.in/">IIT Guwahati</a></li>
          </ul>
        </div>
'''


FOOTER = '''
<div id="footer">
  <p><span>&copy; 2022 <a href="#">Inria, IIT(BHU) Varanasi, IIT Guwahati</a></span><br />
    <!-- img src="img/logo-inria.png" height="40" width="100" class="center" alt="Example content image" / -->
    <span style="font-size: 10%;"> <a href="http://andreasviklund.com/templates/" title="Original CSS template design">Original design</a> by <a href="http://andreasviklund.com/" title="Andreas Viklund">Andreas Viklund</a> | Modified by <a href="http://Jasoncole.ca">Jason Cole</a> | Modified by <a href="http://fr.viadeo.com/fr/profile/hana.baccouch">Hana Baccouch</a> and C. Adjih </span></p>
</div>
'''

#template_file_list = glob.glob(TEMPLATE_DIR + "/*.template")

file_list = [
    ("index.html", "Home"),
    ("partners.html", "Partners"),
    ("publications.html", "Publications"),    
    ("contact.html", "Contact")
]


#for template_file_name in template_file_list:
for (file_name, page_name) in file_list:
    template_file_name = f"template/{file_name}.template"
    with open(template_file_name) as f:
        data = f.read()
    #base_name = Path(template_file_name).name    
    #assert base_name.endswith(".template")
    #output_file_name = base_name.replace(".template", "")
    output_file_name = file_name

    menu = MENU_CONTENT_HEADER
    for other_file_name, other_page_name in file_list:
        if other_file_name == file_name:
            menu += f'''<li><a class="current" href="{other_file_name}">{other_page_name}</a></li>''' + "\n"
        else:
            menu += f'''<li><a href="{other_file_name}">{other_page_name}</a></li>''' + "\n"
    menu += MENU_CONTENT_FOOTER

    output = data.replace("<@MENU@>", menu)
    output = output.replace("<@FOOTER@>", FOOTER)
    
    #assert output_file_name != base_name
    assert output_file_name != template_file_name    
    with open(output_file_name, "w") as f:
        f.write(output)
    print(f"+ generated '{output_file_name}'")

