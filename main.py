from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

from converter.schemas.date_schema import DateConvertSchema
from utils.http.schemas.response_schema import BaseResponse, FailureResponse, SuccessResponse

app = FastAPI(
    title="AD2BS", 
    version="1.0.1", 
    description="""
AD2BS is a powerful and versatile API designed to convert between two widely used date systems: Nepali Bikram Sambat (BS) and Gregorian (AD). This API offers seamless two-way conversion, making it easy to switch between these two calendars with just a few lines of code. Whether you're working on a project that requires a deep understanding of both calendars, or simply need to convert dates for display purposes, AD2BS is the perfect solution. With its fast and accurate algorithms, you can be sure that your conversions will be accurate and reliable, every time.
"""
)



@app.post("/tobs/", tags=["AD TO BS"], description="This API endpoint converts  Gregorian (AD) date to Nepali BS date (Bikram Samwat) by taking the year, month, and day as body parameters in JSON format.")
def convert_ad_to_bs(body: DateConvertSchema):
    try:
        r = requests.post('https://www.ashesh.com.np/linkdate-converter.php', data={
            'year': body.year,
            'month': body.month,
            'day': body.day,
            'submit': 'convert'
        })
        soup = BeautifulSoup(r.text, 'lxml')
        bs_date = (soup.select(".inner")[1].text)[5:]
    except Exception as e:
        return FailureResponse(result="something went wrong cannot convert the date.")
    return SuccessResponse(result=bs_date).dict()


@app.post("/toad/", tags=["BS TO AD"], description="This API endpoint converts Nepali BS date (Bikram Samwat) to Gregorian (AD) date by taking the year, month, and day as body parameters in JSON format.")
def convert_bs_to_ad(body: DateConvertSchema):
    try:
        r = requests.post('https://www.ashesh.com.np/linkdate-converter.php', data={
            'year': body.year,
            'month': body.month,
            'day': body.day,
            'submit': 'convert'
        })
        soup = BeautifulSoup(r.text, 'lxml')
        ad_date = (soup.select(".inner")[1].text)[3:].strip()
    except Exception as e:
        return FailureResponse(result="something went wrong cannot convert the date.")
    return SuccessResponse(result=ad_date).dict()
