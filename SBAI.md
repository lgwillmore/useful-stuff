# SBAI Steps

## Useful

### minions and URLs

    sohotech-azure-sajhb-staging-betx-betsite-frontend:
        sohotech-azure-sajhb-staging-betx-betsite-frontend.staging.sohotech.io
    
    sohotech-azure-sajhb-staging-betx-xturf-admin-frontend:
        sohotech-azure-sajhb-staging-betx-xturf-admin-frontend.staging.sohotech.io
        
    sohotech-azure-sajhb-staging-betx-xturf:
        sohotech-azure-sajhb-staging-betx-xturf.staging.sohotech.io
        
    sohotech-azure-sajhb-staging-betx-betsite-backend:
        sohotech-azure-sajhb-staging-betx-betsite-backend.staging.sohotech.io

## Prep

### Stop containers
    
 - xturf:

       ssh sohotech-azure-sajhb-staging-betx-xturf.staging.sohotech.io
       sudo docker stop xturf-core
       
 - admin-panel:

       ssh sohotech-azure-sajhb-staging-betx-xturf-admin-frontend.staging.sohotech.io
       sudo docker stop xturf-admin-panel-frontend
       
 - betsite-backend:

       ssh sohotech-azure-sajhb-staging-betx-betsite-backend.staging.sohotech.io
       sudo docker stop betsite_backend
       
 - betsite-frontend:

       ssh sohotech-azure-sajhb-staging-betx-betsite-frontend.staging.sohotech.io
       sudo docker stop xturf-betsite-frontend
       
 - Memcached data + tokens
       

