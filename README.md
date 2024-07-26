# VPS Data Analysis Scripts
The following repository consists of scripts that generate data analysis for VPS.

## Prerequisites
- Python 3.10

## Running Scripts
1. Download and unzip the zip file of the source code from the latest release.
2. Open Command Prompt and type `cd 'PATH_TO_DIRECTORY'`, substituting PATH_TO_DIRECTORY with the file path to the directory where the source code was extracted to.
    - Example: `cd 'C:\vps\vps_data_analysis'`
3. Run `pip install -r requirements.txt`. This will install the necessary third-party libraries. You should only ever need to run this once.
4. Run `python -m main 'PATH_TO_SALES_CSV'`, substituting PATH_TO_SALES_CSV with the file path to the sales csv.
5. A web browser will open with the generated interactive choropleth graph. You can save a PNG from there.