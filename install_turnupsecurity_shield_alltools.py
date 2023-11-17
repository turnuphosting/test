#!/usr/bin/env python

import subprocess

# Install ConfigServer Security Firewall
subprocess.run(["wget", "https://download.configserver.com/csf.tgz"])
subprocess.run(["tar", "-xzf", "csf.tgz"])
subprocess.run(["cd", "csf"])
subprocess.run(["sh", "install.sh"])

# Install Rootkit Hunter
subprocess.run(["yum", "update"])
subprocess.run(["yum", "install", "-y" "rkhunter"])

# Install ModSecurity
subprocess.run(["yum", "install", "-y", "libapache2-mod-security2"])

# Install ClamAV
subprocess.run(["yum", "install", "-y", "clamav"])

# Install Wordfence CLI
subprocess.run(["wget", "https://github.com/turnuphosting/wordfence-cli/releases/download/download/wp-cli-2.9.0.phar"])
subprocess.run(["chmod", "+x", "wp-cli.phar"])
subprocess.run(["mv", "wp-cli.phar", "/usr/local/bin/wp"])

# Install Recaptcha v2 server-wide
subprocess.run(["cd", "/"])
subprocess.run(["cd", "/usr/local/src"])
subprocess.run(["wget", "-O", "reCaptcha2_validation-free.tar.gz", "https://github.com/turnuphosting/reCaptcha2_validation-free/archive/master.tar.gz"])
subprocess.run(["tar", "-zxvf", "reCaptcha2_validation-free.tar.gz"])
subprocess.run(["cd", "reCaptcha2_validation-free-master/install/"])
subprocess.run(["./install.sh"])

#Cleaning up Recaptcha v2 server-wide after installation
subprocess.run(["cd", "/"])
subprocess.run(["cd", "/usr/local/src"])
subprocess.run(["rm", "-rf", "reCaptcha2_validation*"])
subprocess.run(["rm", "-rf", "/var/www/html/reCaptcha2_validation-free.tar.gz"])

# Congratulations and Welcome Message From TurnUpSecurity Shield
subprocess.run(["echo", "Congratulations TurnUpSecurity Shield Tools have been successfully installed for your server."])
subprocess.run(["graph", "Welcome To TurnUpSecurity Shield"])

  



  

