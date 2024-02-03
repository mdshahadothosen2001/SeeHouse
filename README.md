# SeeHouse

## Customer APIs
1. Registration API with POST method : `localhost/customer/register/`
```bash
{
    "first_name":"...",
    "last_name":"...",
    "phone_number":"...",
    "email":"...",
    "password":"..."
}
```
2. Token API with POST Method : `localhost/customer/token/`
```bash
{
    "phone_number":"...",
    "password":"..."
}
```
3. Refresh Token API with POST Method : `localhost/customer/token/refresh/`
```bash
{
    "refresh":"..."
}
```
 
# ` `

## Vendor APIs
1. Registration API with POST Method : `localhost/vendor/register/`
```bash
{
    "first_name":"...",
    "last_name":"...",
    "phone_number":"...",
    "email":"...",
    "tin_number":"...",
    "password":"..."
}
```
2. Token API with POST Method : `localhost/vendor/token/`
```bash
{
    "phone_number":"...",
    "password":"..."
}
```
3. Refresh Token API with POST Method : `localhost/vendor/token/refresh/`
```bash
{
    "refresh":"..."
}
```
4. Service list API with GET Method : `localhost/vendor/service/`

5. Creating New shop with POST Method : `localhost/vendor/service/create/`

```bash
{
            "shop_name":"....",
            "shop_number":"...",
            "shop_type":"...",
            "shop_title":"...",
            "fields":"...",
            "about":"...",
            "service_started":"YY-MM-DD"
}
```

# ` `

## Product APIs

1. Product Category list API with GET Method : `localhost/product/category/`

2. Product Subcategory list API with GET Method with category ID : `localhost/product/category/subcategory/`
```bash
{
    "category_id":1
}
```

3. Product list API with GET Method with subcategory ID : `localhost/product/`
```bash
{
    "subcategory_id":1
}
```
