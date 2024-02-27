from datetime import datetime
from pprint import pprint 

# from bgpstreamtool import retrieve_bgp_announcements


def main():
    """
    Demonstrate retrieving BGP announcements using a specified time range, collectors, and prefix filter.

    This script initializes a time range, a list of BGP collectors, and a prefix filter, then uses the
    `retrieve_bgp_announcements` function to create a stream for retrieving BGP announcements.
    It iterates over the retrieved elements, printing their fields.
    """
    # Define the start and end times for the BGP data retrieval
    start_time = datetime(2020, 3, 4, 0, 0)
    end_time = datetime(2020, 3, 4, 0, 10)

    # Define the prefix to filter BGP announcements
    prefix = "157.92.0.0/16"

    # Updated list of collectors to retrieve announcements from, more concisely listed
    collectors = [
        # RouteViews
        "route-views.amsix", "route-views.bdix", "route-views.bknix", "route-views.chicago", 
        "route-views.chile", "route-views.eqix", "route-views.flix", "route-views.fortaleza", 
        "route-views.gixa", "route-views.gorex", "route-views.isc", "route-views.jinx", 
        "route-views.kixp", "route-views.linx", "route-views.linxlondon", "route-views.mwix", 
        "route-views.napafrica", "route-views.nwax", "route-views.perth", "route-views.phoix", 
        "route-views.saopaulo", "route-views.sfmix", "route-views.sg", "route-views.soxrs", 
        "route-views.sydney", "route-views.telxatl", "route-views.wide", "route-views2", 
        "route-views3", "route-views4", "route-views6",
        # RIPE RIS
        "rrc00", "rrc01", "rrc02", "rrc03", "rrc04", "rrc05", "rrc06", "rrc07", 
        "rrc08", "rrc09", "rrc10", "rrc11", "rrc12", "rrc13", "rrc14", "rrc15", 
        "rrc16", "rrc18", "rrc19", "rrc20", "rrc21", "rrc22", "rrc23", "rrc24", 
        "rrc25", "rrc26"
    ]

    # Retrieve BGP announcements from the specified collectors and time range
    bgp_stream = retrieve_bgp_announcements(start_time, end_time, collectors, bgp_stream_filter=f"prefix exact {prefix}", record_type="updates")

    # Iterate over the retrieved BGP announcements and print their fields
    for elem in bgp_stream:
        pprint(elem.fields)


if __name__ == "__main__":
    main()

