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

    with open('dat.txt', 'a+') as f:
        for i in ls:
            new = i.split()
            for w in new: 
                if 'ip4:' in w or 'include:' in w or 'ip6' in w or '\"' in w:
                    f.write(w + ' ')

if __name__ == '__main__':
    lookup()