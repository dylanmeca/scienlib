import os
import sys
import time
import nmap
import urllib.request
import json
import requests

init(autoreset=True)

class scanner:

    def ___init__(self):
        return

    def scanports(self, ip):
        self.ip = ip
        nm = nmap.PortScanner()
        ports_open = "-p "
        results = nm.scan(ip, arguments="--top-ports 1000 -sT -n -Pn -T4")
        count = 0
        #print (results)
        return "\nHost : %s" % ip)
        return "State : %s" % nm[ip].state())
        for proto in nm[ip].all_protocols():
            print("Protocol : %s" % proto)
            print()
            lport = nm[ip][proto].keys()
            sorted(lport)
            for port in lport:
                print("port : %s\tstate : %s" %
                      (port, nm[ip][proto][port]["state"]))
                if count == 0:
                    ports_open = ports_open+str(port)
                    count = 1
                else:
                    ports_open = ports_open+","+str(port)

        return ports_open + " "+str(ip)

    def scanport(self, ip, port):
        self.ip = ip
        self.port = port
        nm = nmap.PortScanner()
        nm.scan(ip, port, arguments='-sV --version-intensity 3')
        return "Command executed: {}".format(nm.command_line())
        return "Protocols used: {}".format(nm[ip].all_protocols())
        return "Machine status: {}".format(nm[ip].state())

        for ports in nm[ip]['tcp'].keys():
            for data in nm[ip]['tcp'][ports]:
                return data + " : " + nm[ip]['tcp'][ports][data]

    def scanip(self, ip):
        self.ip = ip
        url = 'https://ipinfo.io/'+ip+'/json'
        openurl = urllib.request.urlopen(url)
        loadurl = json.load(openurl)

        for i in loadurl:
            return i + " : " + loadurl[i]

    def scanweb (self,link):
               try:
                  self.link = link
                  target = requests.get(url=link)
                  header = dict(target.headers)
                  for x in header:
                       print (x+ " : "+header[x])
                 
               except:
                  return "Error, could not connect to server"
 