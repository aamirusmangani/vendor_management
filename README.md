# Vendor Management System with Performance Metrics

This project is a Vendor Management System built using Django and Django REST Framework. It allows for the management of vendor profiles, tracking of purchase orders, and calculation of vendor performance metrics.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Performance Metrics](#performance-metrics)

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python
- Pip
- Virtualenv (optional but recommended)

### Installation


1. Clone the repository:
   ```bash
   git clone https://github.com/aamirusmangani/vendor_management/
   cd vendor_management


2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


3. Install dependencies:
   ```bash
   pip install -r requirements.txt


4. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

5. Run the development server:
   ```bash
   python manage.py runserver



The application should now be running at http://localhost:8000.


### API Endpoints

* Vendor Profile Management:
  * POST /api/vendors/: Create a new vendor.
  * GET /api/vendors/: List all vendors.
  * GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
  * PUT /api/vendors/{vendor_id}/: Update a vendor's details.
  * DELETE /api/vendors/{vendor_id}/: Delete a vendor.

* Purchase Order Tracking:
  * POST /api/purchase_orders/: Create a purchase order.
  * GET /api/purchase_orders/: List all purchase orders with an option to filter by vendor.
  * GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
  * PUT /api/purchase_orders/{po_id}/: Update a purchase order.
  * DELETE /api/purchase_orders/{po_id}/: Delete a purchase order.

* Vendor Performance Evaluation:
  * GET /api/vendors/{vendor_id}/performance: Retrieve a vendor's performance metrics.

* Update Acknowledgment Endpoint:
  * POST /api/purchase_orders/{po_id}/acknowledge: Vendor acknowledgment of purchase orders.

### Performance Metrics

The system calculates the following performance metrics:

* On-Time Delivery Rate: Percentage of orders delivered by the promised date.
* Quality Rating: Average of quality ratings given to a vendor’s purchase orders.
* Response Time: Average time taken by a vendor to acknowledge or respond to purchase orders.
* Fulfilment Rate: Percentage of purchase orders fulfilled without issues.
