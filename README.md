# 🏭 Automated Inventory Manager (Python & Excel)

## 📋 Overview
This tool was designed to help small businesses (SMEs) transition from manual Excel data entry to **automated inventory management**. 

It analyzes stock levels, calculates re-ordering needs based on safety thresholds, and automatically generates a **formatted, professional Purchase Order (Bon de Commande)** ready to be sent to suppliers.

## 🚀 Key Features
* **Smart Detection:** Instantly identifies items below the "Safety Stock" threshold.
* **Budget Calculation:** Automatically calculates the estimated budget required for replenishment.
* **Prioritization:** Flags items as "CRITICAL" (Red) or "Priority" based on urgency.
* **Professional Output:** Generates a clean `.xlsx` report with conditional formatting (colors, borders, currency) using `XlsxWriter`.

## 🛠️ Technical Stack
* **Python 3.12**
* **Pandas:** For high-performance data manipulation (Vectorization).
* **XlsxWriter:** For programmatic Excel formatting.
* **Colorama:** For terminal interface feedback.

## 📂 Project Structure
* `smart_restock.py`: The main automation logic.
* `generate_data.py`: Script to generate dummy data for testing.
* `output/`: Folder containing the generated Purchase Orders.

## 👨‍💻 Author
**El Walid El Alaoui** *Data Engineer | Microsoft Azure & SQL Specialist* [LinkedIn Profile](https://www.linkedin.com/in/el-walid-el-alaoui-fels-51491538b/)
