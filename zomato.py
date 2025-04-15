import streamlit as st
import pandas as pd
import numpy as np
import mysql.connector
con=mysql.connector.connect(host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",user="3RnQcMjpUJBd2DC.root",port=4000,password="v54Vy0yMLlVESgkm",database='zomato')
cursor=con.cursor()



st.markdown(
    """
    <h1 style="text-align: center;color:Red;">ZOMATO</h1>
    <h6 style="text-align: center;color:blue;">Tastes like home!</h6>
""",
unsafe_allow_html=True
)
st.title('Zomato ')
st.subheader('Tastes like home!')
page=st.sidebar.selectbox("page",["Home","CUSTOMERS_table",'restaurant_table','order_table','deliveries_table','Delivery_persons_table','None'])

if page=="Home":
    st.image("https://www.google.com/imgres?q=zomato&imgurl=https%3A%2F%2Finc42.com%2Fwp-content%2Fuploads%2F2023%2F02%2Fzomato-social.png&imgrefurl=https%3A%2F%2Finc42.com%2Fbuzz%2Fzomato-launches-rebranded-meal-service-zomato-everyday%2F&docid=nVn0eKXO4qovRM&tbnid=M5YIZVUzFQx6zM&vet=12ahUKEwiT0svZos-LAxViQ2cHHZJkIocQM3oECFAQAA..i&w=1200&h=628&hcb=2&ved=2ahUKEwiT0svZos-LAxViQ2cHHZJkIocQM3oECFAQAA")
        

elif page not in ['Home']:
    st.write(page,"is table selected")

if page=="CUSTOMERS_table":
    cursor.execute('select * from CUSTOMERS_table')
    cust_data=cursor.fetchall()
    columns=[j[0] for j in cursor.description]
    cust_df=pd.DataFrame(cust_data,columns=columns)
    st.dataframe(cust_df)

elif page=="restaurant_table":
    cursor.execute('select * from restaurant_table')
    rest_data=cursor.fetchall()
    columns=[j[0] for j in cursor.description]
    rest_df=pd.DataFrame(rest_data,columns=columns)
    st.dataframe(rest_df)

elif page=="order_table":
    cursor.execute('select * from order_table')
    ord_data=cursor.fetchall()
    columns=[j[0] for j in cursor.description]
    ord_df=pd.DataFrame(ord_data,columns=columns)
    st.dataframe(ord_df)

elif page=="deliveries_table":
    cursor.execute('select * from deliveries_table')
    deli_data=cursor.fetchall()
    columns=[j[0] for j in cursor.description]
    deliv_df=pd.DataFrame(deli_data,columns=columns)
    st.dataframe(deliv_df)

elif page=="Delivery_persons_table":
    cursor.execute('select * from Delivery_persons_table')
    dp_data=cursor.fetchall()
    columns=[j[0] for j in cursor.description]
    dpt_df=pd.DataFrame(dp_data,columns=columns)
    st.dataframe(dpt_df)

elif page=="None":
    st.write("")


Query_list=st.sidebar.selectbox("Query_list",['query1','query2','query3','query4','query5','query6','query7','query8','query9',
                                      'query10','query11','query12','query13','query14','query15','query16','query17','query18',
                                      'query19','query20','None'])

if Query_list=="query1":
    st.markdown("<h2>Find the total number of customers</h2>",unsafe_allow_html=True)
    st.markdown("<h4>Query: </h4>",unsafe_allow_html=True)
    # st.text_area("Find the total customer count")
    st.write("select count(customer_id) as cnt from CUSTOMERS_table")
    st.markdown("<h3>output: </h3>",unsafe_allow_html=True)
    cursor.execute("select count(customer_id) as cnt from CUSTOMERS_table")
    result=cursor.fetchall()
    st.write('Total number of custmores in customer table is :',result[0])

if Query_list=="query2":
    st.markdown("<h2>Find the top 5 customer based on the amount  </h2>",unsafe_allow_html=True)
    st.markdown("<h4>Query: </h4>",unsafe_allow_html=True)
    st.write("""select Customer_id,Sum(total_amount) as sum_amt from order_table 
             group by customer_id
             order by sum_amt desc
             limt 5
    """)
    st.markdown("<h3>output: </h3>",unsafe_allow_html=True)
    cursor.execute("select customer_id,sum(total_amount) as sum_amt from order_table group by customer_id order by sum_amt desc limit 5")
    result=cursor.fetchall()
    columns=[j[0]for j in cursor.description]
    df=pd.DataFrame(result,columns=columns)
    st.dataframe(df)

if Query_list=="query3":
    st.markdown("<h2>Find the amount spend by different mode of payment  </h2>",unsafe_allow_html=True)
    st.markdown("<h4>Query: </h4>",unsafe_allow_html=True)
    st.write("""select payment_mode,sum(total_amount) as sum_amt from order_table
              group by payment_mode order by sum_amt desc
    """)
    st.markdown("<h3>output: </h3>",unsafe_allow_html=True)
    cursor.execute("select payment_mode,sum(total_amount) as sum_amt from order_table group by payment_mode order by sum_amt desc")
    result=cursor.fetchall()
    columns=[j[0]for j in cursor.description]
    df=pd.DataFrame(result,columns=columns)
    st.dataframe(df)

if Query_list=="query4":
    st.markdown("<h2>Find the total delivery done by vehicle type  </h2>",unsafe_allow_html=True)
    st.markdown("<h4>Query: </h4>",unsafe_allow_html=True)
    st.write("""select vehicle_type,count(total_deliveries)  as cnt_total_deliver from Delivery_persons_table
              group by vehicle_type
    """)
    st.markdown("<h3>output: </h3>",unsafe_allow_html=True)
    cursor.execute("select vehicle_type,count(total_deliveries)  as cnt_total_deliver from Delivery_persons_table group by vehicle_type")
    result=cursor.fetchall()
    columns=[j[0]for j in cursor.description]
    df=pd.DataFrame(result,columns=columns)
    st.dataframe(df)

if Query_list=="query5":
    st.markdown("<h2>Find the sum of amount based on Restaurant name  </h2>",unsafe_allow_html=True)
    st.markdown("<h4>Query: </h4>",unsafe_allow_html=True)
    st.write("""select distinct a.name ,sum(b.total_amount) as amount from restaurant_table as a 
             left join order_table as b on a.restaurant_id=b.restaurant_id group by a.name

    """)
    st.markdown("<h3>output: </h3>",unsafe_allow_html=True)
    cursor.execute("select distinct a.name ,sum(b.total_amount) as amount from restaurant_table as a left join order_table as b on a.restaurant_id=b.restaurant_id group by a.name")
    result=cursor.fetchall()
    columns=[j[0]for j in cursor.description]
    df=pd.DataFrame(result,columns=columns)
    st.dataframe(df)

if Query_list=="query6":
    st.markdown("<h2>Find the sum of amount based on cuisine type   </h2>",unsafe_allow_html=True)
    st.markdown("<h4>Query: </h4>",unsafe_allow_html=True)
    st.write("""select a.cuisine_type ,sum(b.total_amount) as amount from restaurant_table as a 
             left join order_table as b on a.restaurant_id=b.restaurant_id group by a.cuisine_type


    """)
    st.markdown("<h3>output: </h3>",unsafe_allow_html=True)
    cursor.execute("select a.cuisine_type ,sum(b.total_amount) as amount from restaurant_table as a left join order_table as b on a.restaurant_id=b.restaurant_id group by a.cuisine_type")
    result=cursor.fetchall()
    columns=[j[0]for j in cursor.description]
    df=pd.DataFrame(result,columns=columns)
    st.dataframe(df)

if Query_list=="query7":
    st.markdown("<h2> Count of orders based on the delivery status  </h2>",unsafe_allow_html=True)
    st.markdown("<h4>Query: </h4>",unsafe_allow_html=True)
    st.write("""select delivery_status,count(order_id) as cnt from Deliveries_table group by delivery_status


    """)
    st.markdown("<h3>output: </h3>",unsafe_allow_html=True)
    cursor.execute("select delivery_status,count(order_id) as cnt from Deliveries_table group by delivery_status")
    result=cursor.fetchall()
    columns=[j[0]for j in cursor.description]
    df=pd.DataFrame(result,columns=columns)
    st.dataframe(df)

if Query_list=="query8":
    st.markdown("<h2> Find the Average  rating for cuisine  </h2>",unsafe_allow_html=True)
    st.markdown("<h4>Query: </h4>",unsafe_allow_html=True)
    st.write("""select distinct cuisine_type,round(avg(rating),2) as avg_rating from restaurant_table 
             group by cuisine_type
    """)
    st.markdown("<h3>output: </h3>",unsafe_allow_html=True)
    cursor.execute("select distinct cuisine_type,round(avg(rating),2) as avg_rating from restaurant_table group by cuisine_type")
    result=cursor.fetchall()
    columns=[j[0]for j in cursor.description]
    df=pd.DataFrame(result,columns=columns)
    st.dataframe(df)

if Query_list=="query9":
    st.markdown("<h2> find the total order for south indian preferred cuisine </h2>",unsafe_allow_html=True)
    st.markdown("<h4>Query: </h4>",unsafe_allow_html=True)
    st.write("""select preferred_cuisine,sum(total_orders) as sum_orders  from CUSTOMERS_table where preferred_cuisine in ('Karnataka (Udupi, Mangalorean, Kodava, North Karnataka)',
'Tamil (Chettinad, Kongunadu)','Telangana','Kerala (Malabar, Syrian Christian, Nair)'
)
group by preferred_cuisine order by sum_orders desc
    """)
    st.markdown("<h3>output: </h3>",unsafe_allow_html=True)
    cursor.execute("select preferred_cuisine,sum(total_orders) as sum_orders  from CUSTOMERS_table where preferred_cuisine in ('Karnataka (Udupi, Mangalorean, Kodava, North Karnataka)','Tamil (Chettinad, Kongunadu)','Telangana','Kerala (Malabar, Syrian Christian, Nair)')group by preferred_cuisine order by sum_orders desc")
    result=cursor.fetchall()
    columns=[j[0]for j in cursor.description]
    df=pd.DataFrame(result,columns=columns)
    st.dataframe(df)

if Query_list=="query10":
    st.markdown("<h2> find the total amount with out discount by payment method </h2>",unsafe_allow_html=True)
    st.markdown("<h4>Query: </h4>",unsafe_allow_html=True)
    st.write("""select a.payment_mode,a.discount_applied,sum(total_amount) as amount from order_table as a where discount_applied='No' 
  group by a.payment_mode ,a.discount_applied;
    """)
    st.markdown("<h3>output: </h3>",unsafe_allow_html=True)
    cursor.execute("select a.payment_mode,a.discount_applied,sum(total_amount) as amount from order_table as a where discount_applied='No' group by a.payment_mode ,a.discount_applied")
    result=cursor.fetchall()
    columns=[j[0]for j in cursor.description]
    df=pd.DataFrame(result,columns=columns)
    st.dataframe(df)

if Query_list=="query11":
    st.markdown("<h2> find the customer count more then 5 for the preferred cuisine </h2>",unsafe_allow_html=True)
    st.markdown("<h4>Query: </h4>",unsafe_allow_html=True)
    st.write(""" select preferred_cuisine ,count(customer_id) as Count from CUSTOMERS_table group by preferred_cuisine  having count>=5 
    """)
    st.markdown("<h3>output: </h3>",unsafe_allow_html=True)
    cursor.execute(" select preferred_cuisine ,count(customer_id) as Count from CUSTOMERS_table group by preferred_cuisine  having count>=5 ")
    result=cursor.fetchall()
    columns=[j[0]for j in cursor.description]
    df=pd.DataFrame(result,columns=columns)
    st.dataframe(df)

if Query_list=="query12":
    st.markdown("<h2> find the restaurant Average rating </h2>",unsafe_allow_html=True)
    st.markdown("<h4>Query: </h4>",unsafe_allow_html=True)
    st.write("""  select name,round(avg(rating),2) as avg_rating from restaurant_table group by name order by avg_rating desc
    """)
    st.markdown("<h3>output: </h3>",unsafe_allow_html=True)
    cursor.execute("  select name,round(avg(rating),2) as avg_rating from restaurant_table group by name order by avg_rating desc ")
    result=cursor.fetchall()
    columns=[j[0]for j in cursor.description]
    df=pd.DataFrame(result,columns=columns)
    st.dataframe(df)

if Query_list=="query13":
    st.markdown("<h2> find the Number of orders delivered by vehicle types </h2>",unsafe_allow_html=True)
    st.markdown("<h4>Query: </h4>",unsafe_allow_html=True)
    st.write("""  select vehicle_type,count(order_id) as order_cnt from Deliveries_table group by vehicle_type

    """)
    st.markdown("<h3>output: </h3>",unsafe_allow_html=True)
    cursor.execute(" select vehicle_type,count(order_id) as order_cnt from Deliveries_table group by vehicle_type ")
    result=cursor.fetchall()
    columns=[j[0]for j in cursor.description]
    df=pd.DataFrame(result,columns=columns)
    st.dataframe(df)

if Query_list=="query14":
    st.markdown("<h2> find the Number of orders delivered based on the restaurant name </h2>",unsafe_allow_html=True)
    st.markdown("<h4>Query: </h4>",unsafe_allow_html=True)
    st.write("""  select a.name as restaurant_name,count(b.order_id) as amount from restaurant_table as a left join order_table as b on a.restaurant_id=b.restaurant_id
where status='Delivered' group by a.name  order by amount desc
    """)
    st.markdown("<h3>output: </h3>",unsafe_allow_html=True)
    cursor.execute(" select a.name as restaurant_name,count(b.order_id) as amount from restaurant_table as a left join order_table as b on a.restaurant_id=b.restaurant_id where status='Delivered' group by a.name  order by amount desc; ")
    result=cursor.fetchall()
    columns=[j[0]for j in cursor.description]
    df=pd.DataFrame(result,columns=columns)
    st.dataframe(df)

if Query_list=="query15":
    st.markdown("<h2> find the avgrage  delivery time </h2>",unsafe_allow_html=True)
    st.markdown("<h4>Query: </h4>",unsafe_allow_html=True)
    st.write("""  select round(avg(MINUTE(delivery_time)),2) as avg_mint from Deliveries_table 
    """)
    st.markdown("<h3>output: </h3>",unsafe_allow_html=True)
    cursor.execute(" select round(avg(MINUTE(delivery_time)),2) as avg_mint from Deliveries_table  ")
    result=cursor.fetchall()
    columns=[j[0]for j in cursor.description]
    df=pd.DataFrame(result,columns=columns)
    st.dataframe(df)

if Query_list=="query16":
    st.markdown("<h2> find the avgrage  delivery time by vechicle </h2>",unsafe_allow_html=True)
    st.markdown("<h4>Query: </h4>",unsafe_allow_html=True)
    st.write("""  sselect vehicle_type,round(avg(MINUTE(delivery_time)),2) as avg_mint from Deliveries_table group by vehicle_type
 
    """)
    st.markdown("<h3>output: </h3>",unsafe_allow_html=True)
    cursor.execute(" select vehicle_type,round(avg(MINUTE(delivery_time)),2) as avg_mint from Deliveries_table group by vehicle_type")
    result=cursor.fetchall()
    columns=[j[0]for j in cursor.description]
    df=pd.DataFrame(result,columns=columns)
    st.dataframe(df)

if Query_list=="query17":
    st.markdown("<h2> find the avgrage  delivery time by restaurant name </h2>",unsafe_allow_html=True)
    st.markdown("<h4>Query: </h4>",unsafe_allow_html=True)
    st.write(""" select a.name as restaurant_name,round(avg(MINUTE(delivery_time)),2) as avg_mint 
             from restaurant_table as a left join order_table as b on a.restaurant_id=b.restaurant_id group by a.name
    """)
    st.markdown("<h3>output: </h3>",unsafe_allow_html=True)
    cursor.execute(" select a.name as restaurant_name,round(avg(MINUTE(delivery_time)),2) as avg_mint from restaurant_table as a left join order_table as b on a.restaurant_id=b.restaurant_id group by a.name")
    result=cursor.fetchall()
    columns=[j[0]for j in cursor.description]
    df=pd.DataFrame(result,columns=columns)
    st.dataframe(df)

if Query_list=="query18":
    st.markdown("<h2> find the max distance delivery  by car and bike </h2>",unsafe_allow_html=True)
    st.markdown("<h4>Query: </h4>",unsafe_allow_html=True)
    st.write(""" select vehicle_type,max(distance) as max from Deliveries_table group by vehicle_type
    """)
    st.markdown("<h3>output: </h3>",unsafe_allow_html=True)
    cursor.execute(" select vehicle_type,max(distance) as max from Deliveries_table group by vehicle_type")
    result=cursor.fetchall()
    columns=[j[0]for j in cursor.description]
    df=pd.DataFrame(result,columns=columns)
    st.dataframe(df)

if Query_list=="query19":
    st.markdown("<h2> find the customer count based on gold  and normal </h2>",unsafe_allow_html=True)
    st.markdown("<h4>Query: </h4>",unsafe_allow_html=True)
    st.write(""" select is_premium as premium,count(CUSTOMER_ID) as number_of_cust from CUSTOMERS_table group by is_premium
    """)
    st.markdown("<h3>output: </h3>",unsafe_allow_html=True)
    cursor.execute(" select is_premium as premium,count(CUSTOMER_ID) as number_of_cust from CUSTOMERS_table group by is_premium ")
    result=cursor.fetchall()
    columns=[j[0]for j in cursor.description]
    df=pd.DataFrame(result,columns=columns)
    st.dataframe(df)

if Query_list=="query20":
    st.markdown("<h2> find the count of active custmoer by restaurant </h2>",unsafe_allow_html=True)
    st.markdown("<h4>Query: </h4>",unsafe_allow_html=True)
    st.write(""" select  a.name as  restaurant_name,a.is_active as Active, count(customer_id) as cust_count 
             from restaurant_table as a left join order_table as b on a.restaurant_id=b.restaurant_id where is_active='Acitve'group by 1,2;

    """)
    st.markdown("<h3>output: </h3>",unsafe_allow_html=True)
    cursor.execute("select  a.name as  restaurant_name,a.is_active as Active, count(customer_id) as cust_count from restaurant_table as a left join order_table as b on a.restaurant_id=b.restaurant_id where is_active='Acitve'group by 1,2")
    result=cursor.fetchall()
    columns=[j[0]for j in cursor.description]
    df=pd.DataFrame(result,columns=columns)
    st.dataframe(df)

elif Query_list=="None":
    st.write("")  

st.title("CRUD Operations with Streamlit and MySQL")

choose_operation=st.sidebar.selectbox("select operation",['Create','Read','Update','Delete','None'])
#option=st.selectbox("choose an operation:",['Create','Read','Update','Delete','None'])

if choose_operation=='Create':
    st.subheader("create a record")
    name=st.text_input("Name")
    age=st.number_input("Age",min_value=0)
    email=st.text_input("Enter email")
    if st.button("CREAT"):
        sql="insert into new_table(name,age,email) values(%s,%s,%s)"
        val=(name,age,email)
        cursor.execute(sql,val)
        con.commit()
        st.success("Record created successfully!")

if choose_operation=='Read':
    st.subheader("Read Operations")
    cursor.execute('select * from new_table')
    result=cursor.fetchall()
    columns=[i[0] for i in cursor.description]
    show_df=pd.DataFrame(result,columns=columns)
    st.dataframe(show_df)

if choose_operation=='Update':
    st.subheader('update Record Operation')
    id=st.number_input('Enter Id',min_value=0 )
    name=st.text_input('New name')
    age=st.number_input('New age',min_value=0)
    email=st.text_input('New email')
    if st.button('UPDATE'):
        sql='update new_table set name=%s,age=%s,email=%s where id=%s'
        val=(name,age,email,id)
        cursor.execute(sql,val)
        con.commit()
        st.success('updated successfully')
if choose_operation=='Delete':
    st.subheader('Delete Record operation')
    id=st.number_input('Enter ID',min_value=0)
    if st.button('Delete'):
        sql='delete from new_table where id=%s'
        val=(id,)
        cursor.execute(sql,val)
        con.commit()
        st.success("Record deleted successfully")
elif choose_operation=="None":
    st.write("")

