import requests

post = requests.post('http://169.60.169.211:3000/api/org.jcsdemo.com.Owner', data={'$class': 'org.jcsdemo.com.Owner', 'name': 'distributor1', 'ownerId': 'D1'})
print post
r = requests.get('http://169.60.169.211:3000/api/org.jcsdemo.com.Owner')

print r.text