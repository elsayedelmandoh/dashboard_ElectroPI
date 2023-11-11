import streamlit as st
import mysql.connector as mysql
import pandas as pd
import plotly.express as px

# Function to get data from MySQL
def get_data(query):
    connection = mysql.connect(
        host="localhost",
        user="root",
        password="seven",
        database="demo_database",
    )
    data = pd.read_sql_query(query, connection)
    connection.close()
    return data

st.set_page_config(page_title='Dashboard', page_icon=":bar_chart:", layout='wide')
st.sidebar.title("User Input")
start_date = st.sidebar.date_input("Start Date", pd.to_datetime('2023-01-01'))
start_date = pd.to_datetime(start_date)
end_date = st.sidebar.date_input("End Date", pd.to_datetime('2023-12-31'))
end_date = pd.to_datetime(end_date)

# Task 1: Build a dashboard to `visualize the number of registered users`, and `subscribed users daily`, `weekly`, `monthly`, and `yearly`.
def users_registration_subscriptions():
    st.header(":bar_chart: User Registration and Subscription Analysis")
    query_users = "SELECT user_id, registration_date, subscribed, subscription_date FROM users;"
    data_users = get_data(query_users)
    data_users = data_users[(data_users['registration_date'] >= start_date) & (data_users['registration_date'] <= end_date)]

    if data_users.empty:
        st.warning("No data available for the selected date range. Unable to visualize.")
    else:
        data_users['registration_date'] = pd.to_datetime(data_users['registration_date'])
        data_users['subscription_date'] = pd.to_datetime(data_users['subscription_date'])

        data_users['registration_day'] = data_users['registration_date'].dt.day
        data_users['subscription_day'] = data_users['subscription_date'].dt.day
        data_users['registration_week'] = data_users['registration_date'].dt.weekday
        data_users['subscription_week'] = data_users['subscription_date'].dt.weekday
        data_users['registration_month'] = data_users['registration_date'].dt.month
        data_users['subscription_month'] = data_users['subscription_date'].dt.month
        data_users['registration_year'] = data_users['registration_date'].dt.year
        data_users['subscription_year'] = data_users['subscription_date'].dt.year

        daily_registered = data_users.groupby('registration_day').size()
        daily_subscribed = data_users[data_users['subscribed'] == 1].groupby('subscription_day').size()
        weekly_registered = data_users.groupby('registration_week').size()
        weekly_subscribed = data_users[data_users['subscribed'] == 1].groupby('subscription_week').size()
        monthly_registered = data_users.groupby('registration_month').size()
        monthly_subscribed = data_users[data_users['subscribed'] == 1].groupby('subscription_month').size()
        yearly_registered = data_users.groupby('registration_year').size()
        yearly_subscribed = data_users[data_users['subscribed'] == 1].groupby('subscription_year').size()


        st.subheader("Daily User Registration and Subscription")
        col1, col2 = st.columns(2)

        fig_registered = px.line(daily_registered, 
                                x=daily_registered.index, 
                                y=daily_registered.values, 
                                labels={'x': 'Days', 'y': 'Registered Users'}, 
                                title='Daily Registered Users')
        col1.plotly_chart(fig_registered,
                        use_container_width=True, )

        fig_subscribed = px.line(daily_subscribed, 
                                x=daily_subscribed.index, 
                                y=daily_subscribed.values, 
                                labels={'x': 'Days', 'y': 'Subscribed Users'}, 
                                title='Daily Subscribed Users')
        col2.plotly_chart(fig_subscribed, 
                        use_container_width=True)

        st.subheader("Weekly User Registration and Subscription")
        col3, col4 = st.columns(2)
        fig_weekly_registered = px.line(weekly_registered, 
                                        x=weekly_registered.index, 
                                        y=weekly_registered.values, 
                                        labels={'x': 'Week', 'y': 'Registered Users'}, 
                                        title='Weekly Registered Users')
        col3.plotly_chart(fig_weekly_registered, 
                        use_container_width=True)


        fig_weekly_subscribed = px.line(weekly_subscribed, 
                                        x=weekly_subscribed.index, 
                                        y=weekly_subscribed.values, 
                                        labels={'x': 'Week', 'y': 'Subscribed Users'}, 
                                        title='Weekly Subscribed Users')
        col4.plotly_chart(fig_weekly_subscribed, 
                        use_container_width=True)

        st.subheader("Monthly User Registration and Subscription")
        col5, col6 = st.columns(2)
        fig_monthly_registered = px.bar(monthly_registered, 
                                        x=monthly_registered.index.astype(int), 
                                        y=monthly_registered.values, 
                                        labels={'x': 'Month', 'y': 'Registered Users'}, 
                                        title='Monthly Registered Users').update_xaxes(type='category')
        col5.plotly_chart(fig_monthly_registered, 
                    use_container_width=True)

        fig_monthly_subscribed = px.bar(monthly_subscribed, 
                                        x=monthly_subscribed.index.astype(int), 
                                        y=monthly_subscribed.values, 
                                        labels={'x': 'Month', 'y': 'Subscribed Users'}, 
                                        title='Monthly Subscribed Users').update_xaxes(type='category')
        col6.plotly_chart(fig_monthly_subscribed, 
                    use_container_width=True)

        st.subheader("Yearly User Registration and Subscription")
        col7, col8 = st.columns(2)
        fig_yearly_registered = px.bar(yearly_registered, 
                                        x=yearly_registered.index.astype(int), 
                                        y=yearly_registered.values, 
                                        labels={'x': 'Year', 'y': 'Registered Users'}, 
                                        title='Yearly Registered Users').update_xaxes(type='category')
        col7.plotly_chart(fig_yearly_registered, 
                    use_container_width=True)

        fig_yearly_subscribed = px.bar(yearly_subscribed, 
                                        x=yearly_subscribed.index.astype(int), 
                                        y=yearly_subscribed.values, 
                                        labels={'x': 'Year', 'y': 'Subscribed Users'}, 
                                        title='Yearly Subscribed Users').update_xaxes(type='category')
        col8.plotly_chart(fig_yearly_subscribed, 
                    use_container_width=True)






