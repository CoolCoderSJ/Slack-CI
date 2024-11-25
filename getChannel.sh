response=$(curl --location "https://slack.com/api/conversations.info?channel=$1" \
    --header 'Content-Type: application/json' \
    --header "Authorization: Bearer $TOKEN" \
    --fail)
echo $response