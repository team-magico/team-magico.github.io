# C.A. - Inria - 2022
# Simple possible site generator

from pathlib import Path
import os
import glob

TEMPLATE_DIR = "template"

MENU_CONTENT= '''
	<div id="leftside">
	  <h2 class="hide">Sample menu:</h2>
	  <ul class="avmenu">
            <li><a class="current" href="index.html">Home</a></li>
	    <li><a href="partners.html">Partners</a></li>
	      <!--
		  <li>Menu1</li>
	      <li><a href="Menu2">Menu2</a></li>
	      -->
	     <!-- br -->
	  </ul>
	</div>

        <div id="extras">
          <img src="img/logo-inria.png"  class="center" alt="Inria Logo" />
          <h2>Related links:</h2>
          <ul>
            <li><a href="http://www.inria.fr/">Inria</a></li>
            <li><a href="https://www.iitbhu.ac.in/">IIT (BHU) Varanasi</a></li>
            <li><a href="https://www.iitg.ac.in/">IIT Guwahati</a></li>
          </ul>
        </div>
'''

template_file_list = glob.glob(TEMPLATE_DIR + "/*.template")

for template_file_name in template_file_list:
    with open(template_file_name) as f:
        data = f.read()
    output = data.replace("<@MENU@>", MENU_CONTENT)
    base_name = Path(template_file_name).name
    assert base_name.endswith(".template")
    output_file_name = base_name.replace(".template", "")
    assert output_file_name != base_name
    with open(output_file_name, "w") as f:
        f.write(output)
    print(f"+ generated '{output_file_name}'")

