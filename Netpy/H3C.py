import re

text = """<Huawei>dis mac-address vlan 1
MAC address table of slot 0:
-------------------------------------------------------------------------------
MAC Address    VLAN/       PEVLAN CEVLAN Port            Type      LSP/LSR-ID  
               VSI/SI    MAC-Tunnel  
-------------------------------------------------------------------------------
4c1f-cc54-d69d 1           -      -      GE0/0/1         dynamic   0/-         
4c1f-cc54-559d 1           -      -      TE0/0/4         dynamic   0/-    
-------------------------------------------------------------------------------
Total matching items on slot 0 displayed = 1 

<Huawei>""".splitlines()

regex = r'[0-9a-fA-F]+''-''[0-9a-fA-F]+''-''[0-9a-fA-F]+'

for line in text:
    if re.match(regex, line):
        mac = line[:14]
        int = line[41:48]
        print 'Interface {} has an incoming mac addresss {}'.format(int, mac)


