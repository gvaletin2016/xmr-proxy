
# Ports for your workers
STRATUM_HOST = "68.168.221.143"
STRATUM_PORT = 5221

# Coin address where money goes. If you mine direct to the exchange, you MUST specify payment_id together with wallet of exchange.
WALLET = 'Se3vmM2qMQu7CEGF76RtXJ43AJeCbVP5QSeQuGoDbR3RP81VJhNbeAMFPoaGm5FfRWEybxHxQoGj2H6idPq5iq4o1Tkqma6oQ'
# Only if you mine direct to the exchange
PAYMENT_ID = 'Se3vmM2qMQu7CEGF76RtXJ43AJeCbVP5QSeQuGoDbR3RP81VJhNbeAMFPoaGm5FfRWEybxHxQoGj2H6idPq5iq4o1Tkqma6oQ'

# It's useful for individually monitoring and statistic.
# In your workers you have to use any number as username (without wallet!)
ENABLE_WORKER_ID = True
WORKER_ID_FROM_IP = False

# On DwarfPool you have option to monitor your workers via email.
# If WORKER_ID is enabled, you can monitor every worker/rig separately.
MONITORING = True
MONITORING_EMAIL = 'gvalentin@gmx.com'

# Main pool
POOL_HOST = '78.46.85.142'
POOL_PORT = 5221

# Failover pool
POOL_FAILOVER_ENABLE = False
POOL_HOST_FAILOVER = '78.46.85.142'
POOL_PORT_FAILOVER = 5221

# ERROR, INFO, DEBUG
LOGLEVEL = 'DEBUG'
DEBUG = True
LOGFILE = "logfile.log"
