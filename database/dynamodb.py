import os,boto3
FALLBACK=[{"id":"1","name":"AeroBook Pro 14","price":"79999","category":"Laptop","description":"14-inch productivity laptop.","image":"https://images.unsplash.com/photo-1496181133206-80ce9b88a853"},{"id":"2","name":"PowerCore X15","price":"104999","category":"Laptop","description":"Performance laptop for development.","image":"https://images.unsplash.com/photo-1603302576837-37561b2e2302"},{"id":"3","name":"LiteBook Air","price":"64999","category":"Laptop","description":"Lightweight laptop for professionals.","image":"https://images.unsplash.com/photo-1517336714739-489689fd1ca8"}]
def get_products():
    try:
        t=boto3.resource("dynamodb",region_name=os.getenv("AWS_REGION","ap-south-1")).Table(os.getenv("DYNAMODB_TABLE","shopping-products"))
        return t.scan().get("Items") or FALLBACK
    except Exception as e:
        print("DynamoDB unavailable:",e); return FALLBACK