# Task 2: Build a dashboard to visualize the `number of users subscribed` to each `bundle daily`, `weekly`, `monthly`, and `yearly`.
def subscribed_users_per_bundl():
    st.header(":bar_chart: Bundle Subscriptions Analysis")
    query_bundle = "SELECT bundle_id, if_used, creation_date FROM bundles;"
    data_bundle = get_data(query_bundle)
    data_bundle['creation_date'] = pd.to_datetime(data_bundle['creation_date'].dt.date)
    data_bundle = data_bundle[(data_bundle['creation_date'] >= start_date) & (data_bundle['creation_date'] <= end_date)]

    if data_bundle.empty:
        st.warning("No data available for the selected date range. Unable to visualize.")
    else:
        data_bundle['if_used'].value_counts()
        data_bundle['creation_date'] = pd.to_datetime(data_bundle['creation_date'])
        data_bundle['creation_day'] = data_bundle['creation_date'].dt.day
        data_bundle['creation_week'] = data_bundle['creation_date'].dt.weekday
        data_bundle['creation_month'] = data_bundle['creation_date'].dt.month
        data_bundle['creation_year'] = data_bundle['creation_date'].dt.year

        daily_subscribed_bundle = data_bundle[data_bundle['if_used'] == 1].groupby('creation_day').size()
        weekly_subscribed_bundle = data_bundle[data_bundle['if_used'] == 1].groupby('creation_week').size()
        monthly_subscribed_bundle = data_bundle[data_bundle['if_used'] == 1].groupby('creation_month').size()
        yearly_subscribed_bundle = data_bundle[data_bundle['if_used'] == 1].groupby('creation_year').size()


        st.subheader("Daily and Weekly Subscribed Users for Each Bundle")
        col9, col10 = st.columns(2)

        fig_daily_subscribed_bundle = px.bar(x=daily_subscribed_bundle.index.astype(int).tolist(), 
                                            y=daily_subscribed_bundle.values, 
                                            labels={'x': 'creation_day', 'y': 'Subscribed Users'}, 
                                            title='Daily Subscribed Users for Each Bundle').update_xaxes(type='category')
        col9.plotly_chart(fig_daily_subscribed_bundle, 
                    use_container_width=True)

        fig_weekly_subscribed_bundle = px.bar(x=weekly_subscribed_bundle.index.astype(int), 
                                            y=weekly_subscribed_bundle.values, 
                                            labels={'x': 'creation_Week', 'y': 'Subscribed Users'}, 
                                            title='Weekly Subscribed Users for Each Bundle').update_xaxes(type='category')
        col10.plotly_chart(fig_weekly_subscribed_bundle, 
                        use_container_width=True)

        st.subheader("Monthly and Yearly Subscribed Users for Each Bundle")
        col11, col12 = st.columns(2)
        fig_monthly_subscribed_bundle = px.bar(x=monthly_subscribed_bundle.index.astype(int), 
                                            y=monthly_subscribed_bundle.values,
                                            labels={'x':'creation_month', 'y': 'Subscribed Users'},
                                            title='Monthly Subscribed Users for Each Bundle').update_xaxes(type='category')
        col11.plotly_chart(fig_monthly_subscribed_bundle, 
                        use_container_width=True)

        fig_yearly_subscribed_bundle = px.bar(x=yearly_subscribed_bundle.index.astype(int), 
                                            y=yearly_subscribed_bundle.values,
                                            labels={'x': 'creation_year', 'y': 'Subscribed Users'},
                                            title='Yearly Subscribed Users for Each Bundle').update_xaxes(type='category')
        col12.plotly_chart(fig_yearly_subscribed_bundle, 
                        use_container_width=True)





