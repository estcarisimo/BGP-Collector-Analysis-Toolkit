import pybgpstream

DAY_TO_SECONDS = 86400

import pybgpstream
from datetime import datetime

def retrieve_bgp_announcements(start_time, end_time, collectors, bgp_stream_filter="", record_type="updates"):
    """
    Retrieve BGP announcements within a specified time range from given collectors.

    This function creates and configures a PyBGPStream instance to retrieve BGP announcements
    (either updates or RIBs) within a specified time range from a specified list of collectors.
    It supports filtering BGP data based on a custom filter string and selecting between RIBs and update messages.

    Parameters
    ----------
    start_time : datetime
        The start of the time range for which to retrieve BGP announcements.
    end_time : datetime
        The end of the time range for which to retrieve BGP announcements.
    collectors : list of str
        A list of collector IDs from which to retrieve announcements.
    bgp_stream_filter : str, optional
        A filter string to apply to the BGPStream for custom filtering criteria. Default is "" (no filter).
    record_type : str, optional
        The type of BGP records to retrieve ('updates' or 'ribs'). Default is 'updates'.

    Returns
    -------
    BGPStream
        A configured BGPStream instance ready to retrieve the specified BGP data.

    Raises
    ------
    Exception
        If there's an error initializing the BGPStream instance.

    Notes
    -----
    The function assumes the existence of a constant `DAY_TO_SECONDS` used to limit the BGPStream
    to download only the first dump of BGP data within the specified period. Ensure this constant is defined.
    """
    try:
        # Initialize a BGPStream instance with specified parameters
        stream = pybgpstream.BGPStream(
            from_time=start_time.strftime("%Y-%m-%d %H:%M:%S"),
            until_time=end_time.strftime("%Y-%m-%d %H:%M:%S"),
            collectors=collectors,
            record_type=record_type
        )
        
        if bgp_stream_filter:
            stream.parse_filter_string(bgp_stream_filter)

        # Apply a filter to limit the stream to download only the initial BGP dump in the specified period
        stream.add_rib_period_filter(DAY_TO_SECONDS)

        return stream
    except Exception as e:
        raise Exception(f"Failed to initialize BGPStream: {e}")
