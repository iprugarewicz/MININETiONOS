import controller as c

run = True
n = 10
while run:
    print("This program configures connection in ONOS controller between pairs of hosts")
    configuring = True
    h1 = None
    h2 = None
    bw = None
    controller = c.controller("temp", "sweden_map", "192.168.0.29")
    while configuring:
        print("what is host1")
        h1_chosen = False
        #w linijce poniżej należy uzupełnić argumenty- po kolei: nazwa pliku json bez rozszerzenia, nazwa pliku csv bez rozszerzenia, IP ONOS-a

        while not h1_chosen:
            try:
                h1 = int(input())
                if h1 > n or h1 < 1:
                    raise TypeError
                print("first host =", h1)
                h1_chosen = True
            except ValueError:
                print("type host ID")
            except TypeError:
                print("there's only ", n, "hosts, type correct ID")

        print("what is host2")
        h2_chosen = False
        while not h2_chosen:
            try:
                h2 = int(input())
                if h2 > n or h2 < 1:
                    raise TypeError
                elif h1 == h2:
                    raise EnvironmentError

                print("first host =", h1)
                h2_chosen = True
            except ValueError:
                print("type host ID")
            except TypeError:
                print("there's only ", n, "hosts, type correct ID")
            except EnvironmentError:
                print("host2 can't be equal to host1")

        bw_chosen = False
        print("how much bandwidth do you need?")
        while not bw_chosen:
            try:
                bw = int(input())
                if bw <= 0:
                    raise TypeError
                bw_chosen = True
            except ValueError:
                print("type number")

        controller.generate_flows(h1, h2, bw)

        print("Would you like to configure another connection or send flows to the server? ")
        temp = None
        while temp not in ["Config", "Send"]:
            print("(Config/Send)")
            temp = input()
            if temp == 'Send':
                controller.send()
                configuring = False
            elif temp == "Config":
                continue

    print('____________')
