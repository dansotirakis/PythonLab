import subprocess
import time

directoryRoot = "/home/damianos/Desktop/zallpyCode/"
directoryConfig = "portaloficinas-config/"
directoryEureka = "portaloficinas-eureka/"
directoryGateway = "portaloficinas-gateway/"
directoryApiClient = "portaloficinas-api-client/"
directoryApiAuth = "portaloficinas-api-auth/"
directoryApiEstablishment = "portaloficinas-api-establishment/"
directoryApiPromotion = "portaloficinas-api-promo/"

print("init - Config")
cmd = ['gnome-terminal']
cmd.extend(['-x', 'bash', '-c', (directoryRoot+directoryConfig)+'init-config.sh; exec $SHELL' ])
subprocess.Popen(cmd, stdout=subprocess.PIPE)

time.sleep(15)

print("init - Gatwey")
cmd = ['gnome-terminal']
cmd.extend(['-x', 'bash', '-c', (directoryRoot+directoryGateway)+'init-gateway.sh; exec $SHELL' ])
subprocess.Popen(cmd, stdout=subprocess.PIPE)

print("init - Eureka")
cmd = ['gnome-terminal']
cmd.extend(['-x', 'bash', '-c', (directoryRoot+directoryEureka)+'init-eureka.sh; exec $SHELL' ])
subprocess.Popen(cmd, stdout=subprocess.PIPE)

time.sleep(20)

print("init - API Auth")
cmd = ['gnome-terminal']
cmd.extend(['-x', 'bash', '-c', (directoryRoot+directoryApiAuth)+'init-gateway.sh; exec $SHELL' ])
subprocess.Popen(cmd, stdout=subprocess.PIPE)

print("init - API Client")
cmd = ['gnome-terminal']
cmd.extend(['-x', 'bash', '-c', (directoryRoot+directoryApiClient)+'init-eureka.sh; exec $SHELL' ])
subprocess.Popen(cmd, stdout=subprocess.PIPE)

print("init - API Establishment")
cmd = ['gnome-terminal']
cmd.extend(['-x', 'bash', '-c', (directoryRoot+directoryApiEstablishment)+'init-gateway.sh; exec $SHELL' ])
subprocess.Popen(cmd, stdout=subprocess.PIPE)

print("init - API Promotion")
cmd = ['gnome-terminal']
cmd.extend(['-x', 'bash', '-c', (directoryRoot+directoryApiPromotion)+'init-eureka.sh; exec $SHELL' ])
subprocess.Popen(cmd, stdout=subprocess.PIPE)
