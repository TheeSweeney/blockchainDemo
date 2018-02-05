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
        print 'Who would you like to ship to: \n1) Distributor \n2) Retailer'
        asn = raw_input('')
        if asn == '1' :
            post = requests.post('http://169.60.169.211:3000/api/org.jcsdemo.com.inTransitToDistributor', data = {
                "$class": "org.jcsdemo.com.inTransitToDistributor",
                "order": "O-1001",
                "temp": "30",
                "location": "T-1001",
                "exception": "False",
                "status": "in transit"
            })
            print post
        if asn == '2' :
            post = requests.post('http://169.60.169.211:3000/api/org.jcsdemo.com.inTransitToRetailer', data = {
                "$class": "org.jcsdemo.com.inTransitToRetailer",
                "order": "O-1001",
                "temp": "35",
                "location": "T-1002",
                "exception": "True",
                "status": "in transit"
            })

            print post
    elif text == '3':
        post = requests.post('http://169.60.169.211:3000/api/org.jcsdemo.com.receivedByRetailer', data = {
            "$class": "org.jcsdemo.com.receivedByRetailer",
            "order": 'O-1001',
            "owner": 'R-1001',
            "temp": "31",
            "location": "R-1001",
            "exception": false,
            "status": "received"
        })

        print post
    else:
        print "wrong input"

    print 'What would you like to do? \n1) PO \n2) ASN \n3) RA \n4) EXIT'

    text = raw_input('')


