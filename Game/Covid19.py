from covid import Covid
covid=Covid(source='worldometers')
#data=covid.get_data()
countries=covid.get_status_by_country_name('bangladesh')

print(countries)
death=countries['deaths']
print(death)