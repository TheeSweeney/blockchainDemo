/**
 * Retailer places order
 * @param {org.jcsdemo.com.retailerPlaceOrder} test
 * @transaction
 */

function retailerPlaceOrder(test) {
    test.order.owner = test.owner
    return getAssetRegistry('org.jcsdemo.com.Order')
        .then(function (assetRegistry) {
            return assetRegistry.update(test.order);
        });
 }