# Task 3: Build a dashboard to `show all users in the 10k AI initiative`, the `number of their completed courses`, and the `information of the last completed course` like the `date of completion`, `degree` … etc
def show_10k_AI_initiative():

    # Show all users in the 10k AI initiative
    query_10k_ai_query = "SELECT user_id, registration_date, 10k_AI_initiative FROM users;"
    query_10k_ai_users = get_data(query_10k_ai_query)
    query_10k_ai_users['registration_date'] = pd.to_datetime(query_10k_ai_users['registration_date'])
    query_10k_ai_users = query_10k_ai_users[(query_10k_ai_users['registration_date'] >= start_date) & (query_10k_ai_users['registration_date'] <= end_date)]
    subscribed_users = query_10k_ai_users['10k_AI_initiative'].value_counts()

    query_completed_courses_count = """
        SELECT u.user_id, COUNT(u.course_id) as num_completed_courses, MAX(u.completion_date) as completion_date
        FROM user_completed_courses u
        JOIN users ON u.user_id = users.user_id
        WHERE users.10k_AI_initiative = 1
        GROUP BY u.user_id;
    """
    completed_courses_count = get_data(query_completed_courses_count)
    completed_courses_count['completion_date'] = pd.to_datetime(completed_courses_count['completion_date'].dt.date)
    completed_courses_count = completed_courses_count[(completed_courses_count['completion_date'] >= start_date) & (completed_courses_count['completion_date'] <= end_date)]

    fig_histogram = px.histogram(
        completed_courses_count,
        x='num_completed_courses',
        nbins=30, 
        labels={'num_completed_courses': 'Number of Completed Courses'},
        title='Number of Completed Courses for 10k AI Users'
    )


    query_completed_courses = """
    SELECT u.user_id, c.course_id, c.title, u.course_degree, u.completion_date
    FROM user_completed_courses u
    JOIN Courses c ON u.course_id = c.course_id
    WHERE u.user_id IN (SELECT user_id FROM users WHERE 10k_AI_initiative = 1);
    """
    completed_courses_info = get_data(query_completed_courses)
    completed_courses_info['completion_date'] = pd.to_datetime(completed_courses_info['completion_date'].dt.date)
    completed_courses_info = completed_courses_info[(completed_courses_info['completion_date'] >= start_date) & (completed_courses_info['completion_date'] <= end_date)]

    st.header(":bar_chart: 10k AI Initiative Analysis")
    st.subheader("Subscribed Users for 10k_AI_initiative")
    if subscribed_users.empty:
        st.warning("No data available for the selected date range. Unable to visualize.")
    else:
        st.bar_chart(subscribed_users, 
                    use_container_width=True)

    st.subheader("Number of Completed Courses and Info Courses for 10k AI Users")
    if completed_courses_count.empty:
        st.warning("No data available for the selected date range. Unable to visualize.")
    else:
        col13, col14 = st.columns(2)

        col13.plotly_chart(fig_histogram, 
                        use_container_width=True)
        col14.empty()
        
    if completed_courses_info.empty:
        st.warning("No data available for the selected date range. Unable to info.")
    else:
        user_id_input = st.text_input("Enter User ID:")
        user_id_input = int(user_id_input) if user_id_input.isdigit() else None

        if user_id_input is not None:
            user_completed_courses = completed_courses_info[completed_courses_info['user_id'] == user_id_input]

            if not user_completed_courses.empty:
                last_completed_course = user_completed_courses.sort_values(by='completion_date').iloc[-1]

                st.subheader(f"Last Completed Course Information for User {user_id_input}")
                st.write(f"Course ID: {last_completed_course['course_id']}")
                st.write(f"Course Title: {last_completed_course['title']}")
                st.write(f"Degree: {last_completed_course['course_degree']}")
                st.write(f"Completion Date: {last_completed_course['completion_date']}")
            else:
                st.warning(f"No completed courses found for User {user_id_input}")


