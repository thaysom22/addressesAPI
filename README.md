# addressesAPI

An API built with Django Rest Framework for users to manage addresses

### API endpoints

(*not implemented for v1)

| Endpoint | HTTP Verb | Details | Endpoint Permissions 
| --- | --- | --- | --- |
| * `users/current/` | `GET` | Retrieve User instance detail for currently authenticated user | request must be from an authenticated user |
| * `users/` | `GET` | List all User instances in DB | request by Admin user only |
| * `users/` | `POST` | Create new user instance in DB | request by Admin user only |
| * `users/:pk` | `GET` | Retrieve User instance identified by pk | Admin user only |
| * `users/:pk` | `PUT`, `PATCH` | Update User instance identified by pk | Admin user only |
| * `users/:pk` | `DELETE` | Delete User instance identified by pk (associated Address instances also deleted) | Admin user only |
| | | | |
| `addresses/current-user/` | `GET` | List Address instances associated with currently authenticated user. Optional filtering with `search` request query parameter | request must be from an authenticated user |
| `addresses/current-user/` | `POST` | Create new Address instance for currently authenticated user  | request must be from an authenticated user |
| `addresses/current-user/` | `DELETE` | Delete Address instances for currently authenticated user. Optional filtering with `search` request query parameter (if not provided ALL Address instances belonging to user are deleted) | request must be from an authenticated user |
| * `addresses/` | `GET` | List all address instances in DB | Admin user only |
| * `addresses/` | `POST` | Create new Address instance in DB for any user | Admin user only |
| `addresses/<int:pk>` | `GET` | Get identified address instance  | Address instance must be associated with currently authenticated user or request made by admin user |
| `addresses/<int:pk>` | `PUT`, `PATCH` | Update of identified address instance | Address instance must be associated with currently authenticated user or request made by admin user |
| `addresses/<int:pk>` | `DELETE` | Delete identified address instance | Address instance must be associated with currently authenticated user or request made by admin user |
