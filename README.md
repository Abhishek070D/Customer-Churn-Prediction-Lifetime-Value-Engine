📉 Customer Churn & Retention Analytics

An interactive Power BI analytics report identifying who is churning, why they are churning, which customer segments carry the highest risk, and where a retention team should focus first.

📊 Power BI • 🧮 DAX • 🧹 Power Query • 🐍 Python / Pandas • 📈 Business Intelligence

🧭 Project Overview

Customer churn is a critical challenge for subscription-based businesses. Understanding who is leaving, why they are leaving, and which customers require attention can help organizations design more targeted retention strategies.

This project transforms the IBM Telco Customer Churn dataset into an interactive 5-page Power BI analytics report focused on customer behavior, churn drivers, retention patterns, and risk prioritization.

💡 Core Business Question

Who is churning, why are they churning, which customer segments carry the greatest risk, and where should the retention team focus first?

🎯 Business Objectives
👥 Quantify the scale of customer churn
🔍 Identify customer segments associated with higher churn
📑 Analyze contract types and their relationship with churn
🌐 Understand service-level churn patterns
💳 Analyze payment and billing behavior
⏳ Identify tenure-based churn patterns
⚠️ Segment customers based on observed churn risk
🎯 Provide actionable insights for retention teams
📊 Executive KPIs
KPI	Value
👥 Total Customers	7,043
❌ Churned Customers	1,869
✅ Retained Customers	5,174
📉 Overall Churn Rate	26.54%
💰 Average Monthly Charges	$64.76
⏳ Average Customer Tenure	32.37 months
📐 Key Calculations

Churn Rate

Churn Rate = Churned Customers ÷ Total Customers × 100

1,869 ÷ 7,043 × 100 = 26.54%

Retention Rate

Retention Rate = Retained Customers ÷ Total Customers × 100

5,174 ÷ 7,043 × 100 = 73.46%

🖥️ Dashboard Preview

✨ Dashboard Highlights
📌 Executive KPI cards
📊 Churn vs. retention analysis
📑 Contract-level churn analysis
🌐 Service-level analysis
⏳ Tenure-band analysis
💰 Monthly charge analysis
🔄 Customer retention overview
⚠️ Risk-based customer analysis
🎛️ Interactive slicers and filters
🔎 Customer-level analysis
📑 Report Structure

The report is organized into 5 analytical pages, keeping executive reporting, detailed analysis, risk assessment, and customer-level investigation clearly separated.

Page	Focus	Purpose
01 · Executive Churn Overview	📊 KPIs & Trends	High-level view of churn and retention
02 · Customer & Churn Analysis	👥 Segmentation	Identify customer groups with higher churn
03 · Contract & Service Analysis	📑 Services	Analyze contracts, services and payment behavior
04 · Churn Risk Analysis	⚠️ Risk	Prioritize higher-risk customer segments
05 · Customer Details	🎯 Operations	Filterable customer-level analysis
🔎 Key Business Findings
📉 01 · Overall Churn

The customer base contains:

👥 7,043 total customers
❌ 1,869 churned customers
✅ 5,174 retained customers
📉 26.54% overall churn rate
🔄 73.46% retention rate

This indicates a significant opportunity for improving customer retention.

⏳ 02 · Tenure Is a Major Churn Driver
Tenure Band	Churn Rate
🔴 0–6 Months	52.94%
🟠 6–12 Months	35.89%
🟢 12+ Months	17.13%
💡 Insight

Customers within their first six months have the highest churn rate.

This indicates that the early customer lifecycle is a critical period for retention.

🎯 Recommended Action

Focus on:

🚀 Better customer onboarding
📩 Early engagement campaigns
🛠️ Proactive support
🔍 Early identification of dissatisfaction
📑 03 · Contract Type & Churn
Contract Type	Churned Customers
🔴 Month-to-Month	1,655
🟠 One Year	166
🟢 Two Year	48
💡 Insight

Month-to-month customers represent the largest churn group by a significant margin.

🎯 Recommended Actions
🎁 Incentivize annual contracts
⭐ Introduce loyalty benefits
🔄 Develop contract-upgrade campaigns
🎯 Personalize retention offers
🌐 04 · Internet Service & Churn

The analysis compares churn across:

🌐 DSL
⚡ Fiber Optic
🚫 No Internet Service
💡 Insight

Fiber optic customers show a substantially higher churn rate than DSL customers.

This creates an opportunity to investigate:

🌐 Service quality
💰 Pricing
🛠️ Technical support
😊 Customer experience
🔐 05 · Online Security & Tech Support

Customers without services such as Online Security and Tech Support show substantially higher churn rates than customers who subscribe to these services.

🎯 Business Opportunity

Investigate whether:

Customers perceive insufficient service value
Support experience affects satisfaction
Bundled service offerings could improve retention
💳 06 · Payment Method

Payment behavior is also analyzed as a potential churn indicator.

