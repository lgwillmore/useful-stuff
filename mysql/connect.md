

    mysql -h localhost -u myname -ppassword mydb
    
export XTAPI_MYSQL_USER='xturf@sohotech-azure-sajhb-staging-betx-xturf-mariadb.privatelink'
export XTAPI_MYSQL_PASSWORD='xturf_betx_staging_password'
export XTAPI_MYSQL_DATABASE='sohotech_betx_xturf_staging_db'
export XTAPI_MYSQL_HOST='sohotech-azure-sajhb-staging-betx-xturf-mariadb.privatelink.mariadb.database.azure.com'
export XTAPI_MYSQL_PORT='3306'

export XTAPI_MYSQL_SERVER_VERSION='mariadb-10.4.6'
export XTAPI_MYSQL_USER='soho@sohotech-azure-sajhb-dev-betx-xturf-mariadb.privatelink'
export XTAPI_MYSQL_PASSWORD='UQa_C8gxtklJPoiL'
export XTAPI_MYSQL_PASSWORD='xturf_betx_dev_password'
export XTAPI_MYSQL_DATABASE='sohotech-azure-sajhb-dev-betx-xturf-mariadb'
export XTAPI_MYSQL_HOST='sohotech-azure-sajhb-dev-betx-xturf-mariadb.privatelink.mariadb.database.azure.com'
export XTAPI_MYSQL_PORT='3306'


Connect to azure DB

    mysql -h sohotech-azure-sajhb-staging-betx-xturf-mariadb.privatelink.mariadb.database.azure.com -u xturf@sohotech-azure-sajhb-staging-betx-xturf-mariadb.privatelink
    
    
    mysql -u soho@sohotech-azure-sajhb-dev-betx-xturf-mariadb -p -h sohotech-azure-sajhb-dev-betx-xturf-mariadb.privatelink.mariadb.database.azure.com