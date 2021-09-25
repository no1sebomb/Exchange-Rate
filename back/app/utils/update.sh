crontab << 'EOF'
SHELL=/bin/bash
0 */4 * * * curl -X GET -G 'http://0.0.0.0:5000/api/currency' -d codes=UAH,RUB,PLN,EUR,CAD -d cached=false
EOF