import subprocess
import time

directoryRootDocker = "/home/damianos/Desktop/gitHub/Recursos--SH/initScrips/init-docker.sh"
directoryRoot = "/home/damianos/Desktop/zallpyCode/"
directoryConfig = "portaloficinas-config/"
directoryEureka = "portaloficinas-eureka/"
directoryGateway = "portaloficinas-gateway/"
directoryApiClient = "portaloficinas-api-client/"
directoryApiAuth = "portaloficinas-api-auth/"
directoryCommonObjects = "portaloficinas-common-objects/"
directoryApiEstablishment = "portaloficinas-api-establishment/"
directoryApiPromotion = "portaloficinas-api-promo/"

print("init - Docker")
cmd = ['gnome-terminal']
cmd.extend(['-x', 'bash', '-c', (directoryRootDocker)+'; exec $SHELL' ])
subprocess.Popen(cmd, stdout=subprocess.PIPE)

time.sleep(10)

print("install - Common Objcets")
cmd = ['gnome-terminal']
cmd.extend(['-x', 'bash', '-c', (directoryRoot+directoryCommonObjects)+'install-common-objcets.sh; exec $SHELL' ])
subprocess.Popen(cmd, stdout=subprocess.PIPE)

time.sleep(20)

print("init - Config")
cmd = ['gnome-terminal']
cmd.extend(['-x', 'bash', '-c', (directoryRoot+directoryConfig)+'init-config.sh; exec $SHELL' ])
subprocess.Popen(cmd, stdout=subprocess.PIPE)

time.sleep(20)

print("init - Gatwey")
cmd = ['gnome-terminal']
cmd.extend(['-x', 'bash', '-c', (directoryRoot+directoryGateway)+'init-gateway.sh; exec $SHELL' ])
subprocess.Popen(cmd, stdout=subprocess.PIPE)

print("init - Eureka")
cmd = ['gnome-terminal']
cmd.extend(['-x', 'bash', '-c', (directoryRoot+directoryEureka)+'init-eureka.sh; exec $SHELL' ])
subprocess.Popen(cmd, stdout=subprocess.PIPE)

time.sleep(25)

print("init - API Auth")
cmd = ['gnome-terminal']
cmd.extend(['-x', 'bash', '-c', (directoryRoot+directoryApiAuth)+'init-api-auth.sh; exec $SHELL' ])
subprocess.Popen(cmd, stdout=subprocess.PIPE)

print("init - API Client")
cmd = ['gnome-terminal']
cmd.extend(['-x', 'bash', '-c', (directoryRoot+directoryApiClient)+'init-api-client.sh; exec $SHELL' ])
subprocess.Popen(cmd, stdout=subprocess.PIPE)

print("init - API Establishment")
cmd = ['gnome-terminal']
cmd.extend(['-x', 'bash', '-c', (directoryRoot+directoryApiEstablishment)+'init-api-establishment.sh; exec $SHELL' ])
subprocess.Popen(cmd, stdout=subprocess.PIPE)

print("init - API Promotion")
cmd = ['gnome-terminal']
cmd.extend(['-x', 'bash', '-c', (directoryRoot+directoryApiPromotion)+'init-api-promotion.sh; exec $SHELL' ])
subprocess.Popen(cmd, stdout=subprocess.PIPE)
