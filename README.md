# Exchange Rate sample project

## Description

This is a sample RESTful API project used for 
getting the current exchange rate of specified currency

## Installation & Running

##### Debian/Ubuntu:

1. Install Docker:
   ```shell
   sudo snap install docker
   ```

2. Go to _/back_ and build docker image:
   ```shell
   cd back
   docker build -t exc_app .
   ```

3. Run docker image:
   ```shell
   docker run --network="host" exc_app
   ```