# Task 4: Build a dashboard to `visualize all users`, the `number of their currently learning courses`, and the `number of completed courses` during this `week`, `month`, and `year`.
def users_learning_completed_courses():
    query_all_users = "SELECT user_id, registration_date FROM users;"
    data_all_users = get_data(query_all_users)
    data_all_users['registration_date'] = pd.to_datetime(data_all_users['registration_date'])
    data_all_users = data_all_users[(data_all_users['registration_date'] >= start_date) & (data_all_users['registration_date'] <= end_date)]

    query_currently_learning_count = """
    SELECT u.user_id, COUNT(DISTINCT c.course_id) as num_currently_learning_courses
    FROM users u
    LEFT JOIN capstones c ON u.user_id = c.user_id
    WHERE u.user_id IN (SELECT DISTINCT user_id FROM capstones WHERE `lock` = 0)
    GROUP BY u.user_id;
    """
    currently_learning_count = get_data(query_currently_learning_count)

    query_completed_courses_count_all = """
        SELECT u.user_id, COUNT(u.course_id) as num_completed_courses
        FROM user_completed_courses u
        GROUP BY u.user_id;
    """
    completed_courses_count_all = get_data(query_completed_courses_count_all)


    st.header(":bar_chart: All Users Analysis")
    if data_all_users.empty:
        st.warning("No data available for the selected date range. Unable to visualize.")
    else:
        data_all_users = data_all_users.merge(currently_learning_count, on='user_id', how='left')
        data_all_users = data_all_users.merge(completed_courses_count_all, on='user_id', how='left')

        data_all_users['registration_week'] = data_all_users['registration_date'].dt.weekday
        data_all_users['registration_month'] = data_all_users['registration_date'].dt.month
        data_all_users['registration_year'] = data_all_users['registration_date'].dt.year

        weekly_registered_all = data_all_users.groupby('registration_week').size()
        monthly_registered_all = data_all_users.groupby('registration_month').size()
        yearly_registered_all = data_all_users.groupby('registration_year').size()


        st.subheader("Weekly, Monthly and Yearly User Registration")
        col15, col16 = st.columns(2)
        fig_weekly_registered_all = px.line(weekly_registered_all, 
                                            x=weekly_registered_all.index, 
                                            y=weekly_registered_all.values, 
                                            labels={'x': 'Week', 'y': 'Registered Users'}, 
                                            title='Weekly Registered Users (All Users)')
        col15.plotly_chart(fig_weekly_registered_all, 
                        use_container_width=True)

        fig_monthly_registered_all = px.bar(monthly_registered_all, 
                                            x=monthly_registered_all.index.astype(int), 
                                            y=monthly_registered_all.values, 
                                            labels={'x': 'Month', 'y': 'Registered Users'}, 
                                            title='Monthly Registered Users (All Users)').update_xaxes(type='category')
        col16.plotly_chart(fig_monthly_registered_all, 
                    use_container_width=True)

        col17, col18 = st.columns(2)
        fig_yearly_registered_all = px.bar(yearly_registered_all, 
                                            x=yearly_registered_all.index.astype(int), 
                                            y=yearly_registered_all.values, 
                                            labels={'x': 'Year', 'y': 'Registered Users'}, 
                                            title='Yearly Registered Users (All Users)').update_xaxes(type='category')
        col17.plotly_chart(fig_yearly_registered_all, 
                    use_container_width=True)
        col18.empty()

    st.subheader("Number of Currently Learning")
    if currently_learning_count.empty:
        st.warning("No data available for the selected date range. Unable to visualize.")
    else:
        fig_currently_learning = px.histogram(data_all_users, 
                                            x='num_currently_learning_courses',
                                            labels={'x': 'Number of Currently Learning Courses'},
                                            title='Number of Currently Learning Courses (All Users)')
        st.plotly_chart(fig_currently_learning, 
                        use_container_width=True)

    st.subheader("Number of Completed Courses")
    if completed_courses_count_all.empty:
        st.warning("No data available for the selected date range. Unable to visualize.")
    else:
        fig_completed_courses_all = px.histogram(data_all_users, 
                                                x='num_completed_courses',
                                                labels={'x': 'Number of Completed Courses'},
                                                title='Number of Completed Courses (All Users)')
        st.plotly_chart(fig_completed_courses_all, 
                        use_container_width=True)



