/**
 * Retailer places order
 * @param {org.jcsdemo.com.retailerPlaceOrder} entry
 * @transaction
 */

function retailerPlaceOrder(entry) {
    entry.order.owner = entry.owner
    return getAssetRegistry('org.jcsdemo.com.Order')
        .then(function (assetRegistry) {
            return assetRegistry.update(entry.order);
        });
 }

/**
 * Distributor places order
 * @param {org.jcsdemo.com.distributorPlaceOrder} entry
 * @transaction
 */


 function distributorPlaceOrder(entry) {
    entry.order.owner = entry.owner
    return getAssetRegistry('org.jcsdemo.com.Order')
        .then(function (assetRegistry) {
            return assetRegistry.update(entry.order);
        });
 }

/**
 * Ship to Distributor
 * @param {org.jcsdemo.com.receivedByDistributor} entry
 * @transaction
 */

 function receivedByDistributor(entry) {
    var len = entry.temp.length;
    entry.order.owner = entry.owner
    entry.order.temp = entry.temp[len-1]
    entry.order.location = entry.location[len-1]
    entry.order.status = entry.status
    entry.order.exception = false
    entry.order.exceptionTime = ''
    entry.order.exceptionLocation = ''
    entry.order.exceptionTemp = ''
    

    for (var i = 0; i < len; i++){
        if(entry.temp[i] > 35 || entry.temp[i] < 30){
            entry.order.exception = true;
            entry.order.exceptionTime = entry.time[i]
            entry.order.exceptionLocation = entry.location[i]
            entry.order.exceptionTemp = entry.temp[i]
            break;
        }
    }

    return getAssetRegistry('org.jcsdemo.com.Order')
        .then(function (assetRegistry) {
            return assetRegistry.update(entry.order);
        });
 }

/**
 * Ship to Retailer
 * @param {org.jcsdemo.com.receivedByRetailer} entry
 * @transaction
 */

 function receivedByRetailer(entry) {
    entry.order.owner = entry.owner
    entry.order.temp = entry.temp
    entry.order.location = entry.location
    entry.order.status = entry.status
    entry.order.exception = false
    entry.order.exceptionTime = ''
    entry.order.exceptionLocation = ''
    entry.order.exceptionTemp = ''

    for (var i = 0; i < len; i++){
        if(entry.temp[i] > 35 || entry.temp[i] < 30){
            entry.order.exception = true;
            entry.order.exceptionTime = entry.time[i]
            entry.order.exceptionLocation = entry.location[i]
            entry.order.exceptionTemp = entry.temp[i]
            break;
        }
    }
    
    return getAssetRegistry('org.jcsdemo.com.Order')
        .then(function (assetRegistry) {
            return assetRegistry.update(entry.order);
        });
 }

/**
 * In transit to Distributor
 * @param {org.jcsdemo.com.inTransitToDistributor} entry
 * @transaction
 */

 function inTransitToDistributor(entry) {
 	entry.order.temp = entry.temp
    entry.order.location = entry.location
    entry.order.status = entry.status
    entry.order.exception = false
    entry.order.exceptionTime = ''
    entry.order.exceptionLocation = ''
    entry.order.exceptionTemp = ''

    for (var i = 0; i < len; i++){
        if(entry.temp[i] > 35 || entry.temp[i] < 30){
            entry.order.exception = true;
            entry.order.exceptionTime = entry.time[i]
            entry.order.exceptionLocation = entry.location[i]
            entry.order.exceptionTemp = entry.temp[i]
            break;
        }
    }
    
    return getAssetRegistry('org.jcsdemo.com.Order')
        .then(function (assetRegistry) {
            return assetRegistry.update(entry.order);
        });
 }

/**
 * In transit to Retailer
 * @param {org.jcsdemo.com.inTransitToRetailer} entry
 * @transaction
 */

 function inTransitToRetailer(entry) {
    entry.order.temp = entry.temp
    entry.order.location = entry.location
    entry.order.status = entry.status
    entry.order.exception = false
    entry.order.exceptionTime = ''
    entry.order.exceptionLocation = ''
    entry.order.exceptionTemp = ''

    for (var i = 0; i < len; i++){
        if(entry.temp[i] > 35 || entry.temp[i] < 30){
            entry.order.exception = true;
            entry.order.exceptionTime = entry.time[i]
            entry.order.exceptionLocation = entry.location[i]
            entry.order.exceptionTemp = entry.temp[i]
            break;
        }
    }
    
    return getAssetRegistry('org.jcsdemo.com.Order')
        .then(function (assetRegistry) {
            return assetRegistry.update(entry.order);
        });
 }

