### Start project

1.
```sh
docker-compose build
```

2.
```shell
docker-compose run --rm web python manage.py migrate
```

3.
```
docker-compose up
```

</br>

### API

#### insert fake data (RESTful)

```sh
curl 127.0.0.1:8000/api/v1/rest/fake/insert
```

#### clear fake data (RESTful)

```sh
curl 127.0.0.1:8000/api/v1/rest/fake/clear
```

#### get  members (GraphQL)

127.0.0.1:8000/api/v1/graphql

```graphql
{
  members(input: {
  }){
    platform
    account
    surname
    givenName
    gender
    birthday
    email
    phone
    address
    tripressoCoin
  }
}
```

#### get tour_groups (GraphQL)

127.0.0.1:8000/api/v1/graphql

```sh
{
  tourGroups(input: {
    page: 1
    size: 3
    orderBy: SCORE_ASC | SCORE_DESC | PRICE_ASC | PRICE_DESC
  }) {
    id
    supplierId
    supplierTourCode
    dayAmount
    name
    isRecommend
    defaultPrice
    score
    bucket {
      date
      sell
      adultPrice
      childPrice
      babyPrice
      remark
      goFrom
      backFrom
    }
    memberFavorite
    tags
    locations
  }
}
```

</br>

##### tools
[vishnubob/wait-for-it](https://github.com/vishnubob/wait-for-it/blob/master/wait-for-it.sh)
