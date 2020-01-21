import nmap
import pysnmp

#initalizing our scanner
nmScan = nmap.PortScanner()

#an array, should contain CM ips from an edgehealth server
ipAddress = ['192.168.0.1']

#a dictionary, containing the list of all BCM servers
bcmServerPorts = {7547:'tr-069 service'}
for address in ipAddress:
    nmScan.scan(address, '2-65535')    
    print('Scanned ip address', address)
    print('\nPorts open to TCP')
    #scans for open tcp ports
    for port in nmScan[address]['tcp'].keys():
        if port in bcmServerPorts:
            server = bcmServerPorts[port]
            print('Port : ', port, ' (', server, ')')
        else:
            print('Port : ', port)    
