import ipaddress

while True:
    ip=input ("enter ip address: ")
    mask=input ("Enter network mask: ")
    ipm=ip + "/" + mask

    hostid = ip[-3:]                                #gets the host id
    hostid = hostid.replace(".", "")                #takes the potential "." out of host id
    net1 = ipaddress.ip_interface(ipm)             #first possible host (host1.network)
    subs = ipaddress.ip_network(net1.network)      #Subnet Number of Hosts (net4.num_addresses)
    floor = int(hostid) / int(subs.num_addresses)   #a number to calculate other things, have to turn them both to integrers
    netid = round(floor) * subs.num_addresses       #calculates the network id
    broadid = netid + (subs.num_addresses - 1)      #calculates broadcast id
    host1 = netid + 1                               #calculates the first usable host
    host2 = broadid - 1                             #calculates the last usable host

    print("The network id is:",net1.network)
    #print("The number of subnet hosts is:",subs.num_addresses)
    #print("The network id is:",netid)
    print("The broadcast id is:",broadid)
    print("The first usable host is:",host1)
    print("The last usable host is:",host2)
    
    while True:
        answer = input('Run again? (y/n): ')
        if answer in ('y', 'n'):
            break
        print ('Invalid input.')
    if answer == 'y':
        continue
    else:
        print ('Goodbye')
        break