### Clean the DB

 - Connect from xturf host with (password = `xturf_betx_staging_password`):
 
       mysql -h sohotech-azure-sajhb-staging-betx-xturf-mariadb.privatelink.mariadb.database.azure.com -u xturf@sohotech-azure-sajhb-staging-betx-xturf-mariadb.privatelink -p
     
 - Delete all tables with:
 
       SHOW DATABASES;
       
       USE sohotech_betx_xturf_staging_db;
       SHOW tables;
       
       SELECT concat('DROP TABLE IF EXISTS `', table_name, '`;')
       FROM information_schema.tables
       WHERE table_schema = 'sohotech_betx_xturf_staging_db';
       
       DROP TABLE IF EXISTS `address`;                        
       DROP TABLE IF EXISTS `affiliate`;                      
       DROP TABLE IF EXISTS `affiliate_customer_activity`;    
       DROP TABLE IF EXISTS `affiliates_payment_accounts`;    
       DROP TABLE IF EXISTS `banner`;                         
       DROP TABLE IF EXISTS `bet`;                            
       DROP TABLE IF EXISTS `campaign`;                       
       DROP TABLE IF EXISTS `capability`;                     
       DROP TABLE IF EXISTS `casino_category`;                
       DROP TABLE IF EXISTS `casino_game`;                    
       DROP TABLE IF EXISTS `casino_game_category`;           
       DROP TABLE IF EXISTS `casino_interface`;               
       DROP TABLE IF EXISTS `casino_jackpot`;                 
       DROP TABLE IF EXISTS `casino_lobby`;                   
       DROP TABLE IF EXISTS `casino_lobby_category`;          
       DROP TABLE IF EXISTS `content_block`;                  
       DROP TABLE IF EXISTS `content_item`;                   
       DROP TABLE IF EXISTS `content_item_attribute`;         
       DROP TABLE IF EXISTS `content_item_type`;              
       DROP TABLE IF EXISTS `content_item_type_attribute`;    
       DROP TABLE IF EXISTS `content_page`;                   
       DROP TABLE IF EXISTS `content_page_block`;             
       DROP TABLE IF EXISTS `countries_software_modules`;     
       DROP TABLE IF EXISTS `country`;                        
       DROP TABLE IF EXISTS `country_province`;               
       DROP TABLE IF EXISTS `currency`;                       
       DROP TABLE IF EXISTS `customer`;                       
       DROP TABLE IF EXISTS `customer_ip_log`;                
       DROP TABLE IF EXISTS `customer_limit`;                 
       DROP TABLE IF EXISTS `customer_module_restriction`;    
       DROP TABLE IF EXISTS `customer_restriction`;           
       DROP TABLE IF EXISTS `customers_payment_accounts`;     
       DROP TABLE IF EXISTS `exchange_rate`;                  
       DROP TABLE IF EXISTS `expired_token`;                  
       DROP TABLE IF EXISTS `ext_log_entries`;                
       DROP TABLE IF EXISTS `ext_translations`;               
       DROP TABLE IF EXISTS `extra_field`;                    
       DROP TABLE IF EXISTS `extra_field_category`;           
       DROP TABLE IF EXISTS `extra_field_definition`;         
       DROP TABLE IF EXISTS `extra_field_schema`;             
       DROP TABLE IF EXISTS `game_provider_expired_token`;    
       DROP TABLE IF EXISTS `import_log`;                     
       DROP TABLE IF EXISTS `limit_log`;                      
       DROP TABLE IF EXISTS `menu_item`;                      
       DROP TABLE IF EXISTS `menu_item_i18n`;                 
       DROP TABLE IF EXISTS `menu_node`;                      
       DROP TABLE IF EXISTS `message`;                        
       DROP TABLE IF EXISTS `migrations`;                     
       DROP TABLE IF EXISTS `node`;                           
       DROP TABLE IF EXISTS `payment_account`;                
       DROP TABLE IF EXISTS `payout`;                         
       DROP TABLE IF EXISTS `pending_transaction`;            
       DROP TABLE IF EXISTS `permission_preset`;              
       DROP TABLE IF EXISTS `permission_preset_i18n`;         
       DROP TABLE IF EXISTS `product`;                        
       DROP TABLE IF EXISTS `product_software_module`;        
       DROP TABLE IF EXISTS `remark`;                         
       DROP TABLE IF EXISTS `report_template`;                
       DROP TABLE IF EXISTS `report_template_row`;            
       DROP TABLE IF EXISTS `security_audit`;                 
       DROP TABLE IF EXISTS `software_module`;                
       DROP TABLE IF EXISTS `ticket`;                         
       DROP TABLE IF EXISTS `ticket_limit`;                   
       DROP TABLE IF EXISTS `top_filter`;                     
       DROP TABLE IF EXISTS `top_filter_i18n`;                
       DROP TABLE IF EXISTS `trading_bet_type`;               
       DROP TABLE IF EXISTS `trading_market_outcome_stats`;   
       DROP TABLE IF EXISTS `trading_market_stats`;           
       DROP TABLE IF EXISTS `trading_node_stats`;             
       DROP TABLE IF EXISTS `trading_numbers_game`;           
       DROP TABLE IF EXISTS `trading_parameter`;              
       DROP TABLE IF EXISTS `trading_product`;                
       DROP TABLE IF EXISTS `trading_risk_template`;          
       DROP TABLE IF EXISTS `trading_risk_template_value`;    
       DROP TABLE IF EXISTS `trading_sport_event_stats`;      
       DROP TABLE IF EXISTS `trading_ticker`;                 
       DROP TABLE IF EXISTS `trading_ticker_ticket`;          
       DROP TABLE IF EXISTS `transaction`;                    
       DROP TABLE IF EXISTS `transaction_description`;        
       DROP TABLE IF EXISTS `transaction_description_i18n`;   
       DROP TABLE IF EXISTS `unified_category`;               
       DROP TABLE IF EXISTS `unified_category_dependency`;    
       DROP TABLE IF EXISTS `unified_category_i18n`;          
       DROP TABLE IF EXISTS `unified_club`;                   
       DROP TABLE IF EXISTS `unified_club_i18n`;              
       DROP TABLE IF EXISTS `unified_competitor`;             
       DROP TABLE IF EXISTS `unified_competitor_dependency`;  
       DROP TABLE IF EXISTS `unified_competitor_i18n`;        
       DROP TABLE IF EXISTS `unified_counter`;                
       DROP TABLE IF EXISTS `unified_counter_i18n`;           
       DROP TABLE IF EXISTS `unified_event_competitor`;       
       DROP TABLE IF EXISTS `unified_market`;                 
       DROP TABLE IF EXISTS `unified_market_type`;            
       DROP TABLE IF EXISTS `unified_market_type_attribute`;  
       DROP TABLE IF EXISTS `unified_market_type_blacklist`;  
       DROP TABLE IF EXISTS `unified_market_type_i18n`;       
       DROP TABLE IF EXISTS `unified_market_type_tag`;        
       DROP TABLE IF EXISTS `unified_outcome_set`;            
       DROP TABLE IF EXISTS `unified_outcome_type`;           
       DROP TABLE IF EXISTS `unified_period`;                 
       DROP TABLE IF EXISTS `unified_phase`;                  
       DROP TABLE IF EXISTS `unified_phase_i18n`;             
       DROP TABLE IF EXISTS `unified_player`;                 
       DROP TABLE IF EXISTS `unified_player_dependency`;      
       DROP TABLE IF EXISTS `unified_player_i18n`;            
       DROP TABLE IF EXISTS `unified_provider`;               
       DROP TABLE IF EXISTS `unified_season`;                 
       DROP TABLE IF EXISTS `unified_season_dependency`;      
       DROP TABLE IF EXISTS `unified_season_i18n`;            
       DROP TABLE IF EXISTS `unified_sport`;                  
       DROP TABLE IF EXISTS `unified_sport_counter`;          
       DROP TABLE IF EXISTS `unified_sport_dependency`;       
       DROP TABLE IF EXISTS `unified_sport_event`;            
       DROP TABLE IF EXISTS `unified_sport_event_dependency`; 
       DROP TABLE IF EXISTS `unified_sport_i18n`;             
       DROP TABLE IF EXISTS `unified_sport_period`;           
       DROP TABLE IF EXISTS `unified_sport_phase`;            
       DROP TABLE IF EXISTS `unified_tag`;                    
       DROP TABLE IF EXISTS `unified_tag_i18n`;               
       DROP TABLE IF EXISTS `unified_tournament`;             
       DROP TABLE IF EXISTS `unified_tournament_dependency`;  
       DROP TABLE IF EXISTS `unified_tournament_i18n`;        
       DROP TABLE IF EXISTS `unified_variable`;               
       DROP TABLE IF EXISTS `unified_venue`;                  
       DROP TABLE IF EXISTS `unified_venue_dependency`;       
       DROP TABLE IF EXISTS `unified_venue_i18n`;             
       DROP TABLE IF EXISTS `user`;                           
       DROP TABLE IF EXISTS `user_clients`;                   
       DROP TABLE IF EXISTS `user_message`;                   
       DROP TABLE IF EXISTS `user_node`;                      
       DROP TABLE IF EXISTS `user_permission`;                
       DROP TABLE IF EXISTS `voucher`;                        
       DROP TABLE IF EXISTS `wallet`;                         
       DROP TABLE IF EXISTS `workspace`;
       DROP TABLE IF EXISTS `trading_bet`;
       DROP TABLE IF EXISTS `trading_bet_combination`;
       DROP TABLE IF EXISTS `trading_numbers_game`;
       DROP TABLE IF EXISTS `trading_risk_template`;
       DROP TABLE IF EXISTS `trading_ticket`;
       DROP TABLE IF EXISTS `trading_ticket_reference`;
       DROP TABLE IF EXISTS `unified_category`;
       DROP TABLE IF EXISTS `unified_club`;
       DROP TABLE IF EXISTS `unified_competitor`;
       DROP TABLE IF EXISTS `unified_market_type_whitelist`;
       DROP TABLE IF EXISTS `unified_number_game_result`;
       DROP TABLE IF EXISTS `unified_phase`;
       DROP TABLE IF EXISTS `unified_provider`;
       DROP TABLE IF EXISTS `unified_season`;
       DROP TABLE IF EXISTS `unified_sport`;
       DROP TABLE IF EXISTS `unified_sport_event`;
       DROP TABLE IF EXISTS `unified_tournament`;
       DROP TABLE IF EXISTS `unified_venue`;
       
 - Check tables have been deleted.
 
       SHOW tables;
       
