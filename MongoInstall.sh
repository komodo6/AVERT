set -e

echo "Installing repo"
sudo apt-get install gnupg
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -

echo "deb http://repo.mongodb.org/apt/debian buster/mongodb-org/5.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list

echo "Installing binaries"
sudo apt-get update
sudo apt-get install -y mongodb-org
sudo service mongod stop


echo "Setting up default settings"
sudo rm -rf /var/lib/mongodb/*
sudo cat > sudo /etc/mongod.conf <<'EOF'
storage:
  dbPath: /var/lib/mongodb
  directoryPerDB: true
  journal:
    enabled: true
  engine: "wiredTiger"

systemLog:
  destination: file
  logAppend: true
  path: /var/log/mongodb/mongod.log

net:
  port: 27017
  bindIp: 0.0.0.0
  maxIncomingConnections: 100

replication:
  oplogSizeMB: 128
  replSetName: "rs1"

security:
  authorization: enabled

EOF

sudo service mongod start
sleep 5

mongo admin <<'EOF'
use admin
rs.initiate()
exit
EOF

sleep 5

echo "Adding admin user"
mongo admin <<'EOF'
use admin
rs.initiate()
var user = {
  "user" : "admin",
  "pwd" : "admin",
  roles : [
      {
          "role" : "userAdminAnyDatabase",
          "db" : "admin"
      }
  ]
}
db.createUser(user);
exit
EOF

echo "Complete"
