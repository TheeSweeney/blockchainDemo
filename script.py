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
            "orderId": "O-1002",
            "temp": "32",
            "dateplaced": "2018-02-08T21:41:14.424Z",
            "price": 120,
            "exception": "false",
            "exceptionTime": " ",
            "exceptionTemp": " ",
            "exceptionLocation": " ",
            "quantity": 10,
            "location": "D-1001",
            "status": "Inventory",
            "owner": "D-1001"
        })

        print post

        post = requests.post('http://169.60.169.211:3000/api/org.jcsdemo.com.retailerPlaceOrder', data={
            "$class": "org.jcsdemo.com.retailerPlaceOrder",
            "order": 'O-1002',
            "owner": 'D-1001'
        }) 

        print post
    elif text == '2':
        print 'Who would you like to ship to: \n1) Distributor \n2) Retailer'
        asn = raw_input('')
        if asn == '1' :
            post = requests.post('http://169.60.169.211:3000/api/org.jcsdemo.com.inTransitToDistributor', data = {
                "$class": "org.jcsdemo.com.inTransitToDistributor",
                "order": "O-1002",
                "temp": ["32", "31","33"],
                "time": ["2018-02-08T2:41:14.424Z", "2018-02-08T10:41:14.424Z", "2018-02-08T21:41:14.424Z"],                
                "location": ["T-1001", "T-1001", "T-1001"],
                "status": "in transit"
            })
            print post
        if asn == '2' :
            post = requests.post('http://169.60.169.211:3000/api/org.jcsdemo.com.inTransitToRetailer', data = {
                "$class": "org.jcsdemo.com.inTransitToRetailer",
                "order": "O-1002",
                "temp": ["40", "10", "100"],
                "time": ["2018-02-08T2:41:14.424Z", "2018-02-08T10:41:14.424Z", "2018-02-08T21:41:14.424Z"],                
                "location": ["T-1002", "T-1002", "T-1002"],
                "status": "in transit"
            })

            print post
    elif text == '3':
        post = requests.post('http://169.60.169.211:3000/api/org.jcsdemo.com.receivedByRetailer', data = {
            "$class": "org.jcsdemo.com.receivedByRetailer",
            "order": 'O-1002',
            "owner": 'R-1001',
            "temp": ["31", "30", "33"],
            "time": ["2018-02-08T2:41:14.424Z", "2018-02-08T10:41:14.424Z", "2018-02-08T21:41:14.424Z"],            
            "location": ["R-1001", "R-1001", "R-1001"],
            "status": "received"
        })

        print post
    else:
        print "wrong input"

    print 'What would you like to do? \n1) PO \n2) ASN \n3) RA \n4) EXIT'

    text = raw_input('')


