import redis
import sys

#consts 
REDIS_HOST = 'kyle-test.centralus.redisenterprise.cache.azure.net'
REDIS_PORT = 10000
REDIS_PASS = 'tEVmj44udQPFAoLM3oElKR5TuFVacUSuna7RaCYqRV4=' 

PRODUCTID_MAX = 10000000
LOCATIONID_MAX = 5000
LOCATION_TYPES=['STORE', 'DC']
FULFILLMENT_TYPES=['DI', 'SHIP', 'DELIVERY', 'PICK']
SEGMENTS = ['DEFAULT']
ATP_MAX = 10000
SUPPLY_MAX = 10000
DEMAND_MAX = 10000
SAFETYSTOCK_MAX = 1000

def main():
    # arg0 = sys.argv[0]
    # arg1 = sys.argv[1]
    # arg2 = sys.argv[2]
    # print(arg0 + "\t" + arg1 + "\t" + arg2)

    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASS)

    for x in range(3):
        write_item(r, x)

    print("main complete")

# keyname: productid:locationid
# fields: 
#   1. productid --> VARCHAR2 (64B) - String
#   2. locationid --> VARCHAR2 (64B) - String 
#   3. locationtype --> VARCHAR2 (64B) - String 
#   4. fulfillmenttype --> VARCHAR2 (64B) - String 
#   5. segment --> VARCHAR2 (64B) - String 
#   6. atp --> NUMBER (14,2) - String/Number 
#   7. supply --> NUMBER (14,2) - String/Number  
#   8. demand --> NUMBER (14,2) - String/Number  
#   9. safetystock --> NUMBER (14,2) - String/Number 
def write_item(r: redis.Redis, index: int):
    productid = '12345' + str(index)
    locationid = '12345' + str(index)
    inventory_item = {
        'productid': productid,
        'locationid': locationid,
        'locationtype': '123456',
        'fulfillmenttype': '123456',
        'segment': '123456',
        'atp': '123456',
        'supply': '123456',
        'demand': '123456',
        'safetystock': '123456',
    }
    r.hset(name=productid+':'+locationid, mapping=inventory_item)
    print(index)


if __name__ == "__main__":
    main() 
