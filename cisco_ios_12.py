def propagar_vlan_acceso():
  puerto = input("Interface: ")
  puerto = puerto.lower()
  vlan = input("vlan: ")
  file = open("config.txt")
  for i in file:
    i = i.lower()
    if "interface "+puerto in i:
      print(f"""conf t
      interface {puerto}
      switchport mode access
      no switchport mode trunk
      switchport access vlan {vlan}
      no shut
      """)
      file.close()
      break
  else:
    print("puerto no existe")
    file.close()


def propagar_vlan_trunk():
  puerto = input("Interface: ")
  puerto = puerto.lower()
  vlan = input("vlan: ")
  file = open("config.txt")
  for i in file:
    i = i.lower()
    if "interface "+puerto in i:
      print(f"""conf t
      interface {puerto}
      switchport trunk allowed vlan add {vlan}
      no shut
      """)
      file.close()
      break
  else:
    print("puerto no existe")
    file.close()
  

def propagar_vlan():
  try:
    output = ""
    puerto = input(str("interface: "))
    vlan = int(input("Vlan: "))
    puerto = puerto.lower()
    file = open("config.txt")
    for i in file:
      i = i.lower()
      output += i
    file.close()
    #print(output)
    output = output.split("\n")
    #print(output)
    #print(output.index("interface "+puerto))
    #print(output.index("!",8))
    inicio = output.index("interface "+puerto)
    final = output.index("!",inicio)
    output2 = output[inicio:final+1]
    #print(output2)
    for i in output2:
      if "trunk" in i:
        print(f"""conf t
          interface {puerto}
          switchport trunk allowed vlan add {vlan}
          no shut
          end
          """)
        break
    else:
      print(f"""conf t
        interface {puerto}
        switchport mode access
        no switchport mode trunk
        switchport access vlan {vlan}
        no shut
        end
        """)
  except:
    print("puerto o vlan incorrectos")
