
# Ports for your workers
STRATUM_HOST = "68.168.221.143"
STRATUM_PORT = 3333

# Coin address where money goes. If you mine direct to the exchange, you MUST specify payment_id together with wallet of exchange.
WALLET = '28nLfLUi8CQBcSgo1JqqdqPHQgSuFxSgF4aFbau6eD4dJ1CDTf6XEUM43z54VwGg1YhsTGKbiwXa4GpBZHdR98MA28xro28'
# Only if you mine direct to the exchange
PAYMENT_ID = '28nLfLUi8CQBcSgo1JqqdqPHQgSuFxSgF4aFbau6eD4dJ1CDTf6XEUM43z54VwGg1YhsTGKbiwXa4GpBZHdR98MA28xro28'

# It's useful for individually monitoring and statistic.
# In your workers you have to use any number as username (without wallet!)
ENABLE_WORKER_ID = True
WORKER_ID_FROM_IP = False

# On DwarfPool you have option to monitor your workers via email.
# If WORKER_ID is enabled, you can monitor every worker/rig separately.
MONITORING = True
MONITORING_EMAIL = 'gvalentin@gmx.com'

# Main pool
POOL_HOST = 'bytecoin.pt'
POOL_PORT = 3333

# Failover pool
POOL_FAILOVER_ENABLE = False
POOL_HOST_FAILOVER = 'bytecoin.pt'
POOL_PORT_FAILOVER = 3333

# ERROR, INFO, DEBUG
LOGLEVEL = 'DEBUG'
DEBUG = True
LOGFILE = "logfile.log"
