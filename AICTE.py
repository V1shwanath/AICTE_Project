import contextlib
import socket


octal_addresses = []
hex_addresses = []
binary_addresses = []
class IPV4(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        def isIPv4(s):
            try:
                return str(int(s)) == s and 0 <= int(s) <= 255
            except:
                return False

        if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")):
            return "IPv4"

        return "Not a Valid address"

    def IPV4_conversion(self, list1):

        for i in range(len(list1)):

            ba= socket.inet_aton(list1[i]).hex()
            hex_addresses.append(ba)

            ip2bin =  ".".join(map(str,["{0:08b}".format(int(x)) for x in list1[i].split(".")]))
            binary_addresses.append(ip2bin)

            octalIP='.'.join(["%04o" % int(x) for x in list1[i].split('.')])
            octal_addresses.append(octalIP)

    def Text_conversions(self):
        file_path = 'conversions.txt'
        with open(file_path, "w") as o:
            with contextlib.redirect_stdout(o):
                for i in range(len(list1)):
                    print(i,' ',list1[i] , " ",binary_addresses[i],' ',octal_addresses[i],' ',hex_addresses[i])
                
        file1 = open('conversions.txt', 'r')
        count = 0  
        while True:
            count += 1
        
            # Get next line from file
            line = file1.readline()
    
            # if line is empty
            # end of file is reached
            if not line:
                break
            print(list1[i] , " ",binary_addresses[i],' ',octal_addresses[i],' ',hex_addresses[i],"FILE OUTPUT: ","Line{}: {}".format(count, line.strip()))
        
        file1.close()




list1 = []
for i in range(1,11):
    print(i, ' ')
    a = input()
    ob = IPV4()
    print(ob.validIPAddress(a))
    if (ob.validIPAddress(a) != "Not a Valid address"): 
        list1.append(a)
        


obj  = IPV4()
obj.IPV4_conversion(list1)
obj.Text_conversions()



 