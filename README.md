# FS-Fashion 👗🛍️

![Django](https://img.shields.io/badge/Django-3.2-092E20?style=for-the-badge&logo=django)
![Python](https://img.shields.io/badge/Python-3.8-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTML](https://img.shields.io/badge/HTML-5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

## About FS Fashion

FS Fashion is a modern, responsive online store built with Django. It aims to provide a seamless shopping experience with features like product browsing, cart management, and order processing.

## Features

- User Authentication (Signup, Login, Logout)
- Product Catalog
- Product Search and Filtering
- Shopping Cart
- Admin Dashboard for managing products, orders, and users
- Responsive Design

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.11.9+
- Django 4.0+

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/LucasMedeiros-dev/FS-Fashion.git
   cd fs-fashion
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the application:**

   Open your browser and go to `http://127.0.0.1:8000`

## Project Structure

```
fs_fashion/
├── apps/                # Django applications
│   ├── carrinho/        # Shopping cart functionality
│   ├── clientes/        # Customer management
│   ├── fornecedores/    # Supplier management
│   ├── frente_loja/     # Frontend store functionality
│   ├── marcas/          # Brand management
│   ├── motoboys/        # Delivery personnel management
│   ├── produtos/        # Product management
│   └── vendedores/      # Vendor management
├── core/                # Core functionalities and utilities
├── project/             # Django project settings and configurations
├── .gitignore           # Git ignore file
├── db.sqlite3           # SQLite database file (for development)
├── etiquetas_latest.png # Image file used in the project
├── manage.py            # Django's command-line utility
├── requirements.txt     # Project dependencies
└── teste.py             # Test script
```


---

Thank you for visiting FS-Fashion! Happy Shopping! 🛍️
```

---
