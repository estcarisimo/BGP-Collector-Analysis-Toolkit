from datetime import datetime
from pprint import pprint 

from bgpstreamtool import retrieve_bgp_announcements

def main():
    """
    Demonstrate retrieving BGP announcements using a specified time range and collectors.

    This script initializes a time range and a list of BGP collectors, then uses the
    `retrieve_bgp_announcements` function to create a stream for retrieving BGP announcements.
    It iterates over the retrieved elements, printing their fields.
    """
    # Define the start and end times for the BGP data retrieval
    start_time = datetime(2020, 3, 4, 0, 0)
    end_time = datetime(2020, 3, 4, 0, 10)
    
    # Specify the BGP collectors to retrieve data from
    collectors = ["route-views.sg", "route-views.eqix"]

    # Retrieve BGP announcements from the specified collectors and time range
    bgp_stream = retrieve_bgp_announcements(start_time, end_time, collectors, record_type="updates")

    # Iterate over the retrieved BGP announcements and print their fields
    for announcement in bgp_stream:
        pprint(announcement.fields)

if __name__ == "__main__":
    main()
