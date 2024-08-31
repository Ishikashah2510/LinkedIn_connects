import pandas as pd
from vars import *
import time
import linkedin_helper
import chatgpt_helper
import connect_helper


def read_data(path_to_excel):
    data = pd.read_excel(path_to_excel, header=0)
    return data


def process_data(collected_data):
    not_okay = []

    for index, row in collected_data.iterrows():
        print(f"Working on data for company: {row['Company_name']}")

        updated_company_link = row['Company_link'] + f'people/?facetGeoRegion={geo_region}&keywords=' + row['keyword'].replace(' ', '%20')

        linkedin_profiles = linkedin_helper.main(updated_company_link)
        if not linkedin_profiles:
            not_okay.append(row['Company_name'])

        names = linkedin_profiles.values()

        filtered_profiles = chatgpt_helper.main(names, linkedin_profiles)
        if not filtered_profiles:
            not_okay.append(row['Company_name'])

        all_good = connect_helper.main(filtered_profiles, row['role'], row['Company_name'])

        if not all_good:
            not_okay.append(row['Company_name'])

    return not_okay


if __name__ == '__main__':
    print("Hi there!")

    print("Open your Chrome browser and leave it")
    print(f"Code going to sleep for {sleep_time} seconds")
    time.sleep(sleep_time)

    data = read_data(excel_path)
    perform_all_ops = process_data(data)

    if perform_all_ops:
        print("Something went wrong for the following companies: {}".format(perform_all_ops))

    print("All done, goodbye! :)")

