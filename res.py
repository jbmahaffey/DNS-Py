import dns.resolver

def lookup():
    records = ["_spf.bbnotify.net", "_spf.fortimailcloud.com", "_spf.google.com", "amazonses.com",
                "spf.mailjet.com", "invalidemail.com", "spf.brevo.com"]

    ls = []
    for r in records: 
        res = dns.resolver.resolve(r, 'txt')
        for vl in res:
            l = str(vl).strip('\"v=spf1 ')
            f = l.rstrip('\'lla-')
            s = f.rstrip(" ~")
            p = '\"' + s + ' \"'
            ls.append(p)

    print(ls)

    with open('dat.txt', 'a+') as f:
        for i in ls: 
            f.write(i)


if __name__ == '__main__':
    lookup()