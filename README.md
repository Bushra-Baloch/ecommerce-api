# 🛍️ Django E-Commerce API

A full-featured backend API for an E-Commerce platform built using Django and Django REST Framework.  
Includes user authentication, product management, shopping cart, and order system.

---

## 🚀 Features

- ✅ JWT Authentication (Login/Signup)
- 🛍️ Product Listing, Search & Admin CRUD
- 🛒 User-Specific Cart (Add/Remove Products)
- 🧾 Checkout System with Order History
- 🔍 Search by Product Title & Description
- 🔐 Admin vs User Permissions
- 📊 Admin Panel for Managing Products & Orders

---

## ⚙️ Tech Stack

- **Backend:** Django, Django REST Framework
- **Auth:** JWT (SimpleJWT)
- **Database:** SQLite
- **Testing:** Postman

---

## 🛠️ Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/Bushra-Baloch/ecommerce-api.git
cd ecommerce-api

| Action           | Method | Endpoint                 |
| ---------------- | ------ | ------------------------ |
| JWT Login        | POST   | `/api/token/`            |
| Products List    | GET    | `/api/products/`         |
| Product Search   | GET    | `/api/products/?search=` |
| Add to Cart      | POST   | `/api/cart/add/`         |
| View Cart        | GET    | `/api/cart/`             |
| Remove from Cart | DELETE | `/api/cart/remove/<id>/` |
| Place Order      | POST   | `/api/orders/place/`     |
| Order History    | GET    | `/api/orders/my/`        |

