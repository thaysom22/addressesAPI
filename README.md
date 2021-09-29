# addressesAPI

An API built with Django Rest Framework for users to manage addresses

### API endpoints

* Django `admin.site.urls` endpoints are registered at `admin/` 
* DRF **browsable API** authentication `rest_framework.urls` (`login/` and `logout/`) endpoints are registered at `api-auth/`
* 3rd party `rest-auth` package endpoints are registered at `api/v1/rest-auth/`. 

(*not implemented for v1)

| Endpoint | HTTP Verb | Details | Endpoint Permissions 
| --- | --- | --- | --- |
| * `users/current/` | `GET` | Retrieve User instance detail for currently authenticated user | request must be from an authenticated user |
| * `users/` | `GET` | List all User instances in DB | request by Admin user only |
| * `users/` | `POST` | Create new user instance in DB | request by Admin user only |
| * `users/<int:pk>/` | `GET` | Retrieve User instance identified by pk | Admin user only |
| * `users/<int:pk>/` | `PUT`, `PATCH` | Update User instance identified by pk | Admin user only |
| * `users/<int:pk>/` | `DELETE` | Delete User instance identified by pk (associated Address instances also deleted) | Admin user only |
| | | | |
| `current-user/` | `GET` | List Address instances associated with currently authenticated user. Optional filtering with `search` request query parameter | request must be from an authenticated user |
| `current-user/` | `POST` | Create new Address instance for currently authenticated user  | request must be from an authenticated user |
| `current-user/` | `DELETE` | Delete Address instances for currently authenticated user. Optional filtering with `search` request query parameter (if not provided ALL Address instances belonging to user are deleted) | request must be from an authenticated user |
| * `/` | `GET` | List all address instances in DB | Admin user only |
| * `/` | `POST` | Create new Address instance in DB for any user | Admin user only |
| `<int:pk>/` | `GET` | Get identified address instance  | Address instance must be associated with currently authenticated user or request made by admin user |
| `<int:pk>/` | `PUT`, `PATCH` | Update of identified address instance | Address instance must be associated with currently authenticated user or request made by admin user |
| `<int:pk>/` | `DELETE` | Delete identified address instance | Address instance must be associated with currently authenticated user or request made by admin user |
