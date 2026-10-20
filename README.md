# Silk-Product-Management

> A specialized inventory and supply chain tracking system built for silk producers, textile artisans, and luxury garment retailers.

[![React](https://img.shields.io/badge/Frontend-React-blue?style=flat-square&logo=react)](https://react.dev)
[![Node.js](https://img.shields.io/badge/Backend-Node.js%20%2F%20Express-green?style=flat-square&logo=node.js)](https://nodejs.org)
[![MongoDB](https://img.shields.io/badge/Database-MongoDB%20%2F%20Prisma-darkgreen?style=flat-square&logo=mongodb)](https://www.mongodb.com)
[![License](https://img.shields.io/badge/License-MIT-purple?style=flat-square)](LICENSE)

---

## Overview

Unlike standard retail platforms, the **Silk Product Management System** is built specifically for the unique workflows of the textile industry. It handles multi-stage product lifecycles—from raw silk yarn batches and loom assignments to fabric grading and retail garment distribution.

### Key Capabilities
* **Dual-Unit Stock Tracking:** Supports continuous length inventory (meters/yards of raw woven silk) and individual piece units (sarees, dupattas, shawls).
* **Batch & Dye Lot Lineage:** Track fiber origin, denier ratings, and dye lots to ensure shade consistency across orders.
* **Artisan & Loom Management:** Monitor production timelines, assign work orders, and track artisan piece rates.
* **Quality Assurance Grading:** Categorize items into Export Grade, Standard Grade, or Seconds stock based on pick-count and flaw inspections.
* **Order & Dispatch Logging:** Integrated sales processing and client invoice generation.

---

## Tech Stack

| Domain | Technologies |
| :--- | :--- |
| **Frontend** | React.js, Tailwind CSS, Axios |
| **Backend** | Node.js, Express.js, REST APIs |
| **Database** | MongoDB, Prisma ORM |
| **Tooling** | Git, Postman, Visual Studio Code |

---

## Project Structure

```text
Silk-Product-Management/
├── client/          # React frontend (dashboards, product tables, forms)
├── server/          # Express backend (routes, controllers, models)
├── .gitignore
├── package.json
└── README.md
```

### Quickstart

## 1. Clone the repository

git clone [https://github.com/mahmudfaysal19/Silk-Product-Management.git](https://github.com/mahmudfaysal19/Silk-Product-Management.git)
cd Silk-Product-Management

## 2. Configure Environment
Create a .env file inside the server/ folder:

PORT=5000
DATABASE_URL="your_mongodb_connection_string"
JWT_SECRET="your_secret_key"

## 3. Run Backend

cd server
npm install
npm run dev

## 4. Run Frontend

#In a new terminal

cd client
npm install
npm start

The application will launch at http://localhost:3000.

## License
This project is licensed under the MIT License.
