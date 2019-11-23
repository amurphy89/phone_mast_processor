# from pprint import pprint

class Mast:

    def __init__(self, property_name, address1, address2, address3, address4, unit_name, tenant_name, lease_start_date,
     lease_end_date, lease_years, current_rent):

        self.property_name = property_name
        self.address1 = address1
        self.address2 = address2
        self.address3 = address3
        self.address4 = address4
        self.unit_name = unit_name
        self.tenant_name = tenant_name
        self.lease_start_date = lease_start_date
        self.lease_end_date = lease_end_date 
        self.lease_years = lease_years
        self.current_rent = current_rent

    

    def to_dict(self):
        return {
            "Property Name": self.property_name,
            "Address Line 1": self.address1,
            "Address Line 2": self.address2,
            "Address Line 3": self.address3,
            "Address Line 4": self.address4,
            "Unit Name": self.unit_name,
            "Tenant Name": self.tenant_name,
            "Lease Start Date": self.lease_start_date,
            "Lease End Date": self.lease_end_date,
            "Lease Years": self.lease_years,
            "Current Rent": self.current_rent,
        }
     