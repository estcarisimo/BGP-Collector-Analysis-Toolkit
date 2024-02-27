# BGP Data Retrieval Toolkit

## Overview
This toolkit includes two Python scripts designed to facilitate the retrieval and analysis of Border Gateway Protocol (BGP) announcements from a range of collectors. Using using [CAIDA's PyBGPStream library](https://github.com/CAIDA/pybgpstream), these toolkit is aimed at detecting routing anomalies and understanding global internet routing dynamics.

## Features
- **Basic Query**: Perform general queries to retrieve BGP announcements.
- **Prefix Search**: Specifically retrieve BGP announcements filtered by IP prefix.
- Support for multiple collectors from RouteViews and RIPE RIS.
- Configurable for fetching either updates or RIBs (Routing Information Base).

## Requirements
- Python 3.6+
- pybgpstream

## Installation
Ensure Python is installed on your system and install `pybgpstream` via pip:

```sh
pip install pybgpstream
```

## Scripts

### bgp_collector_basic_query.py
This script performs basic queries to retrieve BGP announcements for a specified time range from a given list of collectors. It can be configured to fetch either updates or RIBs.

#### Usage
Edit the script to include your desired time range and collectors, then run:

```sh
python bgp_collector_basic_query.py
```

### bgp_collector_prefix_search.py
This script is developed for retrieving BGP announcements filtered by a specific IP prefix, from all available collectors, within a specified time range.

#### Usage
Configure the script with the desired time range, collectors, and IP prefix, then execute:

```sh
python bgp_collector_prefix_search.py
```

### Configuring the Scripts
- **Time Range**: Define the start and end times within the scripts to specify the period for retrieving BGP announcements.
- **Collectors**: Modify the list of collectors as required. A comprehensive list is included, but can be adjusted to fit your needs.
- **Prefix Filter** (for `bgp_collector_prefix_search.py`): Adjust the `prefix` variable to filter announcements for a specific IP prefix.

## Contributing
We welcome contributions to improve the BGP Data Retrieval Toolkit. Feel free to submit pull requests or create issues for bugs and feature requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.