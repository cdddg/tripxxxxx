### Start project

```sh
docker-compose up --build
```

</br>

### API

#### RESTful

- ##### insert fake data

  ```sh
  curl 127.0.0.1:8000/api/v1/rest/fake/insert
  ```

- ##### clear fake data

  ```sh
  curl 127.0.0.1:8000/api/v1/rest/fake/clear
  ```

#### GraphQL

127.0.0.1:8000/api/v1/graphql

![example](https://raw.githubusercontent.com/cdddg/tripxxxxx/develop/images/graphql_example.png)

- ##### get  members

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

- ##### get tour_groups

  ```graphql
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
