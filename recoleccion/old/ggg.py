import dns.resolver

myResolver = dns.resolver.Resolver()
myResolver.nameservers = ['8.8.8.8', '8.8.4.4']

try:
    myAnswers = myResolver.query("mikatom.es", "A")
    for rdata in myAnswers:
        print(rdata)
except:
    print("Query failed")


try:
    ip = "8.8.8.8"
    req = '.'.join(reversed(ip.split("."))) + ".in-addr.arpa"
    myAnswers = myResolver.query(req, "PTR")
    for rdata in myAnswers:
        print(rdata)
except:
    print("Query failed")