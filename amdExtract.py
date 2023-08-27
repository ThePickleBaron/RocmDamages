# Extract package names from the content using regular expressions
import re

# Regular expression to match package names in the format "Package: package_name"
package_names = re.findall(r'Package: (\w+)', tex_content)

# Generate a bash script to install the packages using apt
bash_script = "#!/bin/bash\n\n# Auto-generated script to install packages\n"
for package in package_names:
    bash_script += f"sudo apt install -y {package}\n"

# Display the first few lines of the generated bash script for preview
bash_script[:500]
# Save the generated bash script to a file for the user to download
bash_script_path = 'install_packages.sh'
with open(bash_script_path, 'w') as file:
    file.write(bash_script)

bash_script_path

#Forgot the links

# Assuming the URLs to .deb files are listed in the format "Filename: url_to_deb_file"
deb_urls = re.findall(r'Filename: (.+\.deb)', tex_content)

# Append the commands to download and install .deb files to the existing bash script
bash_script += "\n# Commands to download and install .deb files\n"
for url in deb_urls:
    # Extract just the filename from the full URL to use with wget and dpkg
    filename = url.split('/')[-1]
    bash_script += f"wget {url}\n"
    bash_script += f"sudo dpkg -i {filename}\n"
    bash_script += f"rm {filename}\n"  # Remove the downloaded .deb file

# Save the updated bash script to a new file
bash_script_with_deb_path = 'install_packages_with_deb.sh'
with open(bash_script_with_deb_path, 'w') as file:
    file.write(bash_script)

bash_script_with_deb_path
