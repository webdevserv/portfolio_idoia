import streamlit as st
from datetime import date, datetime, timedelta

import yfinance as yf
import pandas as pd
from prophet import Prophet
from prophet.plot import plot_plotly


from plotly import graph_objs as go

TODAY = date.today().strftime("%Y-%m-%d")

st.title("Stock Predictor App")

stocks=("GOOGL","NVDIA","MSFT","META","MELI")
selected_stock = st.selectbox("Select ticker symbol", stocks)

#select history
yearsago = (1, 2, 4, 6, 8, 10, 12, 14)
selected_history = st.selectbox("Select years of history to view", yearsago)

today = datetime.now()
x_years_ago = today - timedelta(days=365*selected_history)
start_date = x_years_ago.strftime('%Y-%m-%d')

n_years = st.slider("Years of prediction:", 1, 4)
period = n_years * 365
end_date = today + timedelta(days=period)

#data = yf.download("SPY AAPL", start="2017-01-01", end="2017-04-30")

#data cached with decorator
@st.cache_data
def load_data(ticker):
    data = yf.download(ticker,start_date, end_date)
    #date in first col
    data.reset_index(inplace=True)
    return data
data_load_state = st.text("Loading data..")
data = load_data(selected_stock)
data_load_state.text("Loading data...completed.")


st.subheader('Raw data from ' + x_years_ago.strftime('%m-%d-%Y') + " to " + end_date.strftime('%m-%d-%Y'))
st.write(data.tail())

def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'],y=data['Open'],name='stock_open'))
    fig.add_trace(go.Scatter(x=data['Date'],y=data['Close'],name='stock_close'))
    fig.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw_data()

#Forecasting
df_train = data[['Date','Close']]
df_train = df_train.rename(columns={'Date':'ds', 'Close':'y'})

m = Prophet()
m.fit(df_train)
#dataframes
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

st.subheader('Forecast data')
st.write(forecast.tail())

st.write('forecast data')
fig1 = plot_plotly(m,forecast)
st.plotly_chart(fig1)

st.write('forecast components')
fig2 = m.plot_components(forecast)
st.write(fig2)