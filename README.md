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


# ` `

## Product APIs

1. Product list API with GET Method with subcategory ID : `localhost/product/`
```bash
{
    "subcategory":1
}
```