# Task 5: Build a dashboard to `allow us to search for a user id of a user` and see the `current user information`, the `user’s bundles`, `courses`, `completed courses`, `completed quizzes` and `degrees`, and `completed capstones` with all details.
def search_user_info():
    st.header("User Search and Information")
    user_id_search = st.text_input("Enter User ID:")
    user_id_search = int(user_id_search) if user_id_search.isdigit() else None

    if user_id_search is not None:
        query_user_info = f"SELECT * FROM users WHERE user_id = {user_id_search} AND registration_date BETWEEN '{start_date}' AND '{end_date}';"
        user_info = get_data(query_user_info)

        if not user_info.empty:
            st.subheader(f"User Information for User {user_id_search}")
            st.table(user_info)

            query_user_bundles = f"SELECT * FROM bundles WHERE user_id = {user_id_search} AND creation_date BETWEEN '{start_date}' AND '{end_date}';"
            user_bundles = get_data(query_user_bundles)
            if not user_bundles.empty:
                st.subheader(f"Bundles for User {user_id_search}")
                st.table(user_bundles)
            else:
                st.warning(f"No bundles found for User {user_id_search}")

            query_user_completed_courses = f"""
                SELECT uc.user_id, uc.course_id, c.title, uc.completion_date, uc.course_degree
                FROM user_completed_courses uc
                JOIN courses c ON uc.course_id = c.course_id
                WHERE uc.user_id = {user_id_search} AND uc.completion_date BETWEEN '{start_date}' AND '{end_date}';
            """
            user_completed_courses = get_data(query_user_completed_courses)
            if not user_completed_courses.empty:
                st.subheader(f"Completed Courses for User {user_id_search}")
                st.table(user_completed_courses)
            else:
                st.warning(f"No completed courses found for User {user_id_search}")

            query_user_completed_capstones = f"SELECT * FROM capstones WHERE user_id = {user_id_search} AND last_submission_date BETWEEN '{start_date}' AND '{end_date}';"
            user_completed_capstones = get_data(query_user_completed_capstones)
            if not user_completed_capstones.empty:
                st.subheader(f"Completed Capstones for User {user_id_search}")
                st.table(user_completed_capstones)
            else:
                st.warning(f"No completed capstones found for User {user_id_search}")
            
        else:
            st.warning(f"No information found for User {user_id_search}")
            

