import redis
import random

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

NUM_ITEMS = 1000000

def main():
    # arg0 = sys.argv[0]
    # arg1 = sys.argv[1]
    # arg2 = sys.argv[2]
    # print(arg0 + "\t" + arg1 + "\t" + arg2)

    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASS)

    for x in range(NUM_ITEMS):
        write_item_hash(r, x)

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
def write_item_hash(r: redis.Redis, index: int):
    # generate not-so-random data
    locationtype = LOCATION_TYPES[index % len(LOCATION_TYPES)]
    fulfillmenttype = FULFILLMENT_TYPES[index % len(FULFILLMENT_TYPES)]
    segment = SEGMENTS[index % len(SEGMENTS)]

    productid = random.randint(PRODUCTID_MAX/2, PRODUCTID_MAX)
    locationid = random.randint(1, LOCATIONID_MAX)
    atp = random.randint(0, ATP_MAX)
    supply = random.randint(0, SUPPLY_MAX)
    demand = random.randint(0, DEMAND_MAX)
    safetystock = random.randint(0, SAFETYSTOCK_MAX)

    inventory_item = {
        'productid': productid,
        'locationid': locationid,
        'locationtype': locationtype,
        'fulfillmenttype': fulfillmenttype,
        'segment': segment,
        'atp': atp,
        'supply': supply,
        'demand': demand,
        'safetystock': safetystock
    }
    r.hset(name=str(productid)+':'+str(locationid), mapping=inventory_item)
    print(index)


if __name__ == "__main__":
    main() 
