import requests

#post = requests.post('http://169.60.169.211:3000/api/org.jcsdemo.com.Order', data={'$class': 'org.jcsdemo.com.Owner', 'name': 'distributor1', 'ownerId': 'D1'})

# post = requests.post('http://169.60.169.211:3000/api/org.jcsdemo.com.Owner', data={'$class': 'org.jcsdemo.com.Owner', 'name': 'distributor1', 'ownerId': 'D1'})
# print post
# r = requests.get('http://169.60.169.211:3000/api/org.jcsdemo.com.Owner')

# print r.text

print 'What would you like to do? \n1) PO \n2) ASN \n3) RA \n4) EXIT'

text = raw_input('')
while (text != '4'):
    if text == '1':
        post = requests.post('http://169.60.169.211:3000/api/org.jcsdemo.com.Order', data={
            "$class": "org.jcsdemo.com.Order",
            "orderId": "O-1001",
            "temp": "12",
            "receivedDate": "2018-02-05T17:35:04.565Z",
            "price": 10,
            "exception": 'false',
            "quantity": 100,
            "location": "D-1001",
            "status": "order placed",
            "owner": 'D-1001'
        })

        print post

        post = requests.post('http://169.60.169.211:3000/api/org.jcsdemo.com.retailerPlaceOrder', data={
            "$class": "org.jcsdemo.com.retailerPlaceOrder",
            "order": 'O-1001',
            "owner": 'D-1001'
        })

        print post
    elif text == '2':
        print 2
    elif text == '3':
        post = requests.post('http://169.60.169.211:3000/api/org.jcsdemo.com.shipToRetailer', data = {
            "$class": "org.jcsdemo.com.shipToRetailer",
            "order": 'O-1001',
            "owner": 'R-1001'
        })

        print post
    else:
        print "wrong input"

    print 'What would you like to do? \n1) PO \n2) ASN \n3) RA \n4) EXIT'

    text = raw_input('')


