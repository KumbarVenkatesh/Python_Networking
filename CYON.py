class Router:
  def __init__(self,name):
    self.name=name
    self.hostname=name
    self.interfaces={}
    self.rip_enabled=False
    self.advertised = []

  def add_interface(self,interface_name,ip_address,subnet_mask):
    self.interfaces[interface_name]={"ip_address":ip_address,"subnet_mask":subnet_mask}

  def enable_rip(self):
    self.rip_enabled = True
    self.calculate_networks()
  
  def calculate_networks(self):
    for interface, details in self.interfaces.items():
      ip_parts = details["ip_address"].split(".")
      subnet_parts = details["subnet_mask"].split(".")
      network = ".".join(str(int(ip_parts[i])&int(subnet_parts[i])) for i in range(4))
      self.advertised_network.append(network)
  def get_config(self):
    return{
    "hostname":self.hostname,
    "interfaces" : self.interfaces,
    "rip_enaabled":self.rip_enabled,
    "advertised":self.advertised
    }

def main():
  routers=[]
  number_routers = int(input("Enter no of routers:"))
  for _ in range(number_routers):
    router_name = input("Enter router name (e.g., R1,R2):")
    router=Router(router_name)
    num_interfaces=int(input(f"Enter no of interfaces for{router_name}:"))
    for _ in range(num_interfaces):
      interface_name = input("Enter interface name(e.g., g0/0,g0/1): ")
      ip_address = input(f"Enter IP address for {interface_name}:")
      subnet_mask = input(f"Enter subnet mask for {interface_name}")
      router.add_interface(interface_name,ip_address,subnet_mask)
    router.enable_rip()
    routers.append(router)
  print("\n Generated RIP Configuration:")
  for router in routers:
    print(router.get_config())

if __name__=="__main__":
  main()

