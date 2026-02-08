🏭 Automated Inventory Manager v2.0 (Python, API & Excel)
📋 Overview
This project is a Smart Supply Chain Automation tool designed for SMEs to eliminate manual monitoring.

The system acts as a "Digital Supervisor": it analyzes stock levels via Pandas, generates professional XlsxWriter reports, and—most importantly—uses the Telegram Bot API to send real-time alerts to managers when stock reaches critical levels.

🚀 Key Features
Real-Time Telegram Alerts: Integrates with the Telegram Bot API to push instant notifications for "CRITICAL" stock levels directly to mobile devices.

Automated Decision Logic: Uses vectorized Pandas operations to calculate re-order quantities and categorize urgency (CRITICAL vs. Priority).

Financial Intelligence: Automatically calculates total procurement budgets in Moroccan Dirham (DH) for executive review.

Professional Reporting: Programmatically generates formatted .xlsx Purchase Orders with conditional formatting, custom borders, and currency symbols.

🛠️ Technical Stack
Python 3.12

API Integration: Telegram Bot API (via requests)

Data Analysis: Pandas (Vectorization & DataFrames)

Reporting: XlsxWriter

Environment Management: python-dotenv for secure API credential handling

📂 Project Structure
restock.py: The core engine that runs analysis and triggers alerts.

alerts.py: Modular API handler for Telegram notifications.

generate.py: Script to simulate inventory data for Moroccan market testing.

.env.example: Template for secure API token configuration.

⚙️ Setup & Security
Install dependencies: pip install -r requirements.txt.

Create a .env file and add your TELEGRAM_TOKEN and CHAT_ID.

Security Note: The .env file is included in .gitignore to prevent leaking API keys on public repositories.

## 👨‍💻 Author
**El Walid El Alaoui** *Data Engineer | Microsoft Azure & SQL Specialist* [LinkedIn Profile](https://www.linkedin.com/in/el-walid-el-alaoui-fels-51491538b/)
