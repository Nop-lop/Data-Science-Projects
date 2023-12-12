## Data Quality
Assessing the quality is arguably of the most vital stages in any Machine Learning project. This is usually done in collaboration with Data Engineers, but I am running solo on this project so we're picking up that part!

These are the main data quality attributes we'll use to assess the data quality of our dataset;
- Accuracy
- Completeness
- Consistency
- Freshness
- Validity
- Uniqueness
- Volume

Before we assess the quality, we have to have a benchmark to measure it against, our data schema.

### Data Schema
The full data schema has been included here for easier project flow; it can also be viewed in BigQuery's console under the schema section for the dataset

Full Data Schema
- date: Telemetry date in format YYYY-MM-DD. This is the partition key
- hour: Telemetry hour in format HH24:MM:SS
- lat: latitude
- long: longitude
- signal: Average Signal measured in ASU (Arbirtary Strength Unit)
- network: Network name
- operator: Operator name
- status: status code {0,1,2,3}
- description: description STATE_POWER_OFF (3), STATE_OUT_OF_SERVICE (1), STATE_IN_SERVICE (0), STATE_EMERGENCY_ONLY (2)
- net: Network type (categorical) : 2G, 3G, 4G
- speed: Source estimated speed
- satellites: Number of GPS satellites
- precision: Constant that describes the provider accuracy
- provider: Position provider name
- activity: User Activity(categorical) : IN_VEHICLE, STILL, ON_FOOT, TITLING, UNKOWN, BICYCLE
- downloadSpeed: Current download speed
- uploadSpeed: Current upload speed
- postal_code: Town postal code
- town_name: Name of the town where the telemetry was obtained
- position_geom: Geographic representation of the location

## Data Quality Checks by  Attributes
### Accuracy
From the main data's details, the dataset was last updated on Feb 05, 2022 10:24:05 PM UTC; there shouldn't be `date` entries greater than 2022-02-05.
Accuracy:

- date: Verify that the date format (YYYY-MM-DD) is correct and that the date does not fall outside the valid range.

- hour: Verify that the hour format (HH24:MM:SS) is correct and that the hour is within the valid range.

- lat: Ensure that the latitude values are within the expected range, such as -90 to 90 degrees.

- long: Ensure that the longitude values are within the expected range, such as -180 to 180 degrees.

- signal: Validate that the signal strength values are between 0 and 100 inclusive.

- network: Verify that the network names are consistent with recognized network providers.

- operator: Validate that the operator names are consistent with known network operators.

- status: Check that the status values are within the expected range: 0 (in service), 1 (out of service), 2 (emergency only), 3 (power off).

- description: Ensure that the status description values match the corresponding status codes.

- net: Check that the network type values are consistent with recognized network technologies (2G, 3G, or 4G).

- speed: Validate that the source estimated speed values are in a reasonable range, such as 0 to 1000 kilometers per hour.

- satellites: Verify that the number of GPS satellites values are within the expected range, typically from 2 to 12.

- precision: Ensure that the provider accuracy values are within a reasonable range, such as 1 to 100 meters.

- provider: Verify that the position provider names are consistent with known position providers.

- activity: Validate that the user activity values are consistent with recognized user activity categories (IN_VEHICLE, STILL, ON_FOOT, TITLING, UNKOWN, BICYCLE).

- downloadSpeed: Check that the current download speed values are within a reasonable range, such as 0 to 100 megabits per second.

- uploadSpeed: Ensure that the current upload speed values are within a reasonable range, such as 0 to 100 megabits per second.

- postal_code: Verify that the postal code format is correct and that the postal code is not an invalid value.

- town_name: Ensure that the town names are consistent with recognized town names in the relevant area.

### Completeness
An aggregate for any null values is to be calculated, afterall there are no noiseless datasets.

### Consistency
Checking each feature entry has the expected data format for the respective feature

### Freshness

### Uniqueness

### Validity & Volume
- Data size: Monitors the overall size of the telemetry dataset to ensure it does not exceed storage capacity or impact performance.

- Growth rate: Track the growth rate of the telemetry dataset to anticipate future storage requirements and data pipeline scaling.

- Data distribution: Analyze the distribution of data across different features and dimensions to identify potential patterns or anomalies.

- Data sparsity: Assess the sparsity of the dataset, which can indicate the presence of missing values or irrelevant data.

#### BigQuery SQL check for Data Validity + Volume
```
# Volume
WITH volume_checks AS (
    -- Check data size
    SELECT
        SUM(BYTES) AS total_bytes
    FROM telemetry_data
)

SELECT
    -- Check data growth rate
    SUM(total_bytes) AS total_bytes,
    SUM(total_bytes - LAG(total_bytes) OVER (ORDER BY timestamp)) AS bytes_added
FROM volume_checks
ORDER BY timestamp

# Validity
WITH validity_checks AS (
    -- Check outliers for signal strength
    SELECT
        signal,
        COUNT(*) AS total_records
    FROM telemetry_data
    WHERE signal < 0 OR signal > 100
    GROUP BY signal
)

SELECT
    signal,
    SUM(total_records) AS total_records_per_outlier
FROM validity_checks
GROUP BY signal
HAVING COUNT(*) > 10

```