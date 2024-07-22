# Dashboard for Data Visualization

## Table of Contents
1. [Project Overview](#project-overview)
2. [Tasks](#tasks)
3. [Tools and Technologies](#tools-and-technologies)
4. [Setup Instructions](#setup-instructions)
5. [Contributing](#contributing)
6. [Author](#author)


## Project Overview

This project aims to create a set of Streamlit dashboards for visualizing and analyzing data within an organization's system. The dashboards provide interactive insights into user activity, subscriptions, course completion, capstone evaluations, coupon usage, and employment grant status.

## Tasks

1. **Registered and Subscribed Users Visualization:**
   - Visualize the number of registered and subscribed users on a daily, weekly, monthly, and yearly basis.

2. **Subscribed Users per Bundle Visualization:**
   - Display the number of users subscribed to each bundle on a daily, weekly, monthly, and yearly basis.

3. **10k AI Initiative Dashboard:**
   - Show all users in the 10k AI initiative.
   - Display the number of completed courses for each user.
   - Provide details of the last completed course, including date of completion and degree.

4. **Users' Learning and Completion Dashboard:**
   - Visualize the number of users currently learning and the number of completed courses during the week, month, and year.

5. **User Information Search Dashboard:**
   - Allow searching for a user by their ID.
   - Display current user information, including bundles, courses, completed courses, quizzes, degrees, and capstones.

6. **Admin Capstone Evaluation Dashboard:**
   - Show each admin and the number of capstones evaluated for today, this week, and this month.

7. **User Capstone Evaluation History Dashboard:**
   - Display each user's capstone and its evaluation history.

8. **Coupon Usage Dashboard:**
   - Show all coupons and the number of actual users who used these coupons.

9. **Users Grouped by Age and Study Degree Dashboard:**
   - Visualize the number of users grouped by age and study degree.

10. **Users Employment Grant Status Dashboard:**
    - Display all users and their employment grant status and history.
    - Include a summary of all employment grant statuses with the number of users in each status.

## Tools and Technologies

- Streamlit for dashboard creation.
- MySQL for database management (import `mysql.connector`).
- Python for data processing and visualization.
- Plotly Express for interactive visualizations.

## Setup Instructions

1. Install required dependencies using `pip install -r requirements.txt`.
2. Import the provided MySQL database (`demo_database.sql`).
3. Configure the database connection in the code.
4. Run the Streamlit application using `streamlit run main.py`.

## Contributing

Contributions are welcome! If you have suggestions, improvements, or additional content to contribute, feel free to open issues, submit pull requests, or provide feedback. 

[![GitHub watchers](https://img.shields.io/github/watchers/elsayedelmandoh/naive-bayes-LSTM-for-sentiment-analysis-NLP-widebot.svg?style=social&label=Watch)](https://GitHub.com/elsayedelmandoh/naive-bayes-LSTM-for-sentiment-analysis-NLP-widebot/watchers/?WT.mc_id=academic-105485-koreyst)
[![GitHub forks](https://img.shields.io/github/forks/elsayedelmandoh/naive-bayes-LSTM-for-sentiment-analysis-NLP-widebot.svg?style=social&label=Fork)](https://GitHub.com/elsayedelmandoh/naive-bayes-LSTM-for-sentiment-analysis-NLP-widebot/network/?WT.mc_id=academic-105485-koreyst)
[![GitHub stars](https://img.shields.io/github/stars/elsayedelmandoh/naive-bayes-LSTM-for-sentiment-analysis-NLP-widebot.svg?style=social&label=Star)](https://GitHub.com/elsayedelmandoh/naive-bayes-LSTM-for-sentiment-analysis-NLP-widebot/stargazers/?WT.mc_id=academic-105485-koreyst)

## Author

This repository is maintained by Elsayed Elmandoh, an AI Engineer. You can connect with Elsayed on [LinkedIn and Twitter/X](https://linktr.ee/elsayedelmandoh) for updates and discussions related to Machine learning, deep learning and NLP.

Happy coding!