# Task 6: Build a dashboard to `show each admin` and the `number of capstones evaluated` for `today`, this `week`, and this `month`.
def admin_capstone_evaluation():
    st.header(":bar_chart: Admin Capstone Evaluation Analysis")
    query_admin_evaluation = f"""
        SELECT admin_id, COUNT(eval_history_id) as num_evaluations, MAX(evaluation_date) as last_evaluation_date
        FROM capstone_evaluation_history
        WHERE evaluation_date BETWEEN '{start_date}' AND '{end_date}'
        GROUP BY admin_id;
    """
    admin_evaluation_data = get_data(query_admin_evaluation)


    if admin_evaluation_data.empty:
        st.warning("No data available for the selected date range. Unable to visualize.")
    else:
        admin_evaluation_data['last_evaluation_date'] = pd.to_datetime(admin_evaluation_data['last_evaluation_date'])
        
        st.subheader("Admin Capstone Evaluation Counts")
        col23, col24 = st.columns(2)

        fig_admin_evaluations = px.bar(
            admin_evaluation_data,
            x='admin_id',
            y='num_evaluations',
            labels={'x': 'Admin ID', 'y': 'Number of Evaluations'},
            title='Admin Capstone Evaluation Counts'
        )
        col23.plotly_chart(fig_admin_evaluations, use_container_width=True)

        fig_last_evaluation_date = px.bar(
            admin_evaluation_data,
            x='admin_id',
            y='last_evaluation_date',
            labels={'x': 'Admin ID', 'y': 'Last Evaluation Date'},
            title='Admin Last Evaluation Date'
        )
        fig_last_evaluation_date.update_layout(yaxis=dict(type='category'))
        col24.plotly_chart(fig_last_evaluation_date, use_container_width=True)


# Task 7: Build a dashboard to `show each user’s capstone` and the `evaluation history` of this capstone.
def user_capstone_evaluation_history():
    st.header(":bar_chart: User Capstone and Evaluation History")
    admin_id_input = st.text_input("Enter Admin ID:")
    query_user_capstones = f"""
        SELECT c.user_id, c.course_id, c.chapter_id, c.lesson_id, c.degree, c.last_submission_date, c.reviewed, c.revision_date,
               eh.admin_id, eh.degree as eval_degree, eh.evaluation_date
        FROM capstones c
        LEFT JOIN capstone_evaluation_history eh ON c.user_id = eh.user_id AND c.course_id = eh.course_id
        WHERE eh.admin_id = {admin_id_input} AND c.last_submission_date BETWEEN '{start_date}' AND '{end_date}';
    """
    user_capstones_data = get_data(query_user_capstones)

    if user_capstones_data.empty:
        st.warning("No data available for the selected admin ID and date range. Unable to visualize.")
    else:
        user_capstones_data['last_submission_date'] = pd.to_datetime(user_capstones_data['last_submission_date'])
        user_capstones_data['evaluation_date'] = pd.to_datetime(user_capstones_data['evaluation_date'])

        st.subheader("User Capstone Info and Evaluation History")
        capstone_info_evaluation = pd.merge(user_capstones_data, 
                               user_capstones_data, 
                               how='inner', 
                               on=['user_id', 'course_id', 'chapter_id', 'lesson_id'])
        st.table(capstone_info_evaluation)
        
# Task 8: Build a dashboard to `show all coupons` and the `number of actual users who used these coupons`.
def coupons_users_count():
    st.header(":gift: Coupons and User Usage")
    query_coupons_users = f"""
        SELECT coupon, COUNT(DISTINCT user_id) as num_users
        FROM users
        WHERE subscription_date BETWEEN '{start_date}' AND '{end_date}' AND coupon IS NOT NULL
        GROUP BY coupon;
    """
    coupons_users_data = get_data(query_coupons_users)

    if coupons_users_data.empty:
        st.warning("No coupon data available. Unable to visualize.")
    else:
        st.subheader("Coupons and User Usage")
        st.table(coupons_users_data)