Electronic Check shows the highest churn rate among the payment methods analyzed.

🎯 Recommended Actions
💳 Investigate payment friction
🔄 Encourage automated payment methods
📩 Improve billing communication
🎁 Consider incentives for autopay adoption
⚠️ Churn Risk Framework

The historical dataset contains a Churn outcome (Yes / No) rather than a native machine-learning churn-probability field.

Therefore, the project uses a transparent rule-based Risk Score based on observed churn drivers rather than presenting an invented probability as a predictive model.

🔍 Risk Drivers

The framework considers:

📑 Contract Type
⏳ Tenure
🌐 Internet Service
🔐 Online Security
🛠️ Tech Support
💳 Payment Method
🚦 Risk Segmentation
Risk Category	Customers	Actual Churn Rate
🔴 High Risk	2,688	53.2%
🟠 Medium Risk	1,900	18.0%
⚪ Low Risk	2,455	3.9%

Note: This is a rule-based risk proxy validated against historical outcomes. It is not a machine-learning prediction model.

🧹 Data Preparation & Quality

The dataset was cleaned and validated before dashboard development.

🧾 TotalCharges

TotalCharges is stored as text and contains 11 blank values, corresponding to customers with tenure = 0.

These records were retained and handled through Power Query type conversion rather than being unnecessarily removed.

👤 SeniorCitizen

The original field uses:

0 = No
1 = Yes

A readable label is used for dashboard analysis and slicers.

🌐 Service Categories

Where applicable, service fields retain separate categories such as:

Yes
No
No internet service

This prevents information from being lost during analysis.

🧮 Data Analysis
👥 Customer Dimensions
Gender
Senior Citizen
Partner
Dependents
Tenure
Contract
Internet Service
Payment Method
🛠️ Service Dimensions
Phone Service
Multiple Lines
Online Security
Online Backup
Device Protection
Tech Support
Streaming TV
Streaming Movies
💰 Financial Metrics
Monthly Charges
Total Charges
📉 Churn Metrics
Churn Status
Churn Rate
Retention Rate
Customer Count
Tenure-based Churn
Risk Category
🛠️ Tools & Technologies
Technology	Purpose
🔷 Power BI Desktop	Data modeling, visualization & dashboard development
🧮 DAX	KPI calculations and analytical measures
🧹 Power Query	Data cleaning and transformation
🐍 Python / Pandas	Data profiling and validation
📊 Excel / CSV	Source data
🌐 HTML / CSS / JavaScript	Interactive browser-based dashboard
📐 DAX Measures
👥 Total Customers

Total Customers = DISTINCTCOUNT(customerID)

❌ Churned Customers

Churned Customers = DISTINCTCOUNT(customerID) where Churn = "Yes"

✅ Retained Customers

Retained Customers = DISTINCTCOUNT(customerID) where Churn = "No"

📉 Churn Rate

Churn Rate = Churned Customers ÷ Total Customers

🔄 Retention Rate

Retention Rate = Retained Customers ÷ Total Customers

💰 Average Monthly Charges

Average Monthly Charges = AVERAGE(MonthlyCharges)

⏳ Average Tenure

Average Tenure = AVERAGE(tenure)

🎛️ Dashboard Interactivity

The report supports interactive analysis through:

🎛️ Multi-select slicers
🔄 Cross-filtering
🖱️ Visual interactions
🔎 Drill-through analysis
📋 Customer-level filtering
🎨 Conditional formatting
📊 Dynamic KPI updates

Users can move from an executive-level KPI to detailed customer-level analysis while maintaining the same analytical context.

💡 Business Recommendations
1️⃣ Focus on New Customers

The 0–6 month segment has the highest churn rate.

Strengthen onboarding and introduce proactive engagement during the early customer lifecycle.

2️⃣ Reduce Month-to-Month Churn

Month-to-month customers contribute the largest number of churned customers.

Encourage longer-term contracts through personalized incentives and loyalty benefits.

3️⃣ Improve Service Experience

Customers without key support and security services show higher churn.

Investigate service experience and consider targeted service bundles.

4️⃣ Address Payment Friction

Electronic-check customers show elevated churn.

Investigate billing experience and encourage automated payment adoption.

5️⃣ Combine Risk With Customer Value

Retention should not focus only on churn likelihood.

A stronger prioritization framework is:

Churn Risk + Customer Value + Retention Cost

This helps identify customers where intervention can potentially deliver the greatest business impact.

📈 Business Impact

The project creates a structured path from raw data to business action:

📁 Raw Data → 🧹 Data Cleaning → 🔍 Analysis → 📊 Churn Drivers → ⚠️ Risk Segmentation → 🎯 Customer Prioritization → 💡 Retention Strategy

The dashboard helps stakeholders move beyond:

“How many customers are churning?”

toward:

“Who is churning, why are they churning, and where should we act first?”
