from scapy.all import sniff

packets = sniff(count=5)
# packets.summary()
packet = packets[0]
packet.show()