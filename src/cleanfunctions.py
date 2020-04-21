from pymongo import MongoClient
import pandas as pd

def officeToGeoPoint(row):
    office = row.offices
    if type(office) == dict:
        if 'latitude' in office and 'longitude' in office:
            if(type(office["latitude"])) == float and type(office["longitude"]) == float:
                return ({
                    "type":"Point",
                    "coordinates":[office["longitude"],office["latitude"]]
                },"success")
            else:
                return(None,"Invalid lat lat and long")
        else:
            return (None,"No lat and long keys in office dict")
    return (None,"No office")

def clean(db):

    all_offices = list(db.companies.find({},{"offices":1,"name":1,"category_code":1,"total_money_raised":1}))
    companydata = pd.DataFrame(all_offices)
    companydata = companydata.explode("offices")
    officesdf= companydata[["offices"]].apply(lambda x: x.offices, result_type="expand",axis=1)
    companydata =pd.concat([companydata,officesdf],axis=1)
    cleaned_offices = companydata.apply(officeToGeoPoint,axis=1, result_type="expand")
    cleaned_offices.columns = ["office","clean_state"]   
    data_cleaned = pd.concat([companydata,cleaned_offices], axis=1)
    data_cleaned = data_cleaned[["name","category_code","office","clean_state","city","country_code","latitude","longitude","total_money_raised"]]
    data_cleaned = data_cleaned.drop(data_cleaned[data_cleaned["clean_state"]=="Invalid lat lat and long"].index)
    company_processed = data_cleaned.drop(data_cleaned[data_cleaned["clean_state"]=="No office"].index)
    company_processed.to_json("OUTPUT/companies_clean.json",orient="records")
    return company_processed




