from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

rpcuser='quaker_quorum'
rpcpassword='franklin_fought_for_continental_cash'
rpcport=8332
rpcip='3.134.159.30'

rpc_connection = AuthServiceProxy("http://%s:%s@%s:%s"%(rpcuser, rpcpassword, rpcip, rpcport))

hash=rpc_connection.getblockhash(0)
print(hash)

blockinfo=rpc_connection.getblock(hash)
print(blockinfo)

time=blockinfo.get("time")
print(time)

i=0
for i in range(777902):
  hash=rpc_connection.getblockhash(i)
  blockinfo=rpc_connection.getblock(hash)
  time=blockinfo.get("time")
  if time>1232100000:
    print("The block has index ", i)
    print("The time is ", time)
    print(blockinfo)
    break
  else:
    continue

#checking
hash=rpc_connection.getblockhash(i)
blockinfo=rpc_connection.getblock(hash)
time1=blockinfo.get("time")
print("Block ",i," has time", time1)

hash=rpc_connection.getblockhash(i-1)
blockinfo=rpc_connection.getblock(hash)
time2=blockinfo.get("time")
print("Block ",i-1," has time", time2)

