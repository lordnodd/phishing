import whois
domain = whois.query('google.com')
print(domain.__dict__)
print(domain.name)
print(domain.expiration_date)

