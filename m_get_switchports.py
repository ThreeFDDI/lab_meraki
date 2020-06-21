import meraki
from pprint import pprint

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

serial = 'Q2HP-Q9S8-BVHB'

response = dashboard.switch_ports.getDeviceSwitchPortStatuses(
    serial
)

for port in response:
    if port["status"] == "Connected":
        pprint(port['portId'])
    