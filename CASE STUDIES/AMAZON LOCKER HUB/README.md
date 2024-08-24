
# Amazon Locker Hub Simulation

## Overview

This project simulates an Amazon Locker Hub system where customers can place orders, packages are delivered to lockers, and notifications are sent to customers about their package status. The system is designed using a modular approach with clear separation of concerns between models, services, and controllers.

## Features

- **Customer Management:** Create and manage customer details.
- **Order Processing:** Place and manage orders linked to customers.
- **Locker Management:** Manage Amazon Lockers, assign packages to lockers, and track locker status.
- **Package Handling:** Assign packages to lockers, track package status.
- **Notifications:** Send notifications to customers regarding their orders and packages.

## Project Structure

```plaintext
.
├── controllers
│   ├── order_controller.py
│   ├── package_controller.py
│   └── notification_controller.py
├── models
│   ├── customer.py
│   ├── order.py
│   ├── package.py
│   ├── amazon_locker_hub.py
│   └── notification.py
├── services
│   ├── order_service.py
│   ├── package_service.py
│   └── notification_service.py
├── strategies
│   ├── locker_assignment_strategy.py
│   └── notification_strategy.py
├── main.py
└── README.md
```

- **`controllers/`**: Contains controllers that mediate between services and the application logic.
- **`models/`**: Defines the data models (e.g., Customer, Order, Package).
- **`services/`**: Contains business logic and handles the main operations (e.g., placing orders, assigning packages).
- **`strategies/`**: Contains different strategies for specific functionalities, such as locker assignment and notification strategies.
- **`main.py`**: Entry point for the application. It initializes the controllers and simulates user actions.

## Schema Design

The schema design represents the relationships between various entities in the Amazon Locker Hub system. Below is a brief overview of the main entities and their relationships:

### Entities

- **Customer**: Represents a customer using the Amazon Locker service.
  - `customer_id`: Unique identifier for the customer.
  - `customer_name`: Name of the customer.
  - `customer_location`: Location of the customer.
  - `customer_status`: Status of the customer (active, inactive).
  - `email_address`: Email address of the customer.
  - `phone_number`: Phone number of the customer.

- **AmazonLockerHub**: Represents a hub containing multiple Amazon Lockers.
  - `hub_id`: Unique identifier for the locker hub.
  - `location`: Location of the hub.
  - `amazon_lockers`: List of Amazon Lockers in the hub.
  - `start_time`: Start time of locker operation.
  - `end_time`: End time of locker operation.

- **AmazonLocker**: Represents an individual locker within a hub.
  - `locker_id`: Unique identifier for the locker.
  - `location_id`: Reference to the AmazonLockerHub where the locker is located.
  - `locker_code`: Unique code for accessing the locker.
  - `package_id`: Reference to the package stored in the locker.
  - `locker_status`: Status of the locker (available, occupied, out of service).

- **OrderItem**: Represents an item within an order.
  - `item_id`: Unique identifier for the item.
  - `quantity`: Quantity of the item ordered.
  - `price`: Price of the item.
  - `order_id`: Reference to the order to which this item belongs.

- **Order**: Represents a customer order.
  - `id`: Unique identifier for the order.
  - `customer_id`: Reference to the customer who placed the order.
  - `order_status`: Status of the order (placed, shipped, delivered).
  - `order_items`: List of items in the order.

- **Package**: Represents a package containing ordered items.
  - `package_id`: Unique identifier for the package.
  - `package_status`: Status of the package (in transit, delivered, at locker).
  - `package_items`: List of orders contained in the package.
  - `locker_id`: Reference to the Amazon Locker where the package is stored.

- **Notification**: Represents a notification sent to a customer.
  - `notification_id`: Unique identifier for the notification.
  - `notification_type`: Type of notification (email, SMS, push).
  - `notification_text`: Content of the notification.
  - `target_id`: ID of the target entity (e.g., order, package).
  - `target_type`: Type of the target entity (order, package).

### Relationships

- **Customer to Order**: One-to-Many. A customer can place multiple orders.
- **Order to OrderItem**: One-to-Many. An order can contain multiple order items.
- **Order to Package**: Many-to-Many. Multiple orders can be grouped into a package.
- **Package to AmazonLocker**: One-to-One. A package is assigned to a single Amazon Locker.
- **AmazonLocker to AmazonLockerHub**: Many-to-One. Multiple lockers are associated with a single hub.
- **Notification to Target Entity**: Polymorphic. A notification can be linked to various entities (Order, Package).

## Example Simulation

After setting up the application, you can run a simulation by executing `main.py`. The simulation will demonstrate the following:

1. Creating a customer.
2. Placing an order for the customer.
3. Assigning a package to a locker.
4. Sending a notification to the customer.

The simulation output will be printed to the console, showing each step of the process.

## Extending the Project

This project is modular and easy to extend. Here are some ideas:

- **Add more notification types**: Expand the notification system to include SMS, email, etc.
- **Enhance locker management**: Implement dynamic locker availability checking and more complex assignment strategies.
- **Order history**: Implement a history feature to track past orders for customers.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
