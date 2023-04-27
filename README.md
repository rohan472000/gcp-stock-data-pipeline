# GCP Stock Data Pipeline
This project fetches the latest data for NDAQ from the Tiingo API, performs ETL transformations using DataProc PySpark cluster, and loads the processed data into BigQuery. This is fully automated project means no human intervention needed as I used scripts to make infra and other things in GCP.

## Technologies used
- Google Cloud Platform (GCP)
- Tiingo API
- DataProc
- BigQuery

## How to Run
- Make a tiingo account from `api.tiingo.com` to access API to fetch data.
- Make a service account with BigQuery and Dataproc editor or admin access, download that service account in JSON format.
- Upload both api and service.json file keys in .env folder.
- Now run the github action through run-scripts.yml in `.github/workflows/run-scripts.yml`


## Architecture
                                +----------------+
                                |    Tiingo API  |
                                +----------------+
                                          |
                                          |
                                          |
                                          v
                                +----------------+
                                |                |
                                |   Fetch Latest |
                                |     Stock Data |
                                |                |
                                +-------+--------+
                                        |
                                        |
                                        |
                                        v
                          +-------------+------------+
                          |                          |
                          |     GitHub Repository    |
                          |                          |
                          +-------------+------------+
                                        |
                                        |
                                        |
                                        v
                    +-------------------+------------------+
                    |                                      |
                    |          GitHub Actions              |
                    |      (Automated ETL Pipeline)        |
                    |                                      |
                    +-------------------+------------------+
                                        |
                                        |
                                        |
                          +-------------v------------+
                          |                          |
                          |     DataProc PySpark     |
                          |                          |
                          +-------------+------------+
                                        |
                                        |
                                        |
                                        v
                           +--------------+-------------+
                           |                            |
                           |           BigQuery         |
                           |                            |
                           +--------------+-------------+
                                          |
                                          |
                                          |
                                          v
                                +----------------+
                                |                |
                                |   Processed    |
                                |   Stock Data   |
                                |                |
                                +----------------+


## Precautions
- Keep the bucket name same everywhere, if changing then then pay attention to worklfows.
- Keep api_key and service_account_key safe.


## Screen Shots
![Screenshot (178)](https://user-images.githubusercontent.com/96521078/234498540-6f22a89f-4bbf-4ef3-84ed-74bf006160e5.png)
![Screenshot (180)](https://user-images.githubusercontent.com/96521078/234498614-90e6424f-b22c-4fa0-a4ac-71e12986e6ac.png)
![Screenshot (181)](https://user-images.githubusercontent.com/96521078/234498679-df642d1d-2a2c-4bbc-bf7a-bbcc95ddfde8.png)
![Screenshot (179)](https://user-images.githubusercontent.com/96521078/234498706-6d5a58a7-7605-4b9f-bd70-e0c62a165f64.png)
![Screenshot (177)](https://user-images.githubusercontent.com/96521078/234498756-945ae33d-75a4-434d-bc1b-97f6b82b807c.png)



## Contributing
Feel free to contribute to this project by opening a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the terms of the MIT license. 

## Contact
For any queries or suggestions, please email me at anand44rohan@gmail.com.
