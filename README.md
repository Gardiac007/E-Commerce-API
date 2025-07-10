### E-Commerce API using DRF
This is an E-Commerce API with multiple models and it has some advanced features of DRF.

### **Features Stack:**
- It has **Custom Permissions** that limits the usage of endpoints (Seller or Customer).
- **Pagination** technique is implemented to access large amount of data into multiple pages.
- Added **Advanced Filtering and Sorting** techniques for data retrieval (SearchFilter, OrderingFilter).
- **JWT** is used for User Authentication.
- **DRF Throttling** is implemented for Rate-Limiting and prevents from DDoS Attacks.
- This API can provides CRUD operations on Products, Categories and Orders.

### [Requirements.txt:](https://github.com/Gardiac007/E-Commerce-API/blob/main/requirements.txt)
```
﻿asgiref==3.9.0
Django==5.2.4
django-filter==25.1
djangorestframework==3.16.0
djangorestframework_simplejwt==5.5.0
PyJWT==2.9.0
sqlparse==0.5.3
tzdata==2025.2
```

> [!NOTE]
> Use **Postman** for JWT Authentication and Use Authentication headers.

### API Endpoints:
For this project, I have made a **Postman** Collection called ```E-Commerce API``` and you can access it by the below link:

```https://priyan-5453260.postman.co/workspace/Priyan's-Workspace~12424d67-9cb2-4a03-8844-138064f76fd8/collection/46233932-eea9b610-d9e8-4e30-90b8-dac5246c7a3b?action=share&creator=46233932```
