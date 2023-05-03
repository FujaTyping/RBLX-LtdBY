import requests, uuid, time, json, threading

with open('config.json') as config:
    config = json.load(config)

assetId = input('>> Enter assetid: ')
print(">> You don't have to enter howmany times to buy")
#amount = int(input('>> Purchase howmany times: '))

class Bot:
    def __init__(self):
        self.session = requests.Session()
        self.session.cookies['.ROBLOSECURITY'] = config['cookie']
        self.user_id = self.session.get('https://www.roblox.com/my/settings/json').json()['UserId']

    def csrf_token(self):
        return self.session.post('https://auth.roblox.com/v2/login').headers['x-csrf-token']

    def item_info(self):
        receive_data = False
        retry = 0
        while receive_data == False :
            try :
                id_response = self.session.get(f'https://catalog.roblox.com/v1/catalog/items/{assetId}/details?itemType=Asset').json()
                self.collectible_id = id_response['collectibleItemId']
                item_data = self.session.post(
                    'https://apis.roblox.com/marketplace-items/v1/items/details',
                    json = {"itemIds": [self.collectible_id]}, headers = {'x-csrf-token': self.csrf_token()}
                ).json()[0]
                self.product_id = item_data['collectibleProductId']
                self.asset_price = item_data['price']
                self.seller_id = item_data['creatorId']
                self.name = item_data['name']
                self.description = item_data['description']
                receive_data = True
                print(">> [LOGS] - Receive data successfully : "+self.name+" | "+self.description)
                retry = 0
            except :
                print(">> [LOGS] - Can't receive item info ( Retry : "+retry+" )")
                retry = retry + 1
                time.sleep(1)

    def purchase_item(self):
        sent_requests = success = 0
        retry = 0
        while 1 :
            try :
                response = self.session.post(
                    f'https://apis.roblox.com/marketplace-sales/v1/item/{self.collectible_id}/purchase-item',
                    json = {
                        "collectibleItemId": self.collectible_id,
                        "expectedCurrency": 1,
                        "expectedPrice": self.asset_price,
                        "expectedPurchaserId": str(self.user_id),
                        "expectedPurchaserType": "User",
                        "expectedSellerId": 1,
                        "expectedSellerType": "User",
                        "idempotencyKey": str(uuid.uuid4()),
                        "collectibleProductId": self.product_id
                    },
                    headers = {
                        'X-CSRF-TOKEN': self.csrf_token()
                    }
                )
                print(">> [LOGS] - "+response.text)
                if response.status_code == 200:
                    success += 1
                sent_requests += 1
                #if amount == success: break
                if sent_requests >= 10: # 10 initial requests, assumes you are not ratelimited just for efficiency
                    time.sleep(7)

                retry = 0
            except :
                print(">> [LOGS] - Can't purchase item ( Retry : "+retry+" )")
                retry = retry + 1
                time.sleep(1)

try :
    a = Bot()
    a.item_info()
    a.purchase_item()
except :
    print(">> [LOGS] - Something happend seem like collectibleId is wrong")
    print(">> [LOGS] - Please check your collectibleId again")