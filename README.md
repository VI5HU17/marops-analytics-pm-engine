# Data-Driven Marketing Operations (MarOps) Engine

## 📌 Executive Summary
This repository contains an end-to-end operational framework designed to bridge the gap between data insights and cross-functional project execution. The project simulates a real-world corporate scenario: resolving a critical customer churn vulnerability for a growing e-commerce brand. 

By functioning as both the **Data Analyst** and the **Technical Project Manager**, I developed a Python-based data segmentation engine to isolate high-value revenue risks, then built a complete Agile/Scrum playbook to coordinate a cross-functional squad (Engineering, Design, and Copywriting) to deploy a targeted retention campaign.

---

## 📋 Live Project Workspace & Visual Board
### 🔗 Active Scrum Sprint Tracker: [Click Here to View Live Kanban Board](https://github.com/users/VI5HU17/projects/1)

Below is the live operational layout of our technical execution sprint board. You can monitor active ticket distributions, feature progression, and task assignments directly via our integrated workspace.

| 📋 Todo (Backlog) | ⚙️ In Progress | ✅ Done |
| :--- | :--- | :--- |
| • **Automation of Segmentation Logic (Sprint 1)**<br>_Feature: Daily cron automation loop_ | • **Database Schema Expansion (Sprint 1)**<br>_Feature: Schema upgrade & indexing_ | • **Initial RFM Engine Core Setup**<br>_Feature: Statistical quartile script_ |
| • **Targeted Email Copywriting (Sprint 2)**<br>_Feature: A/B Testing Variations_ | | |
| • **Bespoke UI Layout Assets (Sprint 2)**<br>_Feature: Premium landing templates_ | | |

---

## 📊 Phase 1: Marketing Analytics & Segmentation
The data engine processes customer transaction records over a dynamic 90-day cycle to compute **Recency, Frequency, and Monetary (RFM)** scores using statistical quartiles.

* **The Core Insight:** The analysis successfully isolated an active **"At Risk VIP"** cohort—representing users with high historical spend who have not made a transaction in over 60 days. This represents a critical, leaking revenue bucket that demands immediate operational intervention.
* **The Deliverable:** A data-driven dataset mapping out explicit user tiers to feed directly into automated marketing operations tools.
* **Core Logic Location:** [Click to View Segmentation Script](https://github.com/VI5HU17/marops-analytics-pm-engine/tree/main/analytics_engine)
* **Data Source:** [Click to View Raw Transactions CSV](https://github.com/VI5HU17/marops-analytics-pm-engine/blob/main/analytics_engine/data/transactions.csv)

---

## 📋 Phase 2: Technical Project Management
Turning data insights into predictable business results requires structured agile execution. The project management playbook outlines how the cross-functional squad will deploy the retention campaign within a strict timeline.

* **Project Charter:** Outlines strict project boundaries, business cases, KPIs, success metrics, and stakeholder ownership. [Click to Read Project Charter File](https://github.com/VI5HU17/marops-analytics-pm-engine/blob/main/pm_playbook/project_charter.md)
* **Agile Backlog & Sprints:** Translates high-level business goals into engineering, data, and creative user stories complete with explicit **Acceptance Criteria**. [Click to Read Agile Backlog File](https://github.com/VI5HU17/marops-analytics-pm-engine/blob/main/pm_playbook/agile_backlog.md)
* **Risk Management:** Preemptively tracks system blockages, data sync integration failures, and creative scope creep using an operational mitigation matrix. [Click to Read Risk Management File](https://github.com/VI5HU17/marops-analytics-pm-engine/blob/main/pm_playbook/risk_management.md)

---

## 🏢 Real-World Enterprise Application
This framework directly mirrors the operational pipelines used by modern corporate tech and software-as-a-service (SaaS) environments:

1. **Retention Marketing Optimization (MarOps):** Growth teams run this precise RFM logic against live customer databases to isolate high-value, slipping accounts so the business can trigger automated, highly targeted win-back email workflows.
2. **Cross-Functional Agile Execution:** A Technical Project Manager uses the exact structured artifacts built here (Project Charters and User Stories) to align multidisciplinary squads—ensuring developers, designers, and copywriters work toward unified corporate KPIs without wasting budget.
3. **Proactive Change & Risk Control:** The mitigation matrix used in this framework stops scope creep and maps out system fallbacks (like API failures) before they hit production.

---

## ⚙️ Environment Setup & Installation
For engineers or analysts looking to replicate the data environment locally, follow these steps:

### Prerequisites
* Python 3.x installed
* Python packages: `pandas`

### Execution Instructions
1. Clone the repository:
```bash
   git clone [https://github.com/VI5HU17/marops-analytics-pm-engine.git](https://github.com/VI5HU17/marops-analytics-pm-engine.git)
   cd marops-analytics-pm-engine