## Do releases and deploys

### Deploy Xturf

 - Trigger build on master
 - Tag
 - Download zip form github and send to GLI
 - Download checksum and send to GLI
 - Update checksum in salt pillar
 - Update version in salt pillar
 - Pull request + merge
 - deploy
 
### Admin Panel

 - Build
 - Tag
 - Update version in salt pillar
 - Pull request + merge
 - deploy

### Betsite Backend

 - build
 - tag
 - update tag in salt
 - create company, shop, till and user
 - Promote user and generate api key
 
       source /srv/xturf-core/env_vars.sh
       /usr/bin/php bin/console digitote:apikey:create betsite-backend 1  2 3000
       
 - Update secrets with generated credentials
 
      echo "my secret" | gpg --armor --batch --trust-model always --encrypt -r "sohotech-azure-sajhb-ss-saltmaster"
      
 - Pull request + merge
 - deploy
 
 ### Betsite Frontend
 
  - Build + Tag
  - Update version in salt pillar
  - Pull request + merge
  - deploy
  
## Evidence

### DB Dump

On xturf host:

    mysqldump -h sohotech-azure-sajhb-staging-betx-xturf-mariadb.privatelink.mariadb.database.azure.com -u xturf@sohotech-azure-sajhb-staging-betx-xturf-mariadb.privatelink -p sohotech_betx_xturf_staging_db > /tmp/xturf_db_dump.sql
    
Exit to jump box:

    scp laurence@sohotech-azure-sajhb-staging-betx-xturf.staging.sohotech.io:/tmp/xturf_db_dump.sql xturf_db_dump.sql
    
From localhost:

    scp laurence@102.133.139.191:xturf_db_dump.sql /tmp/xturf_db_dump.sql
      
   
      




    