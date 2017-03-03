import dpkt
import scapy
import sys
import socket

#Code borrowed from 
#https://jon.oberheide.org/blog/2008/10/15/dpkt-tutorial-2-parsing-a-pcap-file/
#http://engineering-notebook.readthedocs.io/en/latest/engineering/dpkt.html
#

pcapfile = open(sys.argv[1], 'rb')
pcap = dpkt.pcap.Reader(pcapfile)

ip_dict = {}

for timestamp, packet in pcap:
    try:
        ethernet = dpkt.ethernet.Ethernet(packet)
    except Exception as e:
        continue

    if ethernet.type == dpkt.ethernet.ETH_TYPE_IP:
        ip = ethernet.data
        if ip.p == dpkt.ip.IP_PROTO_TCP:
            tcp = ip.data

            syn_flag = (tcp.flags & dpkt.tcp.TH_SYN) != 0
            ack_flag = (tcp.flags & dpkt.tcp.TH_ACK) != 0

            if syn_flag:
                if not ack_flag:
                    #SYN sent
                    ip_src_addr = socket.inet_ntoa(ip.src)
                    if ip_src_addr in ip_dict:
                        ip_dict[ip_src_addr][0] += 1.0

                    else:
                        ip_dict[ip_src_addr] = [1.0,0.0]
                else:
                    #SYN ACK received
                    ip_dst_addr = socket.inet_ntoa(ip.dst)
                    if ip_dst_addr in ip_dict:
                        ip_dict[ip_dst_addr][1] += 1.0

                    else:
                        ip_dict[ip_dst_addr] = [0.0,1.0]


pcapfile.close()

for key, value in ip_dict.items():
    #print key, value[0], value[1],
    if value[1] != 0.0:
        #print value[0] / value[1]
        if value[0] / value[1] >= 3.0:
            print key
    else:
        #2 / 0 is still more than 3*0
        if value[0] != 0.0:
            print key

