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
 * @param {org.jcsdemo.com.shipToDistributor} entry
 * @transaction
 */

 function shipToDistributor(entry) {
    entry.order.owner = entry.owner
    entry.order.temp = entry.temp
    entry.order.location = entry.location
    entry.order.status = entry.status
    entry.order.exception = entry.exception
    return getAssetRegistry('org.jcsdemo.com.Order')
        .then(function (assetRegistry) {
            return assetRegistry.update(entry.order);
        });
 }

/**
 * Ship to Retailer
 * @param {org.jcsdemo.com.shipToRetailer} entry
 * @transaction
 */

 function shipToRetailer(entry) {
    entry.order.owner = entry.owner
    entry.order.temp = entry.temp
    entry.order.location = entry.location
    entry.order.status = entry.status
    entry.order.exception = entry.exception
    return getAssetRegistry('org.jcsdemo.com.Order')
        .then(function (assetRegistry) {
            return assetRegistry.update(entry.order);
        });
 }

//  /**
//  * Ship to Retailer
//  * @param {org.jcsdemo.com.inTransitToDistributor} entry
//  * @transaction
//  */

function inTransitToDistributor(entry) {
    entry.order.temp = entry.temp
    entry.order.location = entry.location
    entry.order.status = entry.status
    entry.order.exception = entry.exception
    return getAssetRegistry('org.jcsdemo.com.Order')
        .then(function (assetRegistry) {
            return assetRegistry.update(entry.order);
        });
 }

//  /**
//  * Ship to Retailer
//  * @param {org.jcsdemo.com.inTransitToRetailer} entry
//  * @transaction
//  */

function inTransitToRetailer(entry) {
    entry.order.temp = entry.temp
    entry.order.location = entry.location
    entry.order.status = entry.status
    entry.order.exception = entry.exception
    return getAssetRegistry('org.jcsdemo.com.Order')
        .then(function (assetRegistry) {
            return assetRegistry.update(entry.order);
        });
 }