# Task 9: Build a dashboard to `show the number of users` grouped by `age`, and `study degree`.
def users_grouped_by_age_degree():
    st.header(":bar_chart: Users Grouped by Age and Study Degree")

    query_users_grouped = f"""
        SELECT age, study_degree, COUNT(user_id) as num_users
        FROM users
        WHERE registration_date BETWEEN '{start_date}' AND '{end_date}'
        GROUP BY age, study_degree;
    """
    users_grouped_data = get_data(query_users_grouped)

    if users_grouped_data.empty:
        st.warning("No user data available. Unable to visualize.")
    else:
        fig = px.bar(users_grouped_data, 
                     x='age', 
                     y='num_users', 
                     color='study_degree', 
                     barmode='group',
                     labels={'num_users': 'Number of Users'}, 
                     title='Users Grouped by Age and Study Degree', 
                    color_discrete_sequence=['#FF5733', '#33FF57']) 
        st.plotly_chart(fig, use_container_width=True)
 
# Task 10: Build a dashboard to `show all users` and their `employment grant status` and `history`, 
# in addition to `all employment grant status with the number of users in this status`.
def users_employment_grant_status():
    st.header(":clipboard: Users Employment Grant Status and History")
    query_users_employment_grant = f"""
        SELECT u.user_id, u.fresh_grad, u.education_title, u.military_status, u.ability_to_travel,
               u.avilable_city_to_travel, u.work_remotly, u.full_time, u.english_level, u.status, u.application_date,
               a.submitted, a.preparation, a.pending, a.hold, a.inreview, a.shortlisted, a.postponed, a.accepted
        FROM users_employment_grant u
        LEFT JOIN users_employment_grant_actions a ON u.user_id = a.user_id
        WHERE u.application_date BETWEEN '{start_date}' AND '{end_date}'
        ORDER BY u.application_date DESC;
    """
    users_employment_grant_data = get_data(query_users_employment_grant)

    if users_employment_grant_data.empty:
        st.warning("No user employment grant data available. Unable to visualize.")
    else:
        st.subheader("All Users and Employment Grant Status/History")
        st.dataframe(users_employment_grant_data)

        st.subheader("Employment Grant Status Summary")
        status_counts = users_employment_grant_data['status'].value_counts()
        fig = px.bar(x=status_counts.index, 
                     y=status_counts.values, 
                     labels={'x': 'Status', 'y': 'Number of Users'},
                     title="Employment Grant Status Summary")
        st.plotly_chart(fig,
                    use_container_width=True)
        

# Sidebar navigation
selected_page = st.sidebar.selectbox(
    "Select a task",
    ["Users Reg/Sub", 
     "Subs Per Bundle", 
     "Show 10k AI", 
     "Users Learning Courses",
     "Search User Info", 
     "Admin Cap Eval", 
     "User Cap Eval History", 
     "Coupons Users Count",
     "Users Grouped by Age/Degree", 
     "Users Employ Grant Status"]
)

if selected_page == "Users Reg/Sub":
    users_registration_subscriptions()
elif selected_page == "Subs Per Bundle":
    subscribed_users_per_bundl()
elif selected_page == "Show 10k AI":
    show_10k_AI_initiative()
elif selected_page == "Users Learning Courses":
    users_learning_completed_courses()
elif selected_page == "Search User Info":
    search_user_info()
elif selected_page == "Admin Cap Eval":
    admin_capstone_evaluation()
elif selected_page == "User Cap Eval History":
    user_capstone_evaluation_history()
elif selected_page == "Coupons Users Count":
    coupons_users_count()
elif selected_page == "Users Grouped by Age/Degree":
    users_grouped_by_age_degree()
elif selected_page == "Users Employ Grant Status":
    users_employment_grant_status()