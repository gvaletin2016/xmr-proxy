
# Ports for your workers
STRATUM_HOST = "64.20.49.26"
STRATUM_PORT = 3334

# Coin address where money goes. If you mine direct to the exchange, you MUST specify payment_id together with wallet of exchange.
WALLET = 'N8jMWXcNWznRPQfeaAPRFXWZRZjFduyQtLH5qQfwpzsbRrVByRGJXHcMv1J98ExAkNBnhnbnPVUKjWwYBXahYdjNPG8XCTZ'
# Only if you mine direct to the exchange
PAYMENT_ID = ''

# It's useful for individually monitoring and statistic.
# In your workers you have to use any number as username (without wallet!)
ENABLE_WORKER_ID = True
WORKER_ID_FROM_IP = False

# On DwarfPool you have option to monitor your workers via email.
# If WORKER_ID is enabled, you can monitor every worker/rig separately.
MONITORING = True
MONITORING_EMAIL = 'gvalentin@gmx.com'

# Main pool
POOL_HOST = 'us-nbr.4miner.me'
POOL_PORT = 3334

# Failover pool
POOL_FAILOVER_ENABLE = False
POOL_HOST_FAILOVER = 'nbr.ciapool.com'
POOL_PORT_FAILOVER = 3333

# ERROR, INFO, DEBUG
LOGLEVEL = 'DEBUG'
DEBUG = True
LOGFILE = "logfile.log"
