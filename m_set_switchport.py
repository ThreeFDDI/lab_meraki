import meraki
from pprint import pprint

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(
    api_key=API_KEY,
    output_log=False,
    print_console=False    
    )

serial = 'Q2HP-Q9S8-BVHB'
number = '7'

response = dashboard.switch_ports.updateDeviceSwitchPort(
    serial, number, 
    name='My switch port', 
    tags='tag1 tag2', 
    enabled=True, 
    type='access', 
    vlan=666, 
    voiceVlan=20, 
)

print(response)