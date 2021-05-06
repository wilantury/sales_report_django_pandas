# Python
import uuid, base64
from io import BytesIO
from matplotlib import colors
# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
# models
from customers.models import Customer
from profiles.models import Profile

def generate_code():
    code = str(uuid.uuid4()).replace('-', '').upper()[:12]
    
    return code

def get_salesman_from_id(val):
    salesman = Profile.objects.get(id=val)
    return salesman.user.username

def get_customer_from_id(val):
    customer = Customer.objects.get(id=val)
    return customer

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_key(res_by):
    key = None
    if res_by == '#1':
        key = 'transaction_id'
    elif res_by == '#2':
        key = 'created'
    return key

def get_chart(chart_type, data, results_by,**kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10,4))
    key = get_key(results_by)
    group_data = data.groupby(key, as_index=False)['total_price'].agg('sum')
    if chart_type == '#1': # bar chart
        # plt.bar(group_data[key], group_data['total_price'])
        # sns.barplot(x='transaction_id', y='price', data=data)
        sns.barplot(x=key, y='total_price', data=group_data)
    elif chart_type == '#2': # pie chart
        # labels = kwargs.get('labels')
        plt.pie(data=group_data, x='total_price', labels=group_data[key].values)
    elif chart_type == '#3': # line chart
        # plt.plot(data['transaction_id'], data['price'], color='green', marker='o', linestyle='dashed')
        plt.plot(group_data[key], group_data['total_price'], color='green', marker='o', linestyle='dashed')
    else:
        print('ups... Wrong chart type')
    plt.tight_layout()
    chart = get_graph()
    return chart